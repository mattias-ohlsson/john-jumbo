%global john_release %{version}-Jumbo-1

Name:           john-jumbo
Version:        1.9.0
Release:        1%{?dist}
Summary:        John the Ripper password cracker

License:        GPLv2
URL:            https://github.com/magnumripper/john
Source0:        https://github.com/magnumripper/john/archive/refs/tags/%{john_release}.tar.gz

Provides:       john
Conflicts:      john

# Fix alignment compile errors on GCC 11:
Patch0:         https://github.com/magnumripper/john/commit/8152ac071bce1ebc98fac6bed962e90e9b92d8cf.patch

BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: yasm gmp-devel
BuildRequires: libpcap-devel
BuildRequires: bzip2-devel

%description
John the Ripper is a fast password cracker. Its primary purpose is to
detect weak Unix passwords, but a number of other hash types are
supported as well. This is the community-enhanced, "jumbo" version of
John the Ripper.

%prep
%autosetup -n john-%{john_release}/src

%build
%configure --with-systemwide
%make_build

%install
cd ..
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/john/rules
install -m 755 run/{john,mailer} %{buildroot}%{_bindir}
install -m 644 run/{*.py,*.pl,*.chr,*.lst,*.conf,*.dic,*.txt,*.pm,*.js,*.rb,*.lua} \
 run/benchmark-unify run/bitlocker2john run/calc_stat run/cprepair run/dmg2john run/genmkvpwd \
 run/hccap2john run/keepass2john run/makechr run/mkvcalcproba run/putty2john run/racf2john run/raw2dyna \
 run/relbench run/tgtsnarf run/uaf2john run/wpapcap2john \
 %{buildroot}%{_datadir}/john
install -m 644 run/rules/*.rule %{buildroot}%{_datadir}/john/rules
mv %{buildroot}%{_datadir}/john/john.conf %{buildroot}%{_sysconfdir}

pushd %{buildroot}%{_bindir}
ln -s john base64conv
ln -s john gpg2john
ln -s john rar2john
ln -s john unafs
ln -s john undrop
ln -s john unique
ln -s john unshadow
ln -s john zip2john
popd

%files
%license ../doc/LICENSE
%doc ../README.md ../doc/*
%{_bindir}/john
%{_bindir}/mailer
%{_bindir}/base64conv
%{_bindir}/gpg2john
%{_bindir}/rar2john
%{_bindir}/unafs
%{_bindir}/undrop
%{_bindir}/unique
%{_bindir}/unshadow
%{_bindir}/zip2john
%{_sysconfdir}/john.conf
%{_datadir}/john/*.py
%{_datadir}/john/*.pl
%{_datadir}/john/*.pm
%{_datadir}/john/*.chr
%{_datadir}/john/*.lst
%{_datadir}/john/*.dic
%{_datadir}/john/*.txt
%{_datadir}/john/*.conf
%{_datadir}/john/rules/*.rule
%{_datadir}/john/benchmark-unify
%{_datadir}/john/bitlocker2john
%{_datadir}/john/calc_stat
%{_datadir}/john/cprepair
%{_datadir}/john/dmg2john
%{_datadir}/john/genincstats.rb
%{_datadir}/john/genmkvpwd
%{_datadir}/john/hccap2john
%{_datadir}/john/keepass2john
%{_datadir}/john/makechr
%{_datadir}/john/mkvcalcproba
%{_datadir}/john/mongodb2john.js
%{_datadir}/john/network2john.lua
%{_datadir}/john/putty2john
%{_datadir}/john/racf2john
%{_datadir}/john/raw2dyna
%{_datadir}/john/relbench
%{_datadir}/john/tgtsnarf
%{_datadir}/john/uaf2john
%{_datadir}/john/wpapcap2john

%changelog
* Tue Apr 19 2022 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.9.0-1
- Initial build.
