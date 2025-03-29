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

# https://github.com/sailfishos/gecko-dev/blob/master/rpm/xulrunner-qt5.spec#L263-L271
# (adapted to use across phases)
%ifarch %arm32
%global SB2_TARGET armv7-unknown-linux-gnueabihf
%endif
%ifarch %arm64
%global SB2_TARGET aarch64-unknown-linux-gnu
%endif
%ifarch %ix86
%global SB2_TARGET i686-unknown-linux-gnu
%endif


%build

%include rpm/rust_env.inc

# -j 1: https://forum.sailfishos.org/t/rust-howto-request/3187/52
# dropped for now, but might have to be restored if this is still a problem
cargo build \
  --verbose \
  --release \
  --manifest-path %{_sourcedir}/../Cargo.toml


%install

# Install executable
install -D \
  %{_sourcedir}/../target/%{SB2_TARGET}/release/%{ProjectName} \
  %{buildroot}%{_bindir}/%{ProjectName}

# Desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
   %{name}.desktop

# Translation files
install -d %{buildroot}%{_datadir}/%{ProjectName}/translations
for filename in %{_sourcedir}/../translations/*.ts; do
    base=$(basename -s .ts $filename)
    lrelease \
        -idbased "%{_sourcedir}/../translations/$base.ts" \
        -qm "%{buildroot}%{_datadir}/%{ProjectName}/translations/$base.qm";
done

# Application icons
for RES in 86x86 108x108 128x128 172x172; do
    install -Dm 644 \
        icons/${RES}/%{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${RES}/apps/%{name}.png
done

# QML files
find ./qml -type f -exec \
    install -Dm 644 "{}" "%{buildroot}%{_datadir}/%{name}/{}" \;


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
