Name:		texlive-papertex
Version:	19230
Release:	2
Summary:	Class for newspapers, etc
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/papertex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class allows LaTeX users to create a paperTeX newspaper.
The final document has a front page and as many inner pages as
desired. News items appear one after another and the user can
choose the number of columns, style and so on. The class allows
users to create newsletters too.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/papertex/papertex.cls
%doc %{_texmfdistdir}/doc/latex/papertex/CHANGES
%doc %{_texmfdistdir}/doc/latex/papertex/README
%doc %{_texmfdistdir}/doc/latex/papertex/example/example.pdf
%doc %{_texmfdistdir}/doc/latex/papertex/example/example.tex
%doc %{_texmfdistdir}/doc/latex/papertex/example/img/ireland.jpg
%doc %{_texmfdistdir}/doc/latex/papertex/example/img/weather/clouds.jpg
%doc %{_texmfdistdir}/doc/latex/papertex/example/img/weather/rain.jpg
%doc %{_texmfdistdir}/doc/latex/papertex/example/img/weather/sun.jpg
%doc %{_texmfdistdir}/doc/latex/papertex/papertex.pdf
#- source
%doc %{_texmfdistdir}/source/latex/papertex/papertex.dtx
%doc %{_texmfdistdir}/source/latex/papertex/papertex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
