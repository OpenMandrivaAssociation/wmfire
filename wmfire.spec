Summary:	A WindowMaker dock.app that displays CPU load as fire in a small icon
Name:		wmfire
Version:	1.2.4
Release:	5
License:	GPLv2
Group:		Graphical desktop/WindowMaker
Url:		http://www.swanson.ukfsn.org/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(x11)

%description
wmfire is an eye-candy dock applet for Window Maker that displays generated
fire, possibly according to how much load the system is experiencing, or from
a number somewhere in a file. wmfire requires very little CPU.
It has options for cyanish or orange/red flames, you can even  set it to
display your motherboard temperature through lm_sensors.

%prep
%setup -q

%build
%configure
%make

%install
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

%files
%doc README ChangeLog INSTALL NEWS AUTHORS COPYING
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*

