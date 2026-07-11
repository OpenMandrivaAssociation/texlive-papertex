%global tl_name papertex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2b
Release:	%{tl_revision}.1
Summary:	Class for newspapers, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/papertex
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/papertex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class allows LaTeX users to create a paperTeX newspaper. The final
document has a front page and as many inner pages as desired. News items
appear one after another and the user can choose the number of columns,
style and so on. The class allows users to create newsletters too.

