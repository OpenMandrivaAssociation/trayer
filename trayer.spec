%define name	trayer
%define version	1.0
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Lightweight GTK2-based system tray
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://fvwm-crystal.berlios.de/
License:	MIT
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel libxmu-devel

%description
trayer is a small program designed to provide systray functionality present in
GNOME/KDE desktop environments for window managers which do not support that
function. System tray is a place, where various applications put their icons,
so they are always visible presenting status of applications and allowing user
to control programs.

%prep
%setup -q

%build
# parallel build fails
make CFLAGS="$RPM_OPT_FLAGS" 
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp %name %buildroot/%_bindir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG CREDITS README
%{_bindir}/%name
