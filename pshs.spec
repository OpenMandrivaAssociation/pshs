Summary:	Pretty small HTTP server - a command-line tool to share files
Name:		pshs
Version:	0.2.1
Release:	1
Group:		Networking/WWW 
License:	GPLv2
Url:		https://github.com/mgorny/pshs/
Source0:	https://github.com/mgorny/pshs/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	pkgconfig(libevent)

%description
Pretty small HTTP server - a command-line tool to share files

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}

