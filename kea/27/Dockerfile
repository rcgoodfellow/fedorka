FROM fedora:27

RUN dnf update -y --refresh
RUN dnf install -y \
  gcc \
  rpm-build \
  rpm-devel \
  rpmlint \
  make \
  python \
  bash \
  coreutils \
  diffutils \
  patch \
  rpmdevtools \
  curl

RUN dnf install -y \
  boost-devel \
  botan-devel \
  log4cplus-devel \
  gtest-devel \
  postgresql postgresql-devel \
  gcc-c++ \
  automake \
  libtool \
  mariadb-devel

RUN mkdir -p /root/rpmbuild/{SPECS,SOURCES}
WORKDIR /root/rpmbuild/SOURCES
RUN curl -JLO https://www.isc.org/downloads/file/kea-1-4-0-beta/?version=tar-gz

COPY ./kea.spec /root/rpmbuild/SPECS/kea.spec

WORKDIR /root/rpmbuild/SPECS
RUN rpmbuild -vv -ba kea.spec
