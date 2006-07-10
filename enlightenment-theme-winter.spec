%define	_theme	winter
Summary:	This is the Winter theme for E17
Summary(pl):	Motyw Winter dla E17
Name:		enlightenment-theme-%{_theme}
Version:	2006.07.02
Release:	1
License:	Creative Commons
Group:		Themes
Source0:	http://www.rephorm.com/files/winter/%{_theme}-e17.edj
# Source0-md5:	54aca01ef02cab2888c703fb2aea67cc
URL:		http://www.rephorm.com/files/winter/
Requires:	enlightenmentDR17
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Winter theme is the default theme for Enlightenment DR16.7. This is
the Winter theme for E17.

%description -l pl
Motyw Winter to domy¶lny motyw dla Enlightenmenta DR16.7. Ten pakiet
zawiera motyw Winter dla E17.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenmentDR17/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenmentDR17/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenmentDR17/data/themes/%{_theme}.edj
