Summary:	Atomix-like game of moving marbles in puzzles
Summary(pl.UTF-8):	Gra podobna do Atomiksa, polegająca na przesuwaniu klocków w układankach
Summary(pt_BR.UTF-8):	Jogo tipo Atomix, de mover bolas de gude em labirintos
Name:		lmarbles
Version:	1.0.8
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	2735ef0cbf39ac79194321ff49e02f0e
Patch0:		%{name}-bugfix.patch
URL:		http://lgames.sourceforge.net/LMarbles
BuildRequires:	SDL-devel >= 1.0.0
BuildRequires:	SDL_mixer-devel >= 1.0.0
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
Obsoletes:	marbles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
Marbles is very similiar to Atomix and was heavily inspired by it.
Goal is to create a more or less complex figure out of single marbles
within a time limit to reach the next level.

Sounds easy? Well, there is a problem: If a marble starts to move it
will not stop until it hits a wall or marble. And to make it even more
interesting there are obstacles like arrows, crumbling walls and
teleports!

%description -l pl.UTF-8
Marbles to gra bardzo podobna do Atomiksa, w dużym stopniu nim
inspirowana. Celem jest stworzenie bardziej lub mniej skomplikowanej
figury z pojedynczych klocków w ograniczonym czasie, aby przejść do
następnego poziomu.

Wydaje się łatwe? Hm, jest pewien problem: jeśli klocek zaczyna się
ruszać, nie zatrzymuje się, dopóki nie uderzy w ścianę lub inny
klocek. Aby gra była jeszcze bardziej interesująca, są przeszkody w
rodzaju strzałek, pękających ścian i teleportów!

%description -l pt_BR.UTF-8
O Marbles é muito parecido com o jogo Atomix, pois foi inspirado nele.
O objetivo é criar uma figura de bolas de gude mais ou menos complexa
dentro de um limite de tempo.

Parece fácil? Bem, há um problema: quando uma bolinha de gude começa a
se mover, só pára quando bate em uma parede ou outra bolinha. E para
ficar mais interessante, há alguns obstáculos como caminhos de mão
única, paredes que desmoronam e teletransporte!

%prep
%setup -q
%patch0 -p1

%{__perl} -pi -e 's@^inst_dir="\$datadir/games/lmarbles"@inst_dir="\$datadir/lmarbles"@' \
	configure.in

%{__perl} -pi -e 's@\$\(datadir\)/icons@\$(datadir)/pixmaps@' Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- marbles < 1.0.6
if [ -f /var/games/marbles.prfs.rpmsave ]; then
	mv -f /var/games/marbles.prfs.rpmsave /var/games/lmarbles.prfs
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO src/manual
%attr(2755,root,games) %{_bindir}/lmarbles
%{_datadir}/lmarbles
%{_desktopdir}/lmarbles.desktop
%{_pixmapsdir}/lmarbles48.gif
%{_mandir}/man6/lmarbles.6*
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/%{name}.prfs
