FROM fedora:28

RUN dnf update -y --refresh
RUN dnf groupinstall -y "C Development Tools and Libraries"
RUN dnf groupinstall -y "RPM Development Tools"
RUN dnf install -y git cmake sudo wget openssl-devel boost-devel catch-devel cpprest-devel protobuf-compiler protobuf-c protobuf-devel clang


WORKDIR /code
RUN git clone https://github.com/grpc/grpc.git
WORKDIR /code/grpc
RUN git submodule update --init
ENV CC clang
ENV CXX clang++
RUN make -j`nproc`
RUN make install

WORKDIR /code
# revert back to upstream pending PR
#RUN git clone https://github.com/nokia/etcd-cpp-apiv3.git
RUN git clone https://github.com/rcgoodfellow/etcd-cpp-apiv3.git
WORKDIR /code/etcd-cpp-apiv3/proto
RUN protoc -I . --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./rpc.proto
RUN protoc -I . --cpp_out=. ./*.proto
WORKDIR /code/etcd-cpp-apiv3/build
#XXX hack: trick build system into thinking this is an 'rpm' system
RUN touch /etc/rc.d/init.d/functions
RUN cmake .. \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DPACKAGE=Y \
  -DCATCH_INCLUDE_DIR=/usr/include/catch \
  -DCPPREST_INCLUDE_DIR=/usr/include/cpprest \
  -DCPPREST_LIB=/usr/lib64/libcpprest.so \
  -DTARGET_COMPONENT=all \
  -DCMAKE_CXX_FLAGS="-Wno-string-compare" 
RUN make -j`nproc`
RUN make package
RUN sudo make install
