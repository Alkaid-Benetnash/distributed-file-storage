# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dfs_bc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dfs_bc.proto',
  package='center',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x64\x66s_bc.proto\x12\x06\x63\x65nter\"\xba\x01\n\x05\x42lock\x12)\n\x06struct\x18\x01 \x01(\x0b\x32\x19.center.Block.BlockStruct\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x1as\n\x0b\x42lockStruct\x12\n\n\x02PK\x18\x01 \x01(\x0c\x12\x0e\n\x06parent\x18\x02 \x01(\x0c\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x14\n\x0cpayload_hash\x18\x04 \x01(\x0c\x12\x11\n\troot_hash\x18\x05 \x01(\x0c\x12\x0f\n\x07sym_key\x18\x06 \x01(\x0c\x42\x1b\n\x12\x63n.edu.ustc.centerB\x05\x44\x46SBCb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BLOCK_BLOCKSTRUCT = _descriptor.Descriptor(
  name='BlockStruct',
  full_name='center.Block.BlockStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PK', full_name='center.Block.BlockStruct.PK', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent', full_name='center.Block.BlockStruct.parent', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='center.Block.BlockStruct.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_hash', full_name='center.Block.BlockStruct.payload_hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_hash', full_name='center.Block.BlockStruct.root_hash', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sym_key', full_name='center.Block.BlockStruct.sym_key', index=5,
      number=6, type=12, cpp_type=9, label=1,
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
  serialized_start=96,
  serialized_end=211,
)

_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='center.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='struct', full_name='center.Block.struct', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='center.Block.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BLOCK_BLOCKSTRUCT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=211,
)

_BLOCK_BLOCKSTRUCT.containing_type = _BLOCK
_BLOCK.fields_by_name['struct'].message_type = _BLOCK_BLOCKSTRUCT
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(

  BlockStruct = _reflection.GeneratedProtocolMessageType('BlockStruct', (_message.Message,), dict(
    DESCRIPTOR = _BLOCK_BLOCKSTRUCT,
    __module__ = 'dfs_bc_pb2'
    # @@protoc_insertion_point(class_scope:center.Block.BlockStruct)
    ))
  ,
  DESCRIPTOR = _BLOCK,
  __module__ = 'dfs_bc_pb2'
  # @@protoc_insertion_point(class_scope:center.Block)
  ))
_sym_db.RegisterMessage(Block)
_sym_db.RegisterMessage(Block.BlockStruct)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022cn.edu.ustc.centerB\005DFSBC'))
# @@protoc_insertion_point(module_scope)
