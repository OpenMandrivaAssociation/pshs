Name:		pshs
Summary:	Pretty small HTTP server - a command-line tool to share files
Version:	0.2.1
Release:	1
Source0:	https://github.com/mgorny/pshs/%{name}-%{version}.tar.bz2
URL:		https://github.com/mgorny/pshs/
Group:		Networking/WWW 
License:	GPL
BuildRequires:	gcc make automake libtool
BuildRequires:	libevent-devel


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
%{_bindir}/%name
