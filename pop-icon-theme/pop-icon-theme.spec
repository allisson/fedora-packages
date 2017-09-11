%global commitdate 20170831
%global commit0 38ecdfe803becbaf27eeaebe68eacf00bf35e8bb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           pop-icon-theme
Version:        0.1.0
Release:        0.1.%{commitdate}git%{shortcommit0}%{?dist}
Summary:        System76 Pop icon theme for Linux

License:        LGPLv3 and CC-BY-SA
URL:            https://github.com/system76/pop-icon-theme
Source0:        https://github.com/system76/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
BuildRequires:  automake
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme


%description
Pop is a free and open source SVG icon theme for Linux, based on Paper Icon 
Set and Papirus.


%prep
%autosetup -n %{name}-%{commit0}


%build
# do nothing


%install
%make_install


%post
/bin/touch --no-create %{_datadir}/icons/Pop &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Pop &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Pop &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Pop &>/dev/null || :


%files
%license LICENSE.cursors LICENSE.icons
%doc README.md
%{_datadir}/icons/Pop


%changelog
* Wed Sep  6 2017 Allisson Azevedo <allisson@gmail.com> - 0.1.0-0.1.20170831git38ecdfe
- Initial RPM release
