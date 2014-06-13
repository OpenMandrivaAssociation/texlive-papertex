# revision 19230
# category Package
# catalog-ctan /macros/latex/contrib/papertex
# catalog-date 2010-06-30 22:56:10 +0200
# catalog-license lppl
# catalog-version 1.2b
Name:		texlive-papertex
Version:	1.2b
Release:	7
Summary:	Class for newspapers, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/papertex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2b-2
+ Revision: 754640
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2b-1
+ Revision: 719188
- texlive-papertex
- texlive-papertex
- texlive-papertex
- texlive-papertex

