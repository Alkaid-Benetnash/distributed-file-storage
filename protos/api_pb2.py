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
  serialized_pb=_b('\n\tapi.proto\x12\x06\x63\x65nter\"9\n\nFS_Request\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.center.Type\x12\x0f\n\x07payload\x18\x02 \x03(\x0c\"Z\n\x0b\x46S_Response\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.center.Type\x12\x1e\n\x06result\x18\x02 \x01(\x0e\x32\x0e.center.Result\x12\x0f\n\x07payload\x18\x03 \x03(\x0c\"=\n\x0frequest_inquiry\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\x1a\n\x12\x63urrent_block_hash\x18\x02 \x01(\x0c\">\n\x0frespond_inquiry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x66orking\x18\x02 \x01(\x05\x12\x0e\n\x06hashes\x18\x03 \x03(\x0c\"\x0c\n\nBC_Request\"\r\n\x0b\x42\x43_Response*P\n\x04Type\x12\x11\n\rFILE_DOWNLOAD\x10\x00\x12\x12\n\x0eINDEX_DOWNLOAD\x10\x01\x12\x0f\n\x0b\x46ILE_UPLOAD\x10\x02\x12\x10\n\x0cINDEX_UPLOAD\x10\x03*-\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0c\x46\x41ST_FORWARD\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x32[\n\nBlockChain\x12M\n\x17receive_request_inquiry\x12\x17.center.request_inquiry\x1a\x17.center.respond_inquiry\"\x00\x32\x41\n\tFSService\x12\x34\n\x07\x46SServe\x12\x12.center.FS_Request\x1a\x13.center.FS_Response\"\x00\x42\x1f\n\x12\x63n.edu.ustc.centerB\tApiProtosb\x06proto3')
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
  serialized_start=328,
  serialized_end=408,
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
  serialized_start=410,
  serialized_end=455,
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


_REQUEST_INQUIRY = _descriptor.Descriptor(
  name='request_inquiry',
  full_name='center.request_inquiry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='center.request_inquiry.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_block_hash', full_name='center.request_inquiry.current_block_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=172,
  serialized_end=233,
)


_RESPOND_INQUIRY = _descriptor.Descriptor(
  name='respond_inquiry',
  full_name='center.respond_inquiry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='center.respond_inquiry.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forking', full_name='center.respond_inquiry.forking', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hashes', full_name='center.respond_inquiry.hashes', index=2,
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
  serialized_start=235,
  serialized_end=297,
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
  serialized_start=299,
  serialized_end=311,
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
  serialized_start=313,
  serialized_end=326,
)

_FS_REQUEST.fields_by_name['type'].enum_type = _TYPE
_FS_RESPONSE.fields_by_name['type'].enum_type = _TYPE
_FS_RESPONSE.fields_by_name['result'].enum_type = _RESULT
DESCRIPTOR.message_types_by_name['FS_Request'] = _FS_REQUEST
DESCRIPTOR.message_types_by_name['FS_Response'] = _FS_RESPONSE
DESCRIPTOR.message_types_by_name['request_inquiry'] = _REQUEST_INQUIRY
DESCRIPTOR.message_types_by_name['respond_inquiry'] = _RESPOND_INQUIRY
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

request_inquiry = _reflection.GeneratedProtocolMessageType('request_inquiry', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_INQUIRY,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.request_inquiry)
  ))
_sym_db.RegisterMessage(request_inquiry)

respond_inquiry = _reflection.GeneratedProtocolMessageType('respond_inquiry', (_message.Message,), dict(
  DESCRIPTOR = _RESPOND_INQUIRY,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.respond_inquiry)
  ))
_sym_db.RegisterMessage(respond_inquiry)

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
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class BlockChainStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.receive_request_inquiry = channel.unary_unary(
        '/center.BlockChain/receive_request_inquiry',
        request_serializer=request_inquiry.SerializeToString,
        response_deserializer=respond_inquiry.FromString,
        )


class BlockChainServicer(object):

  def receive_request_inquiry(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BlockChainServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'receive_request_inquiry': grpc.unary_unary_rpc_method_handler(
          servicer.receive_request_inquiry,
          request_deserializer=request_inquiry.FromString,
          response_serializer=respond_inquiry.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'center.BlockChain', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaBlockChainServicer(object):
  def receive_request_inquiry(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaBlockChainStub(object):
  def receive_request_inquiry(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  receive_request_inquiry.future = None


def beta_create_BlockChain_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('center.BlockChain', 'receive_request_inquiry'): request_inquiry.FromString,
  }
  response_serializers = {
    ('center.BlockChain', 'receive_request_inquiry'): respond_inquiry.SerializeToString,
  }
  method_implementations = {
    ('center.BlockChain', 'receive_request_inquiry'): face_utilities.unary_unary_inline(servicer.receive_request_inquiry),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_BlockChain_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('center.BlockChain', 'receive_request_inquiry'): request_inquiry.SerializeToString,
  }
  response_deserializers = {
    ('center.BlockChain', 'receive_request_inquiry'): respond_inquiry.FromString,
  }
  cardinalities = {
    'receive_request_inquiry': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'center.BlockChain', cardinalities, options=stub_options)


class FSServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FSServe = channel.unary_unary(
        '/center.FSService/FSServe',
        request_serializer=FS_Request.SerializeToString,
        response_deserializer=FS_Response.FromString,
        )


class FSServiceServicer(object):

  def FSServe(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FSServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FSServe': grpc.unary_unary_rpc_method_handler(
          servicer.FSServe,
          request_deserializer=FS_Request.FromString,
          response_serializer=FS_Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'center.FSService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaFSServiceServicer(object):
  def FSServe(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaFSServiceStub(object):
  def FSServe(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  FSServe.future = None


def beta_create_FSService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('center.FSService', 'FSServe'): FS_Request.FromString,
  }
  response_serializers = {
    ('center.FSService', 'FSServe'): FS_Response.SerializeToString,
  }
  method_implementations = {
    ('center.FSService', 'FSServe'): face_utilities.unary_unary_inline(servicer.FSServe),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_FSService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('center.FSService', 'FSServe'): FS_Request.SerializeToString,
  }
  response_deserializers = {
    ('center.FSService', 'FSServe'): FS_Response.FromString,
  }
  cardinalities = {
    'FSServe': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'center.FSService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
