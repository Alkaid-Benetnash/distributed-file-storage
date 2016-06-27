# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='center',
  syntax='proto3',
  serialized_pb=_b('\n\tapi.proto\x12\x06\x63\x65nter\"9\n\nFS_Request\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.center.Type\x12\x0f\n\x07payload\x18\x02 \x03(\x0c\"Z\n\x0b\x46S_Response\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.center.Type\x12\x1e\n\x06result\x18\x02 \x01(\x0e\x32\x0e.center.Result\x12\x0f\n\x07payload\x18\x03 \x03(\x0c\"\x0c\n\nBC_Request\"\r\n\x0b\x42\x43_Response*P\n\x04Type\x12\x11\n\rFILE_DOWNLOAD\x10\x00\x12\x12\n\x0eINDEX_DOWNLOAD\x10\x01\x12\x0f\n\x0b\x46ILE_UPLOAD\x10\x02\x12\x10\n\x0cINDEX_UPLOAD\x10\x03*-\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0c\x46\x41ST_FORWARD\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x32\x41\n\tFSService\x12\x34\n\x07\x46SServe\x12\x12.center.FS_Request\x1a\x13.center.FS_Response\"\x00\x42\x1f\n\x12\x63n.edu.ustc.centerB\tApiProtosb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='center.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE_DOWNLOAD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX_DOWNLOAD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE_UPLOAD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX_UPLOAD', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=201,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='center.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAST_FORWARD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=283,
  serialized_end=328,
)
_sym_db.RegisterEnumDescriptor(_RESULT)

Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
FILE_DOWNLOAD = 0
INDEX_DOWNLOAD = 1
FILE_UPLOAD = 2
INDEX_UPLOAD = 3
OK = 0
FAST_FORWARD = 1
ERROR = 2



_FS_REQUEST = _descriptor.Descriptor(
  name='FS_Request',
  full_name='center.FS_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='center.FS_Request.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='center.FS_Request.payload', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=78,
)


_FS_RESPONSE = _descriptor.Descriptor(
  name='FS_Response',
  full_name='center.FS_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='center.FS_Response.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='center.FS_Response.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='center.FS_Response.payload', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=170,
)


_BC_REQUEST = _descriptor.Descriptor(
  name='BC_Request',
  full_name='center.BC_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=184,
)


_BC_RESPONSE = _descriptor.Descriptor(
  name='BC_Response',
  full_name='center.BC_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=199,
)

_FS_REQUEST.fields_by_name['type'].enum_type = _TYPE
_FS_RESPONSE.fields_by_name['type'].enum_type = _TYPE
_FS_RESPONSE.fields_by_name['result'].enum_type = _RESULT
DESCRIPTOR.message_types_by_name['FS_Request'] = _FS_REQUEST
DESCRIPTOR.message_types_by_name['FS_Response'] = _FS_RESPONSE
DESCRIPTOR.message_types_by_name['BC_Request'] = _BC_REQUEST
DESCRIPTOR.message_types_by_name['BC_Response'] = _BC_RESPONSE
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
DESCRIPTOR.enum_types_by_name['Result'] = _RESULT

FS_Request = _reflection.GeneratedProtocolMessageType('FS_Request', (_message.Message,), dict(
  DESCRIPTOR = _FS_REQUEST,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.FS_Request)
  ))
_sym_db.RegisterMessage(FS_Request)

FS_Response = _reflection.GeneratedProtocolMessageType('FS_Response', (_message.Message,), dict(
  DESCRIPTOR = _FS_RESPONSE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.FS_Response)
  ))
_sym_db.RegisterMessage(FS_Response)

BC_Request = _reflection.GeneratedProtocolMessageType('BC_Request', (_message.Message,), dict(
  DESCRIPTOR = _BC_REQUEST,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.BC_Request)
  ))
_sym_db.RegisterMessage(BC_Request)

BC_Response = _reflection.GeneratedProtocolMessageType('BC_Response', (_message.Message,), dict(
  DESCRIPTOR = _BC_RESPONSE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.BC_Response)
  ))
_sym_db.RegisterMessage(BC_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022cn.edu.ustc.centerB\tApiProtos'))
# @@protoc_insertion_point(module_scope)
