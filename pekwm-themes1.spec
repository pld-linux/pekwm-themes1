%define _dname	%(echo %{name} | cut -d- -f1)
Summary:	Pack of themes for pekwm
Summary(pl):	Zestaw motywów dla pekwm
Name:		pekwm-themes1
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	%{name}.tar.bz2
# Source0-md5:	d41d8cd98f00b204e9800998ecf8427e
Buildarch:	noarch
Requires:	pekwm
Obsoletes:	pekwm-themes-pack1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/%{_dname}/themes

%description
Pack of themes for pekwm: 
Blue-Boxish - Hewbert <josh@hewbert.com>
Blue_Glass - Tilman Sauerbeck <tilman@code-monkey.de> 
BrushedApe - Brian Harbron <harbron@uiuc.edu> 
FatalE Port - Hewbert <josh@hewbert.com> 
Glass - cnx glass-cnx - Xumerle Luciano<ciano@medgen.univr.it>
NeXTSTEP -Julian Leyh <oenone@oenone.de>
Olympic - Hewbert <josh@hewbert.com> 
Vath - Hewbert <josh@hewbert.com> 
bluecurve - port of redhat's by leandro@linuxmag.com.br 
bombskew-p - regret <trueregret@yahoo.se> 
control systems - Dustin Massop<dmassop@engr.uvic.ca> 
monochrome - Xyverz www.xyverz.org 
old_unix-2- elk <elk@cowmob.nu> 
panther - A port by Dustin Massop<dmassop@engr.uvic.ca> 
retro - ported from xfce4 by <texray@gmx.de>

%description -l pl
Pck of themes for pekwm:
Blue-Boxish - Hewbert <josh@hewbert.com>
Blue_Glass - Tilman Sauerbeck <tilman@code-monkey.de>
BrushedApe - Brian Harbron <harbron@uiuc.edu>
FatalE Port - Hewbert <josh@hewbert.com>
Glass - cnx glass-cnx - Xumerle Luciano<ciano@medgen.univr.it>
NeXTSTEP -Julian Leyh <oenone@oenone.de>
Olympic - Hewbert <josh@hewbert.com>
Vath - Hewbert <josh@hewbert.com>
bluecurve - port of redhat's by leandro@linuxmag.com.br
bombskew-p - regret <trueregret@yahoo.se>
control systems - Dustin Massop<dmassop@engr.uvic.ca>
monochrome - Xyverz www.xyverz.org
old_unix-2- elk <elk@cowmob.nu>
panther - A port by Dustin Massop<dmassop@engr.uvic.ca>
retro - ported from xfce4 by <texray@gmx.de>

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
