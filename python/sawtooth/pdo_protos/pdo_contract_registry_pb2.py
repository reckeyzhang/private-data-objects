# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pdo_contract_registry.proto

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
  name='pdo_contract_registry.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1bpdo_contract_registry.proto\"\xbb\x01\n\x0fPdoContractInfo\x12\x13\n\x0b\x63ontract_id\x18\x01 \x01(\t\x12\x1a\n\x12\x63ontract_code_hash\x18\x03 \x01(\t\x12$\n\x1cpdo_contract_creator_pem_key\x18\x04 \x01(\t\x12 \n\x18provisioning_service_ids\x18\x05 \x03(\t\x12/\n\renclaves_info\x18\x06 \x03(\x0b\x32\x18.PdoContractEnclavesInfo\"X\n\x16PdoContractTransaction\x12\x0c\n\x04verb\x18\x01 \x01(\t\x12\x13\n\x0b\x63ontract_id\x18\x02 \x01(\t\x12\x1b\n\x13transaction_details\x18\x03 \x01(\x0c\"\x90\x01\n\x13PdoContractRegister\x12\x1a\n\x12\x63ontract_code_hash\x18\x01 \x01(\t\x12$\n\x1cpdo_contract_creator_pem_key\x18\x02 \x01(\t\x12\x15\n\rpdo_signature\x18\x03 \x01(\t\x12 \n\x18provisioning_service_ids\x18\x04 \x03(\t\"`\n\x16PdoContractAddEnclaves\x12\x15\n\rpdo_signature\x18\x01 \x01(\t\x12/\n\renclaves_info\x18\x02 \x03(\x0b\x32\x18.PdoContractEnclavesInfo\"\xbd\x01\n\x17PdoContractEnclavesInfo\x12\x1b\n\x13\x63ontract_enclave_id\x18\x01 \x01(\t\x12/\n\'encrypted_contract_state_encryption_key\x18\x02 \x01(\t\x12\x19\n\x11\x65nclave_signature\x18\x03 \x01(\t\x12\x39\n\x0c\x65nclaves_map\x18\x04 \x03(\x0b\x32#.PdoProvisioningKeyToStateSecretMap\"\x88\x01\n\"PdoProvisioningKeyToStateSecretMap\x12\'\n\x1fprovisioning_service_public_key\x18\x01 \x01(\t\x12*\n\"provisioning_contract_state_secret\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\"9\n\x19PdoContractRemoveEnclaves\x12\x1c\n\x14\x63ontract_enclave_ids\x18\x01 \x03(\tB\x19\n\x15pdo.sawtooth.protobufP\x01\x62\x06proto3')
)




_PDOCONTRACTINFO = _descriptor.Descriptor(
  name='PdoContractInfo',
  full_name='PdoContractInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='PdoContractInfo.contract_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contract_code_hash', full_name='PdoContractInfo.contract_code_hash', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pdo_contract_creator_pem_key', full_name='PdoContractInfo.pdo_contract_creator_pem_key', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provisioning_service_ids', full_name='PdoContractInfo.provisioning_service_ids', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enclaves_info', full_name='PdoContractInfo.enclaves_info', index=4,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=32,
  serialized_end=219,
)


_PDOCONTRACTTRANSACTION = _descriptor.Descriptor(
  name='PdoContractTransaction',
  full_name='PdoContractTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verb', full_name='PdoContractTransaction.verb', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='PdoContractTransaction.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_details', full_name='PdoContractTransaction.transaction_details', index=2,
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
  serialized_start=221,
  serialized_end=309,
)


_PDOCONTRACTREGISTER = _descriptor.Descriptor(
  name='PdoContractRegister',
  full_name='PdoContractRegister',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_code_hash', full_name='PdoContractRegister.contract_code_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pdo_contract_creator_pem_key', full_name='PdoContractRegister.pdo_contract_creator_pem_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pdo_signature', full_name='PdoContractRegister.pdo_signature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provisioning_service_ids', full_name='PdoContractRegister.provisioning_service_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=312,
  serialized_end=456,
)


_PDOCONTRACTADDENCLAVES = _descriptor.Descriptor(
  name='PdoContractAddEnclaves',
  full_name='PdoContractAddEnclaves',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pdo_signature', full_name='PdoContractAddEnclaves.pdo_signature', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enclaves_info', full_name='PdoContractAddEnclaves.enclaves_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=458,
  serialized_end=554,
)


_PDOCONTRACTENCLAVESINFO = _descriptor.Descriptor(
  name='PdoContractEnclavesInfo',
  full_name='PdoContractEnclavesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_enclave_id', full_name='PdoContractEnclavesInfo.contract_enclave_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypted_contract_state_encryption_key', full_name='PdoContractEnclavesInfo.encrypted_contract_state_encryption_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enclave_signature', full_name='PdoContractEnclavesInfo.enclave_signature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enclaves_map', full_name='PdoContractEnclavesInfo.enclaves_map', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=557,
  serialized_end=746,
)


_PDOPROVISIONINGKEYTOSTATESECRETMAP = _descriptor.Descriptor(
  name='PdoProvisioningKeyToStateSecretMap',
  full_name='PdoProvisioningKeyToStateSecretMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provisioning_service_public_key', full_name='PdoProvisioningKeyToStateSecretMap.provisioning_service_public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provisioning_contract_state_secret', full_name='PdoProvisioningKeyToStateSecretMap.provisioning_contract_state_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='PdoProvisioningKeyToStateSecretMap.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=749,
  serialized_end=885,
)


_PDOCONTRACTREMOVEENCLAVES = _descriptor.Descriptor(
  name='PdoContractRemoveEnclaves',
  full_name='PdoContractRemoveEnclaves',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_enclave_ids', full_name='PdoContractRemoveEnclaves.contract_enclave_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=887,
  serialized_end=944,
)

_PDOCONTRACTINFO.fields_by_name['enclaves_info'].message_type = _PDOCONTRACTENCLAVESINFO
_PDOCONTRACTADDENCLAVES.fields_by_name['enclaves_info'].message_type = _PDOCONTRACTENCLAVESINFO
_PDOCONTRACTENCLAVESINFO.fields_by_name['enclaves_map'].message_type = _PDOPROVISIONINGKEYTOSTATESECRETMAP
DESCRIPTOR.message_types_by_name['PdoContractInfo'] = _PDOCONTRACTINFO
DESCRIPTOR.message_types_by_name['PdoContractTransaction'] = _PDOCONTRACTTRANSACTION
DESCRIPTOR.message_types_by_name['PdoContractRegister'] = _PDOCONTRACTREGISTER
DESCRIPTOR.message_types_by_name['PdoContractAddEnclaves'] = _PDOCONTRACTADDENCLAVES
DESCRIPTOR.message_types_by_name['PdoContractEnclavesInfo'] = _PDOCONTRACTENCLAVESINFO
DESCRIPTOR.message_types_by_name['PdoProvisioningKeyToStateSecretMap'] = _PDOPROVISIONINGKEYTOSTATESECRETMAP
DESCRIPTOR.message_types_by_name['PdoContractRemoveEnclaves'] = _PDOCONTRACTREMOVEENCLAVES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PdoContractInfo = _reflection.GeneratedProtocolMessageType('PdoContractInfo', (_message.Message,), dict(
  DESCRIPTOR = _PDOCONTRACTINFO,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoContractInfo)
  ))
_sym_db.RegisterMessage(PdoContractInfo)

PdoContractTransaction = _reflection.GeneratedProtocolMessageType('PdoContractTransaction', (_message.Message,), dict(
  DESCRIPTOR = _PDOCONTRACTTRANSACTION,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoContractTransaction)
  ))
_sym_db.RegisterMessage(PdoContractTransaction)

PdoContractRegister = _reflection.GeneratedProtocolMessageType('PdoContractRegister', (_message.Message,), dict(
  DESCRIPTOR = _PDOCONTRACTREGISTER,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoContractRegister)
  ))
_sym_db.RegisterMessage(PdoContractRegister)

PdoContractAddEnclaves = _reflection.GeneratedProtocolMessageType('PdoContractAddEnclaves', (_message.Message,), dict(
  DESCRIPTOR = _PDOCONTRACTADDENCLAVES,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoContractAddEnclaves)
  ))
_sym_db.RegisterMessage(PdoContractAddEnclaves)

PdoContractEnclavesInfo = _reflection.GeneratedProtocolMessageType('PdoContractEnclavesInfo', (_message.Message,), dict(
  DESCRIPTOR = _PDOCONTRACTENCLAVESINFO,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoContractEnclavesInfo)
  ))
_sym_db.RegisterMessage(PdoContractEnclavesInfo)

PdoProvisioningKeyToStateSecretMap = _reflection.GeneratedProtocolMessageType('PdoProvisioningKeyToStateSecretMap', (_message.Message,), dict(
  DESCRIPTOR = _PDOPROVISIONINGKEYTOSTATESECRETMAP,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoProvisioningKeyToStateSecretMap)
  ))
_sym_db.RegisterMessage(PdoProvisioningKeyToStateSecretMap)

PdoContractRemoveEnclaves = _reflection.GeneratedProtocolMessageType('PdoContractRemoveEnclaves', (_message.Message,), dict(
  DESCRIPTOR = _PDOCONTRACTREMOVEENCLAVES,
  __module__ = 'pdo_contract_registry_pb2'
  # @@protoc_insertion_point(class_scope:PdoContractRemoveEnclaves)
  ))
_sym_db.RegisterMessage(PdoContractRemoveEnclaves)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025pdo.sawtooth.protobufP\001'))
# @@protoc_insertion_point(module_scope)