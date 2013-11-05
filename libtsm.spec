Summary:	Terminal-emulator State Machine
Name:		libtsm
Version:	3
Release:	1
Group:		System/Libraries
License:	MIT
Url:		http://www.freedesktop.org/wiki/Software/kmscon/$pkgname
Source0:	http://www.freedesktop.org/software/kmscon/releases/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(xkbcommon)

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators.
It tries to support all common standards while keeping compatibility 
to existing emulators like xterm, gnome-terminal, konsole,


%prep
%setup -q
%build
%configure2_5x

%make

%install
%makeinstall_std


%files
