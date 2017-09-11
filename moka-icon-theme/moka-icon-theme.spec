Name:           moka-icon-theme
Version:        5.3.6
Release:        1%{?dist}
Summary:        Moka Icon Theme

License:        CC-BY-SA and GPLv3
URL:            https://snwh.org/moka
Source0:        https://github.com/snwh/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  automake
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme


%description
Moka is simple and modern icon theme with material design influences.


%prep
%autosetup


%build
sh autogen.sh
%make_build


%install
%make_install


%post
/bin/touch --no-create %{_datadir}/icons/Moka &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Moka &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Moka &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Moka &>/dev/null || :


%files
%license LICENSE LICENSE_GPL AUTHORS COPYING
%attr(644, root, root) %doc README.md
%{_datadir}/icons/Moka


%changelog
* Mon Sep  4 2017 Allisson Azevedo <allisson@gmail.com> - 5.3.6-1
- Initial RPM release
