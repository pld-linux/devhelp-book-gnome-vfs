Summary:	DevHelp book: gnome-vfs
Summary(pl):	Ksi±¿ka do DevHelp'a o gnome-vfs
Name:		devhelp-book-gnome-vfs
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gnome-vfs.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gnome-vfs

%description -l pl
Ksi±¿ka do DevHelp o gnome-vfs

%prep
%setup -q -c gnome-vfs -n gnome-vfs

%build
mv -f book gnome-vfs
mv -f book.devhelp gnome-vfs.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gnomevfs
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gnome-vfs.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gnome-vfs/* $RPM_BUILD_ROOT%{_prefix}/books/gnomevfs

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
