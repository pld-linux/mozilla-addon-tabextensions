Summary:	Extends operations of tabbed browsing
Summary(pl):	Rozszerzenie mo¿liwo¶ci przegl±dania w panelach
%define		_realname	tabextensions
Name:		mozilla-addon-%{_realname}
Version:	1.10.2004062101
Release:	4
License:	none
Group:		X11/Applications/Networking
Source0:	http://white.sakura.ne.jp/~piro/xul/xpi/%{_realname}_en.xpi
# Source0-md5:	88ff9f5b05b5836bb2320e05e068e955
Source1:	http://www.ee.pw.edu.pl/~misiejuk/mozilla/moje/%{_realname}_pl.xpi
# Source1-md5:	e09614caa9272f86f31e22a0ff231370
Source2:	%{_realname}-installed-chrome.txt
URL:		http://white.sakura.ne.jp/~piro/xul/_tabextensions.en.html
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
Obsoletes:	mozilla-addon-tabbrowser
Conflicts:	mozilla-addon-multizilla
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
This is an extension for extending operations of tabbed browsing,
e.g., tabs become re-ordable by drag and drop.

%description -l pl
Rozszerzenie tabbrowser jest dodatkiem usprawniaj±cym korzystanie z
paneli w przegl±darce.

%prep
%setup -q -T -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip -j %{SOURCE1} chrome/tabextensions.jar
unzip tabextensions.jar locale/pl-PL/*
rm -f tabextensions.jar
unzip -j %{SOURCE0} chrome/tabextensions.jar
unzip tabextensions.jar
rm -f tabextensions.jar
zip -r -9 -m $RPM_BUILD_ROOT%{_chromedir}/tabextensions.jar ./
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
