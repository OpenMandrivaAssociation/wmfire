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

