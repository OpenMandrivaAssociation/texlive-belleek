# revision 18651
# category Package
# catalog-ctan /fonts/belleek/belleek.zip
# catalog-date 2008-11-30 15:59:19 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-belleek
Version:	20081130
Release:	10
Summary:	Free replacement for basic MathTime fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/belleek/belleek.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/belleek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/belleek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/belleek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package replaces the original MathTime fonts, not
MathTime-Plus or MathTime Professional (the last being the only
currently available commercial bundle).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081130-2
+ Revision: 749564
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081130-1
+ Revision: 717905
- texlive-belleek
- texlive-belleek
- texlive-belleek
- texlive-belleek
- texlive-belleek

