Summary:	Atomix-like game of moving marbles in puzzles
Summary(pl):	Gra podobna do Atomiksa, polegaj�ca na przesuwaniu klock�w w uk�adankach
Summary(pt_BR):	Jogo tipo Atomix, de mover bolas de gude em labirintos
Name:		lmarbles
Version:	1.0.6
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	ad162da8fa298cac680e13c02fea258c
Patch0:		%{name}-bugfix.patch
URL:		http://lgames.sourceforge.net/marbles/marbles.html
BuildRequires:	SDL-devel >= 1.0.0
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
Obsoletes:	marbles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marbles is very similiar to Atomix and was heavily inspired by it.
Goal is to create a more or less complex figure out of single marbles
within a time limit to reach the next level.

Sounds easy? Well, there is a problem: If a marble starts to move it
will not stop until it hits a wall or marble. And to make it even more
interesting there are obstacles like arrows, crumbling walls and
teleports!

%description -l pl
Marbles to gra bardzo podobna do Atomiksa, w du�ym stopniu nim
inspirowana. Celem jest stworzenie bardziej lub mniej skomplikowanej
figury z pojedynczych klock�w w ograniczonym czasie, aby przej�� do
nast�pnego poziomu.

Wydaje si� �atwe? Hm, jest pewien problem: je�li klocek zaczyna si�
rusza�, nie zatrzymuje si�, dop�ki nie uderzy w �cian� lub inny
klocek. Aby gra by�a jeszcze bardziej interesuj�ca, s� przeszkody w
rodzaju strza�ek, p�kaj�cych �cian i teleport�w!

%description -l pt_BR
O Marbles � muito parecido com o jogo Atomix, pois foi inspirado nele.
O objetivo � criar uma figura de bolas de gude mais ou menos complexa
dentro de um limite de tempo.

Parece f�cil? Bem, h� um problema: quando uma bolinha de gude come�a a
se mover, s� p�ra quando bate em uma parede ou outra bolinha. E para
ficar mais interessante, h� alguns obst�culos como caminhos de m�o
�nica, paredes que desmoronam e teletransporte!

%prep
%setup -q
%patch0 -p1

%{__perl} -pi -e 's@^inst_dir="\$datadir/games/lmarbles"@inst_dir="\$datadir/lmarbles"@' \
	configure.in

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-profile-path=/var/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/games

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT/var/games/{marbles,lmarbles}.prfs

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- marbles < 1.0.6
if [ -f /var/games/marbles.prfs.rpmsave ]; then
	mv -f /var/games/marbles.prfs.rpmsave /var/games/lmarbles.prfs
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README src/manual
%attr(2755,root,games) %{_bindir}/lmarbles
%{_datadir}/lmarbles
%{_mandir}/man6/*
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/%{name}.prfs
