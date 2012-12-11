Name:           ocaml-sqlite
Version:        1.5.7
Release:        2
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
BuildRequires:  sqlite3-devel
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




%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 1.5.7-2
+ Revision: 797741
- Rebuild

* Wed Mar 17 2010 Florent Monnier <blue_prawn@mandriva.org> 1.5.7-1mdv2011.0
+ Revision: 522849
- update to new version 1.5.7.

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.6-1mdv2010.1
+ Revision: 496352
- update to new version 1.5.6

  + Florent Monnier <blue_prawn@mandriva.org>
    - new version

* Thu Sep 10 2009 Florent Monnier <blue_prawn@mandriva.org> 1.5.4-3mdv2010.0
+ Revision: 437535
- new version

* Mon Sep 07 2009 Florent Monnier <blue_prawn@mandriva.org> 1.5.3-3mdv2010.0
+ Revision: 432954
- new version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-3mdv2010.0
+ Revision: 390306
- rebuild

* Sat May 23 2009 Florent Monnier <blue_prawn@mandriva.org> 1.5.1-2mdv2010.0
+ Revision: 379085
- updated version
- The initial RPM release was made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones

* Wed Jan 07 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.2-1mdv2009.1
+ Revision: 326814
- corrected group for the devel
- corrected group
- findlib package name
- import ocaml-sqlite

