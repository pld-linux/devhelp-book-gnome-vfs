Summary:	DevHelp book: gnome-vfs 1.0
Summary(pl.UTF-8):	Książka do DevHelpa o gnome-vfs 1.0
Name:		devhelp-book-gnome-vfs
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	http://www.devhelp.net/books/books/gnome-vfs.tar.gz
Source0:	gnome-vfs.tar.gz
# Source0-md5:	2ba7968f4d1ad01d9e8063690ebe5385
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gnome-vfs 1.0.

%description -l pl.UTF-8
Książka do DevHelpa o gnome-vfs 1.0.

%prep
%setup -q -c -n gnome-vfs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gnomevfs,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gnome-vfs.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gnomevfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
