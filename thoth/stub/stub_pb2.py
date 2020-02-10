# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thoth/stub/stub.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='thoth/stub/stub.proto',
  package='stub',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15thoth/stub/stub.proto\x12\x04stub\"V\n\x0cInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x18\n\x10\x63onnexionVersion\x18\x02 \x01(\t\x12\x1b\n\x13jaegerClientVersion\x18\x03 \x01(\t\"\x07\n\x05\x45mpty2/\n\x04Stub\x12\'\n\x04Info\x12\x0b.stub.Empty\x1a\x12.stub.InfoResponseb\x06proto3'),
)




_INFORESPONSE = _descriptor.Descriptor(
  name='InfoResponse',
  full_name='stub.InfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='stub.InfoResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,
    ),
    _descriptor.FieldDescriptor(
      name='connexionVersion', full_name='stub.InfoResponse.connexionVersion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,
    ),
    _descriptor.FieldDescriptor(
      name='jaegerClientVersion', full_name='stub.InfoResponse.jaegerClientVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,
    ),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=117,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='stub.Empty',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['InfoResponse'] = _INFORESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InfoResponse = _reflection.GeneratedProtocolMessageType(
    'InfoResponse', (_message.Message,), dict(
    DESCRIPTOR = _INFORESPONSE,
    __module__ = 'thoth.stub.stub_pb2',
    # @@protoc_insertion_point(class_scope:stub.InfoResponse)
    ),
)
_sym_db.RegisterMessage(InfoResponse)

Empty = _reflection.GeneratedProtocolMessageType(
    'Empty', (_message.Message,), dict(
    DESCRIPTOR = _EMPTY,
    __module__ = 'thoth.stub.stub_pb2',
    # @@protoc_insertion_point(class_scope:stub.Empty)
    ),
)
_sym_db.RegisterMessage(Empty)



_STUB = _descriptor.ServiceDescriptor(
  name='Stub',
  full_name='stub.Stub',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=128,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='Info',
    full_name='stub.Stub.Info',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_INFORESPONSE,
    serialized_options=None,
  ),
],
)
_sym_db.RegisterServiceDescriptor(_STUB)

DESCRIPTOR.services_by_name['Stub'] = _STUB

# @@protoc_insertion_point(module_scope)
