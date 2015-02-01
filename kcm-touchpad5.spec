%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define date 0

Name: kcm-touchpad5
Summary: Systemsettings module for configuring touchpads
Version: 5.2.0
%if %date
Release: 1.%date.1
# Packaged from git for the time being -- no download URL available
Source0: %{name}-%date.tar.xz
%else
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/kcm-touchpad-%{version}.tar.xz
Release: 1
%endif
URL: http://kde.org/
Group: Graphical desktop/KDE
License: GPLv2
BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5Gui) pkgconfig(Qt5Declarative)
BuildRequires: pkgconfig(Qt5DBus) pkgconfig(xorg-synaptics)
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shape) pkgconfig(xcb-xfixes) pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-util) pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-damage) pkgconfig(xcb-dpms) pkgconfig(xcb-dri2)
BuildRequires: pkgconfig(xcb-dri3) pkgconfig(xcb-glx)
BuildRequires: pkgconfig(xcb-icccm) pkgconfig(xcb-image) pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-present) pkgconfig(xcb-record)
BuildRequires: pkgconfig(xcb-screensaver)
BuildRequires: pkgconfig(xcb-res) pkgconfig(xcb-sync) pkgconfig(xcb-xevie)
BuildRequires: pkgconfig(xcb-xf86dri) pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xinput) pkgconfig(xcb-xprint)
BuildRequires: pkgconfig(xcb-xtest) pkgconfig(xcb-xv) pkgconfig(xcb-xvmc)
BuildRequires: cmake(KF5Completion) cmake(KF5Config) cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons) cmake(KF5DBusAddons) cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5I18n) cmake(KF5XmlGui) cmake(KDED)
BuildRequires: cmake ninja extra-cmake-modules5

%description
Systemsettings module for configuring touchpads

%prep
%setup -qn kcm-touchpad-%{version}
%cmake -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

%files
%{_bindir}/kcm-touchpad-list-devices
%{_libdir}/qt5/plugins/kded_touchpad.so
%{_libdir}/qt5/plugins/plasma_engine_touchpad.so
%{_datadir}/config.kcfg/touchpad.kcfg
%{_datadir}/config.kcfg/touchpaddaemon.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.touchpad.xml
%{_datadir}/icons/hicolor/*/devices/input-touchpad.*
%{_datadir}/knotifications5/kcm_touchpad.notifyrc
%{_datadir}/kservices5/kcm_touchpad.desktop
%{_datadir}/kservices5/kded/touchpad.desktop
%{_datadir}/kservices5/plasma-applet-touchpad.desktop
%{_datadir}/kservices5/plasma-dataengine-touchpad.desktop
%{_datadir}/plasma/desktoptheme/default/icons/touchpad.svg
%{_datadir}/plasma/plasmoids/touchpad/contents/ui/touchpad.qml
%{_datadir}/plasma/plasmoids/touchpad/metadata.desktop
%{_datadir}/plasma/services/touchpad.operations
