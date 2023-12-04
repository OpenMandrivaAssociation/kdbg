Name:		kdbg
Version:	3.1.0
Release:	1
License: 	GPLv2+
Summary:	A Graphical Debugger Interface
URL:		http://www.kdbg.org
Group:		Development/Other
Source0:	http://downloads.sourceforge.net/kdbg/%{name}-%{version}.tar.gz
Patch1:		kdbg-2.5.5-ignore-gdb-newlines.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5)
Requires:	gdb

%description
KDbg is a graphical user interface to gdb, the GNU debugger. 
It provides an intuitive interface for setting breakpoints,
inspecting variables, and stepping through code. 

%prep
%autosetup -p1
sed -i -e '/CheckFunctionExists/iinclude(CheckIncludeFiles)' kdbg/CMakeLists.txt
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

%files -f %{name}.lang
%{_kde5_bindir}/%{name}
%{_sysconfdir}/xdg/kdbgrc
%{_kde5_datadir}/applications/%{name}.desktop
%{_kde5_datadir}/%{name}
%{_kde5_datadir}/kxmlgui5/%{name}
%{_iconsdir}/*/*/*/%{name}.*
