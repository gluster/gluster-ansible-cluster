%global docdir %{_datadir}/doc/gluster.cluster
%global rolesdir %{_sysconfdir}/ansible/roles/gluster.cluster
%global buildnum 1

Name:      gluster-ansible-cluster
Version:   1.0.0
Release:   1%{?dist}
Summary:   Ansible roles for GlusterFS volume management

URL:       https://github.com/gluster/gluster-ansible-cluster
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible >= 2.6

%description
Collection of Ansible roles for the creating and managing GlusterFS volumes.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{docdir}
mkdir -p %{buildroot}/%{rolesdir}

install -p -m 644 README.md %{buildroot}/%{docdir}
cp -r examples %{buildroot}/%{docdir}/
cp -dpr defaults handlers meta roles tasks tests LICENSE vars \
   %{buildroot}/%{rolesdir}

%files
%doc %{docdir}/README.md
%doc %{docdir}/examples
%rolesdir

%license LICENSE

%changelog
* Thu Feb 21 2019 Sachidananda Urs <sac@redhat.com> 1.0.0-1
- Bump the version to 1

* Thu Jan 03 2019 Sachidananda Urs <sac@redhat.com> 0.2
- Start glusterd if not already started and enable it

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release, volume creation and set options
