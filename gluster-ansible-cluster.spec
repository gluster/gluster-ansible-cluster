%global docdir %{_datadir}/doc/gluster.cluster
%global rolesdir %{_sysconfdir}/ansible/roles/gluster.cluster
%global buildnum 5

Name:      gluster-ansible-cluster
Version:   1.0
Release:   %{buildnum}%{?dist}
Summary:   Ansible roles for GlusterFS volume management

URL:       https://github.com/gluster/gluster-ansible-cluster
Source0:   %{url}/archive/v%{version}-%{buildnum}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12

%description
Collection of Ansible roles for the creating and managing GlusterFS volumes.

%prep
%setup -q -n %{name}-%{version}-%{buildnum}

%build

%install
mkdir -p %{buildroot}/%{docdir}
install -p -m 644 README.md %{buildroot}/%{docdir}
cp -r examples %{buildroot}/%{docdir}/

mkdir -p %{buildroot}/%{rolesdir}
cp -dpr defaults handlers meta roles tasks tests LICENSE vars \
   %{buildroot}/%{rolesdir}

%files
%doc %{docdir}
%rolesdir

%license LICENSE

%changelog
* Thu May 05 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0-5
- Rebase on v1.0-5

* Fri Apr 01 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0-4
- Rebase on v1.0-4

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release, volume creation and set options
