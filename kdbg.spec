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
%setup -q
%autopatch -p1
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

%changelog
* Tue Oct 09 2012 Giovanni Mariani <mc2374@mclink.it> 2.5.2-1
- New version 2.5.2
- Dropped support for obsolete distro releases
- Dropped BuildRoot and %%clean section

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 2.5.0-1mdv2011.0
+ Revision: 650018
- new version 2.5.0
- Created package structure for kdbg.

* Thu Sep 14 2006 Laurent MONTEL <lmontel@mandriva.com> 2.0.3-2
- Fix generate menu

* Tue Jan 24 2006 Laurent MONTEL <lmontel@mandriva.com> 2.0.3-1
- 2.0.3

* Wed Nov 30 2005 Laurent MONTEL <lmontel@mandriva.com> 2.0.2-1
- 2.0.2

* Wed Oct 26 2005 Laurent MONTEL <lmontel@mandriva.com> 2.0.1-1
- 2.0.1

* Mon Jul 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.0-1mdk
- New release 2.0.0

* Mon Mar 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.9.7-1mdk
- 1.9.7

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.9.6-1mdk
- 1.9.6

* Fri Jun  4 2004  <lmontel@n2.mandrakesoft.com> 1.2.9-4mdk
- Rebuild

* Mon Feb 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.9-3mdk
- Rebuild

* Wed Jan 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.9-2mdk
- Rebuild

* Wed Nov 12 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.9-1mdk
- 1.2.9

* Thu Jul 17 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.8-2mdk
- Rebuild

* Thu Jun 26 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.8-1mdk
- 1.2.8

* Mon Apr 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.7-2mdk
- Fix spec file

* Fri Feb 07 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.7-1mdk
- update

* Sat Nov 16 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.6-2mdk
- Make it lib64 aware

* Sun Oct 20 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.6-1mdk
- 1.2.6

* Wed Aug 14 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.5-4mdk
- Rebuild against gcc-3.2

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.5-3mdk
- Rebuild against gcc-3.2

* Thu Jun 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.5-2mdk
- port to kde3.0

* Wed Mar 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.5-1mdk
- Update code 1.2.5

* Thu Jan 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.4-2mdk
- Add language file (bug reported by DUCLOS Andre <shirka@wanadoo.fr>)

* Sun Jan 21 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.4-1mdk
- Update code (1.2.4)

* Wed Jan 02 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.3-0.1mdk
- update code 

* Mon Nov  5 2001 Stefan van der Eijk <stefan@eijk.nu> 1.2.2-0.4mdk
- BuildRequires revisited

* Thu Oct 18 2001 Daouda LO <daouda@mandrakesoft.com> 1.2.2-0.3mdk
- spec cleanups
- rpmlint compliant

* Thu Sep 06 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.2-0.2mdk
- Rebuild with new kdelibs

* Tue Aug 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.2-0.1mdk
- Update code (1.2.2)

* Sat Jun 02 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-0.2mdk
- Rebuild with kde2.2alpha2

* Wed May 2 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-0.1mdk
- Update code

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.6mdk
- Move KDE menu entry in %%_datadir/applnk
- Rebuild against latest GCC

* Sat Mar 31 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.5mdk
- Fix BuildRequires for non %%ix86 architectures

* Thu Mar 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.0-0.4mdk
- Add build requires 

* Wed Mar 14 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-0.3mdk
- Rebuild against Qt 2.3.0

* Mon Feb 26 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.0-0.2mdk
- rebuild

* Fri Dec 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-0.1mdk
- new in contribs
