# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waWeb/WAWebProtobufsWeb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waE2E import WAWebProtobufsE2E_pb2 as waE2E_dot_WAWebProtobufsE2E__pb2
from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwaWeb/WAWebProtobufsWeb.proto\x12\x11WAWebProtobufsWeb\x1a\x1dwaE2E/WAWebProtobufsE2E.proto\x1a\x17waCommon/WACommon.proto\"\xefL\n\x0eWebMessageInfo\x12!\n\x03key\x18\x01 \x02(\x0b\x32\x14.WACommon.MessageKey\x12+\n\x07message\x18\x02 \x01(\x0b\x32\x1a.WAWebProtobufsE2E.Message\x12\x18\n\x10messageTimestamp\x18\x03 \x01(\x04\x12\x38\n\x06status\x18\x04 \x01(\x0e\x32(.WAWebProtobufsWeb.WebMessageInfo.Status\x12\x13\n\x0bparticipant\x18\x05 \x01(\t\x12\x1b\n\x13messageC2STimestamp\x18\x06 \x01(\x04\x12\x0e\n\x06ignore\x18\x10 \x01(\x08\x12\x0f\n\x07starred\x18\x11 \x01(\x08\x12\x11\n\tbroadcast\x18\x12 \x01(\x08\x12\x10\n\x08pushName\x18\x13 \x01(\t\x12\x1d\n\x15mediaCiphertextSHA256\x18\x14 \x01(\x0c\x12\x11\n\tmulticast\x18\x15 \x01(\x08\x12\x0f\n\x07urlText\x18\x16 \x01(\x08\x12\x11\n\turlNumber\x18\x17 \x01(\x08\x12\x43\n\x0fmessageStubType\x18\x18 \x01(\x0e\x32*.WAWebProtobufsWeb.WebMessageInfo.StubType\x12\x12\n\nclearMedia\x18\x19 \x01(\x08\x12\x1d\n\x15messageStubParameters\x18\x1a \x03(\t\x12\x10\n\x08\x64uration\x18\x1b \x01(\r\x12\x0e\n\x06labels\x18\x1c \x03(\t\x12\x33\n\x0bpaymentInfo\x18\x1d \x01(\x0b\x32\x1e.WAWebProtobufsWeb.PaymentInfo\x12\x41\n\x11\x66inalLiveLocation\x18\x1e \x01(\x0b\x32&.WAWebProtobufsE2E.LiveLocationMessage\x12\x39\n\x11quotedPaymentInfo\x18\x1f \x01(\x0b\x32\x1e.WAWebProtobufsWeb.PaymentInfo\x12\x1f\n\x17\x65phemeralStartTimestamp\x18  \x01(\x04\x12\x19\n\x11\x65phemeralDuration\x18! \x01(\r\x12\x18\n\x10\x65phemeralOffToOn\x18\" \x01(\x08\x12\x1a\n\x12\x65phemeralOutOfSync\x18# \x01(\x08\x12L\n\x10\x62izPrivacyStatus\x18$ \x01(\x0e\x32\x32.WAWebProtobufsWeb.WebMessageInfo.BizPrivacyStatus\x12\x17\n\x0fverifiedBizName\x18% \x01(\t\x12/\n\tmediaData\x18& \x01(\x0b\x32\x1c.WAWebProtobufsWeb.MediaData\x12\x33\n\x0bphotoChange\x18\' \x01(\x0b\x32\x1e.WAWebProtobufsWeb.PhotoChange\x12\x33\n\x0buserReceipt\x18( \x03(\x0b\x32\x1e.WAWebProtobufsWeb.UserReceipt\x12.\n\treactions\x18) \x03(\x0b\x32\x1b.WAWebProtobufsWeb.Reaction\x12\x37\n\x11quotedStickerData\x18* \x01(\x0b\x32\x1c.WAWebProtobufsWeb.MediaData\x12\x17\n\x0f\x66utureproofData\x18+ \x01(\x0c\x12/\n\tstatusPsa\x18, \x01(\x0b\x32\x1c.WAWebProtobufsWeb.StatusPSA\x12\x32\n\x0bpollUpdates\x18- \x03(\x0b\x32\x1d.WAWebProtobufsWeb.PollUpdate\x12I\n\x16pollAdditionalMetadata\x18. \x01(\x0b\x32).WAWebProtobufsWeb.PollAdditionalMetadata\x12\x0f\n\x07\x61gentID\x18/ \x01(\t\x12\x1b\n\x13statusAlreadyViewed\x18\x30 \x01(\x08\x12\x15\n\rmessageSecret\x18\x31 \x01(\x0c\x12\x31\n\nkeepInChat\x18\x32 \x01(\x0b\x32\x1d.WAWebProtobufsWeb.KeepInChat\x12\'\n\x1foriginalSelfAuthorUserJIDString\x18\x33 \x01(\t\x12\x1e\n\x16revokeMessageTimestamp\x18\x34 \x01(\x04\x12/\n\tpinInChat\x18\x36 \x01(\x0b\x32\x1c.WAWebProtobufsWeb.PinInChat\x12\x41\n\x12premiumMessageInfo\x18\x37 \x01(\x0b\x32%.WAWebProtobufsWeb.PremiumMessageInfo\x12\x19\n\x11is1PBizBotMessage\x18\x38 \x01(\x08\x12\x1d\n\x15isGroupHistoryMessage\x18\x39 \x01(\x08\x12\x1c\n\x14\x62otMessageInvokerJID\x18: \x01(\t\x12;\n\x0f\x63ommentMetadata\x18; \x01(\x0b\x32\".WAWebProtobufsWeb.CommentMetadata\x12\x38\n\x0e\x65ventResponses\x18= \x03(\x0b\x32 .WAWebProtobufsWeb.EventResponse\x12\x41\n\x12reportingTokenInfo\x18> \x01(\x0b\x32%.WAWebProtobufsWeb.ReportingTokenInfo\x12\x1a\n\x12newsletterServerID\x18? \x01(\x04\x12K\n\x17\x65ventAdditionalMetadata\x18@ \x01(\x0b\x32*.WAWebProtobufsWeb.EventAdditionalMetadata\x12\x1b\n\x13isMentionedInStatus\x18\x41 \x01(\x08\x12\x16\n\x0estatusMentions\x18\x42 \x03(\t\x12-\n\x0ftargetMessageID\x18\x43 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x36\n\rmessageAddOns\x18\x44 \x03(\x0b\x32\x1f.WAWebProtobufsWeb.MessageAddOn\x12I\n\x18statusMentionMessageInfo\x18\x45 \x01(\x0b\x32\'.WAWebProtobufsWeb.StatusMentionMessage\x12\x1a\n\x12isSupportAiMessage\x18\x46 \x01(\x08\x12\x1c\n\x14statusMentionSources\x18G \x03(\t\x12\x37\n\x12supportAiCitations\x18H \x03(\x0b\x32\x1b.WAWebProtobufsWeb.Citation\x12\x13\n\x0b\x62otTargetID\x18I \x01(\t\"=\n\x10\x42izPrivacyStatus\x12\x08\n\x04\x45\x32\x45\x45\x10\x00\x12\x06\n\x02\x46\x42\x10\x02\x12\x07\n\x03\x42SP\x10\x01\x12\x0e\n\nBSP_AND_FB\x10\x03\"\xbf\x38\n\x08StubType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06REVOKE\x10\x01\x12\x0e\n\nCIPHERTEXT\x10\x02\x12\x0f\n\x0b\x46UTUREPROOF\x10\x03\x12\x1b\n\x17NON_VERIFIED_TRANSITION\x10\x04\x12\x19\n\x15UNVERIFIED_TRANSITION\x10\x05\x12\x17\n\x13VERIFIED_TRANSITION\x10\x06\x12\x18\n\x14VERIFIED_LOW_UNKNOWN\x10\x07\x12\x11\n\rVERIFIED_HIGH\x10\x08\x12\x1c\n\x18VERIFIED_INITIAL_UNKNOWN\x10\t\x12\x18\n\x14VERIFIED_INITIAL_LOW\x10\n\x12\x19\n\x15VERIFIED_INITIAL_HIGH\x10\x0b\x12#\n\x1fVERIFIED_TRANSITION_ANY_TO_NONE\x10\x0c\x12#\n\x1fVERIFIED_TRANSITION_ANY_TO_HIGH\x10\r\x12#\n\x1fVERIFIED_TRANSITION_HIGH_TO_LOW\x10\x0e\x12\'\n#VERIFIED_TRANSITION_HIGH_TO_UNKNOWN\x10\x0f\x12&\n\"VERIFIED_TRANSITION_UNKNOWN_TO_LOW\x10\x10\x12&\n\"VERIFIED_TRANSITION_LOW_TO_UNKNOWN\x10\x11\x12#\n\x1fVERIFIED_TRANSITION_NONE_TO_LOW\x10\x12\x12\'\n#VERIFIED_TRANSITION_NONE_TO_UNKNOWN\x10\x13\x12\x10\n\x0cGROUP_CREATE\x10\x14\x12\x18\n\x14GROUP_CHANGE_SUBJECT\x10\x15\x12\x15\n\x11GROUP_CHANGE_ICON\x10\x16\x12\x1c\n\x18GROUP_CHANGE_INVITE_LINK\x10\x17\x12\x1c\n\x18GROUP_CHANGE_DESCRIPTION\x10\x18\x12\x19\n\x15GROUP_CHANGE_RESTRICT\x10\x19\x12\x19\n\x15GROUP_CHANGE_ANNOUNCE\x10\x1a\x12\x19\n\x15GROUP_PARTICIPANT_ADD\x10\x1b\x12\x1c\n\x18GROUP_PARTICIPANT_REMOVE\x10\x1c\x12\x1d\n\x19GROUP_PARTICIPANT_PROMOTE\x10\x1d\x12\x1c\n\x18GROUP_PARTICIPANT_DEMOTE\x10\x1e\x12\x1c\n\x18GROUP_PARTICIPANT_INVITE\x10\x1f\x12\x1b\n\x17GROUP_PARTICIPANT_LEAVE\x10 \x12#\n\x1fGROUP_PARTICIPANT_CHANGE_NUMBER\x10!\x12\x14\n\x10\x42ROADCAST_CREATE\x10\"\x12\x11\n\rBROADCAST_ADD\x10#\x12\x14\n\x10\x42ROADCAST_REMOVE\x10$\x12\x18\n\x14GENERIC_NOTIFICATION\x10%\x12\x18\n\x14\x45\x32\x45_IDENTITY_CHANGED\x10&\x12\x11\n\rE2E_ENCRYPTED\x10\'\x12\x15\n\x11\x43\x41LL_MISSED_VOICE\x10(\x12\x15\n\x11\x43\x41LL_MISSED_VIDEO\x10)\x12\x1c\n\x18INDIVIDUAL_CHANGE_NUMBER\x10*\x12\x10\n\x0cGROUP_DELETE\x10+\x12&\n\"GROUP_ANNOUNCE_MODE_MESSAGE_BOUNCE\x10,\x12\x1b\n\x17\x43\x41LL_MISSED_GROUP_VOICE\x10-\x12\x1b\n\x17\x43\x41LL_MISSED_GROUP_VIDEO\x10.\x12\x16\n\x12PAYMENT_CIPHERTEXT\x10/\x12\x17\n\x13PAYMENT_FUTUREPROOF\x10\x30\x12,\n(PAYMENT_TRANSACTION_STATUS_UPDATE_FAILED\x10\x31\x12.\n*PAYMENT_TRANSACTION_STATUS_UPDATE_REFUNDED\x10\x32\x12\x33\n/PAYMENT_TRANSACTION_STATUS_UPDATE_REFUND_FAILED\x10\x33\x12\x35\n1PAYMENT_TRANSACTION_STATUS_RECEIVER_PENDING_SETUP\x10\x34\x12<\n8PAYMENT_TRANSACTION_STATUS_RECEIVER_SUCCESS_AFTER_HICCUP\x10\x35\x12)\n%PAYMENT_ACTION_ACCOUNT_SETUP_REMINDER\x10\x36\x12(\n$PAYMENT_ACTION_SEND_PAYMENT_REMINDER\x10\x37\x12*\n&PAYMENT_ACTION_SEND_PAYMENT_INVITATION\x10\x38\x12#\n\x1fPAYMENT_ACTION_REQUEST_DECLINED\x10\x39\x12\"\n\x1ePAYMENT_ACTION_REQUEST_EXPIRED\x10:\x12$\n PAYMENT_ACTION_REQUEST_CANCELLED\x10;\x12)\n%BIZ_VERIFIED_TRANSITION_TOP_TO_BOTTOM\x10<\x12)\n%BIZ_VERIFIED_TRANSITION_BOTTOM_TO_TOP\x10=\x12\x11\n\rBIZ_INTRO_TOP\x10>\x12\x14\n\x10\x42IZ_INTRO_BOTTOM\x10?\x12\x13\n\x0f\x42IZ_NAME_CHANGE\x10@\x12\x1c\n\x18\x42IZ_MOVE_TO_CONSUMER_APP\x10\x41\x12\x1e\n\x1a\x42IZ_TWO_TIER_MIGRATION_TOP\x10\x42\x12!\n\x1d\x42IZ_TWO_TIER_MIGRATION_BOTTOM\x10\x43\x12\r\n\tOVERSIZED\x10\x44\x12(\n$GROUP_CHANGE_NO_FREQUENTLY_FORWARDED\x10\x45\x12\x1c\n\x18GROUP_V4_ADD_INVITE_SENT\x10\x46\x12&\n\"GROUP_PARTICIPANT_ADD_REQUEST_JOIN\x10G\x12\x1c\n\x18\x43HANGE_EPHEMERAL_SETTING\x10H\x12\x16\n\x12\x45\x32\x45_DEVICE_CHANGED\x10I\x12\x0f\n\x0bVIEWED_ONCE\x10J\x12\x15\n\x11\x45\x32\x45_ENCRYPTED_NOW\x10K\x12\"\n\x1e\x42LUE_MSG_BSP_FB_TO_BSP_PREMISE\x10L\x12\x1e\n\x1a\x42LUE_MSG_BSP_FB_TO_SELF_FB\x10M\x12#\n\x1f\x42LUE_MSG_BSP_FB_TO_SELF_PREMISE\x10N\x12\x1e\n\x1a\x42LUE_MSG_BSP_FB_UNVERIFIED\x10O\x12\x37\n3BLUE_MSG_BSP_FB_UNVERIFIED_TO_SELF_PREMISE_VERIFIED\x10P\x12\x1c\n\x18\x42LUE_MSG_BSP_FB_VERIFIED\x10Q\x12\x37\n3BLUE_MSG_BSP_FB_VERIFIED_TO_SELF_PREMISE_UNVERIFIED\x10R\x12(\n$BLUE_MSG_BSP_PREMISE_TO_SELF_PREMISE\x10S\x12#\n\x1f\x42LUE_MSG_BSP_PREMISE_UNVERIFIED\x10T\x12<\n8BLUE_MSG_BSP_PREMISE_UNVERIFIED_TO_SELF_PREMISE_VERIFIED\x10U\x12!\n\x1d\x42LUE_MSG_BSP_PREMISE_VERIFIED\x10V\x12<\n8BLUE_MSG_BSP_PREMISE_VERIFIED_TO_SELF_PREMISE_UNVERIFIED\x10W\x12*\n&BLUE_MSG_CONSUMER_TO_BSP_FB_UNVERIFIED\x10X\x12/\n+BLUE_MSG_CONSUMER_TO_BSP_PREMISE_UNVERIFIED\x10Y\x12+\n\'BLUE_MSG_CONSUMER_TO_SELF_FB_UNVERIFIED\x10Z\x12\x30\n,BLUE_MSG_CONSUMER_TO_SELF_PREMISE_UNVERIFIED\x10[\x12#\n\x1f\x42LUE_MSG_SELF_FB_TO_BSP_PREMISE\x10\\\x12$\n BLUE_MSG_SELF_FB_TO_SELF_PREMISE\x10]\x12\x1f\n\x1b\x42LUE_MSG_SELF_FB_UNVERIFIED\x10^\x12\x38\n4BLUE_MSG_SELF_FB_UNVERIFIED_TO_SELF_PREMISE_VERIFIED\x10_\x12\x1d\n\x19\x42LUE_MSG_SELF_FB_VERIFIED\x10`\x12\x38\n4BLUE_MSG_SELF_FB_VERIFIED_TO_SELF_PREMISE_UNVERIFIED\x10\x61\x12(\n$BLUE_MSG_SELF_PREMISE_TO_BSP_PREMISE\x10\x62\x12$\n BLUE_MSG_SELF_PREMISE_UNVERIFIED\x10\x63\x12\"\n\x1e\x42LUE_MSG_SELF_PREMISE_VERIFIED\x10\x64\x12\x16\n\x12\x42LUE_MSG_TO_BSP_FB\x10\x65\x12\x18\n\x14\x42LUE_MSG_TO_CONSUMER\x10\x66\x12\x17\n\x13\x42LUE_MSG_TO_SELF_FB\x10g\x12*\n&BLUE_MSG_UNVERIFIED_TO_BSP_FB_VERIFIED\x10h\x12/\n+BLUE_MSG_UNVERIFIED_TO_BSP_PREMISE_VERIFIED\x10i\x12+\n\'BLUE_MSG_UNVERIFIED_TO_SELF_FB_VERIFIED\x10j\x12#\n\x1f\x42LUE_MSG_UNVERIFIED_TO_VERIFIED\x10k\x12*\n&BLUE_MSG_VERIFIED_TO_BSP_FB_UNVERIFIED\x10l\x12/\n+BLUE_MSG_VERIFIED_TO_BSP_PREMISE_UNVERIFIED\x10m\x12+\n\'BLUE_MSG_VERIFIED_TO_SELF_FB_UNVERIFIED\x10n\x12#\n\x1f\x42LUE_MSG_VERIFIED_TO_UNVERIFIED\x10o\x12\x36\n2BLUE_MSG_BSP_FB_UNVERIFIED_TO_BSP_PREMISE_VERIFIED\x10p\x12\x32\n.BLUE_MSG_BSP_FB_UNVERIFIED_TO_SELF_FB_VERIFIED\x10q\x12\x36\n2BLUE_MSG_BSP_FB_VERIFIED_TO_BSP_PREMISE_UNVERIFIED\x10r\x12\x32\n.BLUE_MSG_BSP_FB_VERIFIED_TO_SELF_FB_UNVERIFIED\x10s\x12\x37\n3BLUE_MSG_SELF_FB_UNVERIFIED_TO_BSP_PREMISE_VERIFIED\x10t\x12\x37\n3BLUE_MSG_SELF_FB_VERIFIED_TO_BSP_PREMISE_UNVERIFIED\x10u\x12\x1c\n\x18\x45\x32\x45_IDENTITY_UNAVAILABLE\x10v\x12\x12\n\x0eGROUP_CREATING\x10w\x12\x17\n\x13GROUP_CREATE_FAILED\x10x\x12\x11\n\rGROUP_BOUNCED\x10y\x12\x11\n\rBLOCK_CONTACT\x10z\x12!\n\x1d\x45PHEMERAL_SETTING_NOT_APPLIED\x10{\x12\x0f\n\x0bSYNC_FAILED\x10|\x12\x0b\n\x07SYNCING\x10}\x12\x1c\n\x18\x42IZ_PRIVACY_MODE_INIT_FB\x10~\x12\x1d\n\x19\x42IZ_PRIVACY_MODE_INIT_BSP\x10\x7f\x12\x1b\n\x16\x42IZ_PRIVACY_MODE_TO_FB\x10\x80\x01\x12\x1c\n\x17\x42IZ_PRIVACY_MODE_TO_BSP\x10\x81\x01\x12\x16\n\x11\x44ISAPPEARING_MODE\x10\x82\x01\x12\x1c\n\x17\x45\x32\x45_DEVICE_FETCH_FAILED\x10\x83\x01\x12\x11\n\x0c\x41\x44MIN_REVOKE\x10\x84\x01\x12$\n\x1fGROUP_INVITE_LINK_GROWTH_LOCKED\x10\x85\x01\x12 \n\x1b\x43OMMUNITY_LINK_PARENT_GROUP\x10\x86\x01\x12!\n\x1c\x43OMMUNITY_LINK_SIBLING_GROUP\x10\x87\x01\x12\x1d\n\x18\x43OMMUNITY_LINK_SUB_GROUP\x10\x88\x01\x12\"\n\x1d\x43OMMUNITY_UNLINK_PARENT_GROUP\x10\x89\x01\x12#\n\x1e\x43OMMUNITY_UNLINK_SIBLING_GROUP\x10\x8a\x01\x12\x1f\n\x1a\x43OMMUNITY_UNLINK_SUB_GROUP\x10\x8b\x01\x12\x1d\n\x18GROUP_PARTICIPANT_ACCEPT\x10\x8c\x01\x12(\n#GROUP_PARTICIPANT_LINKED_GROUP_JOIN\x10\x8d\x01\x12\x15\n\x10\x43OMMUNITY_CREATE\x10\x8e\x01\x12\x1b\n\x16\x45PHEMERAL_KEEP_IN_CHAT\x10\x8f\x01\x12+\n&GROUP_MEMBERSHIP_JOIN_APPROVAL_REQUEST\x10\x90\x01\x12(\n#GROUP_MEMBERSHIP_JOIN_APPROVAL_MODE\x10\x91\x01\x12\"\n\x1dINTEGRITY_UNLINK_PARENT_GROUP\x10\x92\x01\x12\"\n\x1d\x43OMMUNITY_PARTICIPANT_PROMOTE\x10\x93\x01\x12!\n\x1c\x43OMMUNITY_PARTICIPANT_DEMOTE\x10\x94\x01\x12#\n\x1e\x43OMMUNITY_PARENT_GROUP_DELETED\x10\x95\x01\x12\x34\n/COMMUNITY_LINK_PARENT_GROUP_MEMBERSHIP_APPROVAL\x10\x96\x01\x12\x34\n/GROUP_PARTICIPANT_JOINED_GROUP_AND_PARENT_GROUP\x10\x97\x01\x12\x1a\n\x15MASKED_THREAD_CREATED\x10\x98\x01\x12\x1b\n\x16MASKED_THREAD_UNMASKED\x10\x99\x01\x12\x18\n\x13\x42IZ_CHAT_ASSIGNMENT\x10\x9a\x01\x12\r\n\x08\x43HAT_PSA\x10\x9b\x01\x12\x1f\n\x1a\x43HAT_POLL_CREATION_MESSAGE\x10\x9c\x01\x12\x1e\n\x19\x43\x41G_MASKED_THREAD_CREATED\x10\x9d\x01\x12+\n&COMMUNITY_PARENT_GROUP_SUBJECT_CHANGED\x10\x9e\x01\x12\x18\n\x13\x43\x41G_INVITE_AUTO_ADD\x10\x9f\x01\x12!\n\x1c\x42IZ_CHAT_ASSIGNMENT_UNASSIGN\x10\xa0\x01\x12\x1b\n\x16\x43\x41G_INVITE_AUTO_JOINED\x10\xa1\x01\x12!\n\x1cSCHEDULED_CALL_START_MESSAGE\x10\xa2\x01\x12\x1a\n\x15\x43OMMUNITY_INVITE_RICH\x10\xa3\x01\x12#\n\x1e\x43OMMUNITY_INVITE_AUTO_ADD_RICH\x10\xa4\x01\x12\x1a\n\x15SUB_GROUP_INVITE_RICH\x10\xa5\x01\x12#\n\x1eSUB_GROUP_PARTICIPANT_ADD_RICH\x10\xa6\x01\x12%\n COMMUNITY_LINK_PARENT_GROUP_RICH\x10\xa7\x01\x12#\n\x1e\x43OMMUNITY_PARTICIPANT_ADD_RICH\x10\xa8\x01\x12\"\n\x1dSILENCED_UNKNOWN_CALLER_AUDIO\x10\xa9\x01\x12\"\n\x1dSILENCED_UNKNOWN_CALLER_VIDEO\x10\xaa\x01\x12\x1a\n\x15GROUP_MEMBER_ADD_MODE\x10\xab\x01\x12\x39\n4GROUP_MEMBERSHIP_JOIN_APPROVAL_REQUEST_NON_ADMIN_ADD\x10\xac\x01\x12!\n\x1c\x43OMMUNITY_CHANGE_DESCRIPTION\x10\xad\x01\x12\x12\n\rSENDER_INVITE\x10\xae\x01\x12\x14\n\x0fRECEIVER_INVITE\x10\xaf\x01\x12(\n#COMMUNITY_ALLOW_MEMBER_ADDED_GROUPS\x10\xb0\x01\x12\x1b\n\x16PINNED_MESSAGE_IN_CHAT\x10\xb1\x01\x12!\n\x1cPAYMENT_INVITE_SETUP_INVITER\x10\xb2\x01\x12.\n)PAYMENT_INVITE_SETUP_INVITEE_RECEIVE_ONLY\x10\xb3\x01\x12\x32\n-PAYMENT_INVITE_SETUP_INVITEE_SEND_AND_RECEIVE\x10\xb4\x01\x12\x1c\n\x17LINKED_GROUP_CALL_START\x10\xb5\x01\x12#\n\x1eREPORT_TO_ADMIN_ENABLED_STATUS\x10\xb6\x01\x12\x1a\n\x15\x45MPTY_SUBGROUP_CREATE\x10\xb7\x01\x12\x1a\n\x15SCHEDULED_CALL_CANCEL\x10\xb8\x01\x12+\n&SUBGROUP_ADMIN_TRIGGERED_AUTO_ADD_RICH\x10\xb9\x01\x12(\n#GROUP_CHANGE_RECENT_HISTORY_SHARING\x10\xba\x01\x12$\n\x1fPAID_MESSAGE_SERVER_CAMPAIGN_ID\x10\xbb\x01\x12\x18\n\x13GENERAL_CHAT_CREATE\x10\xbc\x01\x12\x15\n\x10GENERAL_CHAT_ADD\x10\xbd\x01\x12#\n\x1eGENERAL_CHAT_AUTO_ADD_DISABLED\x10\xbe\x01\x12 \n\x1bSUGGESTED_SUBGROUP_ANNOUNCE\x10\xbf\x01\x12!\n\x1c\x42IZ_BOT_1P_MESSAGING_ENABLED\x10\xc0\x01\x12\x14\n\x0f\x43HANGE_USERNAME\x10\xc1\x01\x12\x1f\n\x1a\x42IZ_COEX_PRIVACY_INIT_SELF\x10\xc2\x01\x12%\n BIZ_COEX_PRIVACY_TRANSITION_SELF\x10\xc3\x01\x12\x19\n\x14SUPPORT_AI_EDUCATION\x10\xc4\x01\x12!\n\x1c\x42IZ_BOT_3P_MESSAGING_ENABLED\x10\xc5\x01\x12\x1b\n\x16REMINDER_SETUP_MESSAGE\x10\xc6\x01\x12\x1a\n\x15REMINDER_SENT_MESSAGE\x10\xc7\x01\x12\x1c\n\x17REMINDER_CANCEL_MESSAGE\x10\xc8\x01\x12\x1a\n\x15\x42IZ_COEX_PRIVACY_INIT\x10\xc9\x01\x12 \n\x1b\x42IZ_COEX_PRIVACY_TRANSITION\x10\xca\x01\x12\x16\n\x11GROUP_DEACTIVATED\x10\xcb\x01\x12\'\n\"COMMUNITY_DEACTIVATE_SIBLING_GROUP\x10\xcc\x01\x12\x12\n\rEVENT_UPDATED\x10\xcd\x01\x12\x13\n\x0e\x45VENT_CANCELED\x10\xce\x01\x12\x1c\n\x17\x43OMMUNITY_OWNER_UPDATED\x10\xcf\x01\x12*\n%COMMUNITY_SUB_GROUP_VISIBILITY_HIDDEN\x10\xd0\x01\x12$\n\x1f\x43\x41PI_GROUP_NE2EE_SYSTEM_MESSAGE\x10\xd1\x01\x12\x13\n\x0eSTATUS_MENTION\x10\xd2\x01\x12!\n\x1cUSER_CONTROLS_SYSTEM_MESSAGE\x10\xd3\x01\x12\x1b\n\x16SUPPORT_SYSTEM_MESSAGE\x10\xd4\x01\"X\n\x06Status\x12\t\n\x05\x45RROR\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nSERVER_ACK\x10\x02\x12\x10\n\x0c\x44\x45LIVERY_ACK\x10\x03\x12\x08\n\x04READ\x10\x04\x12\n\n\x06PLAYED\x10\x05\"\x94\x0b\n\x0bPaymentInfo\x12\x43\n\x12\x63urrencyDeprecated\x18\x01 \x01(\x0e\x32\'.WAWebProtobufsWeb.PaymentInfo.Currency\x12\x12\n\namount1000\x18\x02 \x01(\x04\x12\x13\n\x0breceiverJID\x18\x03 \x01(\t\x12\x35\n\x06status\x18\x04 \x01(\x0e\x32%.WAWebProtobufsWeb.PaymentInfo.Status\x12\x1c\n\x14transactionTimestamp\x18\x05 \x01(\x04\x12/\n\x11requestMessageKey\x18\x06 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x17\n\x0f\x65xpiryTimestamp\x18\x07 \x01(\x04\x12\x15\n\rfutureproofed\x18\x08 \x01(\x08\x12\x10\n\x08\x63urrency\x18\t \x01(\t\x12;\n\ttxnStatus\x18\n \x01(\x0e\x32(.WAWebProtobufsWeb.PaymentInfo.TxnStatus\x12\x19\n\x11useNoviFiatFormat\x18\x0b \x01(\x08\x12/\n\rprimaryAmount\x18\x0c \x01(\x0b\x32\x18.WAWebProtobufsE2E.Money\x12\x30\n\x0e\x65xchangeAmount\x18\r \x01(\x0b\x32\x18.WAWebProtobufsE2E.Money\"\x99\x05\n\tTxnStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rPENDING_SETUP\x10\x01\x12\x1a\n\x16PENDING_RECEIVER_SETUP\x10\x02\x12\x08\n\x04INIT\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x12\r\n\tCOMPLETED\x10\x05\x12\n\n\x06\x46\x41ILED\x10\x06\x12\x0f\n\x0b\x46\x41ILED_RISK\x10\x07\x12\x15\n\x11\x46\x41ILED_PROCESSING\x10\x08\x12\x1e\n\x1a\x46\x41ILED_RECEIVER_PROCESSING\x10\t\x12\r\n\tFAILED_DA\x10\n\x12\x13\n\x0f\x46\x41ILED_DA_FINAL\x10\x0b\x12\x10\n\x0cREFUNDED_TXN\x10\x0c\x12\x11\n\rREFUND_FAILED\x10\r\x12\x1c\n\x18REFUND_FAILED_PROCESSING\x10\x0e\x12\x14\n\x10REFUND_FAILED_DA\x10\x0f\x12\x0f\n\x0b\x45XPIRED_TXN\x10\x10\x12\x11\n\rAUTH_CANCELED\x10\x11\x12!\n\x1d\x41UTH_CANCEL_FAILED_PROCESSING\x10\x12\x12\x16\n\x12\x41UTH_CANCEL_FAILED\x10\x13\x12\x10\n\x0c\x43OLLECT_INIT\x10\x14\x12\x13\n\x0f\x43OLLECT_SUCCESS\x10\x15\x12\x12\n\x0e\x43OLLECT_FAILED\x10\x16\x12\x17\n\x13\x43OLLECT_FAILED_RISK\x10\x17\x12\x14\n\x10\x43OLLECT_REJECTED\x10\x18\x12\x13\n\x0f\x43OLLECT_EXPIRED\x10\x19\x12\x14\n\x10\x43OLLECT_CANCELED\x10\x1a\x12\x16\n\x12\x43OLLECT_CANCELLING\x10\x1b\x12\r\n\tIN_REVIEW\x10\x1c\x12\x14\n\x10REVERSAL_SUCCESS\x10\x1d\x12\x14\n\x10REVERSAL_PENDING\x10\x1e\x12\x12\n\x0eREFUND_PENDING\x10\x1f\"\xcc\x01\n\x06Status\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\x08\n\x04SENT\x10\x02\x12\x12\n\x0eNEED_TO_ACCEPT\x10\x03\x12\x0c\n\x08\x43OMPLETE\x10\x04\x12\x16\n\x12\x43OULD_NOT_COMPLETE\x10\x05\x12\x0c\n\x08REFUNDED\x10\x06\x12\x0b\n\x07\x45XPIRED\x10\x07\x12\x0c\n\x08REJECTED\x10\x08\x12\r\n\tCANCELLED\x10\t\x12\x15\n\x11WAITING_FOR_PAYER\x10\n\x12\x0b\n\x07WAITING\x10\x0b\")\n\x08\x43urrency\x12\x14\n\x10UNKNOWN_CURRENCY\x10\x00\x12\x07\n\x03INR\x10\x01\"\xf7\x16\n\x0bWebFeatures\x12:\n\rlabelsDisplay\x18\x01 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x43\n\x16voipIndividualOutgoing\x18\x02 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x35\n\x08groupsV3\x18\x03 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12;\n\x0egroupsV3Create\x18\x04 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12;\n\x0e\x63hangeNumberV2\x18\x05 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x43\n\x16queryStatusV3Thumbnail\x18\x06 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12:\n\rliveLocations\x18\x07 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x37\n\nqueryVname\x18\x08 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x43\n\x16voipIndividualIncoming\x18\t \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12>\n\x11quickRepliesQuery\x18\n \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x35\n\x08payments\x18\x0b \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12=\n\x10stickerPackQuery\x18\x0c \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12?\n\x12liveLocationsFinal\x18\r \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x37\n\nlabelsEdit\x18\x0e \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x38\n\x0bmediaUpload\x18\x0f \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12H\n\x1bmediaUploadRichQuickReplies\x18\x12 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x34\n\x07vnameV2\x18\x13 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12=\n\x10videoPlaybackURL\x18\x14 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12:\n\rstatusRanking\x18\x15 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12@\n\x13voipIndividualVideo\x18\x16 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12?\n\x12thirdPartyStickers\x18\x17 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12G\n\x1a\x66requentlyForwardedSetting\x18\x18 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x43\n\x16groupsV4JoinPermission\x18\x19 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12;\n\x0erecentStickers\x18\x1a \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x34\n\x07\x63\x61talog\x18\x1b \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12<\n\x0fstarredStickers\x18\x1c \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12:\n\rvoipGroupCall\x18\x1d \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12<\n\x0ftemplateMessage\x18\x1e \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12I\n\x1ctemplateMessageInteractivity\x18\x1f \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12>\n\x11\x65phemeralMessages\x18  \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12@\n\x13\x65\x32\x45NotificationSync\x18! \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12=\n\x10recentStickersV2\x18\" \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12=\n\x10recentStickersV3\x18$ \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x37\n\nuserNotice\x18% \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x34\n\x07support\x18\' \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12<\n\x0fgroupUiiCleanup\x18( \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12H\n\x1bgroupDogfoodingInternalOnly\x18) \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x39\n\x0csettingsSync\x18* \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x36\n\tarchiveV2\x18+ \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12G\n\x1a\x65phemeralAllowGroupMembers\x18, \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x41\n\x14\x65phemeral24HDuration\x18- \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12;\n\x0emdForceUpgrade\x18. \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12=\n\x10\x64isappearingMode\x18/ \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x45\n\x18\x65xternalMdOptInAvailable\x18\x30 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\x12\x45\n\x18noDeleteMessageTimeLimit\x18\x31 \x01(\x0e\x32#.WAWebProtobufsWeb.WebFeatures.Flag\"K\n\x04\x46lag\x12\x0f\n\x0bNOT_STARTED\x10\x00\x12\x11\n\rFORCE_UPGRADE\x10\x01\x12\x0f\n\x0b\x44\x45VELOPMENT\x10\x02\x12\x0e\n\nPRODUCTION\x10\x03\"\xa0\x02\n\tPinInChat\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.WAWebProtobufsWeb.PinInChat.Type\x12!\n\x03key\x18\x02 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x19\n\x11senderTimestampMS\x18\x03 \x01(\x03\x12\x19\n\x11serverTimestampMS\x18\x04 \x01(\x03\x12K\n\x17messageAddOnContextInfo\x18\x05 \x01(\x0b\x32*.WAWebProtobufsWeb.MessageAddOnContextInfo\"<\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0f\n\x0bPIN_FOR_ALL\x10\x01\x12\x11\n\rUNPIN_FOR_ALL\x10\x02\"\x91\x04\n\x0cMessageAddOn\x12J\n\x10messageAddOnType\x18\x01 \x01(\x0e\x32\x30.WAWebProtobufsWeb.MessageAddOn.MessageAddOnType\x12\x30\n\x0cmessageAddOn\x18\x02 \x01(\x0b\x32\x1a.WAWebProtobufsE2E.Message\x12\x19\n\x11senderTimestampMS\x18\x03 \x01(\x03\x12\x19\n\x11serverTimestampMS\x18\x04 \x01(\x03\x12\x38\n\x06status\x18\x05 \x01(\x0e\x32(.WAWebProtobufsWeb.WebMessageInfo.Status\x12\x44\n\x10\x61\x64\x64OnContextInfo\x18\x06 \x01(\x0b\x32*.WAWebProtobufsWeb.MessageAddOnContextInfo\x12-\n\x0fmessageAddOnKey\x18\x07 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x37\n\rlegacyMessage\x18\x08 \x01(\x0b\x32 .WAWebProtobufsWeb.LegacyMessage\"e\n\x10MessageAddOnType\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08REACTION\x10\x01\x12\x12\n\x0e\x45VENT_RESPONSE\x10\x02\x12\x0f\n\x0bPOLL_UPDATE\x10\x03\x12\x0f\n\x0bPIN_IN_CHAT\x10\x04\"U\n\x0f\x43ommentMetadata\x12.\n\x10\x63ommentParentKey\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x12\n\nreplyCount\x18\x02 \x01(\r\"\x95\x01\n\x14WebNotificationsInfo\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x13\n\x0bunreadChats\x18\x03 \x01(\r\x12\x1a\n\x12notifyMessageCount\x18\x04 \x01(\r\x12\x39\n\x0enotifyMessages\x18\x05 \x03(\x0b\x32!.WAWebProtobufsWeb.WebMessageInfo\"\x98\x01\n\x17NotificationMessageInfo\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12+\n\x07message\x18\x02 \x01(\x0b\x32\x1a.WAWebProtobufsE2E.Message\x12\x18\n\x10messageTimestamp\x18\x03 \x01(\x04\x12\x13\n\x0bparticipant\x18\x04 \x01(\t\"*\n\x12ReportingTokenInfo\x12\x14\n\x0creportingTag\x18\x01 \x01(\x0c\"\x1e\n\tMediaData\x12\x11\n\tlocalPath\x18\x01 \x01(\t\"E\n\x0bPhotoChange\x12\x10\n\x08oldPhoto\x18\x01 \x01(\x0c\x12\x10\n\x08newPhoto\x18\x02 \x01(\x0c\x12\x12\n\nnewPhotoID\x18\x03 \x01(\r\"D\n\tStatusPSA\x12\x12\n\ncampaignID\x18, \x02(\x04\x12#\n\x1b\x63\x61mpaignExpirationTimestamp\x18- \x01(\x04\"\x9e\x01\n\x0bUserReceipt\x12\x0f\n\x07userJID\x18\x01 \x02(\t\x12\x18\n\x10receiptTimestamp\x18\x02 \x01(\x03\x12\x15\n\rreadTimestamp\x18\x03 \x01(\x03\x12\x17\n\x0fplayedTimestamp\x18\x04 \x01(\x03\x12\x18\n\x10pendingDeviceJID\x18\x05 \x03(\t\x12\x1a\n\x12\x64\x65liveredDeviceJID\x18\x06 \x03(\t\"{\n\x08Reaction\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x13\n\x0bgroupingKey\x18\x03 \x01(\t\x12\x19\n\x11senderTimestampMS\x18\x04 \x01(\x03\x12\x0e\n\x06unread\x18\x05 \x01(\x08\"\xb8\x01\n\nPollUpdate\x12\x32\n\x14pollUpdateMessageKey\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x30\n\x04vote\x18\x02 \x01(\x0b\x32\".WAWebProtobufsE2E.PollVoteMessage\x12\x19\n\x11senderTimestampMS\x18\x03 \x01(\x03\x12\x19\n\x11serverTimestampMS\x18\x04 \x01(\x03\x12\x0e\n\x06unread\x18\x05 \x01(\x08\"1\n\x16PollAdditionalMetadata\x12\x17\n\x0fpollInvalidated\x18\x01 \x01(\x08\"*\n\x17\x45ventAdditionalMetadata\x12\x0f\n\x07isStale\x18\x01 \x01(\x08\"\xc0\x01\n\nKeepInChat\x12-\n\x08keepType\x18\x01 \x01(\x0e\x32\x1b.WAWebProtobufsE2E.KeepType\x12\x17\n\x0fserverTimestamp\x18\x02 \x01(\x03\x12!\n\x03key\x18\x03 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x11\n\tdeviceJID\x18\x04 \x01(\t\x12\x19\n\x11\x63lientTimestampMS\x18\x05 \x01(\x03\x12\x19\n\x11serverTimestampMS\x18\x06 \x01(\x03\"\x9b\x01\n\x17MessageAddOnContextInfo\x12\"\n\x1amessageAddOnDurationInSecs\x18\x01 \x01(\r\x12\\\n\x16messageAddOnExpiryType\x18\x02 \x01(\x0e\x32<.WAWebProtobufsE2E.MessageContextInfo.MessageAddonExpiryType\".\n\x12PremiumMessageInfo\x12\x18\n\x10serverCampaignID\x18\x01 \x01(\t\"\xb2\x01\n\rEventResponse\x12\x35\n\x17\x65ventResponseMessageKey\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x13\n\x0btimestampMS\x18\x02 \x01(\x03\x12\x45\n\x14\x65ventResponseMessage\x18\x03 \x01(\x0b\x32\'.WAWebProtobufsE2E.EventResponseMessage\x12\x0e\n\x06unread\x18\x04 \x01(\x08\"\x8c\x01\n\rLegacyMessage\x12\x45\n\x14\x65ventResponseMessage\x18\x01 \x01(\x0b\x32\'.WAWebProtobufsE2E.EventResponseMessage\x12\x34\n\x08pollVote\x18\x02 \x01(\x0b\x32\".WAWebProtobufsE2E.PollVoteMessage\"H\n\x14StatusMentionMessage\x12\x30\n\x0cquotedStatus\x18\x01 \x01(\x0b\x32\x1a.WAWebProtobufsE2E.Message\"L\n\x08\x43itation\x12\r\n\x05title\x18\x01 \x02(\t\x12\x10\n\x08subtitle\x18\x02 \x02(\t\x12\r\n\x05\x63msID\x18\x03 \x02(\t\x12\x10\n\x08imageURL\x18\x04 \x02(\tB!Z\x1fgo.mau.fi/whatsmeow/proto/waWeb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waWeb.WAWebProtobufsWeb_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\037go.mau.fi/whatsmeow/proto/waWeb'
  _globals['_WEBMESSAGEINFO']._serialized_start=109
  _globals['_WEBMESSAGEINFO']._serialized_end=9948
  _globals['_WEBMESSAGEINFO_BIZPRIVACYSTATUS']._serialized_start=2563
  _globals['_WEBMESSAGEINFO_BIZPRIVACYSTATUS']._serialized_end=2624
  _globals['_WEBMESSAGEINFO_STUBTYPE']._serialized_start=2627
  _globals['_WEBMESSAGEINFO_STUBTYPE']._serialized_end=9858
  _globals['_WEBMESSAGEINFO_STATUS']._serialized_start=9860
  _globals['_WEBMESSAGEINFO_STATUS']._serialized_end=9948
  _globals['_PAYMENTINFO']._serialized_start=9951
  _globals['_PAYMENTINFO']._serialized_end=11379
  _globals['_PAYMENTINFO_TXNSTATUS']._serialized_start=10464
  _globals['_PAYMENTINFO_TXNSTATUS']._serialized_end=11129
  _globals['_PAYMENTINFO_STATUS']._serialized_start=11132
  _globals['_PAYMENTINFO_STATUS']._serialized_end=11336
  _globals['_PAYMENTINFO_CURRENCY']._serialized_start=11338
  _globals['_PAYMENTINFO_CURRENCY']._serialized_end=11379
  _globals['_WEBFEATURES']._serialized_start=11382
  _globals['_WEBFEATURES']._serialized_end=14317
  _globals['_WEBFEATURES_FLAG']._serialized_start=14242
  _globals['_WEBFEATURES_FLAG']._serialized_end=14317
  _globals['_PININCHAT']._serialized_start=14320
  _globals['_PININCHAT']._serialized_end=14608
  _globals['_PININCHAT_TYPE']._serialized_start=14548
  _globals['_PININCHAT_TYPE']._serialized_end=14608
  _globals['_MESSAGEADDON']._serialized_start=14611
  _globals['_MESSAGEADDON']._serialized_end=15140
  _globals['_MESSAGEADDON_MESSAGEADDONTYPE']._serialized_start=15039
  _globals['_MESSAGEADDON_MESSAGEADDONTYPE']._serialized_end=15140
  _globals['_COMMENTMETADATA']._serialized_start=15142
  _globals['_COMMENTMETADATA']._serialized_end=15227
  _globals['_WEBNOTIFICATIONSINFO']._serialized_start=15230
  _globals['_WEBNOTIFICATIONSINFO']._serialized_end=15379
  _globals['_NOTIFICATIONMESSAGEINFO']._serialized_start=15382
  _globals['_NOTIFICATIONMESSAGEINFO']._serialized_end=15534
  _globals['_REPORTINGTOKENINFO']._serialized_start=15536
  _globals['_REPORTINGTOKENINFO']._serialized_end=15578
  _globals['_MEDIADATA']._serialized_start=15580
  _globals['_MEDIADATA']._serialized_end=15610
  _globals['_PHOTOCHANGE']._serialized_start=15612
  _globals['_PHOTOCHANGE']._serialized_end=15681
  _globals['_STATUSPSA']._serialized_start=15683
  _globals['_STATUSPSA']._serialized_end=15751
  _globals['_USERRECEIPT']._serialized_start=15754
  _globals['_USERRECEIPT']._serialized_end=15912
  _globals['_REACTION']._serialized_start=15914
  _globals['_REACTION']._serialized_end=16037
  _globals['_POLLUPDATE']._serialized_start=16040
  _globals['_POLLUPDATE']._serialized_end=16224
  _globals['_POLLADDITIONALMETADATA']._serialized_start=16226
  _globals['_POLLADDITIONALMETADATA']._serialized_end=16275
  _globals['_EVENTADDITIONALMETADATA']._serialized_start=16277
  _globals['_EVENTADDITIONALMETADATA']._serialized_end=16319
  _globals['_KEEPINCHAT']._serialized_start=16322
  _globals['_KEEPINCHAT']._serialized_end=16514
  _globals['_MESSAGEADDONCONTEXTINFO']._serialized_start=16517
  _globals['_MESSAGEADDONCONTEXTINFO']._serialized_end=16672
  _globals['_PREMIUMMESSAGEINFO']._serialized_start=16674
  _globals['_PREMIUMMESSAGEINFO']._serialized_end=16720
  _globals['_EVENTRESPONSE']._serialized_start=16723
  _globals['_EVENTRESPONSE']._serialized_end=16901
  _globals['_LEGACYMESSAGE']._serialized_start=16904
  _globals['_LEGACYMESSAGE']._serialized_end=17044
  _globals['_STATUSMENTIONMESSAGE']._serialized_start=17046
  _globals['_STATUSMENTIONMESSAGE']._serialized_end=17118
  _globals['_CITATION']._serialized_start=17120
  _globals['_CITATION']._serialized_end=17196
# @@protoc_insertion_point(module_scope)
