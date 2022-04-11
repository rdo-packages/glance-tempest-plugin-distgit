%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%global service glance
%global plugin glance-tempest-plugin
%global module glance_tempest_plugin

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests to cover the glance project. \
Additionally it provides a plugin to automatically load these tests \
into Tempest.

Name:       python-%{service}-tests-tempest
Version:    0.3.0
Release:    1%{?dist}
Summary:    Tempest Integration of Glance Project
License:    ASL 2.0
URL:        https://opendev.org/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-pbr >= 2.0.0
Requires:   python3-six >= 1.10.0
Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-oslo-config >= 2:5.1.0
Requires:   python3-oslo-serialization >= 2.18.0

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%changelog
* Mon Apr 11 2022 RDO <dev@lists.rdoproject.org> 0.3.0-1
- Update to 0.3.0

* Thu Oct 14 2021 RDO <dev@lists.rdoproject.org> 0.2.0-1
- Update to 0.2.0

