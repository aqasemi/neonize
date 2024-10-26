from __future__ import annotations
import ctypes
import asyncio
import segno
from ..events import EVENT_TO_INT, UnsupportedEvent, log
from ..proto.Neonize_pb2 import (
    QR as QREv,
    PairStatus as PairStatusEv,
    Connected as ConnectedEv,
    KeepAliveTimeout as KeepAliveTimeoutEv,
    KeepAliveRestored as KeepAliveRestoredEv,
    LoggedOut as LoggedOutEv,
    StreamReplaced as StreamReplacedEv,
    TemporaryBan as TemporaryBanEv,
    ConnectFailure as ConnectFailureEv,
    ClientOutdated as ClientOutdatedEv,
    StreamError as StreamErrorEv,
    Disconnected as DisconnectedEv,
    HistorySync as HistorySyncEv,
    NewsLetterMessageMeta as NewsLetterMessageMetaEv,
    Message as MessageEv,
    Receipt as ReceiptEv,
    ChatPresence as ChatPresenceEv,
    Presence as PresenceEv,
    JoinedGroup as JoinedGroupEv,
    GroupInfoEvent as GroupInfoEv,
    Picture as PictureEv,
    IdentityChange as IdentityChangeEv,
    privacySettingsEvent as PrivacySettingsEv,
    OfflineSyncPreview as OfflineSyncPreviewEv,
    OfflineSyncCompleted as OfflineSyncCompletedEv,
    BlocklistEvent as BlocklistEv,
    BlocklistChange as BlocklistChangeEv,
    NewsletterJoin as NewsletterJoinEv,
    NewsletterLeave as NewsletterLeaveEv,
    NewsletterMuteChange as NewsletterMuteChangeEv,
    NewsletterLiveUpdate as NewsletterLiveUpdateEV,
    CallOffer as CallOfferEv,
    CallAccept as CallAcceptEv,
    CallPreAccept as CallPreAcceptEv,
    CallTransport as CallTransportEv,
    CallOfferNotice as CallOfferNoticeEv,
    CallRelayLatency as CallRelayLatencyEV,
    CallTerminate as CallTerminateEv,
    UnknownCallEvent as UnknownCallEventEV,
)

from google.protobuf.message import Message
from typing import Awaitable, Coroutine, Dict, Callable, Type, TypeVar, TYPE_CHECKING
from asyncio import Event as IOEvent

if TYPE_CHECKING:
    from .client import NewAClient
EventType = TypeVar("EventType", bound=Message)
event = IOEvent()


class Event:
    def __init__(self, client: NewAClient):
        """
        Initializes the Event class with a client of type NewClient.
        Also sets up a default blocking function and an empty dictionary for list functions.

        :param client: An instance of the NewClient class
        :type client: NewClient
        """
        self.client = client
        self.blocking_func = self.blocking(self.default_blocking)
        self.list_func: Dict[int, Callable[[int, int], None]] = {}
        self._qr = self.__onqr

    def execute(self, binary: int, size: int, code: int):
        """Executes a function from the list of functions based on the given code.

        :param binary: The binary data to be processed by the function.
        :type binary: int
        :param size: The size of the binary data.
        :type size: int
        :param code: The index of the function to be executed from the list of functions.
        :type code: int
        """
        self.list_func[code](binary, size)

    def wrap(
        self,
        f: Callable[[NewAClient, EventType], Awaitable[None]],
        event: Type[EventType],
    ):
        """
        This method wraps the function 'f' and returns a new function 'serialization' that
        takes two parameters - binary and size. The 'serialization' function calls 'f' with
        the client and an event deserialized from a string.

        :param f: Function to be wrapped. It should accept two parameters - a NewClient object and an EventType object.
        :type f: Callable[[NewClient, EventType], None]
        :param event: Type of the event.
        :type event: Type[EventType]
        :raises UnsupportedEvent: If the provided event is not supported.
        :return: Returns a function 'serialization' that accepts two parameters - binary and size.
        :rtype: Callable[[int, int], None]
        """
        if event not in EVENT_TO_INT:
            raise UnsupportedEvent()

        def serialization(binary: int, size: int):
            loop = asyncio.new_event_loop()
            awaitable = f(self.client, event.FromString(ctypes.string_at(binary, size)))
            loop.run_until_complete(awaitable)
            loop.close()

        return serialization

    async def __onqr(self, _: NewAClient, data_qr: bytes):
        """
        Handles QR code generation and display.

        :param _: The client instance (not used in the function).
        :type _: NewClient
        :param data_qr: The data to be encoded in the QR code.
        :type data_qr: bytes
        """
        segno.make_qr(data_qr).terminal(compact=True)

    def qr(self, f: Callable[[NewAClient, bytes], Awaitable[None]]):
        """
        Sets a callback function for handling QR code data.

        :param f: The callback function that takes a NewClient instance and QR code data in bytes.
        :type f: Callable[[NewClient, bytes], None]
        """
        self._qr = f

    @property
    def blocking(self):
        def block(f: Callable[[NewAClient], Awaitable[None]]):
            """This method assigns a blocking function to process a new client and prevents the process from ending.

            :param f: A function that takes a new client as an argument and returns nothing.
            :type f: Callable[[NewClient], None]
            """

            def wrap_blocking(_):
                loop = asyncio.new_event_loop()
                loop.run_until_complete(f(self.client))
                loop.close()

            self.blocking_func = wrap_blocking
            return self.blocking_func

        return block

    @classmethod
    async def default_blocking(cls, _):
        log.debug("🚧 The blocking function has been called.")
        await event.wait()
        log.debug("🚦 The function has been unblocked.")

    def __call__(
        self, event: Type[EventType]
    ) -> Callable[[Callable[[NewAClient, EventType], Awaitable[None]]], None]:
        """
        Registers a callback function for a specific event type.

        :param event: The type of event to register the callback for.
        :type event: Type[EventType]
        :return: A decorator that registers the callback function.
        :rtype: Callable[[Callable[[NewClient, EventType], None]], None]
        """

        def callback(func: Callable[[NewAClient, EventType], Awaitable[None]]) -> None:
            wrapped_func = self.wrap(func, event)
            self.list_func.update({EVENT_TO_INT[event]: wrapped_func})

        return callback