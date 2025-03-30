Name:       %{ProjectName}

Summary:    %{Summary}
Version:    %{Version}
Release:    1
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
BuildRequires:  rust >= 1.52.1+git1-1
BuildRequires:  cargo >= 1.52.1+git1-1
BuildRequires:  rust-std-static

%{load:%{_sourcedir}/macros.share}
%{load:%{_sourcedir}/macros.rust}

%description
%{Description}


%prep
%setup -q -n %{name}-%{version}


%build

%rust_env
%rust_build


%install

%rust_install

%install_desktop %{name}.desktop
%install_data_dir qml
%install_app_icons
%install_translations


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
