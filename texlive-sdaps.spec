%global tl_name sdaps
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.10
Release:	%{tl_revision}.1
Summary:	LaTeX support files for SDAPS
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sdaps
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sdaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sdaps.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sdaps.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(environ)
Requires:	texlive(lastpage)
Requires:	texlive(pgf)
Requires:	texlive(qrcode)
Requires:	texlive(sectsty)
Requires:	texlive(translator)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains LaTeX classes and packages to create machine
readable questionnaires. Metadata is generated for the whole document
and it is possible to process created forms fully automatically using
the SDAPS main program. Features include: PDF Form generation Advanced
array-like layout Can flow over multiple pages and repeats the header
automatically Optional document wide alignment of array environments Has
complex layout features like rotating the headers to safe space Ability
to exchange rows and columns on the fly Different question types:
Freeform text Single/multiple choice questions Range questions Layouting
questions in rows or columns Possibility to pre-fill questionnaires from
LaTeX

