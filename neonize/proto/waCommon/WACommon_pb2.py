# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waCommon/WACommon.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 2, "", "waCommon/WACommon.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17waCommon/WACommon.proto\x12\x08WACommon"P\n\nMessageKey\x12\x11\n\tremoteJID\x18\x01 \x01(\t\x12\x0e\n\x06\x66romMe\x18\x02 \x01(\x08\x12\n\n\x02ID\x18\x03 \x01(\t\x12\x13\n\x0bparticipant\x18\x04 \x01(\t"\xb7\x01\n\x07\x43ommand\x12\x32\n\x0b\x63ommandType\x18\x01 \x01(\x0e\x32\x1d.WACommon.Command.CommandType\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0e\n\x06length\x18\x03 \x01(\r\x12\x17\n\x0fvalidationToken\x18\x04 \x01(\t"?\n\x0b\x43ommandType\x12\x0c\n\x08\x45VERYONE\x10\x01\x12\n\n\x06SILENT\x10\x02\x12\x06\n\x02\x41I\x10\x03\x12\x0e\n\nAI_IMAGINE\x10\x04"V\n\x0bMessageText\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0cmentionedJID\x18\x02 \x03(\t\x12#\n\x08\x63ommands\x18\x03 \x03(\x0b\x32\x11.WACommon.Command"/\n\x0bSubProtocol\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x0f\n\x07version\x18\x02 \x01(\x05*F\n\x13\x46utureProofBehavior\x12\x0f\n\x0bPLACEHOLDER\x10\x00\x12\x12\n\x0eNO_PLACEHOLDER\x10\x01\x12\n\n\x06IGNORE\x10\x02\x42$Z"go.mau.fi/whatsmeow/proto/waCommon'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "waCommon.WACommon_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b'Z"go.mau.fi/whatsmeow/proto/waCommon'
    _globals["_FUTUREPROOFBEHAVIOR"]._serialized_start = 442
    _globals["_FUTUREPROOFBEHAVIOR"]._serialized_end = 512
    _globals["_MESSAGEKEY"]._serialized_start = 37
    _globals["_MESSAGEKEY"]._serialized_end = 117
    _globals["_COMMAND"]._serialized_start = 120
    _globals["_COMMAND"]._serialized_end = 303
    _globals["_COMMAND_COMMANDTYPE"]._serialized_start = 240
    _globals["_COMMAND_COMMANDTYPE"]._serialized_end = 303
    _globals["_MESSAGETEXT"]._serialized_start = 305
    _globals["_MESSAGETEXT"]._serialized_end = 391
    _globals["_SUBPROTOCOL"]._serialized_start = 393
    _globals["_SUBPROTOCOL"]._serialized_end = 440
# @@protoc_insertion_point(module_scope)
