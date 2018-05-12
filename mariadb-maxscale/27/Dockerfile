FROM fedora:27

RUN dnf update -y --refresh
RUN dnf groupinstall -y "C Development Tools and Libraries"
RUN dnf install -y git cmake sudo wget openssl-devel

WORKDIR /code
RUN git clone https://github.com/mariadb-corporation/MaxScale.git
WORKDIR /code/MaxScale/build
RUN ../BUILD/install_build_deps.sh
#XXX hack: trick build system into thinking this is an 'rpm' system
RUN touch /etc/rc.d/init.d/functions
RUN mkdir -p /opt
RUN cmake .. \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DWITH_SCRIPTS=y \
  -DPACKAGE=Y \
  -DTARGET_COMPONENT=all
RUN make
RUN make package
RUN sudo make install
RUN sudo ./postinst

