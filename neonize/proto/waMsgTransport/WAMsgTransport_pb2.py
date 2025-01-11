# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waMsgTransport/WAMsgTransport.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 2, "", "waMsgTransport/WAMsgTransport.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#waMsgTransport/WAMsgTransport.proto\x12\x0eWAMsgTransport\x1a\x17waCommon/WACommon.proto"\xa4\r\n\x10MessageTransport\x12\x39\n\x07payload\x18\x01 \x01(\x0b\x32(.WAMsgTransport.MessageTransport.Payload\x12;\n\x08protocol\x18\x02 \x01(\x0b\x32).WAMsgTransport.MessageTransport.Protocol\x1ap\n\x07Payload\x12\x31\n\x12\x61pplicationPayload\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12\x32\n\x0b\x66utureProof\x18\x03 \x01(\x0e\x32\x1d.WACommon.FutureProofBehavior\x1a\xa5\x0b\n\x08Protocol\x12\x44\n\x08integral\x18\x01 \x01(\x0b\x32\x32.WAMsgTransport.MessageTransport.Protocol.Integral\x12\x46\n\tancillary\x18\x02 \x01(\x0b\x32\x33.WAMsgTransport.MessageTransport.Protocol.Ancillary\x1a\xdd\x08\n\tAncillary\x12^\n\x04skdm\x18\x02 \x01(\x0b\x32P.WAMsgTransport.MessageTransport.Protocol.Ancillary.SenderKeyDistributionMessage\x12>\n\x12\x64\x65viceListMetadata\x18\x03 \x01(\x0b\x32".WAMsgTransport.DeviceListMetadata\x12X\n\x04icdc\x18\x04 \x01(\x0b\x32J.WAMsgTransport.MessageTransport.Protocol.Ancillary.ICDCParticipantDevices\x12\\\n\x0f\x62\x61\x63kupDirective\x18\x05 \x01(\x0b\x32\x43.WAMsgTransport.MessageTransport.Protocol.Ancillary.BackupDirective\x1a\xe8\x01\n\x0f\x42\x61\x63kupDirective\x12\x11\n\tmessageID\x18\x01 \x01(\t\x12\x62\n\nactionType\x18\x02 \x01(\x0e\x32N.WAMsgTransport.MessageTransport.Protocol.Ancillary.BackupDirective.ActionType\x12\x17\n\x0fsupplementalKey\x18\x03 \x01(\t"E\n\nActionType\x12\x08\n\x04NOOP\x10\x00\x12\n\n\x06UPSERT\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\x15\n\x11UPSERT_AND_DELETE\x10\x03\x1a\xae\x03\n\x16ICDCParticipantDevices\x12~\n\x0esenderIdentity\x18\x01 \x01(\x0b\x32\x66.WAMsgTransport.MessageTransport.Protocol.Ancillary.ICDCParticipantDevices.ICDCIdentityListDescription\x12\x83\x01\n\x13recipientIdentities\x18\x02 \x03(\x0b\x32\x66.WAMsgTransport.MessageTransport.Protocol.Ancillary.ICDCParticipantDevices.ICDCIdentityListDescription\x12\x19\n\x11recipientUserJIDs\x18\x03 \x03(\t\x1as\n\x1bICDCIdentityListDescription\x12\x0b\n\x03seq\x18\x01 \x01(\x05\x12\x15\n\rsigningDevice\x18\x02 \x01(\x0c\x12\x16\n\x0eunknownDevices\x18\x03 \x03(\x0c\x12\x18\n\x10unknownDeviceIDs\x18\x04 \x03(\x05\x1a\\\n\x1cSenderKeyDistributionMessage\x12\x0f\n\x07groupID\x18\x01 \x01(\t\x12+\n#axolotlSenderKeyDistributionMessage\x18\x02 \x01(\x0c\x1a\xaa\x01\n\x08Integral\x12\x0f\n\x07padding\x18\x01 \x01(\x0c\x12Q\n\x03\x44SM\x18\x02 \x01(\x0b\x32\x44.WAMsgTransport.MessageTransport.Protocol.Integral.DeviceSentMessage\x1a:\n\x11\x44\x65viceSentMessage\x12\x16\n\x0e\x64\x65stinationJID\x18\x01 \x01(\t\x12\r\n\x05phash\x18\x02 \x01(\t"z\n\x12\x44\x65viceListMetadata\x12\x15\n\rsenderKeyHash\x18\x01 \x01(\x0c\x12\x17\n\x0fsenderTimestamp\x18\x02 \x01(\x04\x12\x18\n\x10recipientKeyHash\x18\x08 \x01(\x0c\x12\x1a\n\x12recipientTimestamp\x18\t \x01(\x04\x42*Z(go.mau.fi/whatsmeow/proto/waMsgTransport'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "waMsgTransport.WAMsgTransport_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"Z(go.mau.fi/whatsmeow/proto/waMsgTransport"
    _globals["_MESSAGETRANSPORT"]._serialized_start = 81
    _globals["_MESSAGETRANSPORT"]._serialized_end = 1781
    _globals["_MESSAGETRANSPORT_PAYLOAD"]._serialized_start = 221
    _globals["_MESSAGETRANSPORT_PAYLOAD"]._serialized_end = 333
    _globals["_MESSAGETRANSPORT_PROTOCOL"]._serialized_start = 336
    _globals["_MESSAGETRANSPORT_PROTOCOL"]._serialized_end = 1781
    _globals["_MESSAGETRANSPORT_PROTOCOL_ANCILLARY"]._serialized_start = 491
    _globals["_MESSAGETRANSPORT_PROTOCOL_ANCILLARY"]._serialized_end = 1608
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_BACKUPDIRECTIVE"
    ]._serialized_start = 849
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_BACKUPDIRECTIVE"
    ]._serialized_end = 1081
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_BACKUPDIRECTIVE_ACTIONTYPE"
    ]._serialized_start = 1012
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_BACKUPDIRECTIVE_ACTIONTYPE"
    ]._serialized_end = 1081
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_ICDCPARTICIPANTDEVICES"
    ]._serialized_start = 1084
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_ICDCPARTICIPANTDEVICES"
    ]._serialized_end = 1514
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_ICDCPARTICIPANTDEVICES_ICDCIDENTITYLISTDESCRIPTION"
    ]._serialized_start = 1399
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_ICDCPARTICIPANTDEVICES_ICDCIDENTITYLISTDESCRIPTION"
    ]._serialized_end = 1514
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_SENDERKEYDISTRIBUTIONMESSAGE"
    ]._serialized_start = 1516
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_ANCILLARY_SENDERKEYDISTRIBUTIONMESSAGE"
    ]._serialized_end = 1608
    _globals["_MESSAGETRANSPORT_PROTOCOL_INTEGRAL"]._serialized_start = 1611
    _globals["_MESSAGETRANSPORT_PROTOCOL_INTEGRAL"]._serialized_end = 1781
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_INTEGRAL_DEVICESENTMESSAGE"
    ]._serialized_start = 1723
    _globals[
        "_MESSAGETRANSPORT_PROTOCOL_INTEGRAL_DEVICESENTMESSAGE"
    ]._serialized_end = 1781
    _globals["_DEVICELISTMETADATA"]._serialized_start = 1783
    _globals["_DEVICELISTMETADATA"]._serialized_end = 1905
# @@protoc_insertion_point(module_scope)
