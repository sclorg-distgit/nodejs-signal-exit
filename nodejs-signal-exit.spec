%{?scl:%scl_package nodejs-signal-exit}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename signal-exit
%global enable_tests 0
# tests disabled in order to bootstrap newer npm(tap)

Name:		%{?scl_prefix}nodejs-signal-exit
Version:	3.0.0
Release:	2%{?dist}
Summary:	When you want to fire an event no matter how a process exits

License:	ISC
URL:		https://github.com/bcoe/signal-exit.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
When you want to fire an event no matter how a process exits.

%prep
%setup -q -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#%{_bindir}/tap --timeout=240 ./test/*.js
#%else
#%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-2
- Built for RHSCL

* Wed Jul 13 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.0-1
- Update to upstream 3.0.0 release

* Tue Oct 27 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.2-1
- Initial packaging
- Disable tests until we can bootstrap a newer npm(tap)
