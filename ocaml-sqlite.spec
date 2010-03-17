Name:           ocaml-sqlite
Version:        1.5.7
Release:        %mkrel 1
Summary:        OCaml library for accessing SQLite3 databases

Group:          Development/Other
License:        BSD
URL:            http://www.ocaml.info/home/ocaml_sources.html#ocaml-sqlite3
Source0:        http://www.ocaml.info/ocaml_sources/ocaml-sqlite3-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/ocaml-sqlite3/archive/release-%{version}.tar.bz2 > ocaml-sqlite3-release-%{version}.tar.bz2
Patch0:         ocaml-sqlite-debian-install-no-mktop.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRequires:  libsqlite3-devel
BuildRequires:  chrpath

%description
SQLite 3 database library wrapper for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ocaml-sqlite3-release-%{version}
%patch0 -p1

./configure --libdir=%{_libdir}

%build
make all
make docs


%check
pushd test
for f in test_db test_exec test_stmt test_fun; do
  ocamlopt -I .. str.cmxa sqlite3.cmxa $f.ml -o $f
  ./$f
done
popd


%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/ocaml/sqlite3
%exclude %{_libdir}/ocaml/sqlite3/*.a
%exclude %{_libdir}/ocaml/sqlite3/*.cmxa
%exclude %{_libdir}/ocaml/sqlite3/*.cmx
%exclude %{_libdir}/ocaml/sqlite3/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%defattr(-,root,root,-)
%doc COPYING Changelog doc README.txt TODO
%{_libdir}/ocaml/sqlite3/*.a
%{_libdir}/ocaml/sqlite3/*.cmxa
%{_libdir}/ocaml/sqlite3/*.cmx
%{_libdir}/ocaml/sqlite3/*.mli


