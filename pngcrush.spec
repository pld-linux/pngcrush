Summary:	Optimizer for png files
Summary(pl):	Optymalizator plików png
Summary(pt_BR):	Utilitário para compressão de pngs
Name:		pngcrush
Version:	1.5.10
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/pmt/%{name}-%{version}.tar.bz2
Patch0:		%{name}-system-libs.patch
URL:		http://pmt.sf.net/pngcrush/
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
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
%patch -p1

%build
%{__make} -f Makefile.gcc \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \

# create some real documentation
head -n 24 pngcrush.c | cut -b 4- > README
head -n 372 pngcrush.c | tail -n 305 | cut -b 4- > CHANGELOG
head -n 409 pngcrush.c | tail -n 35 | cut -b 4- > TODO

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
