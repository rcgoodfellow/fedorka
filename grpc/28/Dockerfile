FROM fedora:28

RUN dnf update -y --refresh
RUN dnf groupinstall -y "C Development Tools and Libraries"
RUN dnf groupinstall -y "RPM Development Tools"
RUN dnf install -y \
  git \
  clang \
  cmake \
  protobuf-devel \
  protobuf-compiler \
  protobuf-c

WORKDIR /root/rpmbuild/SPECS
ADD ./grpc.spec /root/rpmbuild/SPECS/grpc.spec

RUN rpmbuild -vv -ba grpc.spec

