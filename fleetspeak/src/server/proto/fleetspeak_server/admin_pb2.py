# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fleetspeak/src/server/proto/fleetspeak_server/admin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from fleetspeak.src.common.proto.fleetspeak import common_pb2 as fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2
from fleetspeak.src.server.proto.fleetspeak_server import broadcasts_pb2 as fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_broadcasts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fleetspeak/src/server/proto/fleetspeak_server/admin.proto',
  package='fleetspeak.server',
  syntax='proto3',
  serialized_pb=_b('\n9fleetspeak/src/server/proto/fleetspeak_server/admin.proto\x12\x11\x66leetspeak.server\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x33\x66leetspeak/src/common/proto/fleetspeak/common.proto\x1a>fleetspeak/src/server/proto/fleetspeak_server/broadcasts.proto\"X\n\x16\x43reateBroadcastRequest\x12/\n\tbroadcast\x18\x01 \x01(\x0b\x32\x1c.fleetspeak.server.Broadcast\x12\r\n\x05limit\x18\x02 \x01(\x04\"3\n\x1bListActiveBroadcastsRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\"P\n\x1cListActiveBroadcastsResponse\x12\x30\n\nbroadcasts\x18\x01 \x03(\x0b\x32\x1c.fleetspeak.server.Broadcast\"(\n\x12ListClientsRequest\x12\x12\n\nclient_ids\x18\x01 \x03(\x0c\"A\n\x13ListClientsResponse\x12*\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x19.fleetspeak.server.Client\"\x93\x01\n\x06\x43lient\x12\x11\n\tclient_id\x18\x01 \x01(\x0c\x12!\n\x06labels\x18\x02 \x03(\x0b\x32\x11.fleetspeak.Label\x12\x35\n\x11last_contact_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x14last_contact_address\x18\x04 \x01(\t\"-\n\x17GetMessageStatusRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\x0c\"x\n\x18GetMessageStatusResponse\x12\x31\n\rcreation_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x06result\x18\x02 \x01(\x0b\x32\x19.fleetspeak.MessageResult\"I\n\x10StoreFileRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x32\xfe\x04\n\x05\x41\x64min\x12X\n\x0f\x43reateBroadcast\x12).fleetspeak.server.CreateBroadcastRequest\x1a\x18.fleetspeak.EmptyMessage\"\x00\x12y\n\x14ListActiveBroadcasts\x12..fleetspeak.server.ListActiveBroadcastsRequest\x1a/.fleetspeak.server.ListActiveBroadcastsResponse\"\x00\x12^\n\x0bListClients\x12%.fleetspeak.server.ListClientsRequest\x1a&.fleetspeak.server.ListClientsResponse\"\x00\x12m\n\x10GetMessageStatus\x12*.fleetspeak.server.GetMessageStatusRequest\x1a+.fleetspeak.server.GetMessageStatusResponse\"\x00\x12@\n\rInsertMessage\x12\x13.fleetspeak.Message\x1a\x18.fleetspeak.EmptyMessage\"\x00\x12L\n\tStoreFile\x12#.fleetspeak.server.StoreFileRequest\x1a\x18.fleetspeak.EmptyMessage\"\x00\x12\x41\n\tKeepAlive\x12\x18.fleetspeak.EmptyMessage\x1a\x18.fleetspeak.EmptyMessage\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.DESCRIPTOR,fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_broadcasts__pb2.DESCRIPTOR,])




_CREATEBROADCASTREQUEST = _descriptor.Descriptor(
  name='CreateBroadcastRequest',
  full_name='fleetspeak.server.CreateBroadcastRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='broadcast', full_name='fleetspeak.server.CreateBroadcastRequest.broadcast', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='fleetspeak.server.CreateBroadcastRequest.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=230,
  serialized_end=318,
)


_LISTACTIVEBROADCASTSREQUEST = _descriptor.Descriptor(
  name='ListActiveBroadcastsRequest',
  full_name='fleetspeak.server.ListActiveBroadcastsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='fleetspeak.server.ListActiveBroadcastsRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=320,
  serialized_end=371,
)


_LISTACTIVEBROADCASTSRESPONSE = _descriptor.Descriptor(
  name='ListActiveBroadcastsResponse',
  full_name='fleetspeak.server.ListActiveBroadcastsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='broadcasts', full_name='fleetspeak.server.ListActiveBroadcastsResponse.broadcasts', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=373,
  serialized_end=453,
)


_LISTCLIENTSREQUEST = _descriptor.Descriptor(
  name='ListClientsRequest',
  full_name='fleetspeak.server.ListClientsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_ids', full_name='fleetspeak.server.ListClientsRequest.client_ids', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=455,
  serialized_end=495,
)


_LISTCLIENTSRESPONSE = _descriptor.Descriptor(
  name='ListClientsResponse',
  full_name='fleetspeak.server.ListClientsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients', full_name='fleetspeak.server.ListClientsResponse.clients', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=497,
  serialized_end=562,
)


_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='fleetspeak.server.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='fleetspeak.server.Client.client_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='fleetspeak.server.Client.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_contact_time', full_name='fleetspeak.server.Client.last_contact_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_contact_address', full_name='fleetspeak.server.Client.last_contact_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=565,
  serialized_end=712,
)


_GETMESSAGESTATUSREQUEST = _descriptor.Descriptor(
  name='GetMessageStatusRequest',
  full_name='fleetspeak.server.GetMessageStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='fleetspeak.server.GetMessageStatusRequest.message_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=714,
  serialized_end=759,
)


_GETMESSAGESTATUSRESPONSE = _descriptor.Descriptor(
  name='GetMessageStatusResponse',
  full_name='fleetspeak.server.GetMessageStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='fleetspeak.server.GetMessageStatusResponse.creation_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='fleetspeak.server.GetMessageStatusResponse.result', index=1,
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
  serialized_start=761,
  serialized_end=881,
)


_STOREFILEREQUEST = _descriptor.Descriptor(
  name='StoreFileRequest',
  full_name='fleetspeak.server.StoreFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='fleetspeak.server.StoreFileRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='fleetspeak.server.StoreFileRequest.file_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='fleetspeak.server.StoreFileRequest.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=883,
  serialized_end=956,
)

_CREATEBROADCASTREQUEST.fields_by_name['broadcast'].message_type = fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_broadcasts__pb2._BROADCAST
_LISTACTIVEBROADCASTSRESPONSE.fields_by_name['broadcasts'].message_type = fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_broadcasts__pb2._BROADCAST
_LISTCLIENTSRESPONSE.fields_by_name['clients'].message_type = _CLIENT
_CLIENT.fields_by_name['labels'].message_type = fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._LABEL
_CLIENT.fields_by_name['last_contact_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETMESSAGESTATUSRESPONSE.fields_by_name['creation_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETMESSAGESTATUSRESPONSE.fields_by_name['result'].message_type = fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._MESSAGERESULT
DESCRIPTOR.message_types_by_name['CreateBroadcastRequest'] = _CREATEBROADCASTREQUEST
DESCRIPTOR.message_types_by_name['ListActiveBroadcastsRequest'] = _LISTACTIVEBROADCASTSREQUEST
DESCRIPTOR.message_types_by_name['ListActiveBroadcastsResponse'] = _LISTACTIVEBROADCASTSRESPONSE
DESCRIPTOR.message_types_by_name['ListClientsRequest'] = _LISTCLIENTSREQUEST
DESCRIPTOR.message_types_by_name['ListClientsResponse'] = _LISTCLIENTSRESPONSE
DESCRIPTOR.message_types_by_name['Client'] = _CLIENT
DESCRIPTOR.message_types_by_name['GetMessageStatusRequest'] = _GETMESSAGESTATUSREQUEST
DESCRIPTOR.message_types_by_name['GetMessageStatusResponse'] = _GETMESSAGESTATUSRESPONSE
DESCRIPTOR.message_types_by_name['StoreFileRequest'] = _STOREFILEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBroadcastRequest = _reflection.GeneratedProtocolMessageType('CreateBroadcastRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEBROADCASTREQUEST,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.CreateBroadcastRequest)
  ))
_sym_db.RegisterMessage(CreateBroadcastRequest)

ListActiveBroadcastsRequest = _reflection.GeneratedProtocolMessageType('ListActiveBroadcastsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTACTIVEBROADCASTSREQUEST,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.ListActiveBroadcastsRequest)
  ))
_sym_db.RegisterMessage(ListActiveBroadcastsRequest)

ListActiveBroadcastsResponse = _reflection.GeneratedProtocolMessageType('ListActiveBroadcastsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTACTIVEBROADCASTSRESPONSE,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.ListActiveBroadcastsResponse)
  ))
_sym_db.RegisterMessage(ListActiveBroadcastsResponse)

ListClientsRequest = _reflection.GeneratedProtocolMessageType('ListClientsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLIENTSREQUEST,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.ListClientsRequest)
  ))
_sym_db.RegisterMessage(ListClientsRequest)

ListClientsResponse = _reflection.GeneratedProtocolMessageType('ListClientsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLIENTSRESPONSE,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.ListClientsResponse)
  ))
_sym_db.RegisterMessage(ListClientsResponse)

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), dict(
  DESCRIPTOR = _CLIENT,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.Client)
  ))
_sym_db.RegisterMessage(Client)

GetMessageStatusRequest = _reflection.GeneratedProtocolMessageType('GetMessageStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMESSAGESTATUSREQUEST,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.GetMessageStatusRequest)
  ))
_sym_db.RegisterMessage(GetMessageStatusRequest)

GetMessageStatusResponse = _reflection.GeneratedProtocolMessageType('GetMessageStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETMESSAGESTATUSRESPONSE,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.GetMessageStatusResponse)
  ))
_sym_db.RegisterMessage(GetMessageStatusResponse)

StoreFileRequest = _reflection.GeneratedProtocolMessageType('StoreFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _STOREFILEREQUEST,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.admin_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.StoreFileRequest)
  ))
_sym_db.RegisterMessage(StoreFileRequest)



_ADMIN = _descriptor.ServiceDescriptor(
  name='Admin',
  full_name='fleetspeak.server.Admin',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=959,
  serialized_end=1597,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBroadcast',
    full_name='fleetspeak.server.Admin.CreateBroadcast',
    index=0,
    containing_service=None,
    input_type=_CREATEBROADCASTREQUEST,
    output_type=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._EMPTYMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListActiveBroadcasts',
    full_name='fleetspeak.server.Admin.ListActiveBroadcasts',
    index=1,
    containing_service=None,
    input_type=_LISTACTIVEBROADCASTSREQUEST,
    output_type=_LISTACTIVEBROADCASTSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListClients',
    full_name='fleetspeak.server.Admin.ListClients',
    index=2,
    containing_service=None,
    input_type=_LISTCLIENTSREQUEST,
    output_type=_LISTCLIENTSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMessageStatus',
    full_name='fleetspeak.server.Admin.GetMessageStatus',
    index=3,
    containing_service=None,
    input_type=_GETMESSAGESTATUSREQUEST,
    output_type=_GETMESSAGESTATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InsertMessage',
    full_name='fleetspeak.server.Admin.InsertMessage',
    index=4,
    containing_service=None,
    input_type=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._MESSAGE,
    output_type=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._EMPTYMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StoreFile',
    full_name='fleetspeak.server.Admin.StoreFile',
    index=5,
    containing_service=None,
    input_type=_STOREFILEREQUEST,
    output_type=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._EMPTYMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='KeepAlive',
    full_name='fleetspeak.server.Admin.KeepAlive',
    index=6,
    containing_service=None,
    input_type=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._EMPTYMESSAGE,
    output_type=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2._EMPTYMESSAGE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADMIN)

DESCRIPTOR.services_by_name['Admin'] = _ADMIN

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class AdminStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.CreateBroadcast = channel.unary_unary(
          '/fleetspeak.server.Admin/CreateBroadcast',
          request_serializer=CreateBroadcastRequest.SerializeToString,
          response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
          )
      self.ListActiveBroadcasts = channel.unary_unary(
          '/fleetspeak.server.Admin/ListActiveBroadcasts',
          request_serializer=ListActiveBroadcastsRequest.SerializeToString,
          response_deserializer=ListActiveBroadcastsResponse.FromString,
          )
      self.ListClients = channel.unary_unary(
          '/fleetspeak.server.Admin/ListClients',
          request_serializer=ListClientsRequest.SerializeToString,
          response_deserializer=ListClientsResponse.FromString,
          )
      self.GetMessageStatus = channel.unary_unary(
          '/fleetspeak.server.Admin/GetMessageStatus',
          request_serializer=GetMessageStatusRequest.SerializeToString,
          response_deserializer=GetMessageStatusResponse.FromString,
          )
      self.InsertMessage = channel.unary_unary(
          '/fleetspeak.server.Admin/InsertMessage',
          request_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.Message.SerializeToString,
          response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
          )
      self.StoreFile = channel.unary_unary(
          '/fleetspeak.server.Admin/StoreFile',
          request_serializer=StoreFileRequest.SerializeToString,
          response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
          )
      self.KeepAlive = channel.unary_unary(
          '/fleetspeak.server.Admin/KeepAlive',
          request_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
          response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
          )


  class AdminServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def CreateBroadcast(self, request, context):
      """CreateBroadcast creates a FS broadcast, potentially sending a message to
      many machines in the fleet.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ListActiveBroadcasts(self, request, context):
      """ListActiveBroadcasts lists the currently active FS broadcasts.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ListClients(self, request, context):
      """ListClients lists the currently active FS clients.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetMessageStatus(self, request, context):
      """GetMessageStatus retrieves the current status of a message.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def InsertMessage(self, request, context):
      """InsertMessage inserts a message into the Fleetspeak system to be processed
      by the server or delivered to a client.
      TODO: Have this method return the message that is written to the
      datastore (or at least the id).
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def StoreFile(self, request, context):
      """StoreFile inserts a file into the Fleetspeak system.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def KeepAlive(self, request, context):
      """KeepAlive does as little as possible.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AdminServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateBroadcast': grpc.unary_unary_rpc_method_handler(
            servicer.CreateBroadcast,
            request_deserializer=CreateBroadcastRequest.FromString,
            response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
        ),
        'ListActiveBroadcasts': grpc.unary_unary_rpc_method_handler(
            servicer.ListActiveBroadcasts,
            request_deserializer=ListActiveBroadcastsRequest.FromString,
            response_serializer=ListActiveBroadcastsResponse.SerializeToString,
        ),
        'ListClients': grpc.unary_unary_rpc_method_handler(
            servicer.ListClients,
            request_deserializer=ListClientsRequest.FromString,
            response_serializer=ListClientsResponse.SerializeToString,
        ),
        'GetMessageStatus': grpc.unary_unary_rpc_method_handler(
            servicer.GetMessageStatus,
            request_deserializer=GetMessageStatusRequest.FromString,
            response_serializer=GetMessageStatusResponse.SerializeToString,
        ),
        'InsertMessage': grpc.unary_unary_rpc_method_handler(
            servicer.InsertMessage,
            request_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.Message.FromString,
            response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
        ),
        'StoreFile': grpc.unary_unary_rpc_method_handler(
            servicer.StoreFile,
            request_deserializer=StoreFileRequest.FromString,
            response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
        ),
        'KeepAlive': grpc.unary_unary_rpc_method_handler(
            servicer.KeepAlive,
            request_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
            response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'fleetspeak.server.Admin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAdminServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def CreateBroadcast(self, request, context):
      """CreateBroadcast creates a FS broadcast, potentially sending a message to
      many machines in the fleet.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ListActiveBroadcasts(self, request, context):
      """ListActiveBroadcasts lists the currently active FS broadcasts.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ListClients(self, request, context):
      """ListClients lists the currently active FS clients.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetMessageStatus(self, request, context):
      """GetMessageStatus retrieves the current status of a message.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def InsertMessage(self, request, context):
      """InsertMessage inserts a message into the Fleetspeak system to be processed
      by the server or delivered to a client.
      TODO: Have this method return the message that is written to the
      datastore (or at least the id).
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def StoreFile(self, request, context):
      """StoreFile inserts a file into the Fleetspeak system.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def KeepAlive(self, request, context):
      """KeepAlive does as little as possible.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAdminStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def CreateBroadcast(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """CreateBroadcast creates a FS broadcast, potentially sending a message to
      many machines in the fleet.
      """
      raise NotImplementedError()
    CreateBroadcast.future = None
    def ListActiveBroadcasts(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """ListActiveBroadcasts lists the currently active FS broadcasts.
      """
      raise NotImplementedError()
    ListActiveBroadcasts.future = None
    def ListClients(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """ListClients lists the currently active FS clients.
      """
      raise NotImplementedError()
    ListClients.future = None
    def GetMessageStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """GetMessageStatus retrieves the current status of a message.
      """
      raise NotImplementedError()
    GetMessageStatus.future = None
    def InsertMessage(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """InsertMessage inserts a message into the Fleetspeak system to be processed
      by the server or delivered to a client.
      TODO: Have this method return the message that is written to the
      datastore (or at least the id).
      """
      raise NotImplementedError()
    InsertMessage.future = None
    def StoreFile(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """StoreFile inserts a file into the Fleetspeak system.
      """
      raise NotImplementedError()
    StoreFile.future = None
    def KeepAlive(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """KeepAlive does as little as possible.
      """
      raise NotImplementedError()
    KeepAlive.future = None


  def beta_create_Admin_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('fleetspeak.server.Admin', 'CreateBroadcast'): CreateBroadcastRequest.FromString,
      ('fleetspeak.server.Admin', 'GetMessageStatus'): GetMessageStatusRequest.FromString,
      ('fleetspeak.server.Admin', 'InsertMessage'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.Message.FromString,
      ('fleetspeak.server.Admin', 'KeepAlive'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
      ('fleetspeak.server.Admin', 'ListActiveBroadcasts'): ListActiveBroadcastsRequest.FromString,
      ('fleetspeak.server.Admin', 'ListClients'): ListClientsRequest.FromString,
      ('fleetspeak.server.Admin', 'StoreFile'): StoreFileRequest.FromString,
    }
    response_serializers = {
      ('fleetspeak.server.Admin', 'CreateBroadcast'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ('fleetspeak.server.Admin', 'GetMessageStatus'): GetMessageStatusResponse.SerializeToString,
      ('fleetspeak.server.Admin', 'InsertMessage'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ('fleetspeak.server.Admin', 'KeepAlive'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ('fleetspeak.server.Admin', 'ListActiveBroadcasts'): ListActiveBroadcastsResponse.SerializeToString,
      ('fleetspeak.server.Admin', 'ListClients'): ListClientsResponse.SerializeToString,
      ('fleetspeak.server.Admin', 'StoreFile'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
    }
    method_implementations = {
      ('fleetspeak.server.Admin', 'CreateBroadcast'): face_utilities.unary_unary_inline(servicer.CreateBroadcast),
      ('fleetspeak.server.Admin', 'GetMessageStatus'): face_utilities.unary_unary_inline(servicer.GetMessageStatus),
      ('fleetspeak.server.Admin', 'InsertMessage'): face_utilities.unary_unary_inline(servicer.InsertMessage),
      ('fleetspeak.server.Admin', 'KeepAlive'): face_utilities.unary_unary_inline(servicer.KeepAlive),
      ('fleetspeak.server.Admin', 'ListActiveBroadcasts'): face_utilities.unary_unary_inline(servicer.ListActiveBroadcasts),
      ('fleetspeak.server.Admin', 'ListClients'): face_utilities.unary_unary_inline(servicer.ListClients),
      ('fleetspeak.server.Admin', 'StoreFile'): face_utilities.unary_unary_inline(servicer.StoreFile),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Admin_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('fleetspeak.server.Admin', 'CreateBroadcast'): CreateBroadcastRequest.SerializeToString,
      ('fleetspeak.server.Admin', 'GetMessageStatus'): GetMessageStatusRequest.SerializeToString,
      ('fleetspeak.server.Admin', 'InsertMessage'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.Message.SerializeToString,
      ('fleetspeak.server.Admin', 'KeepAlive'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ('fleetspeak.server.Admin', 'ListActiveBroadcasts'): ListActiveBroadcastsRequest.SerializeToString,
      ('fleetspeak.server.Admin', 'ListClients'): ListClientsRequest.SerializeToString,
      ('fleetspeak.server.Admin', 'StoreFile'): StoreFileRequest.SerializeToString,
    }
    response_deserializers = {
      ('fleetspeak.server.Admin', 'CreateBroadcast'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
      ('fleetspeak.server.Admin', 'GetMessageStatus'): GetMessageStatusResponse.FromString,
      ('fleetspeak.server.Admin', 'InsertMessage'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
      ('fleetspeak.server.Admin', 'KeepAlive'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
      ('fleetspeak.server.Admin', 'ListActiveBroadcasts'): ListActiveBroadcastsResponse.FromString,
      ('fleetspeak.server.Admin', 'ListClients'): ListClientsResponse.FromString,
      ('fleetspeak.server.Admin', 'StoreFile'): fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
    }
    cardinalities = {
      'CreateBroadcast': cardinality.Cardinality.UNARY_UNARY,
      'GetMessageStatus': cardinality.Cardinality.UNARY_UNARY,
      'InsertMessage': cardinality.Cardinality.UNARY_UNARY,
      'KeepAlive': cardinality.Cardinality.UNARY_UNARY,
      'ListActiveBroadcasts': cardinality.Cardinality.UNARY_UNARY,
      'ListClients': cardinality.Cardinality.UNARY_UNARY,
      'StoreFile': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'fleetspeak.server.Admin', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)