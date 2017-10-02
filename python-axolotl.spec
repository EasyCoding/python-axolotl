%global appname axolotl

%global appsum Python port of libaxolotl
%global appdesc This is a Python port of libsignal-protocol-java originally written by Moxie Marlinspike

Name: python-%{appname}
Version: 0.1.39
Release: 1%{?dist}
Summary: %{appsum}

License: GPLv3+
URL: https://github.com/tgalal/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel

BuildRequires: python2dist(crypto)
BuildRequires: python3dist(crypto)
BuildRequires: python2dist(axolotl-curve25519)
BuildRequires: python3dist(axolotl-curve25519)
BuildRequires: python2dist(protobuf)
BuildRequires: python3dist(protobuf)

%description
%{appdesc}.

%package -n python2-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python2-%{appname}}

%description -n python2-%{appname}
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{appname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python3-%{appname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Mon Oct 02 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.39-1
- Initial SPEC release.
