%global appname axolotl-curve25519

%global commit0 e4a9c4de0eae27223200579c58d1f8f6d20637e2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20150217

%global appsum Python wrapper for curve25519 library with ed25519 signatures
%global appdesc This is Python wrapper for curve25519 library with ed25519 signatures.

Name: python-%{appname}
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}
Summary: %{appsum}

License: GPLv3+
URL: https://github.com/tgalal/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel
BuildRequires: gcc

BuildRequires: python2dist(crypto)
BuildRequires: python3dist(crypto)

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
%autosetup -n %{name}-%{commit0} -p1

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
