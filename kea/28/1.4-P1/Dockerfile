FROM fedora:28

RUN dnf update -y --refresh
RUN dnf install -y --allowerasing \
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
  curl \
  git

RUN dnf install -y --allowerasing \
  boost-devel \
  botan-devel \
  log4cplus-devel \
  gtest-devel \
  postgresql postgresql-devel \
  gcc-c++ \
  community-mysql-devel \
  automake \
  libtool \
  procps-ng \
  valgrind-devel
  
  #mariadb-devel \
  #mariadb-connector-c-devel \

RUN mkdir -p /root/rpmbuild/{SPECS,SOURCES}
WORKDIR /root/rpmbuild/SOURCES
RUN curl -JLO https://ftp.isc.org/isc/kea/1.4.0-P1/kea-1.4.0-P1.tar.gz

WORKDIR /tmp
#RUN git clone https://src.fedoraproject.org/git/rpms/kea.git
RUN echo 'poo'
RUN git clone --branch v1.4-P1 https://github.com/rcgoodfellow/fedora-kea.git kea
RUN cp kea/kea.spec /root/rpmbuild/SPECS/
RUN cp kea/*.patch /root/rpmbuild/SOURCES/

WORKDIR /root/rpmbuild/SPECS
RUN rpmbuild -vv -ba kea.spec
