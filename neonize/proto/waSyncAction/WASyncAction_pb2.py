# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waSyncAction/WASyncAction.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 2, "", "waSyncAction/WASyncAction.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waChatLockSettings import (
    WAProtobufsChatLockSettings_pb2 as waChatLockSettings_dot_WAProtobufsChatLockSettings__pb2,
)
from waDeviceCapabilities import (
    WAProtobufsDeviceCapabilities_pb2 as waDeviceCapabilities_dot_WAProtobufsDeviceCapabilities__pb2,
)
from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fwaSyncAction/WASyncAction.proto\x12\x0cWASyncAction\x1a\x34waChatLockSettings/WAProtobufsChatLockSettings.proto\x1a\x38waDeviceCapabilities/WAProtobufsDeviceCapabilities.proto\x1a\x17waCommon/WACommon.proto"\xfa\x06\n\rCallLogRecord\x12:\n\ncallResult\x18\x01 \x01(\x0e\x32&.WASyncAction.CallLogRecord.CallResult\x12\x11\n\tisDndMode\x18\x02 \x01(\x08\x12@\n\rsilenceReason\x18\x03 \x01(\x0e\x32).WASyncAction.CallLogRecord.SilenceReason\x12\x10\n\x08\x64uration\x18\x04 \x01(\x03\x12\x11\n\tstartTime\x18\x05 \x01(\x03\x12\x12\n\nisIncoming\x18\x06 \x01(\x08\x12\x0f\n\x07isVideo\x18\x07 \x01(\x08\x12\x12\n\nisCallLink\x18\x08 \x01(\x08\x12\x15\n\rcallLinkToken\x18\t \x01(\t\x12\x17\n\x0fscheduledCallID\x18\n \x01(\t\x12\x0e\n\x06\x63\x61llID\x18\x0b \x01(\t\x12\x16\n\x0e\x63\x61llCreatorJID\x18\x0c \x01(\t\x12\x10\n\x08groupJID\x18\r \x01(\t\x12\x41\n\x0cparticipants\x18\x0e \x03(\x0b\x32+.WASyncAction.CallLogRecord.ParticipantInfo\x12\x36\n\x08\x63\x61llType\x18\x0f \x01(\x0e\x32$.WASyncAction.CallLogRecord.CallType\x1a^\n\x0fParticipantInfo\x12\x0f\n\x07userJID\x18\x01 \x01(\t\x12:\n\ncallResult\x18\x02 \x01(\x0e\x32&.WASyncAction.CallLogRecord.CallResult";\n\x08\x43\x61llType\x12\x0b\n\x07REGULAR\x10\x00\x12\x12\n\x0eSCHEDULED_CALL\x10\x01\x12\x0e\n\nVOICE_CHAT\x10\x02"F\n\rSilenceReason\x12\x08\n\x04NONE\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07PRIVACY\x10\x02\x12\x0f\n\x0bLIGHTWEIGHT\x10\x03"\xaf\x01\n\nCallResult\x12\r\n\tCONNECTED\x10\x00\x12\x0c\n\x08REJECTED\x10\x01\x12\r\n\tCANCELLED\x10\x02\x12\x15\n\x11\x41\x43\x43\x45PTEDELSEWHERE\x10\x03\x12\n\n\x06MISSED\x10\x04\x12\x0b\n\x07INVALID\x10\x05\x12\x0f\n\x0bUNAVAILABLE\x10\x06\x12\x0c\n\x08UPCOMING\x10\x07\x12\n\n\x06\x46\x41ILED\x10\x08\x12\r\n\tABANDONED\x10\t\x12\x0b\n\x07ONGOING\x10\n"\x8e\x01\n\x1cWaffleAccountLinkStateAction\x12N\n\tlinkState\x18\x02 \x01(\x0e\x32;.WASyncAction.WaffleAccountLinkStateAction.AccountLinkState"\x1e\n\x10\x41\x63\x63ountLinkState\x12\n\n\x06\x41\x43TIVE\x10\x00"\xc1\x01\n\x1cMerchantPaymentPartnerAction\x12\x41\n\x06status\x18\x01 \x02(\x0e\x32\x31.WASyncAction.MerchantPaymentPartnerAction.Status\x12\x0f\n\x07\x63ountry\x18\x02 \x02(\t\x12\x13\n\x0bgatewayName\x18\x03 \x01(\t\x12\x14\n\x0c\x63redentialID\x18\x04 \x01(\t""\n\x06Status\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01"\xc5\x01\n\x0eNoteEditAction\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.WASyncAction.NoteEditAction.NoteType\x12\x0f\n\x07\x63hatJID\x18\x02 \x01(\t\x12\x11\n\tcreatedAt\x18\x03 \x01(\x03\x12\x0f\n\x07\x64\x65leted\x18\x04 \x01(\x08\x12\x1b\n\x13unstructuredContent\x18\x05 \x01(\t",\n\x08NoteType\x12\x10\n\x0cUNSTRUCTURED\x10\x01\x12\x0e\n\nSTRUCTURED\x10\x02"\xb5\x01\n\x13StatusPrivacyAction\x12\x46\n\x04mode\x18\x01 \x01(\x0e\x32\x38.WASyncAction.StatusPrivacyAction.StatusDistributionMode\x12\x0f\n\x07userJID\x18\x02 \x03(\t"E\n\x16StatusDistributionMode\x12\x0e\n\nALLOW_LIST\x10\x00\x12\r\n\tDENY_LIST\x10\x01\x12\x0c\n\x08\x43ONTACTS\x10\x02"\x87\x02\n\x16MarketingMessageAction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12P\n\x04type\x18\x03 \x01(\x0e\x32\x42.WASyncAction.MarketingMessageAction.MarketingMessagePrototypeType\x12\x11\n\tcreatedAt\x18\x04 \x01(\x03\x12\x12\n\nlastSentAt\x18\x05 \x01(\x03\x12\x11\n\tisDeleted\x18\x06 \x01(\x08\x12\x0f\n\x07mediaID\x18\x07 \x01(\t"1\n\x1dMarketingMessagePrototypeType\x12\x10\n\x0cPERSONALIZED\x10\x00"\x8f\x01\n\x1bUsernameChatStartModeAction\x12N\n\rchatStartMode\x18\x01 \x01(\x0e\x32\x37.WASyncAction.UsernameChatStartModeAction.ChatStartMode" \n\rChatStartMode\x12\x07\n\x03LID\x10\x01\x12\x06\n\x02PN\x10\x02"\x8a\x02\n\x0fLabelEditAction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\x05\x12\x14\n\x0cpredefinedID\x18\x03 \x01(\x05\x12\x0f\n\x07\x64\x65leted\x18\x04 \x01(\x08\x12\x12\n\norderIndex\x18\x05 \x01(\x05\x12\x10\n\x08isActive\x18\x06 \x01(\x08\x12\x34\n\x04type\x18\x07 \x01(\x0e\x32&.WASyncAction.LabelEditAction.ListType"W\n\x08ListType\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06UNREAD\x10\x01\x12\n\n\x06GROUPS\x10\x02\x12\r\n\tFAVORITES\x10\x03\x12\x0e\n\nPREDEFINED\x10\x04\x12\n\n\x06\x43USTOM\x10\x05"\xa4\x03\n\x0ePatchDebugData\x12\x15\n\rcurrentLthash\x18\x01 \x01(\x0c\x12\x11\n\tnewLthash\x18\x02 \x01(\x0c\x12\x14\n\x0cpatchVersion\x18\x03 \x01(\x0c\x12\x16\n\x0e\x63ollectionName\x18\x04 \x01(\x0c\x12/\n\'firstFourBytesFromAHashOfSnapshotMACKey\x18\x05 \x01(\x0c\x12\x19\n\x11newLthashSubtract\x18\x06 \x01(\x0c\x12\x11\n\tnumberAdd\x18\x07 \x01(\x05\x12\x14\n\x0cnumberRemove\x18\x08 \x01(\x05\x12\x16\n\x0enumberOverride\x18\t \x01(\x05\x12=\n\x0esenderPlatform\x18\n \x01(\x0e\x32%.WASyncAction.PatchDebugData.Platform\x12\x17\n\x0fisSenderPrimary\x18\x0b \x01(\x08"U\n\x08Platform\x12\x0b\n\x07\x41NDROID\x10\x00\x12\x08\n\x04SMBA\x10\x01\x12\n\n\x06IPHONE\x10\x02\x12\x08\n\x04SMBI\x10\x03\x12\x07\n\x03WEB\x10\x04\x12\x07\n\x03UWP\x10\x05\x12\n\n\x06\x44\x41RWIN\x10\x06"2\n\x11RecentEmojiWeight\x12\r\n\x05\x65moji\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x02"\xd8\x1a\n\x0fSyncActionValue\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12,\n\nstarAction\x18\x02 \x01(\x0b\x32\x18.WASyncAction.StarAction\x12\x32\n\rcontactAction\x18\x03 \x01(\x0b\x32\x1b.WASyncAction.ContactAction\x12,\n\nmuteAction\x18\x04 \x01(\x0b\x32\x18.WASyncAction.MuteAction\x12*\n\tpinAction\x18\x05 \x01(\x0b\x32\x17.WASyncAction.PinAction\x12N\n\x1bsecurityNotificationSetting\x18\x06 \x01(\x0b\x32).WASyncAction.SecurityNotificationSetting\x12\x36\n\x0fpushNameSetting\x18\x07 \x01(\x0b\x32\x1d.WASyncAction.PushNameSetting\x12\x38\n\x10quickReplyAction\x18\x08 \x01(\x0b\x32\x1e.WASyncAction.QuickReplyAction\x12H\n\x18recentEmojiWeightsAction\x18\x0b \x01(\x0b\x32&.WASyncAction.RecentEmojiWeightsAction\x12\x36\n\x0flabelEditAction\x18\x0e \x01(\x0b\x32\x1d.WASyncAction.LabelEditAction\x12\x44\n\x16labelAssociationAction\x18\x0f \x01(\x0b\x32$.WASyncAction.LabelAssociationAction\x12\x32\n\rlocaleSetting\x18\x10 \x01(\x0b\x32\x1b.WASyncAction.LocaleSetting\x12:\n\x11\x61rchiveChatAction\x18\x11 \x01(\x0b\x32\x1f.WASyncAction.ArchiveChatAction\x12H\n\x18\x64\x65leteMessageForMeAction\x18\x12 \x01(\x0b\x32&.WASyncAction.DeleteMessageForMeAction\x12\x32\n\rkeyExpiration\x18\x13 \x01(\x0b\x32\x1b.WASyncAction.KeyExpiration\x12@\n\x14markChatAsReadAction\x18\x14 \x01(\x0b\x32".WASyncAction.MarkChatAsReadAction\x12\x36\n\x0f\x63learChatAction\x18\x15 \x01(\x0b\x32\x1d.WASyncAction.ClearChatAction\x12\x38\n\x10\x64\x65leteChatAction\x18\x16 \x01(\x0b\x32\x1e.WASyncAction.DeleteChatAction\x12\x42\n\x15unarchiveChatsSetting\x18\x17 \x01(\x0b\x32#.WASyncAction.UnarchiveChatsSetting\x12\x34\n\x0eprimaryFeature\x18\x18 \x01(\x0b\x32\x1c.WASyncAction.PrimaryFeature\x12J\n\x19\x61ndroidUnsupportedActions\x18\x1a \x01(\x0b\x32\'.WASyncAction.AndroidUnsupportedActions\x12.\n\x0b\x61gentAction\x18\x1b \x01(\x0b\x32\x19.WASyncAction.AgentAction\x12<\n\x12subscriptionAction\x18\x1c \x01(\x0b\x32 .WASyncAction.SubscriptionAction\x12@\n\x14userStatusMuteAction\x18\x1d \x01(\x0b\x32".WASyncAction.UserStatusMuteAction\x12\x38\n\x10timeFormatAction\x18\x1e \x01(\x0b\x32\x1e.WASyncAction.TimeFormatAction\x12*\n\tnuxAction\x18\x1f \x01(\x0b\x32\x17.WASyncAction.NuxAction\x12@\n\x14primaryVersionAction\x18  \x01(\x0b\x32".WASyncAction.PrimaryVersionAction\x12\x32\n\rstickerAction\x18! \x01(\x0b\x32\x1b.WASyncAction.StickerAction\x12J\n\x19removeRecentStickerAction\x18" \x01(\x0b\x32\'.WASyncAction.RemoveRecentStickerAction\x12:\n\x0e\x63hatAssignment\x18# \x01(\x0b\x32".WASyncAction.ChatAssignmentAction\x12R\n\x1a\x63hatAssignmentOpenedStatus\x18$ \x01(\x0b\x32..WASyncAction.ChatAssignmentOpenedStatusAction\x12<\n\x12pnForLidChatAction\x18% \x01(\x0b\x32 .WASyncAction.PnForLidChatAction\x12\x44\n\x16marketingMessageAction\x18& \x01(\x0b\x32$.WASyncAction.MarketingMessageAction\x12V\n\x1fmarketingMessageBroadcastAction\x18\' \x01(\x0b\x32-.WASyncAction.MarketingMessageBroadcastAction\x12\x42\n\x15\x65xternalWebBetaAction\x18( \x01(\x0b\x32#.WASyncAction.ExternalWebBetaAction\x12N\n\x1bprivacySettingRelayAllCalls\x18) \x01(\x0b\x32).WASyncAction.PrivacySettingRelayAllCalls\x12\x32\n\rcallLogAction\x18* \x01(\x0b\x32\x1b.WASyncAction.CallLogAction\x12\x38\n\rstatusPrivacy\x18, \x01(\x0b\x32!.WASyncAction.StatusPrivacyAction\x12\x46\n\x17\x62otWelcomeRequestAction\x18- \x01(\x0b\x32%.WASyncAction.BotWelcomeRequestAction\x12L\n\x17\x64\x65leteIndividualCallLog\x18. \x01(\x0b\x32+.WASyncAction.DeleteIndividualCallLogAction\x12\x42\n\x15labelReorderingAction\x18/ \x01(\x0b\x32#.WASyncAction.LabelReorderingAction\x12:\n\x11paymentInfoAction\x18\x30 \x01(\x0b\x32\x1f.WASyncAction.PaymentInfoAction\x12L\n\x1a\x63ustomPaymentMethodsAction\x18\x31 \x01(\x0b\x32(.WASyncAction.CustomPaymentMethodsAction\x12\x34\n\x0elockChatAction\x18\x32 \x01(\x0b\x32\x1c.WASyncAction.LockChatAction\x12G\n\x10\x63hatLockSettings\x18\x33 \x01(\x0b\x32-.WAProtobufsChatLockSettings.ChatLockSettings\x12H\n\x18wamoUserIdentifierAction\x18\x34 \x01(\x0b\x32&.WASyncAction.WamoUserIdentifierAction\x12\x66\n\'privacySettingDisableLinkPreviewsAction\x18\x35 \x01(\x0b\x32\x35.WASyncAction.PrivacySettingDisableLinkPreviewsAction\x12M\n\x12\x64\x65viceCapabilities\x18\x36 \x01(\x0b\x32\x31.WAProtobufsDeviceCapabilities.DeviceCapabilities\x12\x34\n\x0enoteEditAction\x18\x37 \x01(\x0b\x32\x1c.WASyncAction.NoteEditAction\x12\x36\n\x0f\x66\x61voritesAction\x18\x38 \x01(\x0b\x32\x1d.WASyncAction.FavoritesAction\x12P\n\x1cmerchantPaymentPartnerAction\x18\x39 \x01(\x0b\x32*.WASyncAction.MerchantPaymentPartnerAction\x12P\n\x1cwaffleAccountLinkStateAction\x18: \x01(\x0b\x32*.WASyncAction.WaffleAccountLinkStateAction\x12H\n\x15usernameChatStartMode\x18; \x01(\x0b\x32).WASyncAction.UsernameChatStartModeAction"d\n\x0f\x46\x61voritesAction\x12\x39\n\tfavorites\x18\x01 \x03(\x0b\x32&.WASyncAction.FavoritesAction.Favorite\x1a\x16\n\x08\x46\x61vorite\x12\n\n\x02ID\x18\x01 \x01(\t"E\n\'PrivacySettingDisableLinkPreviewsAction\x12\x1a\n\x12isPreviewsDisabled\x18\x01 \x01(\x08".\n\x18WamoUserIdentifierAction\x12\x12\n\nidentifier\x18\x01 \x01(\t" \n\x0eLockChatAction\x12\x0e\n\x06locked\x18\x01 \x01(\x08"]\n\x1a\x43ustomPaymentMethodsAction\x12?\n\x14\x63ustomPaymentMethods\x18\x01 \x03(\x0b\x32!.WASyncAction.CustomPaymentMethod"\x87\x01\n\x13\x43ustomPaymentMethod\x12\x14\n\x0c\x63redentialID\x18\x01 \x02(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\x12;\n\x08metadata\x18\x04 \x03(\x0b\x32).WASyncAction.CustomPaymentMethodMetadata"9\n\x1b\x43ustomPaymentMethodMetadata\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t" \n\x11PaymentInfoAction\x12\x0b\n\x03\x63pi\x18\x01 \x01(\t"/\n\x15LabelReorderingAction\x12\x16\n\x0esortedLabelIDs\x18\x01 \x03(\x05"D\n\x1d\x44\x65leteIndividualCallLogAction\x12\x0f\n\x07peerJID\x18\x01 \x01(\t\x12\x12\n\nisIncoming\x18\x02 \x01(\x08")\n\x17\x42otWelcomeRequestAction\x12\x0e\n\x06isSent\x18\x01 \x01(\x08"C\n\rCallLogAction\x12\x32\n\rcallLogRecord\x18\x01 \x01(\x0b\x32\x1b.WASyncAction.CallLogRecord"0\n\x1bPrivacySettingRelayAllCalls\x12\x11\n\tisEnabled\x18\x01 \x01(\x08"(\n\x15\x45xternalWebBetaAction\x12\x0f\n\x07isOptIn\x18\x01 \x01(\x08"7\n\x1fMarketingMessageBroadcastAction\x12\x14\n\x0crepliedCount\x18\x01 \x01(\x05"#\n\x12PnForLidChatAction\x12\r\n\x05pnJID\x18\x01 \x01(\t"6\n ChatAssignmentOpenedStatusAction\x12\x12\n\nchatOpened\x18\x01 \x01(\x08"-\n\x14\x43hatAssignmentAction\x12\x15\n\rdeviceAgentID\x18\x01 \x01(\t"\xda\x01\n\rStickerAction\x12\x0b\n\x03URL\x18\x01 \x01(\t\x12\x15\n\rfileEncSHA256\x18\x02 \x01(\x0c\x12\x10\n\x08mediaKey\x18\x03 \x01(\x0c\x12\x10\n\x08mimetype\x18\x04 \x01(\t\x12\x0e\n\x06height\x18\x05 \x01(\r\x12\r\n\x05width\x18\x06 \x01(\r\x12\x12\n\ndirectPath\x18\x07 \x01(\t\x12\x12\n\nfileLength\x18\x08 \x01(\x04\x12\x12\n\nisFavorite\x18\t \x01(\x08\x12\x14\n\x0c\x64\x65viceIDHint\x18\n \x01(\r\x12\x10\n\x08isLottie\x18\x0b \x01(\x08"6\n\x19RemoveRecentStickerAction\x12\x19\n\x11lastStickerSentTS\x18\x01 \x01(\x03"\'\n\x14PrimaryVersionAction\x12\x0f\n\x07version\x18\x01 \x01(\t"!\n\tNuxAction\x12\x14\n\x0c\x61\x63knowledged\x18\x01 \x01(\x08"9\n\x10TimeFormatAction\x12%\n\x1disTwentyFourHourFormatEnabled\x18\x01 \x01(\x08"%\n\x14UserStatusMuteAction\x12\r\n\x05muted\x18\x01 \x01(\x08"[\n\x12SubscriptionAction\x12\x15\n\risDeactivated\x18\x01 \x01(\x08\x12\x16\n\x0eisAutoRenewing\x18\x02 \x01(\x08\x12\x16\n\x0e\x65xpirationDate\x18\x03 \x01(\x03"@\n\x0b\x41gentAction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65viceID\x18\x02 \x01(\x05\x12\x11\n\tisDeleted\x18\x03 \x01(\x08",\n\x19\x41ndroidUnsupportedActions\x12\x0f\n\x07\x61llowed\x18\x01 \x01(\x08"\x1f\n\x0ePrimaryFeature\x12\r\n\x05\x66lags\x18\x01 \x03(\t"(\n\rKeyExpiration\x12\x17\n\x0f\x65xpiredKeyEpoch\x18\x01 \x01(\x05"I\n\x11SyncActionMessage\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x11\n\ttimestamp\x18\x02 \x01(\x03"\x8d\x01\n\x16SyncActionMessageRange\x12\x1c\n\x14lastMessageTimestamp\x18\x01 \x01(\x03\x12"\n\x1alastSystemMessageTimestamp\x18\x02 \x01(\x03\x12\x31\n\x08messages\x18\x03 \x03(\x0b\x32\x1f.WASyncAction.SyncActionMessage"/\n\x15UnarchiveChatsSetting\x12\x16\n\x0eunarchiveChats\x18\x01 \x01(\x08"N\n\x10\x44\x65leteChatAction\x12:\n\x0cmessageRange\x18\x01 \x01(\x0b\x32$.WASyncAction.SyncActionMessageRange"M\n\x0f\x43learChatAction\x12:\n\x0cmessageRange\x18\x01 \x01(\x0b\x32$.WASyncAction.SyncActionMessageRange"`\n\x14MarkChatAsReadAction\x12\x0c\n\x04read\x18\x01 \x01(\x08\x12:\n\x0cmessageRange\x18\x02 \x01(\x0b\x32$.WASyncAction.SyncActionMessageRange"I\n\x18\x44\x65leteMessageForMeAction\x12\x13\n\x0b\x64\x65leteMedia\x18\x01 \x01(\x08\x12\x18\n\x10messageTimestamp\x18\x02 \x01(\x03"a\n\x11\x41rchiveChatAction\x12\x10\n\x08\x61rchived\x18\x01 \x01(\x08\x12:\n\x0cmessageRange\x18\x02 \x01(\x0b\x32$.WASyncAction.SyncActionMessageRange"L\n\x18RecentEmojiWeightsAction\x12\x30\n\x07weights\x18\x01 \x03(\x0b\x32\x1f.WASyncAction.RecentEmojiWeight")\n\x16LabelAssociationAction\x12\x0f\n\x07labeled\x18\x01 \x01(\x08"g\n\x10QuickReplyAction\x12\x10\n\x08shortcut\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x10\n\x08keywords\x18\x03 \x03(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x12\x0f\n\x07\x64\x65leted\x18\x05 \x01(\x08"\x1f\n\rLocaleSetting\x12\x0e\n\x06locale\x18\x01 \x01(\t"\x1f\n\x0fPushNameSetting\x12\x0c\n\x04name\x18\x01 \x01(\t"7\n\x1bSecurityNotificationSetting\x12\x18\n\x10showNotification\x18\x01 \x01(\x08"\x1b\n\tPinAction\x12\x0e\n\x06pinned\x18\x01 \x01(\x08"H\n\nMuteAction\x12\r\n\x05muted\x18\x01 \x01(\x08\x12\x18\n\x10muteEndTimestamp\x18\x02 \x01(\x03\x12\x11\n\tautoMuted\x18\x03 \x01(\x08"f\n\rContactAction\x12\x10\n\x08\x66ullName\x18\x01 \x01(\t\x12\x11\n\tfirstName\x18\x02 \x01(\t\x12\x0e\n\x06lidJID\x18\x03 \x01(\t\x12 \n\x18saveOnPrimaryAddressbook\x18\x04 \x01(\x08"\x1d\n\nStarAction\x12\x0f\n\x07starred\x18\x01 \x01(\x08"o\n\x0eSyncActionData\x12\r\n\x05index\x18\x01 \x01(\x0c\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.WASyncAction.SyncActionValue\x12\x0f\n\x07padding\x18\x03 \x01(\x0c\x12\x0f\n\x07version\x18\x04 \x01(\x05\x42(Z&go.mau.fi/whatsmeow/proto/waSyncAction'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "waSyncAction.WASyncAction_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"Z&go.mau.fi/whatsmeow/proto/waSyncAction"
    _globals["_CALLLOGRECORD"]._serialized_start = 187
    _globals["_CALLLOGRECORD"]._serialized_end = 1077
    _globals["_CALLLOGRECORD_PARTICIPANTINFO"]._serialized_start = 672
    _globals["_CALLLOGRECORD_PARTICIPANTINFO"]._serialized_end = 766
    _globals["_CALLLOGRECORD_CALLTYPE"]._serialized_start = 768
    _globals["_CALLLOGRECORD_CALLTYPE"]._serialized_end = 827
    _globals["_CALLLOGRECORD_SILENCEREASON"]._serialized_start = 829
    _globals["_CALLLOGRECORD_SILENCEREASON"]._serialized_end = 899
    _globals["_CALLLOGRECORD_CALLRESULT"]._serialized_start = 902
    _globals["_CALLLOGRECORD_CALLRESULT"]._serialized_end = 1077
    _globals["_WAFFLEACCOUNTLINKSTATEACTION"]._serialized_start = 1080
    _globals["_WAFFLEACCOUNTLINKSTATEACTION"]._serialized_end = 1222
    _globals["_WAFFLEACCOUNTLINKSTATEACTION_ACCOUNTLINKSTATE"]._serialized_start = 1192
    _globals["_WAFFLEACCOUNTLINKSTATEACTION_ACCOUNTLINKSTATE"]._serialized_end = 1222
    _globals["_MERCHANTPAYMENTPARTNERACTION"]._serialized_start = 1225
    _globals["_MERCHANTPAYMENTPARTNERACTION"]._serialized_end = 1418
    _globals["_MERCHANTPAYMENTPARTNERACTION_STATUS"]._serialized_start = 1384
    _globals["_MERCHANTPAYMENTPARTNERACTION_STATUS"]._serialized_end = 1418
    _globals["_NOTEEDITACTION"]._serialized_start = 1421
    _globals["_NOTEEDITACTION"]._serialized_end = 1618
    _globals["_NOTEEDITACTION_NOTETYPE"]._serialized_start = 1574
    _globals["_NOTEEDITACTION_NOTETYPE"]._serialized_end = 1618
    _globals["_STATUSPRIVACYACTION"]._serialized_start = 1621
    _globals["_STATUSPRIVACYACTION"]._serialized_end = 1802
    _globals["_STATUSPRIVACYACTION_STATUSDISTRIBUTIONMODE"]._serialized_start = 1733
    _globals["_STATUSPRIVACYACTION_STATUSDISTRIBUTIONMODE"]._serialized_end = 1802
    _globals["_MARKETINGMESSAGEACTION"]._serialized_start = 1805
    _globals["_MARKETINGMESSAGEACTION"]._serialized_end = 2068
    _globals[
        "_MARKETINGMESSAGEACTION_MARKETINGMESSAGEPROTOTYPETYPE"
    ]._serialized_start = 2019
    _globals[
        "_MARKETINGMESSAGEACTION_MARKETINGMESSAGEPROTOTYPETYPE"
    ]._serialized_end = 2068
    _globals["_USERNAMECHATSTARTMODEACTION"]._serialized_start = 2071
    _globals["_USERNAMECHATSTARTMODEACTION"]._serialized_end = 2214
    _globals["_USERNAMECHATSTARTMODEACTION_CHATSTARTMODE"]._serialized_start = 2182
    _globals["_USERNAMECHATSTARTMODEACTION_CHATSTARTMODE"]._serialized_end = 2214
    _globals["_LABELEDITACTION"]._serialized_start = 2217
    _globals["_LABELEDITACTION"]._serialized_end = 2483
    _globals["_LABELEDITACTION_LISTTYPE"]._serialized_start = 2396
    _globals["_LABELEDITACTION_LISTTYPE"]._serialized_end = 2483
    _globals["_PATCHDEBUGDATA"]._serialized_start = 2486
    _globals["_PATCHDEBUGDATA"]._serialized_end = 2906
    _globals["_PATCHDEBUGDATA_PLATFORM"]._serialized_start = 2821
    _globals["_PATCHDEBUGDATA_PLATFORM"]._serialized_end = 2906
    _globals["_RECENTEMOJIWEIGHT"]._serialized_start = 2908
    _globals["_RECENTEMOJIWEIGHT"]._serialized_end = 2958
    _globals["_SYNCACTIONVALUE"]._serialized_start = 2961
    _globals["_SYNCACTIONVALUE"]._serialized_end = 6377
    _globals["_FAVORITESACTION"]._serialized_start = 6379
    _globals["_FAVORITESACTION"]._serialized_end = 6479
    _globals["_FAVORITESACTION_FAVORITE"]._serialized_start = 6457
    _globals["_FAVORITESACTION_FAVORITE"]._serialized_end = 6479
    _globals["_PRIVACYSETTINGDISABLELINKPREVIEWSACTION"]._serialized_start = 6481
    _globals["_PRIVACYSETTINGDISABLELINKPREVIEWSACTION"]._serialized_end = 6550
    _globals["_WAMOUSERIDENTIFIERACTION"]._serialized_start = 6552
    _globals["_WAMOUSERIDENTIFIERACTION"]._serialized_end = 6598
    _globals["_LOCKCHATACTION"]._serialized_start = 6600
    _globals["_LOCKCHATACTION"]._serialized_end = 6632
    _globals["_CUSTOMPAYMENTMETHODSACTION"]._serialized_start = 6634
    _globals["_CUSTOMPAYMENTMETHODSACTION"]._serialized_end = 6727
    _globals["_CUSTOMPAYMENTMETHOD"]._serialized_start = 6730
    _globals["_CUSTOMPAYMENTMETHOD"]._serialized_end = 6865
    _globals["_CUSTOMPAYMENTMETHODMETADATA"]._serialized_start = 6867
    _globals["_CUSTOMPAYMENTMETHODMETADATA"]._serialized_end = 6924
    _globals["_PAYMENTINFOACTION"]._serialized_start = 6926
    _globals["_PAYMENTINFOACTION"]._serialized_end = 6958
    _globals["_LABELREORDERINGACTION"]._serialized_start = 6960
    _globals["_LABELREORDERINGACTION"]._serialized_end = 7007
    _globals["_DELETEINDIVIDUALCALLLOGACTION"]._serialized_start = 7009
    _globals["_DELETEINDIVIDUALCALLLOGACTION"]._serialized_end = 7077
    _globals["_BOTWELCOMEREQUESTACTION"]._serialized_start = 7079
    _globals["_BOTWELCOMEREQUESTACTION"]._serialized_end = 7120
    _globals["_CALLLOGACTION"]._serialized_start = 7122
    _globals["_CALLLOGACTION"]._serialized_end = 7189
    _globals["_PRIVACYSETTINGRELAYALLCALLS"]._serialized_start = 7191
    _globals["_PRIVACYSETTINGRELAYALLCALLS"]._serialized_end = 7239
    _globals["_EXTERNALWEBBETAACTION"]._serialized_start = 7241
    _globals["_EXTERNALWEBBETAACTION"]._serialized_end = 7281
    _globals["_MARKETINGMESSAGEBROADCASTACTION"]._serialized_start = 7283
    _globals["_MARKETINGMESSAGEBROADCASTACTION"]._serialized_end = 7338
    _globals["_PNFORLIDCHATACTION"]._serialized_start = 7340
    _globals["_PNFORLIDCHATACTION"]._serialized_end = 7375
    _globals["_CHATASSIGNMENTOPENEDSTATUSACTION"]._serialized_start = 7377
    _globals["_CHATASSIGNMENTOPENEDSTATUSACTION"]._serialized_end = 7431
    _globals["_CHATASSIGNMENTACTION"]._serialized_start = 7433
    _globals["_CHATASSIGNMENTACTION"]._serialized_end = 7478
    _globals["_STICKERACTION"]._serialized_start = 7481
    _globals["_STICKERACTION"]._serialized_end = 7699
    _globals["_REMOVERECENTSTICKERACTION"]._serialized_start = 7701
    _globals["_REMOVERECENTSTICKERACTION"]._serialized_end = 7755
    _globals["_PRIMARYVERSIONACTION"]._serialized_start = 7757
    _globals["_PRIMARYVERSIONACTION"]._serialized_end = 7796
    _globals["_NUXACTION"]._serialized_start = 7798
    _globals["_NUXACTION"]._serialized_end = 7831
    _globals["_TIMEFORMATACTION"]._serialized_start = 7833
    _globals["_TIMEFORMATACTION"]._serialized_end = 7890
    _globals["_USERSTATUSMUTEACTION"]._serialized_start = 7892
    _globals["_USERSTATUSMUTEACTION"]._serialized_end = 7929
    _globals["_SUBSCRIPTIONACTION"]._serialized_start = 7931
    _globals["_SUBSCRIPTIONACTION"]._serialized_end = 8022
    _globals["_AGENTACTION"]._serialized_start = 8024
    _globals["_AGENTACTION"]._serialized_end = 8088
    _globals["_ANDROIDUNSUPPORTEDACTIONS"]._serialized_start = 8090
    _globals["_ANDROIDUNSUPPORTEDACTIONS"]._serialized_end = 8134
    _globals["_PRIMARYFEATURE"]._serialized_start = 8136
    _globals["_PRIMARYFEATURE"]._serialized_end = 8167
    _globals["_KEYEXPIRATION"]._serialized_start = 8169
    _globals["_KEYEXPIRATION"]._serialized_end = 8209
    _globals["_SYNCACTIONMESSAGE"]._serialized_start = 8211
    _globals["_SYNCACTIONMESSAGE"]._serialized_end = 8284
    _globals["_SYNCACTIONMESSAGERANGE"]._serialized_start = 8287
    _globals["_SYNCACTIONMESSAGERANGE"]._serialized_end = 8428
    _globals["_UNARCHIVECHATSSETTING"]._serialized_start = 8430
    _globals["_UNARCHIVECHATSSETTING"]._serialized_end = 8477
    _globals["_DELETECHATACTION"]._serialized_start = 8479
    _globals["_DELETECHATACTION"]._serialized_end = 8557
    _globals["_CLEARCHATACTION"]._serialized_start = 8559
    _globals["_CLEARCHATACTION"]._serialized_end = 8636
    _globals["_MARKCHATASREADACTION"]._serialized_start = 8638
    _globals["_MARKCHATASREADACTION"]._serialized_end = 8734
    _globals["_DELETEMESSAGEFORMEACTION"]._serialized_start = 8736
    _globals["_DELETEMESSAGEFORMEACTION"]._serialized_end = 8809
    _globals["_ARCHIVECHATACTION"]._serialized_start = 8811
    _globals["_ARCHIVECHATACTION"]._serialized_end = 8908
    _globals["_RECENTEMOJIWEIGHTSACTION"]._serialized_start = 8910
    _globals["_RECENTEMOJIWEIGHTSACTION"]._serialized_end = 8986
    _globals["_LABELASSOCIATIONACTION"]._serialized_start = 8988
    _globals["_LABELASSOCIATIONACTION"]._serialized_end = 9029
    _globals["_QUICKREPLYACTION"]._serialized_start = 9031
    _globals["_QUICKREPLYACTION"]._serialized_end = 9134
    _globals["_LOCALESETTING"]._serialized_start = 9136
    _globals["_LOCALESETTING"]._serialized_end = 9167
    _globals["_PUSHNAMESETTING"]._serialized_start = 9169
    _globals["_PUSHNAMESETTING"]._serialized_end = 9200
    _globals["_SECURITYNOTIFICATIONSETTING"]._serialized_start = 9202
    _globals["_SECURITYNOTIFICATIONSETTING"]._serialized_end = 9257
    _globals["_PINACTION"]._serialized_start = 9259
    _globals["_PINACTION"]._serialized_end = 9286
    _globals["_MUTEACTION"]._serialized_start = 9288
    _globals["_MUTEACTION"]._serialized_end = 9360
    _globals["_CONTACTACTION"]._serialized_start = 9362
    _globals["_CONTACTACTION"]._serialized_end = 9464
    _globals["_STARACTION"]._serialized_start = 9466
    _globals["_STARACTION"]._serialized_end = 9495
    _globals["_SYNCACTIONDATA"]._serialized_start = 9497
    _globals["_SYNCACTIONDATA"]._serialized_end = 9608
# @@protoc_insertion_point(module_scope)
