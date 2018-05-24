Name:	    kea
Version:	1.4.0
Release:	1.4.0%{?dist}
Summary:	isc kea dhcp server

Group:		Networking
License:	MPLv2.0 and Boost
URL:		  https://kea.isc.org
#Source0:  https://www.isc.org/downloads/file/kea-1-4-0-beta/?version=tar-gz
Source0:  https://ftp.isc.org/isc/kea/1.4.0-beta/kea-1.4.0-beta.tar.gz

BuildRequires: boost-devel botan-devel log4cplus-devel gtest-devel postgresql postgresql-devel mariadb-devel gcc-c++ automake libtool curl automake libtool
Requires:	 boost botan log4cplus gtest postgresql mariadb 

%description
The kea dhcp server version 1.4


%prep
%setup -n kea-1.4.0-beta


%build
%configure \
    --disable-dependency-tracking \
    --disable-rpath \
    --disable-silent-rules \
    --disable-static \
    --enable-debug \
    --enable-systemd \
    --with-dhcp-mysql \
    --with-dhcp-pgsql \
    --with-gnu-ld \
    --with-log4cplus \
    --with-openssl 

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# Get rid of .la files
find %{buildroot} -type f -name "*.la" -delete -print



%files
%doc

%{_sysconfdir}/kea/kea-ctrl-agent.conf
%{_sysconfdir}/kea/kea-dhcp-ddns.conf
%{_sysconfdir}/kea/kea-dhcp4.conf
%{_sysconfdir}/kea/kea-dhcp6.conf
%{_sysconfdir}/kea/keactrl.conf
/usr/lib/debug/usr/lib64/hooks/libdhcp_lease_cmds.so-1.4.0-1.4.0.fc27.x86_64.debug
/usr/lib/debug/usr/lib64/hooks/libdhcp_stat_cmds.so-1.4.0-1.4.0.fc27.x86_64.debug
/usr/lib64/hooks/libdhcp_lease_cmds.so
/usr/lib64/hooks/libdhcp_stat_cmds.so
/usr/share/doc/kea/COPYING



%{_sbindir}/kea-admin
%{_sbindir}/kea-dhcp-ddns
%{_sbindir}/kea-dhcp4
%{_sbindir}/kea-dhcp6
%{_sbindir}/kea-lfc
%{_sbindir}/keactrl
%{_sbindir}/perfdhcp
%{_bindir}/kea-msg-compiler
%{_sbindir}/kea-ctrl-agent
# %%{_unitdir}/kea-dhcp4.service
# %%{_unitdir}/kea-dhcp6.service
# %%{_unitdir}/kea-dhcp-ddns.service
# %%dir %%{_sysconfdir}/kea/
# %%config(noreplace) %%{_sysconfdir}/kea/kea-ctrl-agent.conf
# %%config(noreplace) %%{_sysconfdir}/kea/keactrl.conf
# %%config(noreplace) %%{_sysconfdir}/kea/kea-dhcp4.conf
# %%config(noreplace) %%{_sysconfdir}/kea/kea-dhcp6.conf
# %%config(noreplace) %%{_sysconfdir}/kea/kea-dhcp-ddns.conf
# %%dir %{_datarootdir}/kea/
%{_datarootdir}/kea/scripts
# %%dir /run/kea/
# %%{_tmpfilesdir}/kea.conf
# %%{_datarootdir}/kea/dhcp-ddns.spec
# %%{_datarootdir}/kea/dhcp4.spec
# %%{_datarootdir}/kea/dhcp6.spec
# %%dir %{_sharedstatedir}/kea
# %%config(noreplace) %%{_sharedstatedir}/kea/kea-leases4.csv
# %%config(noreplace) %%{_sharedstatedir}/kea/kea-leases6.csv
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/README
%{_pkgdocdir}/examples
%{_pkgdocdir}/kea-guide.*
%{_pkgdocdir}/kea-logo-100x70.png
%{_pkgdocdir}/kea-messages.html
%{_mandir}/man8/kea-admin.8.gz
%{_mandir}/man8/kea-dhcp-ddns.8.gz
%{_mandir}/man8/kea-dhcp4.8.gz
%{_mandir}/man8/kea-dhcp6.8.gz
%{_mandir}/man8/kea-lfc.8.gz
%{_mandir}/man8/keactrl.8.gz
%{_mandir}/man8/perfdhcp.8.gz
%{_mandir}/man8/kea-ctrl-agent.8.gz

# %%files libs
%license COPYING
# %%license ext/coroutine/LICENSE_1_0.txt
%{_libdir}/libkea-asiodns.so.*
%{_libdir}/libkea-asiolink.so.*
%{_libdir}/libkea-cc.so.*
%{_libdir}/libkea-cfgclient.so.*
%{_libdir}/libkea-cryptolink.so.*
%{_libdir}/libkea-dhcp++.so.*
%{_libdir}/libkea-dhcp_ddns.so.*
%{_libdir}/libkea-dhcpsrv.so.*
%{_libdir}/libkea-dns++.so.*
%{_libdir}/libkea-eval.so.*
%{_libdir}/libkea-exceptions.so.*
%{_libdir}/libkea-hooks.so.*
%{_libdir}/libkea-log.so.*
%{_libdir}/libkea-stats.so.*
%{_libdir}/libkea-threads.so.*
%{_libdir}/libkea-util-io.so.*
%{_libdir}/libkea-util.so.*
%{_libdir}/libkea-http.so*
%{_libdir}/libkea-process.so*

# %%files devel
%{_includedir}/kea
%{_libdir}/libkea-asiodns.so
%{_libdir}/libkea-asiolink.so
%{_libdir}/libkea-cc.so
%{_libdir}/libkea-cfgclient.so
%{_libdir}/libkea-cryptolink.so
%{_libdir}/libkea-dhcp++.so
%{_libdir}/libkea-dhcp_ddns.so
%{_libdir}/libkea-dhcpsrv.so
%{_libdir}/libkea-dns++.so
%{_libdir}/libkea-eval.so
%{_libdir}/libkea-exceptions.so
%{_libdir}/libkea-hooks.so
%{_libdir}/libkea-log.so
%{_libdir}/libkea-stats.so
%{_libdir}/libkea-threads.so
%{_libdir}/libkea-util-io.so
%{_libdir}/libkea-util.so
%{_libdir}/pkgconfig/dns++.pc

%changelog
* Thu May 24 2018 Ryan Goodfellow <ry@goodwu.net>
- first packaging of 1.4 for fedora 27

