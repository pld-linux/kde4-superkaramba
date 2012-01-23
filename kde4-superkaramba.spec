%define		_state		stable
%define		orgname		superkaramba
%define		qtver		4.8.0

Summary:	Little interactive widgets on KDE desktop
Summary(pl.UTF-8):	Małe interaktywne widżety na pulpicie KDE
Name:		kde4-superkaramba
Version:	4.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	554c3e5dd470b2428f5792cd72224fdf
URL:		http://www.kde.org/
BuildRequires:	python-devel
BuildRequires:	qimageblitz-devel >= 0.0.6
Obsoletes:	kde4-kdeutils-superkaramba < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuperKaramba is a tool that allows anyone to easily create and run
little interactive widgets on a KDE desktop.

%description -l pl.UTF-8
SuperKaramba to narzędzie pozwalające na łatwe tworzenie i
uruchamianie małych interaktywnych widżetów na pulpicie KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/superkaramba
%attr(755,root,root) %{_libdir}/kde4/plasma_package_superkaramba.so
%attr(755,root,root) %{_libdir}/kde4/plasma_scriptengine_superkaramba.so
%attr(755,root,root) %{_libdir}/libsuperkaramba.so
%attr(755,root,root) %{_libdir}/libsuperkaramba.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsuperkaramba.so.?
%{_desktopdir}/kde4/superkaramba.desktop
%{_datadir}/apps/superkaramba
%{_datadir}/config/superkaramba.knsrc
%{_datadir}/dbus-1/interfaces/org.kde.superkaramba.xml
%{_iconsdir}/hicolor/*x*/apps/superkaramba.png
%{_iconsdir}/hicolor/scalable/apps/superkaramba.svgz
%{_datadir}/kde4/services/plasma-package-superkaramba.desktop
%{_datadir}/kde4/services/plasma-scriptengine-superkaramba.desktop