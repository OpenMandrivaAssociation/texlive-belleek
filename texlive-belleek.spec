Name:		texlive-belleek
Version:	20081130
Release:	1
Summary:	Free replacement for basic MathTime fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/belleek/belleek.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/belleek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/belleek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/belleek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package replaces the original MathTime fonts, not
MathTime-Plus or MathTime Professional (the last being the only
currently available commercial bundle).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/belleek/belleek.map
%{_texmfdistdir}/fonts/truetype/public/belleek/blex.ttf
%{_texmfdistdir}/fonts/truetype/public/belleek/blsy.ttf
%{_texmfdistdir}/fonts/truetype/public/belleek/rblmi.ttf
%{_texmfdistdir}/fonts/type1/public/belleek/blex.pfb
%{_texmfdistdir}/fonts/type1/public/belleek/blsy.pfb
%{_texmfdistdir}/fonts/type1/public/belleek/rblmi.pfb
%doc %{_texmfdistdir}/doc/fonts/belleek/README
#- source
%doc %{_texmfdistdir}/source/latex/belleek/my1mtt.fd
%doc %{_texmfdistdir}/source/latex/belleek/my2mtt.fd
%doc %{_texmfdistdir}/source/latex/belleek/my3mtt.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
