Summary:	Simulation of water waves on the X Window System desktop
Summary(pl):	Symulacja fal wodnych na pulpicie X Window System
Name:		xdesktopwaves
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://dl.sourceforge.net/xdesktopwaves/%{name}-%{version}.tar.gz
# Source0-md5:	4ef1233527cb3bbf06b8fdc407b04ebe
URL:		http://xdesktopwaves.sourceforge.net/
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdesktopwaves is a cellular automata setting the background of your X
Window System desktop under water. Windows and mouse are like ships on
the sea. Each movement of these ends up in moving water waves. You can
even have rain and/or storm stirring up the water.

%description -l pl
xdesktopwaves to automat komórkowy sprawiaj±cy, ¿e pulpit X Window
System znajduje siê pod wod±. Okna i mysz s± jak statki na morzu.
Ka¿dy ich ruch powoduje powstanie fal. Mo¿na te¿ w³±czyæ deszcz i/lub
sztorm burz±cy powierzchniê wody.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LINK="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LFLAGS="%{rpmldflags} -L%{_prefix}/X11R6/%{_lib}" \

%{__make} -C xdwapi \
	CC="%{__cc}" \
	LINK="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LFLAGS="%{rpmldflags} -L%{_prefix}/X11R6/%{_lib}" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xdesktopwaves		$RPM_BUILD_ROOT%{_bindir}
install xdwapi/xdwapidemo	$RPM_BUILD_ROOT%{_bindir}
install xdesktopwaves.1		$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xdwapi/README.xdwapi
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
