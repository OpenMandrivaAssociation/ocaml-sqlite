%define _disable_ld_no_undefined 1

Name:		ocaml-sqlite
Version:	5.4.1
Release:	2
Summary:	OCaml library for accessing SQLite3 databases
License:	MIT
Group:		Development/OCaml
Url:		https://mmottl.github.io/sqlite3-ocaml
Source0:	https://github.com/mmottl/sqlite3-ocaml/archive/%{version}/sqlite3-ocaml-%{version}.tar.gz

# Modern sqlite3-ocaml uses dune; no camlp4/camlp5 preprocessor is required.
BuildRequires:	make
BuildRequires:	ocaml >= 4.12
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-dune >= 2.7
BuildRequires:	ocaml-dune-configurator-devel
BuildRequires:	pkgconfig(sqlite3)

%description
SQLite3 database library wrapper for OCaml (bindings to the SQLite3 C API).

%package devel
Summary:	Development files for %{name}
Group:		Development/OCaml
Requires:	%{name}%{?_isa} = %{EVRD}
Requires:	pkgconfig(sqlite3)

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n sqlite3-ocaml-%{version}

%build
%dune_build -p sqlite3

%install
%dune_install

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel
%license LICENSE.md
%doc CHANGELOG.md README.md
