Name:           rxvt-unicode
Version:        8.8
Release:        1%{?dist}
Summary:        Rxvt-unicode is an unicode version of rxvt

Group:          User Interface/X
License:        GPLv2+
URL:            http://software.schmorp.de/
Source0:        http://dist.schmorp.de/%name/%name-%version.tar.bz2
Source1:        rxvt-unicode.desktop
#Patch0:         urxvt-utempter.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  /usr/bin/tic
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  perl-devel
BuildRequires:  libAfterImage-devel
#BuildRequires:  libutempter-devel

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.


%prep
%setup -q
#%patch0
#autoreconf -f

%build
#  --enable-utempter --disable-utmp --disable-wtmp --disable-lastlog \
%configure --enable-xft --enable-font-styles --enable-afterimage \
  --enable-utmp --enable-wtmp --enable-lastlog \
  --enable-transparency --enable-fading \
  --enable-rxvt-scroll --enable-xterm-scroll --enable-next-scroll \
  --enable-plain-scroll \
  --enable-keepscrolling --enable-selectionscrolling \
  --enable-mousewheel --enable-slipwheeling --enable-smart-resize \
  --enable-pointer-blank \
  --enable-xim --enable-resources \
  --with-codesets=all --enable-iso14755 --enable-frills

make CFLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
  --vendor=fedora \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category=X-Fedora \
  %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.FAQ INSTALL doc/README.xvt doc/etc doc/changes.txt COPYING
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_libdir}/urxvt

%changelog
* Mon Dec 17 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.8-1
- version upgrade

* Wed Dec 12 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.5a-2
- remove utempter patch for now

* Thu Nov 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.5a-1
- version upgrade

* Wed Nov 07 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.4-2
- fix #368921 (Rxvt.backgroundPixmap needs libAfterImage support BR now)
- add patch for utempter support

* Sun Oct 28 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.4-1
- version upgrade

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.3-1
- version upgrade
- new license tag

* Sat Jun 02 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.2-1
- version upgrade (#239421)

* Sun Jan 21 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.1-2
- drop terminfo file it is included in ncurses now

* Fri Dec 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.1-1
- version upgrade

* Thu Nov 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.0-1
- version upgrade

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.9-2
- FE6 rebuild

* Tue Aug 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.9-1
- version upgrade

* Tue Jul 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.8-1
- version upgrade

* Tue Feb 21 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.7-1
- version upgrade

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.6-2
- Rebuild for Fedora Extras 5

* Fri Feb 10 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.6-1
- version upgrade

* Tue Jan 31 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.5-1
- version upgrade

* Sat Jan 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.4-1
- version upgrade

* Fri Jan 27 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.3a-1
- version upgrade

* Mon Jan 23 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.2-1
- version upgrade (should resolve #178561)

* Thu Jan 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.1-1
- version upgrade

* Sat Jan 14 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.0-1
- version upgrade

* Thu Jan 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.3-1
- version upgrade

* Tue Jan 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.2-1 
- version upgrade

* Wed Dec 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.1-1
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.0-1
- version upgrade

* Sun Dec 18 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.9-1
- version upgrade

* Fri Nov 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.8-2
- modular xorg integration

* Tue Oct 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.8-1
- version upgrade

* Sun Oct 16 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-3
- enable frills (#170965)

* Sat Sep 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-2
- enable iso14755 (#168548)

* Tue Aug 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-1
- version upgrade

* Sun Jun 05 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-3
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
