%define major 3
%define libname %mklibname tsm %{major}
%define develname %mklibname tsm -d

Summary:	Terminal-emulator State Machine
Name:		libtsm
Version:	3
Release:	16
Epoch:		1
Group:		System/Libraries
License:	MIT
Url:		http://www.freedesktop.org/wiki/Software/kmscon
Source0:	http://www.freedesktop.org/software/kmscon/releases/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(xkbcommon)

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators.
It tries to support all common standards while keeping compatibility 
to existing emulators like xterm, gnome-terminal, konsole.

%package -n %{libname}
Summary:	Terminal-emulator State Machine
Group:		System/Libraries
Obsoletes:	%{mklibname tsm 1} = 7-2

%description -n %{libname}
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators.
It tries to support all common standards while keeping compatibility 
to existing emulators like xterm, gnome-terminal, konsole.

%package -n %{develname}
Summary:	Headers and development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{mklibname tsm -d} = 7-2

%description -n %{develname}
Headers and development files for %{name}.

%prep
%autosetup -p1

%build
%configure \
		--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libtsm.so.%{major}*

%files -n %{develname}
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/libtsm.pc

