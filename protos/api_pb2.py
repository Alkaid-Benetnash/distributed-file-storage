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


import dfs_bc_pb2 as dfs__bc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='center',
  syntax='proto3',
  serialized_pb=_b('\n\tapi.proto\x12\x06\x63\x65nter\x1a\x0c\x64\x66s_bc.proto\"9\n\nFS_Request\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.center.Type\x12\x0f\n\x07payload\x18\x02 \x03(\x0c\"Z\n\x0b\x46S_Response\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.center.Type\x12\x1e\n\x06result\x18\x02 \x01(\x0e\x32\x0e.center.Result\x12\x0f\n\x07payload\x18\x03 \x03(\x0c\"=\n\x0frequest_inquiry\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\x1a\n\x12\x63urrent_block_hash\x18\x02 \x01(\x0c\"?\n\x10response_inquiry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x66orking\x18\x02 \x01(\x08\x12\x0e\n\x06hashes\x18\x03 \x03(\x0c\")\n\x0brequest_syn\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06hashes\x18\x02 \x03(\x0c\":\n\x0cresponse_syn\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x1c\n\x05\x62lock\x18\x02 \x01(\x0b\x32\r.center.Block\",\n\x0crequest_push\x12\x1c\n\x05\x62lock\x18\x01 \x01(\x0b\x32\r.center.Block\",\n\rresponse_push\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63onfirm\x18\x02 \x01(\x08*Z\n\x04Type\x12\x11\n\rFILE_DOWNLOAD\x10\x00\x12\x12\n\x0eINDEX_DOWNLOAD\x10\x01\x12\x0f\n\x0b\x46ILE_UPLOAD\x10\x02\x12\x10\n\x0cINDEX_UPLOAD\x10\x03\x12\x08\n\x04\x45XIT\x10\x04*-\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0c\x46\x41ST_FORWARD\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x32\xe9\x01\n\nBlockChain\x12N\n\x17receive_request_inquiry\x12\x17.center.request_inquiry\x1a\x18.center.response_inquiry\"\x00\x12\x44\n\x13receive_request_syn\x12\x13.center.request_syn\x1a\x14.center.response_syn\"\x00\x30\x01\x12\x45\n\x14receive_request_push\x12\x14.center.request_push\x1a\x15.center.response_push\"\x00\x32\xee\x01\n\x0bJavaForward\x12P\n\x17request_inquiry_forward\x12\x17.center.request_inquiry\x1a\x18.center.response_inquiry\"\x00\x30\x01\x12\x44\n\x13request_syn_forward\x12\x13.center.request_syn\x1a\x14.center.response_syn\"\x00\x30\x01\x12G\n\x14request_push_forward\x12\x14.center.request_push\x1a\x15.center.response_push\"\x00\x30\x01\x32\x41\n\tFSService\x12\x34\n\x07\x46SServe\x12\x12.center.FS_Request\x1a\x13.center.FS_Response\"\x00\x42\x1f\n\x12\x63n.edu.ustc.centerB\tApiProtosb\x06proto3')
  ,
  dependencies=[dfs__bc__pb2.DESCRIPTOR,])
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
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=509,
  serialized_end=599,
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
  serialized_start=601,
  serialized_end=646,
)
_sym_db.RegisterEnumDescriptor(_RESULT)

Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
FILE_DOWNLOAD = 0
INDEX_DOWNLOAD = 1
FILE_UPLOAD = 2
INDEX_UPLOAD = 3
EXIT = 4
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
  serialized_start=35,
  serialized_end=92,
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
  serialized_start=94,
  serialized_end=184,
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
  serialized_start=186,
  serialized_end=247,
)


_RESPONSE_INQUIRY = _descriptor.Descriptor(
  name='response_inquiry',
  full_name='center.response_inquiry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='center.response_inquiry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forking', full_name='center.response_inquiry.forking', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hashes', full_name='center.response_inquiry.hashes', index=2,
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
  serialized_start=249,
  serialized_end=312,
)


_REQUEST_SYN = _descriptor.Descriptor(
  name='request_syn',
  full_name='center.request_syn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='center.request_syn.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hashes', full_name='center.request_syn.hashes', index=1,
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
  serialized_start=314,
  serialized_end=355,
)


_RESPONSE_SYN = _descriptor.Descriptor(
  name='response_syn',
  full_name='center.response_syn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='center.response_syn.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='center.response_syn.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=357,
  serialized_end=415,
)


_REQUEST_PUSH = _descriptor.Descriptor(
  name='request_push',
  full_name='center.request_push',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='center.request_push.block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=417,
  serialized_end=461,
)


_RESPONSE_PUSH = _descriptor.Descriptor(
  name='response_push',
  full_name='center.response_push',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='center.response_push.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confirm', full_name='center.response_push.confirm', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=463,
  serialized_end=507,
)

_FS_REQUEST.fields_by_name['type'].enum_type = _TYPE
_FS_RESPONSE.fields_by_name['type'].enum_type = _TYPE
_FS_RESPONSE.fields_by_name['result'].enum_type = _RESULT
_RESPONSE_SYN.fields_by_name['block'].message_type = dfs__bc__pb2._BLOCK
_REQUEST_PUSH.fields_by_name['block'].message_type = dfs__bc__pb2._BLOCK
DESCRIPTOR.message_types_by_name['FS_Request'] = _FS_REQUEST
DESCRIPTOR.message_types_by_name['FS_Response'] = _FS_RESPONSE
DESCRIPTOR.message_types_by_name['request_inquiry'] = _REQUEST_INQUIRY
DESCRIPTOR.message_types_by_name['response_inquiry'] = _RESPONSE_INQUIRY
DESCRIPTOR.message_types_by_name['request_syn'] = _REQUEST_SYN
DESCRIPTOR.message_types_by_name['response_syn'] = _RESPONSE_SYN
DESCRIPTOR.message_types_by_name['request_push'] = _REQUEST_PUSH
DESCRIPTOR.message_types_by_name['response_push'] = _RESPONSE_PUSH
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

response_inquiry = _reflection.GeneratedProtocolMessageType('response_inquiry', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_INQUIRY,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.response_inquiry)
  ))
_sym_db.RegisterMessage(response_inquiry)

request_syn = _reflection.GeneratedProtocolMessageType('request_syn', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_SYN,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.request_syn)
  ))
_sym_db.RegisterMessage(request_syn)

response_syn = _reflection.GeneratedProtocolMessageType('response_syn', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_SYN,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.response_syn)
  ))
_sym_db.RegisterMessage(response_syn)

request_push = _reflection.GeneratedProtocolMessageType('request_push', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_PUSH,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.request_push)
  ))
_sym_db.RegisterMessage(request_push)

response_push = _reflection.GeneratedProtocolMessageType('response_push', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_PUSH,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:center.response_push)
  ))
_sym_db.RegisterMessage(response_push)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022cn.edu.ustc.centerB\tApiProtos'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class BlockChainStub(object):
  """
  说明：
  receive_request_inquiry是第一种需要广播的模型
  调用过程是 发起请求的python端构造request_inquiry, 调用JavaForward的reques_inquiry_forward, java传给对面的java之后，java调用BlockChain的receive_request_inquiry, python会返回一个respond_inquiry，其中id是无效的，java接收到之后要补上id，回复给请求端的java。再之后，请求端的java要把广播得到的回复放到一个队列里，通过stream response的方式返回给python.
  receive_request_syn是第二种指定连接对象的模型
  调用过程是 发起请求的python端构造request_syn, 调用JavaForward的request_syn_forward, java根据request的id域指示连接指定的java, 对面的java再调用BlockChain的receive_request_syn, 返回一个stream的response_syn, 最后java负责传递stream的response到请求端的python.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.receive_request_inquiry = channel.unary_unary(
        '/center.BlockChain/receive_request_inquiry',
        request_serializer=request_inquiry.SerializeToString,
        response_deserializer=response_inquiry.FromString,
        )
    self.receive_request_syn = channel.unary_stream(
        '/center.BlockChain/receive_request_syn',
        request_serializer=request_syn.SerializeToString,
        response_deserializer=response_syn.FromString,
        )
    self.receive_request_push = channel.unary_unary(
        '/center.BlockChain/receive_request_push',
        request_serializer=request_push.SerializeToString,
        response_deserializer=response_push.FromString,
        )


class BlockChainServicer(object):
  """
  说明：
  receive_request_inquiry是第一种需要广播的模型
  调用过程是 发起请求的python端构造request_inquiry, 调用JavaForward的reques_inquiry_forward, java传给对面的java之后，java调用BlockChain的receive_request_inquiry, python会返回一个respond_inquiry，其中id是无效的，java接收到之后要补上id，回复给请求端的java。再之后，请求端的java要把广播得到的回复放到一个队列里，通过stream response的方式返回给python.
  receive_request_syn是第二种指定连接对象的模型
  调用过程是 发起请求的python端构造request_syn, 调用JavaForward的request_syn_forward, java根据request的id域指示连接指定的java, 对面的java再调用BlockChain的receive_request_syn, 返回一个stream的response_syn, 最后java负责传递stream的response到请求端的python.
  """

  def receive_request_inquiry(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def receive_request_syn(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def receive_request_push(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BlockChainServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'receive_request_inquiry': grpc.unary_unary_rpc_method_handler(
          servicer.receive_request_inquiry,
          request_deserializer=request_inquiry.FromString,
          response_serializer=response_inquiry.SerializeToString,
      ),
      'receive_request_syn': grpc.unary_stream_rpc_method_handler(
          servicer.receive_request_syn,
          request_deserializer=request_syn.FromString,
          response_serializer=response_syn.SerializeToString,
      ),
      'receive_request_push': grpc.unary_unary_rpc_method_handler(
          servicer.receive_request_push,
          request_deserializer=request_push.FromString,
          response_serializer=response_push.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'center.BlockChain', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaBlockChainServicer(object):
  """
  说明：
  receive_request_inquiry是第一种需要广播的模型
  调用过程是 发起请求的python端构造request_inquiry, 调用JavaForward的reques_inquiry_forward, java传给对面的java之后，java调用BlockChain的receive_request_inquiry, python会返回一个respond_inquiry，其中id是无效的，java接收到之后要补上id，回复给请求端的java。再之后，请求端的java要把广播得到的回复放到一个队列里，通过stream response的方式返回给python.
  receive_request_syn是第二种指定连接对象的模型
  调用过程是 发起请求的python端构造request_syn, 调用JavaForward的request_syn_forward, java根据request的id域指示连接指定的java, 对面的java再调用BlockChain的receive_request_syn, 返回一个stream的response_syn, 最后java负责传递stream的response到请求端的python.
  """
  def receive_request_inquiry(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def receive_request_syn(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def receive_request_push(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaBlockChainStub(object):
  """
  说明：
  receive_request_inquiry是第一种需要广播的模型
  调用过程是 发起请求的python端构造request_inquiry, 调用JavaForward的reques_inquiry_forward, java传给对面的java之后，java调用BlockChain的receive_request_inquiry, python会返回一个respond_inquiry，其中id是无效的，java接收到之后要补上id，回复给请求端的java。再之后，请求端的java要把广播得到的回复放到一个队列里，通过stream response的方式返回给python.
  receive_request_syn是第二种指定连接对象的模型
  调用过程是 发起请求的python端构造request_syn, 调用JavaForward的request_syn_forward, java根据request的id域指示连接指定的java, 对面的java再调用BlockChain的receive_request_syn, 返回一个stream的response_syn, 最后java负责传递stream的response到请求端的python.
  """
  def receive_request_inquiry(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  receive_request_inquiry.future = None
  def receive_request_syn(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  def receive_request_push(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  receive_request_push.future = None


def beta_create_BlockChain_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('center.BlockChain', 'receive_request_inquiry'): request_inquiry.FromString,
    ('center.BlockChain', 'receive_request_push'): request_push.FromString,
    ('center.BlockChain', 'receive_request_syn'): request_syn.FromString,
  }
  response_serializers = {
    ('center.BlockChain', 'receive_request_inquiry'): response_inquiry.SerializeToString,
    ('center.BlockChain', 'receive_request_push'): response_push.SerializeToString,
    ('center.BlockChain', 'receive_request_syn'): response_syn.SerializeToString,
  }
  method_implementations = {
    ('center.BlockChain', 'receive_request_inquiry'): face_utilities.unary_unary_inline(servicer.receive_request_inquiry),
    ('center.BlockChain', 'receive_request_push'): face_utilities.unary_unary_inline(servicer.receive_request_push),
    ('center.BlockChain', 'receive_request_syn'): face_utilities.unary_stream_inline(servicer.receive_request_syn),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_BlockChain_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('center.BlockChain', 'receive_request_inquiry'): request_inquiry.SerializeToString,
    ('center.BlockChain', 'receive_request_push'): request_push.SerializeToString,
    ('center.BlockChain', 'receive_request_syn'): request_syn.SerializeToString,
  }
  response_deserializers = {
    ('center.BlockChain', 'receive_request_inquiry'): response_inquiry.FromString,
    ('center.BlockChain', 'receive_request_push'): response_push.FromString,
    ('center.BlockChain', 'receive_request_syn'): response_syn.FromString,
  }
  cardinalities = {
    'receive_request_inquiry': cardinality.Cardinality.UNARY_UNARY,
    'receive_request_push': cardinality.Cardinality.UNARY_UNARY,
    'receive_request_syn': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'center.BlockChain', cardinalities, options=stub_options)


class JavaForwardStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.request_inquiry_forward = channel.unary_stream(
        '/center.JavaForward/request_inquiry_forward',
        request_serializer=request_inquiry.SerializeToString,
        response_deserializer=response_inquiry.FromString,
        )
    self.request_syn_forward = channel.unary_stream(
        '/center.JavaForward/request_syn_forward',
        request_serializer=request_syn.SerializeToString,
        response_deserializer=response_syn.FromString,
        )
    self.request_push_forward = channel.unary_stream(
        '/center.JavaForward/request_push_forward',
        request_serializer=request_push.SerializeToString,
        response_deserializer=response_push.FromString,
        )


class JavaForwardServicer(object):

  def request_inquiry_forward(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def request_syn_forward(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def request_push_forward(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JavaForwardServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'request_inquiry_forward': grpc.unary_stream_rpc_method_handler(
          servicer.request_inquiry_forward,
          request_deserializer=request_inquiry.FromString,
          response_serializer=response_inquiry.SerializeToString,
      ),
      'request_syn_forward': grpc.unary_stream_rpc_method_handler(
          servicer.request_syn_forward,
          request_deserializer=request_syn.FromString,
          response_serializer=response_syn.SerializeToString,
      ),
      'request_push_forward': grpc.unary_stream_rpc_method_handler(
          servicer.request_push_forward,
          request_deserializer=request_push.FromString,
          response_serializer=response_push.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'center.JavaForward', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaJavaForwardServicer(object):
  def request_inquiry_forward(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def request_syn_forward(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def request_push_forward(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaJavaForwardStub(object):
  def request_inquiry_forward(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  def request_syn_forward(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  def request_push_forward(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_JavaForward_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('center.JavaForward', 'request_inquiry_forward'): request_inquiry.FromString,
    ('center.JavaForward', 'request_push_forward'): request_push.FromString,
    ('center.JavaForward', 'request_syn_forward'): request_syn.FromString,
  }
  response_serializers = {
    ('center.JavaForward', 'request_inquiry_forward'): response_inquiry.SerializeToString,
    ('center.JavaForward', 'request_push_forward'): response_push.SerializeToString,
    ('center.JavaForward', 'request_syn_forward'): response_syn.SerializeToString,
  }
  method_implementations = {
    ('center.JavaForward', 'request_inquiry_forward'): face_utilities.unary_stream_inline(servicer.request_inquiry_forward),
    ('center.JavaForward', 'request_push_forward'): face_utilities.unary_stream_inline(servicer.request_push_forward),
    ('center.JavaForward', 'request_syn_forward'): face_utilities.unary_stream_inline(servicer.request_syn_forward),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_JavaForward_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('center.JavaForward', 'request_inquiry_forward'): request_inquiry.SerializeToString,
    ('center.JavaForward', 'request_push_forward'): request_push.SerializeToString,
    ('center.JavaForward', 'request_syn_forward'): request_syn.SerializeToString,
  }
  response_deserializers = {
    ('center.JavaForward', 'request_inquiry_forward'): response_inquiry.FromString,
    ('center.JavaForward', 'request_push_forward'): response_push.FromString,
    ('center.JavaForward', 'request_syn_forward'): response_syn.FromString,
  }
  cardinalities = {
    'request_inquiry_forward': cardinality.Cardinality.UNARY_STREAM,
    'request_push_forward': cardinality.Cardinality.UNARY_STREAM,
    'request_syn_forward': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'center.JavaForward', cardinalities, options=stub_options)


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
