%global release_version 2.0.7-0

Name:           pop-gtk-theme
Version:        2.0.7.0
Release:        1%{?dist}
Summary:        Version 2 of the Pop GTK+ Theme

License:        GPLv2 
URL:            https://github.com/system76/pop-gtk-theme
Source0:        https://github.com/system76/%{name}/archive/%{release_version}.tar.gz

BuildArch:      noarch
BuildRequires:  sassc
BuildRequires:  glib2-devel
BuildRequires:  gnome-shell
Requires:       filesystem
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine
Requires:       mozilla-fira-sans-fonts
Requires:       mozilla-fira-mono-fonts
Requires:       google-roboto-slab-fonts

%description
An adaptive Gtk+ theme based on the Flat-Plat GTK+ theme.


%prep
%autosetup -n %{name}-%{release_version}


%build
chmod 0644 src/index-compact.theme
chmod 0644 src/index-dark-compact.theme
chmod 0644 src/index-dark.theme
chmod 0644 src/index-light-compact.theme
chmod 0644 src/index-light.theme
chmod 0644 src/index.theme
chmod 0644 src/gtk-2.0/gtkrc-light
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING
%doc README.md
%exclude %{_datadir}/themes/Pop-compact/COPYING
%exclude %{_datadir}/themes/Pop-dark-compact/COPYING
%exclude %{_datadir}/themes/Pop-dark/COPYING
%exclude %{_datadir}/themes/Pop-light-compact/COPYING
%exclude %{_datadir}/themes/Pop-light/COPYING
%exclude %{_datadir}/themes/Pop/COPYING
%{_datadir}/themes/Pop-compact
%{_datadir}/themes/Pop-dark-compact
%{_datadir}/themes/Pop-dark
%{_datadir}/themes/Pop-light-compact
%{_datadir}/themes/Pop-light
%{_datadir}/themes/Pop


%changelog
* Thu Sep  7 2017 Allisson Azevedo <allisson@gmail.com> - 2.0.7.0-1
- Initial RPM release
