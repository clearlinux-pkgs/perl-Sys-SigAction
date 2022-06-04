#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sys-SigAction
Version  : 0.23
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/L/LB/LBAXTER/Sys-SigAction-0.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LB/LBAXTER/Sys-SigAction-0.23.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsys-sigaction-perl/libsys-sigaction-perl_0.23-1.debian.tar.xz
Summary  : 'Perl extension for Consistent Signal Handling'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sys-SigAction-license = %{version}-%{release}
Requires: perl-Sys-SigAction-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Sys/SigAction
Sys::SigAction provides EASY access to POSIX::sigaction() for signal
handling on systems the support sigaction().

%package dev
Summary: dev components for the perl-Sys-SigAction package.
Group: Development
Provides: perl-Sys-SigAction-devel = %{version}-%{release}
Requires: perl-Sys-SigAction = %{version}-%{release}

%description dev
dev components for the perl-Sys-SigAction package.


%package license
Summary: license components for the perl-Sys-SigAction package.
Group: Default

%description license
license components for the perl-Sys-SigAction package.


%package perl
Summary: perl components for the perl-Sys-SigAction package.
Group: Default
Requires: perl-Sys-SigAction = %{version}-%{release}

%description perl
perl components for the perl-Sys-SigAction package.


%prep
%setup -q -n Sys-SigAction-0.23
cd %{_builddir}
tar xf %{_sourcedir}/libsys-sigaction-perl_0.23-1.debian.tar.xz
cd %{_builddir}/Sys-SigAction-0.23
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sys-SigAction-0.23/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sys-SigAction
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Sys-SigAction/59fa8c2f00007f54e7e95e6ae265cd96b97613e8
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sys::SigAction.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sys-SigAction/59fa8c2f00007f54e7e95e6ae265cd96b97613e8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
