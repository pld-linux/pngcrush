Summary:	Optimizer for png files
Summary(pl):	Optymalizator plików png
Summary(pt_BR):	Utilitário para compressão de pngs
Name:		pngcrush
Version:	1.5.8
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(cs):	Aplikace/Grafika
Group(da):	Programmer/Grafik
Group(de):	Applikationen/Graphiken
Group(es):	Aplicaciones/Gráficos
Group(fr):	Applications/Graphiques
Group(id):	Aplikasi/Grafik
Group(is):	Forrit/Myndvinnsla
Group(it):	Applicazioni/Immagini
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥°¥é¥Õ¥£¥Ã¥¯¥¹
Group(no):	Applikasjoner/Grafikk
Group(pl):	Aplikacje/Grafika
Group(pt):	Aplicações/Gráficos
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/çÒÁÆÉËÁ
Group(sl):	Programi/Grafika
Group(sv):	Tillämpningar/Grafik
Source0:	http://prdownloads.sourceforge.net/pmt/%{name}-%{version}.tar.gz
URL:		http://pmt.sf.net/pngcrush/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program reads in a PNG image, and writes it out again, with the
optimum filter_method and zlib_level. It uses brute force (trying
filter_method none, and libpng adaptive filtering, with compression
levels 3 and 9). It does the most time-consuming method last in case
it turns out to be the best.

%description -l pl
Ten program wczytuje obrazek PNG i zapisuje go ponownie z optymalnymi
parametrami filter_method i zlib_level. U¿ywa metody brute force.

%description -l pt_BR
O pngcrush é um otimizador para arquivos PNG (Portable Network
Graphics). Ele pode comprimir os arquivos em até 40%, sem perdas.

%prep
%setup -q

%build
%{__make} -f Makefile.gcc CC="%{__cc}" CFLAGS="%{rpmcflags}"

# create some real documentation
head -n 24 pngcrush.c | cut -b 4- > README
head -n 361 pngcrush.c | tail -n 294 | cut -b 4- > CHANGELOG
head -n 398 pngcrush.c | tail -n 35 | cut -b 4- > TODO

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pngcrush $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README CHANGELOG TODO README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
