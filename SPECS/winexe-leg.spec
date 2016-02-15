Name: winexe
Version: 1.1
Release: b787d2%{?dist}
Summary: Remote Windows command executor.


Group: Applications/System
License: GPLv3
URL: http://sourceforge.net/projects/winexe/
Source: %{name}-%{version}.tar.gz


AutoReqProv: no
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: libtalloc-devel
BuildRequires: samba4-devel >= 4.0.0
BuildRequires: popt-devel
BuildRequires: mingw64-gcc
BuildRequires: mingw32-gcc
Requires: samba4-libs >= 4.0.0
BuildRoot: %{_tmppath}/%{name}-%{version}-build


%description
Winexe remotely executes commands on Windows
NT/2000/XP/2003/Vista/7/2008/8/2012 systems from GNU/Linux.


%prep
%setup -q


%build
cd source
./waf configure build


%install
echo %{buildroot}
rm -rf %{buildroot}
%__install -d %{buildroot}/usr/bin
%__install source/build/winexe %{buildroot}/usr/bin


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/winexe


%changelog
* Sun Feb 14 2016 Randy Thompson <randy@heroictek.com> - 1.1-b787d2
- b787d2a2c4b1abc3653bad10aec943b8efcd7aab from git://git.code.sf.net/p/winexe/winexe-waf
