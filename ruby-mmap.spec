# TODO: optflags
Summary:	Ruby mmap Library
Name:		ruby-mmap
Version:	0.2.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	ftp://moulon.inra.fr/pub/ruby/mmap.tar.gz
# Source0-md5:	79cbb830ee6f76461f8875b05482ae5c
URL:		http://moulon.inra.fr/ruby/mmap.html
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby mmap Library.

%prep
%setup -q -n mmap-%{version}

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc -o rdoc *.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{ruby_archdir}/mmap.so