%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library for accessing SQLite 3 databases
Name:		ocaml-sqlite
Version:	2.0.5
Release:	1
License:	BSD
Group:		Development/Other
Url:		http://www.ocaml.info/home/ocaml_sources.html#ocaml-sqlite3
Source0:	http://www.ocaml.info/ocaml_sources/sqlite3-ocaml-%{version}.tar.gz
BuildRequires:	camlp4
BuildRequires:	chrpath
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	pkgconfig(sqlite3)

%description
SQLite 3 database library wrapper for OCaml.

%files
%doc COPYING.txt
%{_libdir}/ocaml/sqlite3
%exclude %{_libdir}/ocaml/sqlite3/*.a
%exclude %{_libdir}/ocaml/sqlite3/*.cmxa
%exclude %{_libdir}/ocaml/sqlite3/*.cmx
%exclude %{_libdir}/ocaml/sqlite3/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc COPYING.txt README.md
%{_libdir}/ocaml/sqlite3/*.a
%{_libdir}/ocaml/sqlite3/*.cmxa
%{_libdir}/ocaml/sqlite3/*.cmx
%{_libdir}/ocaml/sqlite3/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n sqlite3-ocaml-%{version}

%build
./configure \
	--enable-tests \
	--prefix %{_prefix} \
	--destdir '%{buildroot}' \
	--docdir %{_docdir}/%{name}-devel/

make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

