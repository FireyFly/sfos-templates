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

%description
%{Description}


%prep
%setup -q -n %{name}-%{version}


%build
%qmake5

%include rpm/rust_build.inc


%make_build


%install
%qmake5_install

%ifarch %arm
targetdir=%{_sourcedir}/../target/armv7-unknown-linux-gnueabihf/release/
%endif
%ifarch aarch64
targetdir=%{_sourcedir}/../target/aarch64-unknown-linux-gnu/release/
%endif
%ifarch %ix86
targetdir=%{_sourcedir}/../target/i686-unknown-linux-gnu/release/
%endif

install -d %{buildroot}%{_datadir}/%{ProjectName}/translations
for filename in %{_sourcedir}/../translations/*.ts; do
    base=$(basename -s .ts $filename)
    lrelease \
        -idbased "%{_sourcedir}/../translations/$base.ts" \
        -qm "%{buildroot}%{_datadir}/%{ProjectName}/translations/$base.qm";
done

install -D $targetdir/%{ProjectName} %{buildroot}%{_bindir}/%{ProjectName}

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
