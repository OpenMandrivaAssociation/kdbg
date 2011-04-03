Name: 		kdbg
Version: 	2.5.0
Release: 	%mkrel 1
License: 	GPLv2+
Summary: 	A Graphical Debugger Interface
URL: 		http://www.kdbg.org
Group: 		Development/Other
Source: 	http://downloads.sourceforge.net/kdbg/%{name}-%{version}.tar.gz
BuildRoot: 	%_tmppath/%{name}-buildroot
Requires:	gdb
BuildRequires:	kdelibs4-devel

%description
KDbg is a graphical user interface to gdb, the GNU debugger. 

It provides an intuitive interface for setting breakpoints,
inspecting variables, and stepping through code. 

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%find_lang %name --with-html

%if %mdkversion < 200900
%post 
%update_menus
%endif
  
%if %mdkversion < 200900
%postun 
%clean_menus
%endif

%clean
rm -fr %buildroot

%files -f %{name}.lang
%defattr (-,root,root)
%_kde_bindir/%name
%_kde_datadir/config/kdbgrc
%_kde_datadir/applications/kde4/kdbg.desktop
%_kde_datadir/apps/kdbg
