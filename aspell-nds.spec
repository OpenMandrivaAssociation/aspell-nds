%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Low-Saxon
%define languagecode nds
%define lc_ctype nds_DE

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.01.0
Release:	13
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

# if there is isn't a qwertz.kbd provided by aspell, create it
if [ ! -r %{buildroot}/%{_libdir}/aspell-%{aspell_ver}/qwertz.kbd \
	-a ! -r /%{_libdir}/aspell-%{aspell_ver}/qwertz.kbd ]
then
	cat /%{_libdir}/aspell-%{aspell_ver}/standard.kbd | \
	sed  -e 's/ty/tz/; s/yu/zu/; s/zx/yx/' \
	> %{buildroot}/%{_libdir}/aspell-%{aspell_ver}/qwertz.kbd
fi

%files
%doc Copyright README*
%{_libdir}/aspell-%{aspell_ver}/*

