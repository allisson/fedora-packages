Name:           evopop-gtk-theme
Version:        2.1.3
Release:        1%{?dist}
Summary:        Modern Desktop Theme Suite

License:        CC-BY-SA and GPLv3
URL:            https://github.com/solus-project/evopop-gtk-theme
Source0:        https://github.com/solus-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  automake
Requires:       filesystem
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine
   

%description
EvoPop is a modern desktop theme suite. Its design is mostly flat with a 
minimal use of shadows for depth. Requires Gtk 3.20 to function properly. 
The theme is primarily build for the Solus Project, this means I can only 
provide Budgie, Mate and Gnome support.


%prep
%autosetup


%build
# remove shebangs
chmod 0644 AUTHORS
chmod 0644 LICENSE
chmod 0644 README.md
find EvoPop -type f | xargs chmod 0644
sh autogen.sh
%make_build


%install
%make_install


%files
%license LICENSE
%doc AUTHORS README.md
%{_datadir}/themes/EvoPop


%changelog
* Mon Sep 11 2017 Allisson Azevedo <allisson@gmail.com> - 2.1.3-1
- Initial RPM release
