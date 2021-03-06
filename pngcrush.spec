#
# Conditional build:
%bcond_with	systemlibs	# use system libraries instead of modified ones
#				  (modified can give little better results)
# NOTE:
# - to use system libs, read desc from homepage: http://pmt.sourceforge.net/pngcrush/
# - bundled zlib-1.2.3 differs from zlib-1.2.3 that it defines TOO_FAR
#   32767 instead of 4096
# - libpng diffs (this is bad?):
#diff -ur ../libpng-1.2.8/pngrutil.c ./pngrutil.c
#--- ../libpng-1.2.8/pngrutil.c    2006-03-21 16:12:37.000000000 +0200
#+++ ./pngrutil.c    2005-02-28 15:55:20.000000000 +0200
#@@ -1056,12 +1056,6 @@
#    prefix_length = profile - chunkdata;
#    chunkdata = png_decompress_chunk(png_ptr, compression_type, chunkdata,
#                                     slength, prefix_length, &data_length);
#-   if(chunkdata)
#-       png_set_iCCP(png_ptr, info_ptr, chunkdata, compression_type,
#-               chunkdata + prefix_length, data_length);
#-   else
#-       png_set_iCCP(png_ptr, info_ptr, chunkdata, compression_type,
#-               0x00, prefix_length);
#
#    profile_length = data_length - prefix_length;
#
Summary:	Optimizer for png files
Summary(pl.UTF-8):	Optymalizator plików png
Summary(pt_BR.UTF-8):	Utilitário para compressão de pngs
Name:		pngcrush
Version:	1.8.13
Release:	1
License:	BSD-like (see LICENSE)
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/pmt/%{name}-%{version}.tar.xz
# Source0-md5:	2eeb072fcb56dcc4f7ccc35bd4238bd3
Patch0:		%{name}-ptrdiff.patch
URL:		http://pmt.sourceforge.net/pngcrush/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with systemlibs}
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program reads in a PNG image, and writes it out again, with the
optimum filter_method and zlib_level. It uses brute force (trying
filter_method none, and libpng adaptive filtering, with compression
levels 3 and 9). It does the most time-consuming method last in case
it turns out to be the best.

%description -l pl.UTF-8
Ten program wczytuje obrazek PNG i zapisuje go ponownie z optymalnymi
parametrami filter_method i zlib_level. Używa metody brute force
(próbuje filter_method none oraz adaptacyjnego filtrowania libpng ze
stopniami kompresji 3 i 9).

%description -l pt_BR.UTF-8
O pngcrush é um otimizador para arquivos PNG (Portable Network
Graphics). Ele pode comprimir os arquivos em até 40%, sem perdas.

%prep
%setup -q
%patch0 -p1

# create some real documentation
# NOTE: remember to check these on upgrade!
sed -ne '1,/*\//p' pngcrush.c | cut -b 4- > README
sed -ne '/\/\* To do/,/*\/$/p;/PNG_INTERNAL/q' pngcrush.c | cut -b 4- > TODO
sed -ne '/* COPYRIGHT/,/*\/$/p;' pngcrush.c | cut -b 4- > LICENSE

%build
%{__make} %{?with_systemlibs:-f Makefile-nolib} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=c90 -Wall" \
	OPTIONS="%{rpmcppflags}" \
	LD="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
%if %{with systemlibs}
	PNGINC=$(pkg-config --variable=includedir libpng) \
	PNGLIB=%{_libdir} \
	ZINC=%{_includedir} \
	ZLIB=%{_libdir}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p pngcrush $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO ChangeLog.html
%attr(755,root,root) %{_bindir}/pngcrush
