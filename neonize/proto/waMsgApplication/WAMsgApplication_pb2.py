# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waMsgApplication/WAMsgApplication.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'waMsgApplication/WAMsgApplication.proto\x12\x10WAMsgApplication\x1a\x17waCommon/WACommon.proto\"\xec\x0f\n\x12MessageApplication\x12=\n\x07payload\x18\x01 \x01(\x0b\x32,.WAMsgApplication.MessageApplication.Payload\x12?\n\x08metadata\x18\x02 \x01(\x0b\x32-.WAMsgApplication.MessageApplication.Metadata\x1a\x8c\x08\n\x08Metadata\x12U\n\x14\x63hatEphemeralSetting\x18\x01 \x01(\x0b\x32\x35.WAMsgApplication.MessageApplication.EphemeralSettingH\x00\x12\x61\n\x14\x65phemeralSettingList\x18\x02 \x01(\x0b\x32\x41.WAMsgApplication.MessageApplication.Metadata.EphemeralSettingMapH\x00\x12\x1f\n\x15\x65phemeralSharedSecret\x18\x03 \x01(\x0cH\x00\x12\x17\n\x0f\x66orwardingScore\x18\x05 \x01(\r\x12\x13\n\x0bisForwarded\x18\x06 \x01(\x08\x12/\n\x10\x62usinessMetadata\x18\x07 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12\x13\n\x0b\x66rankingKey\x18\x08 \x01(\x0c\x12\x17\n\x0f\x66rankingVersion\x18\t \x01(\x05\x12R\n\rquotedMessage\x18\n \x01(\x0b\x32;.WAMsgApplication.MessageApplication.Metadata.QuotedMessage\x12L\n\nthreadType\x18\x0b \x01(\x0e\x32\x38.WAMsgApplication.MessageApplication.Metadata.ThreadType\x12!\n\x19readonlyMetadataDataclass\x18\x0c \x01(\t\x12\x0f\n\x07groupID\x18\r \x01(\t\x12\x11\n\tgroupSize\x18\x0e \x01(\r\x12\x12\n\ngroupIndex\x18\x0f \x01(\r\x12\x15\n\rbotResponseID\x18\x10 \x01(\t\x12\x15\n\rcollapsibleID\x18\x11 \x01(\t\x12\x15\n\rsecondaryOtid\x18\x12 \x01(\t\x1a\x88\x01\n\rQuotedMessage\x12\x10\n\x08stanzaID\x18\x01 \x01(\t\x12\x11\n\tremoteJID\x18\x02 \x01(\t\x12\x13\n\x0bparticipant\x18\x03 \x01(\t\x12=\n\x07payload\x18\x04 \x01(\x0b\x32,.WAMsgApplication.MessageApplication.Payload\x1aw\n\x13\x45phemeralSettingMap\x12\x0f\n\x07\x63hatJID\x18\x01 \x01(\t\x12O\n\x10\x65phemeralSetting\x18\x02 \x01(\x0b\x32\x35.WAMsgApplication.MessageApplication.EphemeralSetting\"E\n\nThreadType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0f\n\x0bVANISH_MODE\x10\x01\x12\x19\n\x15\x44ISAPPEARING_MESSAGES\x10\x02\x42\x0b\n\tephemeral\x1a\xb9\x02\n\x07Payload\x12\x43\n\x0b\x63oreContent\x18\x01 \x01(\x0b\x32,.WAMsgApplication.MessageApplication.ContentH\x00\x12=\n\x06signal\x18\x02 \x01(\x0b\x32+.WAMsgApplication.MessageApplication.SignalH\x00\x12O\n\x0f\x61pplicationData\x18\x03 \x01(\x0b\x32\x34.WAMsgApplication.MessageApplication.ApplicationDataH\x00\x12N\n\x0bsubProtocol\x18\x04 \x01(\x0b\x32\x37.WAMsgApplication.MessageApplication.SubProtocolPayloadH\x00\x42\t\n\x07\x63ontent\x1a\xed\x02\n\x12SubProtocolPayload\x12\x30\n\x0f\x63onsumerMessage\x18\x02 \x01(\x0b\x32\x15.WACommon.SubProtocolH\x00\x12\x30\n\x0f\x62usinessMessage\x18\x03 \x01(\x0b\x32\x15.WACommon.SubProtocolH\x00\x12/\n\x0epaymentMessage\x18\x04 \x01(\x0b\x32\x15.WACommon.SubProtocolH\x00\x12,\n\x0bmultiDevice\x18\x05 \x01(\x0b\x32\x15.WACommon.SubProtocolH\x00\x12%\n\x04voip\x18\x06 \x01(\x0b\x32\x15.WACommon.SubProtocolH\x00\x12*\n\tarmadillo\x18\x07 \x01(\x0b\x32\x15.WACommon.SubProtocolH\x00\x12\x32\n\x0b\x66utureProof\x18\x01 \x01(\x0e\x32\x1d.WACommon.FutureProofBehaviorB\r\n\x0bsubProtocol\x1a\x11\n\x0f\x41pplicationData\x1a\x08\n\x06Signal\x1a\t\n\x07\x43ontent\x1as\n\x10\x45phemeralSetting\x12\x1b\n\x13\x65phemeralExpiration\x18\x02 \x01(\r\x12!\n\x19\x65phemeralSettingTimestamp\x18\x03 \x01(\x03\x12\x1f\n\x17isEphemeralSettingReset\x18\x04 \x01(\x08\x42,Z*go.mau.fi/whatsmeow/proto/waMsgApplication')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waMsgApplication.WAMsgApplication_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*go.mau.fi/whatsmeow/proto/waMsgApplication'
  _globals['_MESSAGEAPPLICATION']._serialized_start=87
  _globals['_MESSAGEAPPLICATION']._serialized_end=2115
  _globals['_MESSAGEAPPLICATION_METADATA']._serialized_start=238
  _globals['_MESSAGEAPPLICATION_METADATA']._serialized_end=1274
  _globals['_MESSAGEAPPLICATION_METADATA_QUOTEDMESSAGE']._serialized_start=933
  _globals['_MESSAGEAPPLICATION_METADATA_QUOTEDMESSAGE']._serialized_end=1069
  _globals['_MESSAGEAPPLICATION_METADATA_EPHEMERALSETTINGMAP']._serialized_start=1071
  _globals['_MESSAGEAPPLICATION_METADATA_EPHEMERALSETTINGMAP']._serialized_end=1190
  _globals['_MESSAGEAPPLICATION_METADATA_THREADTYPE']._serialized_start=1192
  _globals['_MESSAGEAPPLICATION_METADATA_THREADTYPE']._serialized_end=1261
  _globals['_MESSAGEAPPLICATION_PAYLOAD']._serialized_start=1277
  _globals['_MESSAGEAPPLICATION_PAYLOAD']._serialized_end=1590
  _globals['_MESSAGEAPPLICATION_SUBPROTOCOLPAYLOAD']._serialized_start=1593
  _globals['_MESSAGEAPPLICATION_SUBPROTOCOLPAYLOAD']._serialized_end=1958
  _globals['_MESSAGEAPPLICATION_APPLICATIONDATA']._serialized_start=1960
  _globals['_MESSAGEAPPLICATION_APPLICATIONDATA']._serialized_end=1977
  _globals['_MESSAGEAPPLICATION_SIGNAL']._serialized_start=1979
  _globals['_MESSAGEAPPLICATION_SIGNAL']._serialized_end=1987
  _globals['_MESSAGEAPPLICATION_CONTENT']._serialized_start=1989
  _globals['_MESSAGEAPPLICATION_CONTENT']._serialized_end=1998
  _globals['_MESSAGEAPPLICATION_EPHEMERALSETTING']._serialized_start=2000
  _globals['_MESSAGEAPPLICATION_EPHEMERALSETTING']._serialized_end=2115
# @@protoc_insertion_point(module_scope)
