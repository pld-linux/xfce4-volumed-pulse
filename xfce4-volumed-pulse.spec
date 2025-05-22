Summary:	Volume management daemon for XFCE
Summary(pl.UTF-8):	Demon poziomu dźwięku XFCE
Name:		xfce4-volumed-pulse
Version:	0.3.0
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://archive.xfce.org/src/apps/xfce4-volumed-pulse/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	b9c4388ad911a7d1b251abe52a402e83
URL:		https://launchpad.net/xfce4-volumed-pulse
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	keybinder3-devel >= 0.2.0
BuildRequires:	libnotify-devel >= 0.1.3
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel >= 0.9.19
BuildRequires:	xfce4-dev-tools >= 4.18.0
BuildRequires:	xfconf-devel >= 4.18.0
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/xfce4-volumed-pulse
/etc/xdg/autostart/xfce4-volumed-pulse.desktop
