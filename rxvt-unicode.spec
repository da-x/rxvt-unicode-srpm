Name:           rxvt-unicode
Version:        5.5
Release:        3.fc5
Summary:        Rxvt-unicode is an unicode version of rxvt

Group:          User Interface/X
License:        GPL
URL:            http://software.schmorp.de/
Source0:        http://dist.schmorp.de/%name/%name-%version.tar.bz2
Source1:        rxvt-unicode.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  /usr/bin/tic
BuildRequires:  desktop-file-utils

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.


%prep
%setup -q


%build
%configure --enable-xft --enable-font-styles --enable-utmp --enable-wtmp \
  --enable-lastlog --enable-transparency --enable-tinting --enable-fading \
  --enable-menubar --enable-rxvt-scroll --enable-xterm-scroll \
  --enable-plain-scroll --enable-half-shadow --enable-xgetdefault \
  --enable-24bit --enable-keepscrolling --enable-selectionscrolling \
  --enable-mousewheel --enable-slipwheeling --enable-smart-resize \
  --enable-pointer-blank --enable-xpm-background --enable-next-scroll \
  --enable-xim --enable-linespace --with-save-lines=2000 --enable-resources \
  --with-codesets=all

make CFLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

tic -o $RPM_BUILD_ROOT/%_datadir/terminfo doc/etc/rxvt-unicode.terminfo

desktop-file-install \
  --vendor=fedora \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category=X-Fedora \
  %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.FAQ INSTALL doc/README.menu doc/README.xvt doc/etc doc/menu COPYING
%{_bindir}/*
%{_datadir}/terminfo/r/*
%{_mandir}/man*/*
%{_datadir}/applications/*

%changelog
* Sun Jun 05 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Thu Jun 02 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-2
- minor cleanups

* Thu May 12 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-1
- Version upgrade (5.5)

* Mon Mar 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:5.3-1
- Version upgrade (5.3)

* Wed Feb 09 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- Initial RPM release.
