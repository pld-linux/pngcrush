#
# Conditional build:
%bcond_with	systemlibs	# use system libraries instead of modified ones
#				  (modified can give little better results)
#
Summary:	Optimizer for png files
Summary(pl):	Optymalizator plików png
Summary(pt_BR):	Utilitário para compressão de pngs
Name:		pngcrush
Version:	1.5.10
Release:	2
License:	BSD-like (see README.txt)
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/pmt/%{name}-%{version}.tar.bz2
# Source0-md5:	a659cc4d9f7cf57bbc979193a054704f
URL:		http://pmt.sf.net/pngcrush/
%if %{with systemlibs}
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program reads in a PNG image, and writes it out again, with the
optimum filter_method and zlib_level. It uses brute force (trying
filter_method none, and libpng adaptive filtering, with compression
levels 3 and 9). It does the most time-consuming method last in case
it turns out to be the best.

%description -l pl
Ten program wczytuje obrazek PNG i zapisuje go ponownie z optymalnymi
parametrami filter_method i zlib_level. U¿ywa metody brute force
(próbuje filter_method none oraz adaptacyjnego filtrowania libpng ze
stopniami kompresji 3 i 9).

%description -l pt_BR
O pngcrush é um otimizador para arquivos PNG (Portable Network
Graphics). Ele pode comprimir os arquivos em até 40%, sem perdas.

%prep
%setup -q

%if %{with systemlibs}
# workaround for Makefile and #include "png.h"
echo '#include <png.h>' > png.h
%endif

%build
%{__make} -f Makefile.gcc \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
%if %{with systemlibs}
	OBJS="pngcrush.o" \
	LDFLAGS="%{rpmldflags} -lpng -lz"
%endif

# create some real documentation
# NOTE: remember to update line numbers on upgrade!
head -n 24 pngcrush.c | cut -b 4- > README
head -n 378 pngcrush.c | tail -n 310 | cut -b 4- > CHANGELOG
head -n 415 pngcrush.c | tail -n 35 | cut -b 4- > TODO

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pngcrush $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG TODO README.txt
%attr(755,root,root) %{_bindir}/*
