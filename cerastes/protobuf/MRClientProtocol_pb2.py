# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import Security_pb2
import mr_service_protos_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='MRClientProtocol.proto',
  package='hadoop.mapreduce',
  serialized_pb='\n\x16MRClientProtocol.proto\x12\x10hadoop.mapreduce\x1a\x0eSecurity.proto\x1a\x17mr_service_protos.proto2\xdc\x0c\n\x17MRClientProtocolService\x12g\n\x0cgetJobReport\x12*.hadoop.mapreduce.GetJobReportRequestProto\x1a+.hadoop.mapreduce.GetJobReportResponseProto\x12j\n\rgetTaskReport\x12+.hadoop.mapreduce.GetTaskReportRequestProto\x1a,.hadoop.mapreduce.GetTaskReportResponseProto\x12\x7f\n\x14getTaskAttemptReport\x12\x32.hadoop.mapreduce.GetTaskAttemptReportRequestProto\x1a\x33.hadoop.mapreduce.GetTaskAttemptReportResponseProto\x12\x64\n\x0bgetCounters\x12).hadoop.mapreduce.GetCountersRequestProto\x1a*.hadoop.mapreduce.GetCountersResponseProto\x12\x9d\x01\n\x1egetTaskAttemptCompletionEvents\x12<.hadoop.mapreduce.GetTaskAttemptCompletionEventsRequestProto\x1a=.hadoop.mapreduce.GetTaskAttemptCompletionEventsResponseProto\x12m\n\x0egetTaskReports\x12,.hadoop.mapreduce.GetTaskReportsRequestProto\x1a-.hadoop.mapreduce.GetTaskReportsResponseProto\x12m\n\x0egetDiagnostics\x12,.hadoop.mapreduce.GetDiagnosticsRequestProto\x1a-.hadoop.mapreduce.GetDiagnosticsResponseProto\x12s\n\x12getDelegationToken\x12-.hadoop.common.GetDelegationTokenRequestProto\x1a..hadoop.common.GetDelegationTokenResponseProto\x12X\n\x07killJob\x12%.hadoop.mapreduce.KillJobRequestProto\x1a&.hadoop.mapreduce.KillJobResponseProto\x12[\n\x08killTask\x12&.hadoop.mapreduce.KillTaskRequestProto\x1a\'.hadoop.mapreduce.KillTaskResponseProto\x12p\n\x0fkillTaskAttempt\x12-.hadoop.mapreduce.KillTaskAttemptRequestProto\x1a..hadoop.mapreduce.KillTaskAttemptResponseProto\x12p\n\x0f\x66\x61ilTaskAttempt\x12-.hadoop.mapreduce.FailTaskAttemptRequestProto\x1a..hadoop.mapreduce.FailTaskAttemptResponseProto\x12y\n\x14renewDelegationToken\x12/.hadoop.common.RenewDelegationTokenRequestProto\x1a\x30.hadoop.common.RenewDelegationTokenResponseProto\x12|\n\x15\x63\x61ncelDelegationToken\x12\x30.hadoop.common.CancelDelegationTokenRequestProto\x1a\x31.hadoop.common.CancelDelegationTokenResponseProtoB6\n\x1corg.apache.hadoop.yarn.protoB\x10MRClientProtocol\x88\x01\x01\x90\x01\x01')





_MRCLIENTPROTOCOLSERVICE = descriptor.ServiceDescriptor(
  name='MRClientProtocolService',
  full_name='hadoop.mapreduce.MRClientProtocolService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=86,
  serialized_end=1714,
  methods=[
  descriptor.MethodDescriptor(
    name='getJobReport',
    full_name='hadoop.mapreduce.MRClientProtocolService.getJobReport',
    index=0,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETJOBREPORTREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETJOBREPORTRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getTaskReport',
    full_name='hadoop.mapreduce.MRClientProtocolService.getTaskReport',
    index=1,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETTASKREPORTREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETTASKREPORTRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getTaskAttemptReport',
    full_name='hadoop.mapreduce.MRClientProtocolService.getTaskAttemptReport',
    index=2,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETTASKATTEMPTREPORTREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETTASKATTEMPTREPORTRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getCounters',
    full_name='hadoop.mapreduce.MRClientProtocolService.getCounters',
    index=3,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETCOUNTERSREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETCOUNTERSRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getTaskAttemptCompletionEvents',
    full_name='hadoop.mapreduce.MRClientProtocolService.getTaskAttemptCompletionEvents',
    index=4,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETTASKATTEMPTCOMPLETIONEVENTSREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETTASKATTEMPTCOMPLETIONEVENTSRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getTaskReports',
    full_name='hadoop.mapreduce.MRClientProtocolService.getTaskReports',
    index=5,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETTASKREPORTSREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETTASKREPORTSRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getDiagnostics',
    full_name='hadoop.mapreduce.MRClientProtocolService.getDiagnostics',
    index=6,
    containing_service=None,
    input_type=mr_service_protos_pb2._GETDIAGNOSTICSREQUESTPROTO,
    output_type=mr_service_protos_pb2._GETDIAGNOSTICSRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getDelegationToken',
    full_name='hadoop.mapreduce.MRClientProtocolService.getDelegationToken',
    index=7,
    containing_service=None,
    input_type=Security_pb2._GETDELEGATIONTOKENREQUESTPROTO,
    output_type=Security_pb2._GETDELEGATIONTOKENRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='killJob',
    full_name='hadoop.mapreduce.MRClientProtocolService.killJob',
    index=8,
    containing_service=None,
    input_type=mr_service_protos_pb2._KILLJOBREQUESTPROTO,
    output_type=mr_service_protos_pb2._KILLJOBRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='killTask',
    full_name='hadoop.mapreduce.MRClientProtocolService.killTask',
    index=9,
    containing_service=None,
    input_type=mr_service_protos_pb2._KILLTASKREQUESTPROTO,
    output_type=mr_service_protos_pb2._KILLTASKRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='killTaskAttempt',
    full_name='hadoop.mapreduce.MRClientProtocolService.killTaskAttempt',
    index=10,
    containing_service=None,
    input_type=mr_service_protos_pb2._KILLTASKATTEMPTREQUESTPROTO,
    output_type=mr_service_protos_pb2._KILLTASKATTEMPTRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='failTaskAttempt',
    full_name='hadoop.mapreduce.MRClientProtocolService.failTaskAttempt',
    index=11,
    containing_service=None,
    input_type=mr_service_protos_pb2._FAILTASKATTEMPTREQUESTPROTO,
    output_type=mr_service_protos_pb2._FAILTASKATTEMPTRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='renewDelegationToken',
    full_name='hadoop.mapreduce.MRClientProtocolService.renewDelegationToken',
    index=12,
    containing_service=None,
    input_type=Security_pb2._RENEWDELEGATIONTOKENREQUESTPROTO,
    output_type=Security_pb2._RENEWDELEGATIONTOKENRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='cancelDelegationToken',
    full_name='hadoop.mapreduce.MRClientProtocolService.cancelDelegationToken',
    index=13,
    containing_service=None,
    input_type=Security_pb2._CANCELDELEGATIONTOKENREQUESTPROTO,
    output_type=Security_pb2._CANCELDELEGATIONTOKENRESPONSEPROTO,
    options=None,
  ),
])

class MRClientProtocolService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _MRCLIENTPROTOCOLSERVICE
class MRClientProtocolService_Stub(MRClientProtocolService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _MRCLIENTPROTOCOLSERVICE

# @@protoc_insertion_point(module_scope)