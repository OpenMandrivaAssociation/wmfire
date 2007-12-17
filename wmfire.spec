Summary: A WindowMaker dock.app that displays CPU load as fire in a small icon
Name:		wmfire
Version: 1.2.3
Release: %mkrel 2
License:	GPL
Group:		Graphical desktop/WindowMaker
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.swanson.ukfsn.org/%{name}-%{version}.tar.gz
BuildRequires:	X11-devel, libgtop2.0-devel, xpm-devel
BuildRequires:	gtk+2-devel


%description
wmfire is an eye-candy dock applet for Window Maker that displays generated
fire, possibly according to how much load the system is experiencing, or from
a number somewhere in a file. wmfire requires very little CPU.
It has options for cyanish or orange/red flames, you can even  set it to
display your motherboard temperature through lm_sensors.


%prep
rm -rf %buildroot

%setup

%build
%configure 
%make

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%_bindir
install -m 755 src/%{name} %buildroot%_bindir
#{fireload_cpu,fireload_file}
install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 48x48.png > %buildroot%{_liconsdir}/%{name}.png

install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" icon="%{name}.png"\\
                 needs="X11" section="System/Monitoring" title="WmFire"\\
                 longtitle="A dock.app that displays CPU load as fire in a small icon"
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}

%files
%defattr (-,root,root)
%doc README ChangeLog INSTALL NEWS AUTHORS COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}

