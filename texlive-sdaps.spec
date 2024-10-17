Name:		texlive-sdaps
Version:	65345
Release:	1
Summary:	LaTeX support files for SDAPS
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sdaps
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdaps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdaps.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdaps.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains LaTeX classes and packages to create
machine readable questionnaires. Metadata is generated for the
whole document and it is possible to process created forms
fully automatically using the SDAPS main program. Features
include: PDF Form generation Advanced array like layouting Can
flow over multiple pages and repeats the header automatically
Optional document wide alignment of array environments Has
complex layout features like rotating the headers to safe space
Ability to exchange rows and columns on the fly Different
question types: Freeform text Single/multiple choice questions
Range questions Layouting questions in rows or columns
Possibility to pre-fill questionnaires from LaTeX

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/sdaps
%{_texmfdistdir}/tex/latex/sdaps
%doc %{_texmfdistdir}/doc/latex/sdaps

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
