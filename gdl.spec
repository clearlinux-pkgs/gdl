#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : gdl
Version  : 3.40.0
Release  : 10
URL      : https://download.gnome.org/sources/gdl/3.40/gdl-3.40.0.tar.xz
Source0  : https://download.gnome.org/sources/gdl/3.40/gdl-3.40.0.tar.xz
Summary  : Gnome Docking Library
Group    : Development/Tools
License  : LGPL-2.0
Requires: gdl-data = %{version}-%{release}
Requires: gdl-lib = %{version}-%{release}
Requires: gdl-license = %{version}-%{release}
Requires: gdl-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Gnome Docking library
=====================
Provides docking features for gtk+. Currently used by anjuta and lumiera.

%package data
Summary: data components for the gdl package.
Group: Data

%description data
data components for the gdl package.


%package dev
Summary: dev components for the gdl package.
Group: Development
Requires: gdl-lib = %{version}-%{release}
Requires: gdl-data = %{version}-%{release}
Provides: gdl-devel = %{version}-%{release}
Requires: gdl = %{version}-%{release}

%description dev
dev components for the gdl package.


%package doc
Summary: doc components for the gdl package.
Group: Documentation

%description doc
doc components for the gdl package.


%package lib
Summary: lib components for the gdl package.
Group: Libraries
Requires: gdl-data = %{version}-%{release}
Requires: gdl-license = %{version}-%{release}

%description lib
lib components for the gdl package.


%package license
Summary: license components for the gdl package.
Group: Default

%description license
license components for the gdl package.


%package locales
Summary: locales components for the gdl package.
Group: Default

%description locales
locales components for the gdl package.


%prep
%setup -q -n gdl-3.40.0
cd %{_builddir}/gdl-3.40.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680023632
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1680023632
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdl
cp %{_builddir}/gdl-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gdl/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
%make_install
%find_lang gdl-3

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gdl-3.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libgdl-3.0/gdl/gdl-dock-bar.h
/usr/include/libgdl-3.0/gdl/gdl-dock-item-grip.h
/usr/include/libgdl-3.0/gdl/gdl-dock-item.h
/usr/include/libgdl-3.0/gdl/gdl-dock-layout.h
/usr/include/libgdl-3.0/gdl/gdl-dock-master.h
/usr/include/libgdl-3.0/gdl/gdl-dock-object.h
/usr/include/libgdl-3.0/gdl/gdl-dock-placeholder.h
/usr/include/libgdl-3.0/gdl/gdl-dock.h
/usr/include/libgdl-3.0/gdl/gdl.h
/usr/include/libgdl-3.0/gdl/libgdltypebuiltins.h
/usr/lib64/libgdl-3.so
/usr/lib64/pkgconfig/gdl-3.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gdl-3.0/GdlDock.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockBar.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockItem.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockItemButtonImage.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockItemGrip.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockLayout.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockMaster.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockNotebook.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockObject.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockPaned.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockPlaceholder.html
/usr/share/gtk-doc/html/gdl-3.0/GdlDockTablabel.html
/usr/share/gtk-doc/html/gdl-3.0/GdlPreviewWindow.html
/usr/share/gtk-doc/html/gdl-3.0/GdlSwitcher.html
/usr/share/gtk-doc/html/gdl-3.0/annotation-glossary.html
/usr/share/gtk-doc/html/gdl-3.0/api-index-full.html
/usr/share/gtk-doc/html/gdl-3.0/api.html
/usr/share/gtk-doc/html/gdl-3.0/core.html
/usr/share/gtk-doc/html/gdl-3.0/deprecated.html
/usr/share/gtk-doc/html/gdl-3.0/gdl-3.0.devhelp2
/usr/share/gtk-doc/html/gdl-3.0/home.png
/usr/share/gtk-doc/html/gdl-3.0/index.html
/usr/share/gtk-doc/html/gdl-3.0/left-insensitive.png
/usr/share/gtk-doc/html/gdl-3.0/left.png
/usr/share/gtk-doc/html/gdl-3.0/private.html
/usr/share/gtk-doc/html/gdl-3.0/right-insensitive.png
/usr/share/gtk-doc/html/gdl-3.0/right.png
/usr/share/gtk-doc/html/gdl-3.0/style.css
/usr/share/gtk-doc/html/gdl-3.0/up-insensitive.png
/usr/share/gtk-doc/html/gdl-3.0/up.png
/usr/share/gtk-doc/html/gdl-3.0/widget.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdl-3.so.5
/usr/lib64/libgdl-3.so.5.0.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdl/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f gdl-3.lang
%defattr(-,root,root,-)

