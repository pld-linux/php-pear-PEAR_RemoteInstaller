%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	RemoteInstaller
%define		_status		alpha
%define		_pearname	PEAR_RemoteInstaller

Summary:	%{_pearname} - PEAR Remote installation plugin through FTP
Summary(pl):	%{_pearname} - wtyczka do zdalnej instalacji PEAR poprzez FTP
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	689a05f91c6a292a3a8c0fccf3c95bf8
URL:		http://pear.php.net/package/PEAR_RemoteInstaller/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(ssh2.*)'

%description
Originally part of the 1.4.0 new features, remote installation through
FTP, FTPS and SFTP is now its own package. This package adds the
commands "remote-install" "remote-upgrade" "remote-uninstall" and
"remote-upgrade-all" to the PEAR core.

To take advantage, you must have a config file on the remote ftp
server and full access to the server to create and remove files. The
config-create command can be used to get started, and the
remote_config configuration variable is set to the full URL as in
- ftp://ftp.example.com/path/to/pear.ini,
- ftps://user:pass@ftp.example.com/path/to/pear.ini,
- ssh2.sftp://user:pass@ftp.example.com/path/to/pear.ini"

After this is done, install/upgrade as normal using the remote*
commands as if they were local.

In PEAR status of this package is: %{_status}.

%description -l pl
Pocz±tkowo czê¶æ instalatora PEAR 1.4.0, zdalna instalacja przy u¿yciu
FTP, FTPS lub SFTP jest teraz w osobnym pakiecie. Pakiet ten dostarcza
polecenia "remote-install", "remote-upgrade", "remote-uinnstall" oraz
"remote-upgrade-all" do g³ównej czê¶ci PEAR.

Aby skorzystaæ z tej funkcjonalno¶ci, konieczne jest posiadanie pliku
konfiguracyjnego na zdalnym serwerze oraz mo¿liwo¶æ tworzenia i
usuwania na nim plików. Polecenie "config-create" mo¿e byæ u¿yte, aby
rozpocz±æ, a w zmiennej remote_config powinna znajdowaæ siê pe³na
¶cie¿ka (URL), np:
- ftp://ftp.example.com/path/to/pear.ini,
- ftps://user:pass@ftp.example.com/path/to/pear.ini,
- ssh2.sftp://user:pass@ftp.example.com/path/to/pear.ini"

Gdy to bêdzie zrobione, mo¿liwa jest instalacja/aktualizacja przy
u¿yciu poleceñ remote* tak jakby operacje przeprowadzane by³y na
lokalnym repozytorium.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/Command/Remoteinstall.xml
%{php_pear_dir}/PEAR/Command/Remoteinstall.php
%{php_pear_dir}/PEAR/FTP.php
%{php_pear_dir}/PEAR/RemoteInstaller.php
