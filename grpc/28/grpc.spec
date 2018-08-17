Name:	    grpc-devel	
Version:  2.0.0
Release:	1%{?dist}
Summary:	An RPC library and framework

License:  Apache-2.0
URL:	    https://grpc.io	

BuildRequires: cmake gcc-c++ protobuf-devel	protobuf-compiler
Requires:	protobuf-c

%description
gRPC is a modern, open source, high-performance remote procedure call (RPC) 
framework that can run anywhere. It enables client and server applications to 
communicate transparently, and makes it easier to build connected systems.

%prep
if [[ ! -d grpc-devel-2.0.0 ]]; then
  git clone -b master https://github.com/grpc/grpc grpc-devel-2.0.0
fi

%build
cd grpc-devel-2.0.0
git submodule update --init
export CC=clang
export CXX=clang++
make %{?_smp_mflags}

%install
cd grpc-devel-2.0.0
export prefix=%{buildroot}
make install

%files
/bin/grpc_cpp_plugin
/bin/grpc_csharp_plugin
/bin/grpc_node_plugin
/bin/grpc_objective_c_plugin
/bin/grpc_php_plugin
/bin/grpc_python_plugin
/bin/grpc_ruby_plugin
/include/grpc++/alarm.h
/include/grpc++/channel.h
/include/grpc++/client_context.h
/include/grpc++/completion_queue.h
/include/grpc++/create_channel.h
/include/grpc++/create_channel_posix.h
/include/grpc++/ext/health_check_service_server_builder_option.h
/include/grpc++/ext/proto_server_reflection_plugin.h
/include/grpc++/generic/async_generic_service.h
/include/grpc++/generic/generic_stub.h
/include/grpc++/grpc++.h
/include/grpc++/health_check_service_interface.h
/include/grpc++/impl/call.h
/include/grpc++/impl/channel_argument_option.h
/include/grpc++/impl/client_unary_call.h
/include/grpc++/impl/codegen/async_stream.h
/include/grpc++/impl/codegen/async_unary_call.h
/include/grpc++/impl/codegen/byte_buffer.h
/include/grpc++/impl/codegen/call.h
/include/grpc++/impl/codegen/call_hook.h
/include/grpc++/impl/codegen/channel_interface.h
/include/grpc++/impl/codegen/client_context.h
/include/grpc++/impl/codegen/client_unary_call.h
/include/grpc++/impl/codegen/completion_queue.h
/include/grpc++/impl/codegen/completion_queue_tag.h
/include/grpc++/impl/codegen/config.h
/include/grpc++/impl/codegen/config_protobuf.h
/include/grpc++/impl/codegen/core_codegen.h
/include/grpc++/impl/codegen/core_codegen_interface.h
/include/grpc++/impl/codegen/create_auth_context.h
/include/grpc++/impl/codegen/grpc_library.h
/include/grpc++/impl/codegen/metadata_map.h
/include/grpc++/impl/codegen/method_handler_impl.h
/include/grpc++/impl/codegen/proto_utils.h
/include/grpc++/impl/codegen/rpc_method.h
/include/grpc++/impl/codegen/rpc_service_method.h
/include/grpc++/impl/codegen/security/auth_context.h
/include/grpc++/impl/codegen/serialization_traits.h
/include/grpc++/impl/codegen/server_context.h
/include/grpc++/impl/codegen/server_interface.h
/include/grpc++/impl/codegen/service_type.h
/include/grpc++/impl/codegen/slice.h
/include/grpc++/impl/codegen/status.h
/include/grpc++/impl/codegen/status_code_enum.h
/include/grpc++/impl/codegen/string_ref.h
/include/grpc++/impl/codegen/stub_options.h
/include/grpc++/impl/codegen/sync_stream.h
/include/grpc++/impl/codegen/time.h
/include/grpc++/impl/grpc_library.h
/include/grpc++/impl/method_handler_impl.h
/include/grpc++/impl/rpc_method.h
/include/grpc++/impl/rpc_service_method.h
/include/grpc++/impl/serialization_traits.h
/include/grpc++/impl/server_builder_option.h
/include/grpc++/impl/server_builder_plugin.h
/include/grpc++/impl/server_initializer.h
/include/grpc++/impl/service_type.h
/include/grpc++/resource_quota.h
/include/grpc++/security/auth_context.h
/include/grpc++/security/auth_metadata_processor.h
/include/grpc++/security/credentials.h
/include/grpc++/security/server_credentials.h
/include/grpc++/server.h
/include/grpc++/server_builder.h
/include/grpc++/server_context.h
/include/grpc++/server_posix.h
/include/grpc++/support/async_stream.h
/include/grpc++/support/async_unary_call.h
/include/grpc++/support/byte_buffer.h
/include/grpc++/support/channel_arguments.h
/include/grpc++/support/config.h
/include/grpc++/support/error_details.h
/include/grpc++/support/slice.h
/include/grpc++/support/status.h
/include/grpc++/support/status_code_enum.h
/include/grpc++/support/string_ref.h
/include/grpc++/support/stub_options.h
/include/grpc++/support/sync_stream.h
/include/grpc++/support/time.h
/include/grpc/byte_buffer.h
/include/grpc/byte_buffer_reader.h
/include/grpc/census.h
/include/grpc/compression.h
/include/grpc/fork.h
/include/grpc/grpc.h
/include/grpc/grpc_cronet.h
/include/grpc/grpc_posix.h
/include/grpc/grpc_security.h
/include/grpc/grpc_security_constants.h
/include/grpc/impl/codegen/atm.h
/include/grpc/impl/codegen/atm_gcc_atomic.h
/include/grpc/impl/codegen/atm_gcc_sync.h
/include/grpc/impl/codegen/atm_windows.h
/include/grpc/impl/codegen/byte_buffer.h
/include/grpc/impl/codegen/byte_buffer_reader.h
/include/grpc/impl/codegen/compression_types.h
/include/grpc/impl/codegen/connectivity_state.h
/include/grpc/impl/codegen/fork.h
/include/grpc/impl/codegen/gpr_slice.h
/include/grpc/impl/codegen/gpr_types.h
/include/grpc/impl/codegen/grpc_types.h
/include/grpc/impl/codegen/log.h
/include/grpc/impl/codegen/port_platform.h
/include/grpc/impl/codegen/propagation_bits.h
/include/grpc/impl/codegen/slice.h
/include/grpc/impl/codegen/status.h
/include/grpc/impl/codegen/sync.h
/include/grpc/impl/codegen/sync_custom.h
/include/grpc/impl/codegen/sync_generic.h
/include/grpc/impl/codegen/sync_posix.h
/include/grpc/impl/codegen/sync_windows.h
/include/grpc/load_reporting.h
/include/grpc/slice.h
/include/grpc/slice_buffer.h
/include/grpc/status.h
/include/grpc/support/alloc.h
/include/grpc/support/atm.h
/include/grpc/support/atm_gcc_atomic.h
/include/grpc/support/atm_gcc_sync.h
/include/grpc/support/atm_windows.h
/include/grpc/support/cpu.h
/include/grpc/support/log.h
/include/grpc/support/log_windows.h
/include/grpc/support/port_platform.h
/include/grpc/support/string_util.h
/include/grpc/support/sync.h
/include/grpc/support/sync_custom.h
/include/grpc/support/sync_generic.h
/include/grpc/support/sync_posix.h
/include/grpc/support/sync_windows.h
/include/grpc/support/thd_id.h
/include/grpc/support/time.h
/include/grpc/support/workaround_list.h
/include/grpcpp/alarm.h
/include/grpcpp/channel.h
/include/grpcpp/client_context.h
/include/grpcpp/completion_queue.h
/include/grpcpp/create_channel.h
/include/grpcpp/create_channel_posix.h
/include/grpcpp/ext/health_check_service_server_builder_option.h
/include/grpcpp/ext/proto_server_reflection_plugin.h
/include/grpcpp/generic/async_generic_service.h
/include/grpcpp/generic/generic_stub.h
/include/grpcpp/grpcpp.h
/include/grpcpp/health_check_service_interface.h
/include/grpcpp/impl/call.h
/include/grpcpp/impl/channel_argument_option.h
/include/grpcpp/impl/client_unary_call.h
/include/grpcpp/impl/codegen/async_generic_service.h
/include/grpcpp/impl/codegen/async_stream.h
/include/grpcpp/impl/codegen/async_unary_call.h
/include/grpcpp/impl/codegen/byte_buffer.h
/include/grpcpp/impl/codegen/call.h
/include/grpcpp/impl/codegen/call_hook.h
/include/grpcpp/impl/codegen/channel_interface.h
/include/grpcpp/impl/codegen/client_context.h
/include/grpcpp/impl/codegen/client_unary_call.h
/include/grpcpp/impl/codegen/completion_queue.h
/include/grpcpp/impl/codegen/completion_queue_tag.h
/include/grpcpp/impl/codegen/config.h
/include/grpcpp/impl/codegen/config_protobuf.h
/include/grpcpp/impl/codegen/core_codegen.h
/include/grpcpp/impl/codegen/core_codegen_interface.h
/include/grpcpp/impl/codegen/create_auth_context.h
/include/grpcpp/impl/codegen/grpc_library.h
/include/grpcpp/impl/codegen/metadata_map.h
/include/grpcpp/impl/codegen/method_handler_impl.h
/include/grpcpp/impl/codegen/proto_buffer_reader.h
/include/grpcpp/impl/codegen/proto_buffer_writer.h
/include/grpcpp/impl/codegen/proto_utils.h
/include/grpcpp/impl/codegen/rpc_method.h
/include/grpcpp/impl/codegen/rpc_service_method.h
/include/grpcpp/impl/codegen/security/auth_context.h
/include/grpcpp/impl/codegen/serialization_traits.h
/include/grpcpp/impl/codegen/server_context.h
/include/grpcpp/impl/codegen/server_interface.h
/include/grpcpp/impl/codegen/service_type.h
/include/grpcpp/impl/codegen/slice.h
/include/grpcpp/impl/codegen/status.h
/include/grpcpp/impl/codegen/status_code_enum.h
/include/grpcpp/impl/codegen/string_ref.h
/include/grpcpp/impl/codegen/stub_options.h
/include/grpcpp/impl/codegen/sync_stream.h
/include/grpcpp/impl/codegen/time.h
/include/grpcpp/impl/grpc_library.h
/include/grpcpp/impl/method_handler_impl.h
/include/grpcpp/impl/rpc_method.h
/include/grpcpp/impl/rpc_service_method.h
/include/grpcpp/impl/serialization_traits.h
/include/grpcpp/impl/server_builder_option.h
/include/grpcpp/impl/server_builder_plugin.h
/include/grpcpp/impl/server_initializer.h
/include/grpcpp/impl/service_type.h
/include/grpcpp/resource_quota.h
/include/grpcpp/security/auth_context.h
/include/grpcpp/security/auth_metadata_processor.h
/include/grpcpp/security/credentials.h
/include/grpcpp/security/server_credentials.h
/include/grpcpp/server.h
/include/grpcpp/server_builder.h
/include/grpcpp/server_context.h
/include/grpcpp/server_posix.h
/include/grpcpp/support/async_stream.h
/include/grpcpp/support/async_unary_call.h
/include/grpcpp/support/byte_buffer.h
/include/grpcpp/support/channel_arguments.h
/include/grpcpp/support/config.h
/include/grpcpp/support/error_details.h
/include/grpcpp/support/proto_buffer_reader.h
/include/grpcpp/support/proto_buffer_writer.h
/include/grpcpp/support/slice.h
/include/grpcpp/support/status.h
/include/grpcpp/support/status_code_enum.h
/include/grpcpp/support/string_ref.h
/include/grpcpp/support/stub_options.h
/include/grpcpp/support/sync_stream.h
/include/grpcpp/support/time.h
/include/grpcpp/ext/channelz_service_plugin.h
/lib/libaddress_sorting.a
/lib/libaddress_sorting.so
/lib/libaddress_sorting.so.6
/lib/libgpr.a
/lib/libgpr.so
/lib/libgpr.so.6
/lib/libgrpc++.a
/lib/libgrpc++.so
/lib/libgrpc++.so.1
/lib/libgrpc++.so.6
/lib/libgrpc++_cronet.a
/lib/libgrpc++_cronet.so
/lib/libgrpc++_cronet.so.1
/lib/libgrpc++_cronet.so.6
/lib/libgrpc++_error_details.a
/lib/libgrpc++_error_details.so
/lib/libgrpc++_error_details.so.1
/lib/libgrpc++_error_details.so.6
/lib/libgrpc++_reflection.a
/lib/libgrpc++_reflection.so
/lib/libgrpc++_reflection.so.1
/lib/libgrpc++_reflection.so.6
/lib/libgrpc++_unsecure.a
/lib/libgrpc++_unsecure.so
/lib/libgrpc++_unsecure.so.1
/lib/libgrpc++_unsecure.so.6
/lib/libgrpc.a
/lib/libgrpc.so
/lib/libgrpc.so.6
/lib/libgrpc_cronet.a
/lib/libgrpc_cronet.so
/lib/libgrpc_cronet.so.6
/lib/libgrpc_unsecure.a
/lib/libgrpc_unsecure.so
/lib/libgrpc_unsecure.so.6
/lib/pkgconfig/grpc++.pc
/lib/pkgconfig/grpc++_unsecure.pc
/lib/pkgconfig/grpc.pc
/lib/pkgconfig/grpc_unsecure.pc
/lib/libaddress_sorting.so.6.0.0-dev
/lib/libgpr.so.6.0.0-dev
/lib/libgrpc++.so.1.15.0-dev
/lib/libgrpc++_cronet.so.1.15.0-dev
/lib/libgrpc++_error_details.so.1.15.0-dev
/lib/libgrpc++_reflection.so.1.15.0-dev
/lib/libgrpc++_unsecure.so.1.15.0-dev
/lib/libgrpc.so.6.0.0-dev
/lib/libgrpc_cronet.so.6.0.0-dev
/lib/libgrpc_unsecure.so.6.0.0-dev
/lib/libgrpcpp_channelz.a
/lib/libgrpcpp_channelz.so
/lib/libgrpcpp_channelz.so.1
/lib/libgrpcpp_channelz.so.1.15.0-dev
/lib/libgrpcpp_channelz.so.6
/lib/pkgconfig/gpr.pc
/share/grpc/roots.pem


%changelog
* Thu Aug 16 2018 Ryan Goodfellow <rgoodfel@isi.edu> - 2.0.0-0
- Initial
