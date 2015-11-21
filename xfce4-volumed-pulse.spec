Summary:	Volume management daemon for XFCE
Summary(pl.UTF-8):	Demon poziomu dźwięku XFCE
Name:		xfce4-volumed-pulse
Version:	0.2.0
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://launchpadlibrarian.net/133628016/%{name}-%{version}.tar.bz2
# Source0-md5:	e70d8a2b2c6e36bf28bda47927e3756e
URL:		https://launchpad.net/xfce4-volumed-pulse
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	gtk+2-devel >= 2:2.20
BuildRequires:	pulseaudio-devel >= 0.9.19
BuildRequires:	keybinder-devel >= 0.2.2
BuildRequires:	libnotify-devel >= 0.1.3
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfconf-devel >= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This daemon is responsible of making the volume up/down and mute
keys of the keyboard work automatically, and uses the XFCE mixer's
defined card and track for chosing which track to act on.
It also provides volume change / mute toggle notifications.

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
