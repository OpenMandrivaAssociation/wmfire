Summary:	A WindowMaker dock.app that displays CPU load as fire in a small icon
Name:		wmfire
Version:	1.2.4
Release:	1
License:	GPLv2
Group:		Graphical desktop/WindowMaker
Source:		%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
URL:		http://www.swanson.ukfsn.org/%{name}-%{version}.tar.gz
BuildRequires:	gtk+2-devel
BuildRequires:	libx11-devel
BuildRequires:	libgtop2.0-devel

%description
wmfire is an eye-candy dock applet for Window Maker that displays generated
fire, possibly according to how much load the system is experiencing, or from
a number somewhere in a file. wmfire requires very little CPU.
It has options for cyanish or orange/red flames, you can even  set it to
display your motherboard temperature through lm_sensors.


%prep
%setup -q

%build
%configure2_5x
%make

%install
[ -d %buildroot ] && rm -rf %buildroot

%makeinstall_std

install -m 755 -d %buildroot%{_datadir}/pixmaps
tar xOjf %SOURCE1 48x48.png > %buildroot%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=System;Monitor;
Name=WmFire                 
Comment=A dock.app that displays CPU load as fire in a small icon
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}

%files
%defattr (-,root,root)
%doc README ChangeLog INSTALL NEWS AUTHORS COPYING
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*



%changelog
* Tue Oct 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.4-1
+ Revision: 705304
- new version 1.2.4
  cleaned up spec

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.2.3-7
+ Revision: 634796
- add patch
- fix link

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.2.3-6mdv2010.0
+ Revision: 434848
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-5mdv2009.0
+ Revision: 262050
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-4mdv2009.0
+ Revision: 256137
- rebuild
- fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
  extension, but there should be no extension as described in the Icon Theme
  Specification if the value is not an absolute path'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.2.3-2mdv2008.1
+ Revision: 135511
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import wmfire


* Fri Apr 21 2006 Frederic Crozat <fcrozat@mandriva.com> 1.2.3-2mdk
- Rebuild

* Fri Mar 10 2006 Jerome Soyer <saispo@mandriva.org> 1.2.3-1mdk
- New release 1.2.3

* Wed May 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.2-4mdk
- Rebuild

* Sat Mar 19 2005 Nicolas Lécureuil <neoclust@mandrake.org> 1.2.2-3mdk
- Fix summary 
- Rebuild 

* Fri Sep 17 2004 Franck Villaume <fvill@freesurf.fr> 1.2.2-2mdk
- BuildRequires

* Mon Jun 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2

* Thu Apr 29 2004 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 1.2.0-1mdk
- New version 1.2.0

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.3.9pre4-8mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.3.9pre4-7mdk
- rebuild

* Mon Feb 11 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.0.3.9pre4-6mdk
- xpm icons converted to png.
- I know that the version number won't let people upgrade cleanly to 0.0.3.9
  when that one will be out, but look, the website is dead, and there has
  been no updates at all since Oct 1999, so that's not likely to happen at all.

* Fri Aug 31 2001 Etienne Faure <etienne@mandrakesoft.com> 0.0.3.9pre4-5mdk
- rebuild

* Wed Feb 21 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.0.3.9pre4-4mdk
- merge between Lenny's spec and mine

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.0.3.9pre4-3mdk
- fix files section (thx Viet) 

* Tue Oct 31 2000 HA Quôc-Viêt <viet@mandrakesoft.com> 0.0.3.9pre4-3mdk
- small fix in spec file : _tmppath
- not released

* Wed Sep 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.3.9pre4-2mdk
- macros

* Mon Aug 02 2000 HA Quôc-Viêt <viet@mandrakesoft.com> 0.0.3.9pre4-1mdk
- menu entry added
- 16x16, 32x32 and 48x48 icons added

* Mon Jul 31 2000 HA Quôc-Viêt <viet@mandrakesoft.com> 0.0.3.9pre4-1mdk
- better list of dependencies 
- the version  number was missing in the last changelog
- the package revision has been adjusted to the naming convention
- not released

* Wed Jul 12 2000 HA Quôc-Viêt <viet@mandrakesoft.com> 0.0.3.9pre4-0mdk
- Initial release.
- no changes made to the original archive
