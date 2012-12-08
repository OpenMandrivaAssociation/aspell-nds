%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Low-Saxon
%define languagecode nds
%define lc_ctype nds_DE

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.01.0
Release:       %mkrel 13
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

# if there is isn't a qwertz.kbd provided by aspell, create it
if [ ! -r ${RPM_BUILD_ROOT}/%{_libdir}/aspell-%{aspell_ver}/qwertz.kbd \
	-a ! -r /%{_libdir}/aspell-%{aspell_ver}/qwertz.kbd ]
then
	cat /%{_libdir}/aspell-%{aspell_ver}/standard.kbd | \
	perl -p -e 's/ty/tz/; s/yu/zu/; s/zx/yx/' \
	> ${RPM_BUILD_ROOT}/%{_libdir}/aspell-%{aspell_ver}/qwertz.kbd
fi

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright README*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-11mdv2011.0
+ Revision: 662855
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-10mdv2011.0
+ Revision: 603447
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-9mdv2010.1
+ Revision: 518948
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-8mdv2010.0
+ Revision: 413090
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.01.0-7mdv2009.1
+ Revision: 350080
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.01.0-6mdv2009.0
+ Revision: 220432
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.01.0-5mdv2008.1
+ Revision: 182505
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.01.0-4mdv2008.1
+ Revision: 148832
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-3mdv2007.1
+ Revision: 123337
- Import aspell-nds

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Thu Feb 17 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.01.0-2mdk
- added missing qwertz.kbd file

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.01.0-1mdk
- first version

