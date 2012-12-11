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


%changelog
* Mon Jun 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.1-1
+ Revision: 806801
- version update 0.2.1

* Fri Nov 11 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.1-1
+ Revision: 730165
- imported package pshs

