Summary:	Extends operations of tabbed browsing
Summary(pl.UTF-8):	Rozszerzenie możliwości przeglądania w panelach
%define		_realname	tabextensions
Name:		mozilla-addon-%{_realname}
Version:	1.13.2005011702
Release:	1
License:	none
Group:		X11/Applications/Networking
Source0:	http://white.sakura.ne.jp/~piro/xul/xpi/%{_realname}_en.xpi
# Source0-md5:	cc2a395362b7db688d2cf12b70fc9b55
Source1:	%{_realname}_1.12.2005010801_pl.xpi
# Source1-md5:	dd8eee574ab7317189726728b5c39f8e
Source2:	%{_realname}-installed-chrome.txt
URL:		http://white.sakura.ne.jp/~piro/xul/_tabextensions.en.html
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
Obsoletes:	mozilla-addon-tabbrowser
Conflicts:	mozilla-addon-multizilla
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
This is an extension for extending operations of tabbed browsing,
e.g., tabs become re-ordable by drag and drop.

%description -l pl.UTF-8
Rozszerzenie tabbrowser jest dodatkiem usprawniającym korzystanie z
paneli w przeglądarce.

%prep
%setup -q -c -T

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
