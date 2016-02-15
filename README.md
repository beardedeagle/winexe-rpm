# winexe-rpm
Bash script and spec file to prep and build a winexe 1.1 rpm. Built and tested against:
* RedHat
  * 7.2 / 6.7
  * 4.2.* / 4.0.*
* CentOS
  * 7.2 / 6.7
  * 4.2.* / 4.0.*

Winexe remotely executes commands on Windows NT/2000/XP/2003/Vista/7/2008/8/2012 systems from GNU/Linux.

Winexe project home: <http://sourceforge.net/projects/winexe/>
Samba project home: <https://www.samba.org/>

> All pull requests are welcome. This package is essential to my own infrastructure so any improvements that can be made are great. If you have the ability, think about picking up development for winexe itself. Thank you in advance for any and all suggestions and help with this package.

## Requirements

These are handled by the winexe-rpm bash script. Depending on your system and configuration, you may need to install epel-release.

Installed against RedHat/Centos 7:
* gcc
* perl
* mingw-binutils-generic
* mingw-filesystem-base
* mingw32-binutils
* mingw32-cpp
* mingw32-crt
* mingw32-filesystem
* mingw32-gcc
* mingw32-headers
* mingw64-binutils
* mingw64-cpp
* mingw64-crt
* mingw64-filesystem
* mingw64-gcc
* mingw64-headers
* libcom_err-devel
* popt-devel
* zlib-devel
* zlib-static
* glibc-devel
* glibc-static
* python-devel
* git
* gnutls-devel
* libacl-devel
* openldap-devel
* rpm-build
* pkgconfig

Installed against RedHat/Centos 6:
* git
* rpm-build
* gcc
* pkgconfig
* libtalloc-devel
* samba4-devel
* popt-devel
* mingw64-gcc
* mingw32-gcc

Removed:
* libbsd-devel

## Building fresh RPMs

Clone the repo:

```
git clone https://github.com/beardedeagle/winexe-rpm.git
cd winexe-rpm
chmod +x winexe-rpm
```

## Build the winexe RPM

Build the RPMs:

`./winexe-rpm`

And install:

`rpm -iUvh RPMS/$HOSTTYPE/winexe-1.1-b787d2.*.$HOSTTYPE.rpm`

## Acknowledgements
I would like to thank Julio Gonzalez Gil as this repo is modeled heavily after his <https://github.com/juliogonzalez/winexe-rpm>.
I would also like to thank the developers of Winexe and Samba for making these fine packages.
