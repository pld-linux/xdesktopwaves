Summary:	Simulation of water waves on the X Window desktop
Summary(pl):	Symulacja fali wodnych na pulpicie X Window
Name:		xdesktopwaves
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://dl.sf.net/xdesktopwaves/%{name}-%{version}.tar.gz
# Source0-md5:	a4760fd21010fe292682d8680d4ff083
URL:		http://xdesktopwaves.sourceforge.net/
ExcludeArch:	amd64
BuildRequires:	X11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdesktopwaves is a cellular automata setting the background of your X
Window desktop under water. Windows and mouse are like ships on the
sea. Each movement of these ends up in moving water waves. You can
even have rain and/or storm stirring up the water.

%description -l pl
xdesktopwaves to automat komórkowy sprawiaj±cy, ¿e pulpit X Window
znajduje siê pod wod±. Okna i mysz s± jak statki na morzu. Ka¿dy ich
ruch powoduje powstanie fal. Mo¿na te¿ w³±czyæ deszcz i/lub sztorm
burz±cy powierzchniê wody.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LINK="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LFLAGS="%{rpmldflags} -L%{_prefix}/X11R6/%{_lib}" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xdesktopwaves	$RPM_BUILD_ROOT%{_bindir}
install xdesktopwaves.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
