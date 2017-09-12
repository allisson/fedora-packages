Name:           evopop-icon-theme
Version:        0.11
Release:        1%{?dist}
Summary:        Icon theme with some inspiration from Google Material Design

License:        CC-BY
URL:            https://github.com/solus-cold-storage/evopop-icon-theme
Source0:        https://github.com/solus-cold-storage/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  automake
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme  

%description
A simple icon theme with some inspiration from Google Material Design.


%prep
%autosetup


%build
# remove shebangs
chmod 0644 CREDITS README.md LICENSE
find EvoPop -type f | xargs chmod 0644
sh autogen.sh
%make_build


%install
%make_install


%post
/bin/touch --no-create %{_datadir}/icons/EvoPop &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/EvoPop &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/EvoPop &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/EvoPop &>/dev/null || :


%files
%license LICENSE
%doc CREDITS README.md
%{_datadir}/icons/EvoPop


%changelog
* Mon Sep 11 2017 Allisson Azevedo <allisson@gmail.com> - 0.11-1
- Initial RPM release
