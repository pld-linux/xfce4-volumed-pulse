Summary:	Volume management daemon for XFCE
Summary(pl.UTF-8):	Demon poziomu dźwięku XFCE
Name:		xfce4-volumed-pulse
Version:	0.2.5
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://archive.xfce.org/src/apps/xfce4-volumed-pulse/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	28f99564069c6a4ee6c37c957d69a4ad
URL:		https://launchpad.net/xfce4-volumed-pulse
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	keybinder3-devel >= 0.2.0
BuildRequires:	libnotify-devel >= 0.1.3
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel >= 0.9.19
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfconf-devel >= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This daemon is responsible of making the volume up/down and mute keys
of the keyboard work automatically, and uses the XFCE mixer's defined
card and track for chosing which track to act on. It also provides
volume change / mute toggle notifications.

%description -l pl.UTF-8
Ten demon zapewnia automatyczne działanie klawiszy głośności na
klawiaturze przy użyciu miksera XFCE. Udostępnia również
powiadomienia.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/xfce4-volumed-pulse
/etc/xdg/autostart/xfce4-volumed-pulse.desktop
