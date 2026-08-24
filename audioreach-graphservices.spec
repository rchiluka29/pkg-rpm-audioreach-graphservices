%global debug_package %{nil}

Name:           audioreach-graphservices
Version:        1.0.0
Release:        1%{?dist}
Summary:        AudioReach graph service libraries
License:        BSD-3-Clause
URL:            https://github.com/Audioreach/audioreach-graphservices
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkg-config
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  audioreach-kernel-headers

%description
Provides cross-platform libraries for managing audio graphs
in the AudioReach framework, including setup, control,
data exchange, and calibration handling.

%package        devel
Summary:        AudioReach graphservices - development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
AudioReach graph service libraries — development files.
Provides cross-platform libraries for managing audio graphs
in the AudioReach framework, including setup, control,
data exchange, and calibration handling.

This package contains library headers and pkg-config files for the shared
libraries shipped in the audioreach-graphservices package.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -fi
%configure \
    --with-glib \
    --without-cutils \
    --with-syslog \
    --with-dummy_diag \
    --without-qcom \
    --without-audio_dma_support \
    --without-ats_transport_tcp_ip \
    --without-ats_data_logging \
    --with-msm-audio-ion-disable
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_bindir}/ats_gateway

%files
%license LICENSE
%{_libdir}/*.so.*
%{_libdir}/*.so

%files devel
%{_includedir}/*.h
%{_includedir}/*/*.h
%{_includedir}/*/*/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jul 09 2026 Qualcomm Linux <quic_linux@quicinc.com> - 1.0.0-1
- Initial RPM packaging of audioreach-graphservices version 1.0.0
