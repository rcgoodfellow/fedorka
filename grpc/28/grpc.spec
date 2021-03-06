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
export prefix=%{buildroot}/usr
make install

%files
/usr/bin/grpc_cpp_plugin
/usr/bin/grpc_csharp_plugin
/usr/bin/grpc_node_plugin
/usr/bin/grpc_objective_c_plugin
/usr/bin/grpc_php_plugin
/usr/bin/grpc_python_plugin
/usr/bin/grpc_ruby_plugin
/usr/include/grpc++/alarm.h
/usr/include/grpc++/channel.h
/usr/include/grpc++/client_context.h
/usr/include/grpc++/completion_queue.h
/usr/include/grpc++/create_channel.h
/usr/include/grpc++/create_channel_posix.h
/usr/include/grpc++/ext/health_check_service_server_builder_option.h
/usr/include/grpc++/ext/proto_server_reflection_plugin.h
/usr/include/grpc++/generic/async_generic_service.h
/usr/include/grpc++/generic/generic_stub.h
/usr/include/grpc++/grpc++.h
/usr/include/grpc++/health_check_service_interface.h
/usr/include/grpc++/impl/call.h
/usr/include/grpc++/impl/channel_argument_option.h
/usr/include/grpc++/impl/client_unary_call.h
/usr/include/grpc++/impl/codegen/async_stream.h
/usr/include/grpc++/impl/codegen/async_unary_call.h
/usr/include/grpc++/impl/codegen/byte_buffer.h
/usr/include/grpc++/impl/codegen/call.h
/usr/include/grpc++/impl/codegen/call_hook.h
/usr/include/grpc++/impl/codegen/channel_interface.h
/usr/include/grpc++/impl/codegen/client_context.h
/usr/include/grpc++/impl/codegen/client_unary_call.h
/usr/include/grpc++/impl/codegen/completion_queue.h
/usr/include/grpc++/impl/codegen/completion_queue_tag.h
/usr/include/grpc++/impl/codegen/config.h
/usr/include/grpc++/impl/codegen/config_protobuf.h
/usr/include/grpc++/impl/codegen/core_codegen.h
/usr/include/grpc++/impl/codegen/core_codegen_interface.h
/usr/include/grpc++/impl/codegen/create_auth_context.h
/usr/include/grpc++/impl/codegen/grpc_library.h
/usr/include/grpc++/impl/codegen/metadata_map.h
/usr/include/grpc++/impl/codegen/method_handler_impl.h
/usr/include/grpc++/impl/codegen/proto_utils.h
/usr/include/grpc++/impl/codegen/rpc_method.h
/usr/include/grpc++/impl/codegen/rpc_service_method.h
/usr/include/grpc++/impl/codegen/security/auth_context.h
/usr/include/grpc++/impl/codegen/serialization_traits.h
/usr/include/grpc++/impl/codegen/server_context.h
/usr/include/grpc++/impl/codegen/server_interface.h
/usr/include/grpc++/impl/codegen/service_type.h
/usr/include/grpc++/impl/codegen/slice.h
/usr/include/grpc++/impl/codegen/status.h
/usr/include/grpc++/impl/codegen/status_code_enum.h
/usr/include/grpc++/impl/codegen/string_ref.h
/usr/include/grpc++/impl/codegen/stub_options.h
/usr/include/grpc++/impl/codegen/sync_stream.h
/usr/include/grpc++/impl/codegen/time.h
/usr/include/grpc++/impl/grpc_library.h
/usr/include/grpc++/impl/method_handler_impl.h
/usr/include/grpc++/impl/rpc_method.h
/usr/include/grpc++/impl/rpc_service_method.h
/usr/include/grpc++/impl/serialization_traits.h
/usr/include/grpc++/impl/server_builder_option.h
/usr/include/grpc++/impl/server_builder_plugin.h
/usr/include/grpc++/impl/server_initializer.h
/usr/include/grpc++/impl/service_type.h
/usr/include/grpc++/resource_quota.h
/usr/include/grpc++/security/auth_context.h
/usr/include/grpc++/security/auth_metadata_processor.h
/usr/include/grpc++/security/credentials.h
/usr/include/grpc++/security/server_credentials.h
/usr/include/grpc++/server.h
/usr/include/grpc++/server_builder.h
/usr/include/grpc++/server_context.h
/usr/include/grpc++/server_posix.h
/usr/include/grpc++/support/async_stream.h
/usr/include/grpc++/support/async_unary_call.h
/usr/include/grpc++/support/byte_buffer.h
/usr/include/grpc++/support/channel_arguments.h
/usr/include/grpc++/support/config.h
/usr/include/grpc++/support/error_details.h
/usr/include/grpc++/support/slice.h
/usr/include/grpc++/support/status.h
/usr/include/grpc++/support/status_code_enum.h
/usr/include/grpc++/support/string_ref.h
/usr/include/grpc++/support/stub_options.h
/usr/include/grpc++/support/sync_stream.h
/usr/include/grpc++/support/time.h
/usr/include/grpc/byte_buffer.h
/usr/include/grpc/byte_buffer_reader.h
/usr/include/grpc/census.h
/usr/include/grpc/compression.h
/usr/include/grpc/fork.h
/usr/include/grpc/grpc.h
/usr/include/grpc/grpc_cronet.h
/usr/include/grpc/grpc_posix.h
/usr/include/grpc/grpc_security.h
/usr/include/grpc/grpc_security_constants.h
/usr/include/grpc/impl/codegen/atm.h
/usr/include/grpc/impl/codegen/atm_gcc_atomic.h
/usr/include/grpc/impl/codegen/atm_gcc_sync.h
/usr/include/grpc/impl/codegen/atm_windows.h
/usr/include/grpc/impl/codegen/byte_buffer.h
/usr/include/grpc/impl/codegen/byte_buffer_reader.h
/usr/include/grpc/impl/codegen/compression_types.h
/usr/include/grpc/impl/codegen/connectivity_state.h
/usr/include/grpc/impl/codegen/fork.h
/usr/include/grpc/impl/codegen/gpr_slice.h
/usr/include/grpc/impl/codegen/gpr_types.h
/usr/include/grpc/impl/codegen/grpc_types.h
/usr/include/grpc/impl/codegen/log.h
/usr/include/grpc/impl/codegen/port_platform.h
/usr/include/grpc/impl/codegen/propagation_bits.h
/usr/include/grpc/impl/codegen/slice.h
/usr/include/grpc/impl/codegen/status.h
/usr/include/grpc/impl/codegen/sync.h
/usr/include/grpc/impl/codegen/sync_custom.h
/usr/include/grpc/impl/codegen/sync_generic.h
/usr/include/grpc/impl/codegen/sync_posix.h
/usr/include/grpc/impl/codegen/sync_windows.h
/usr/include/grpc/load_reporting.h
/usr/include/grpc/slice.h
/usr/include/grpc/slice_buffer.h
/usr/include/grpc/status.h
/usr/include/grpc/support/alloc.h
/usr/include/grpc/support/atm.h
/usr/include/grpc/support/atm_gcc_atomic.h
/usr/include/grpc/support/atm_gcc_sync.h
/usr/include/grpc/support/atm_windows.h
/usr/include/grpc/support/cpu.h
/usr/include/grpc/support/log.h
/usr/include/grpc/support/log_windows.h
/usr/include/grpc/support/port_platform.h
/usr/include/grpc/support/string_util.h
/usr/include/grpc/support/sync.h
/usr/include/grpc/support/sync_custom.h
/usr/include/grpc/support/sync_generic.h
/usr/include/grpc/support/sync_posix.h
/usr/include/grpc/support/sync_windows.h
/usr/include/grpc/support/thd_id.h
/usr/include/grpc/support/time.h
/usr/include/grpc/support/workaround_list.h
/usr/include/grpcpp/alarm.h
/usr/include/grpcpp/channel.h
/usr/include/grpcpp/client_context.h
/usr/include/grpcpp/completion_queue.h
/usr/include/grpcpp/create_channel.h
/usr/include/grpcpp/create_channel_posix.h
/usr/include/grpcpp/ext/health_check_service_server_builder_option.h
/usr/include/grpcpp/ext/proto_server_reflection_plugin.h
/usr/include/grpcpp/generic/async_generic_service.h
/usr/include/grpcpp/generic/generic_stub.h
/usr/include/grpcpp/grpcpp.h
/usr/include/grpcpp/health_check_service_interface.h
/usr/include/grpcpp/impl/call.h
/usr/include/grpcpp/impl/channel_argument_option.h
/usr/include/grpcpp/impl/client_unary_call.h
/usr/include/grpcpp/impl/codegen/async_generic_service.h
/usr/include/grpcpp/impl/codegen/async_stream.h
/usr/include/grpcpp/impl/codegen/async_unary_call.h
/usr/include/grpcpp/impl/codegen/byte_buffer.h
/usr/include/grpcpp/impl/codegen/call.h
/usr/include/grpcpp/impl/codegen/call_hook.h
/usr/include/grpcpp/impl/codegen/channel_interface.h
/usr/include/grpcpp/impl/codegen/client_context.h
/usr/include/grpcpp/impl/codegen/client_unary_call.h
/usr/include/grpcpp/impl/codegen/completion_queue.h
/usr/include/grpcpp/impl/codegen/completion_queue_tag.h
/usr/include/grpcpp/impl/codegen/config.h
/usr/include/grpcpp/impl/codegen/config_protobuf.h
/usr/include/grpcpp/impl/codegen/core_codegen.h
/usr/include/grpcpp/impl/codegen/core_codegen_interface.h
/usr/include/grpcpp/impl/codegen/create_auth_context.h
/usr/include/grpcpp/impl/codegen/grpc_library.h
/usr/include/grpcpp/impl/codegen/metadata_map.h
/usr/include/grpcpp/impl/codegen/method_handler_impl.h
/usr/include/grpcpp/impl/codegen/proto_buffer_reader.h
/usr/include/grpcpp/impl/codegen/proto_buffer_writer.h
/usr/include/grpcpp/impl/codegen/proto_utils.h
/usr/include/grpcpp/impl/codegen/rpc_method.h
/usr/include/grpcpp/impl/codegen/rpc_service_method.h
/usr/include/grpcpp/impl/codegen/security/auth_context.h
/usr/include/grpcpp/impl/codegen/serialization_traits.h
/usr/include/grpcpp/impl/codegen/server_context.h
/usr/include/grpcpp/impl/codegen/server_interface.h
/usr/include/grpcpp/impl/codegen/service_type.h
/usr/include/grpcpp/impl/codegen/slice.h
/usr/include/grpcpp/impl/codegen/status.h
/usr/include/grpcpp/impl/codegen/status_code_enum.h
/usr/include/grpcpp/impl/codegen/string_ref.h
/usr/include/grpcpp/impl/codegen/stub_options.h
/usr/include/grpcpp/impl/codegen/sync_stream.h
/usr/include/grpcpp/impl/codegen/time.h
/usr/include/grpcpp/impl/grpc_library.h
/usr/include/grpcpp/impl/method_handler_impl.h
/usr/include/grpcpp/impl/rpc_method.h
/usr/include/grpcpp/impl/rpc_service_method.h
/usr/include/grpcpp/impl/serialization_traits.h
/usr/include/grpcpp/impl/server_builder_option.h
/usr/include/grpcpp/impl/server_builder_plugin.h
/usr/include/grpcpp/impl/server_initializer.h
/usr/include/grpcpp/impl/service_type.h
/usr/include/grpcpp/resource_quota.h
/usr/include/grpcpp/security/auth_context.h
/usr/include/grpcpp/security/auth_metadata_processor.h
/usr/include/grpcpp/security/credentials.h
/usr/include/grpcpp/security/server_credentials.h
/usr/include/grpcpp/server.h
/usr/include/grpcpp/server_builder.h
/usr/include/grpcpp/server_context.h
/usr/include/grpcpp/server_posix.h
/usr/include/grpcpp/support/async_stream.h
/usr/include/grpcpp/support/async_unary_call.h
/usr/include/grpcpp/support/byte_buffer.h
/usr/include/grpcpp/support/channel_arguments.h
/usr/include/grpcpp/support/config.h
/usr/include/grpcpp/support/error_details.h
/usr/include/grpcpp/support/proto_buffer_reader.h
/usr/include/grpcpp/support/proto_buffer_writer.h
/usr/include/grpcpp/support/slice.h
/usr/include/grpcpp/support/status.h
/usr/include/grpcpp/support/status_code_enum.h
/usr/include/grpcpp/support/string_ref.h
/usr/include/grpcpp/support/stub_options.h
/usr/include/grpcpp/support/sync_stream.h
/usr/include/grpcpp/support/time.h
/usr/include/grpcpp/ext/channelz_service_plugin.h
/usr/lib/libaddress_sorting.a
/usr/lib/libaddress_sorting.so
/usr/lib/libaddress_sorting.so.6
/usr/lib/libgpr.a
/usr/lib/libgpr.so
/usr/lib/libgpr.so.6
/usr/lib/libgrpc++.a
/usr/lib/libgrpc++.so
/usr/lib/libgrpc++.so.1
/usr/lib/libgrpc++.so.6
/usr/lib/libgrpc++_cronet.a
/usr/lib/libgrpc++_cronet.so
/usr/lib/libgrpc++_cronet.so.1
/usr/lib/libgrpc++_cronet.so.6
/usr/lib/libgrpc++_error_details.a
/usr/lib/libgrpc++_error_details.so
/usr/lib/libgrpc++_error_details.so.1
/usr/lib/libgrpc++_error_details.so.6
/usr/lib/libgrpc++_reflection.a
/usr/lib/libgrpc++_reflection.so
/usr/lib/libgrpc++_reflection.so.1
/usr/lib/libgrpc++_reflection.so.6
/usr/lib/libgrpc++_unsecure.a
/usr/lib/libgrpc++_unsecure.so
/usr/lib/libgrpc++_unsecure.so.1
/usr/lib/libgrpc++_unsecure.so.6
/usr/lib/libgrpc.a
/usr/lib/libgrpc.so
/usr/lib/libgrpc.so.6
/usr/lib/libgrpc_cronet.a
/usr/lib/libgrpc_cronet.so
/usr/lib/libgrpc_cronet.so.6
/usr/lib/libgrpc_unsecure.a
/usr/lib/libgrpc_unsecure.so
/usr/lib/libgrpc_unsecure.so.6
/usr/lib/pkgconfig/grpc++.pc
/usr/lib/pkgconfig/grpc++_unsecure.pc
/usr/lib/pkgconfig/grpc.pc
/usr/lib/pkgconfig/grpc_unsecure.pc
/usr/lib/libaddress_sorting.so.6.0.0-dev
/usr/lib/libgpr.so.6.0.0-dev
/usr/lib/libgrpc++.so.1.15.0-dev
/usr/lib/libgrpc++_cronet.so.1.15.0-dev
/usr/lib/libgrpc++_error_details.so.1.15.0-dev
/usr/lib/libgrpc++_reflection.so.1.15.0-dev
/usr/lib/libgrpc++_unsecure.so.1.15.0-dev
/usr/lib/libgrpc.so.6.0.0-dev
/usr/lib/libgrpc_cronet.so.6.0.0-dev
/usr/lib/libgrpc_unsecure.so.6.0.0-dev
/usr/lib/libgrpcpp_channelz.a
/usr/lib/libgrpcpp_channelz.so
/usr/lib/libgrpcpp_channelz.so.1
/usr/lib/libgrpcpp_channelz.so.1.15.0-dev
/usr/lib/libgrpcpp_channelz.so.6
/usr/lib/pkgconfig/gpr.pc
/usr/share/grpc/roots.pem


%changelog
* Thu Aug 16 2018 Ryan Goodfellow <rgoodfel@isi.edu> - 2.0.0-0
- Initial
