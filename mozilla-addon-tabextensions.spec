Summary:	Extends operations of tabbed browsing
Summary(pl):	Rozszerza mo¿liwo¶ci przegl±dania w panelach
Name:		mozilla-addon-tabbrowser
%define		_realname	tabextensions
Version:	1.10.2004040401
Release:	1
License:	none
Group:		X11/Applications/Networking
Source0:	http://white.sakura.ne.jp/~piro/xul/xpi/%{_realname}_en.xpi
# Source0-md5:	fb5caeea6f1a78dfa1a18b313432558c
Source1:	http://www.ee.pw.edu.pl/~misiejuk/mozilla/%{_realname}_pl.xpi
# Source1-md5:	a19084dc7e60a7def98998e512b47333
Source2:	%{_realname}-installed-chrome.txt
URL:		http://white.sakura.ne.jp/~piro/xul/_tabextensions.en.html
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
Obsoletes:	mozilla-addon-multizilla
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
This is an extension for extending operations of tabbed browsing,
e.g., tabs become re-ordable by drag and drop.

%description -l pl
Tabbrowser Extension jest dodatkiem usprawniaj±cym korzystanie z
paneli w przegl±darce.

%prep
%setup -q -T -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE1} tabextensions.jar
unzip tabextensions.jar locale/pl-PL/*
rm -f tabextensions.jar
unzip %{SOURCE0} tabextensions.jar
unzip tabextensions.jar
rm -f tabextensions.jar
zip -r -9 -m $RPM_BUILD_ROOT%{_chromedir}/tabextensions.jar ./
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
