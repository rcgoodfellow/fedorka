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
  autoconf \
  automake \
  docbook-style-xsl \
  ebtables \
  gettext \
  glib2-devel \
  intltool \
  ipset \
  iptables \
  libxslt \
  python2-devel \
  python3-devel

RUN mkdir -p /root/rpmbuild/{SPECS,SOURCES}
WORKDIR /root/rpmbuild/SOURCES
RUN curl -JLO https://github.com/firewalld/firewalld/archive/v0.5.2.tar.gz

WORKDIR /tmp
#RUN git clone https://src.fedoraproject.org/git/rpms/kea.git
RUN git clone https://src.fedoraproject.org/git/rpms/firewalld.git
WORKDIR /tmp/firewalld
RUN git checkout a86d697d59d08a5f42f3eebbd2194f747f87c384
workdir /tmp
RUN cp firewalld/firewalld.spec /root/rpmbuild/SPECS/
RUN cp firewalld/*.patch /root/rpmbuild/SOURCES/
RUN cp firewalld/*.xml /root/rpmbuild/SOURCES/

WORKDIR /root/rpmbuild/SPECS
RUN rpmbuild -vv -ba firewalld.spec
