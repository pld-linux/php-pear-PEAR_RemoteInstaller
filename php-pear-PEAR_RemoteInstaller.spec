%define		_status		alpha
%define		_pearname	PEAR_RemoteInstaller
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - PEAR Remote installation plugin through FTP
Summary(pl.UTF-8):	%{_pearname} - wtyczka do zdalnej instalacji PEAR poprzez FTP
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	27a510eae4ce30bd7e35cd81e72a5613
URL:		http://pear.php.net/package/PEAR_RemoteInstaller/
BuildRequires:	php-pear-PEAR >= 1:1.5.0-0.RC1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	php(ssh2)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Początkowo część instalatora PEAR 1.4.0, zdalna instalacja przy użyciu
FTP, FTPS lub SFTP jest teraz w osobnym pakiecie. Pakiet ten dostarcza
polecenia "remote-install", "remote-upgrade", "remote-uinnstall" oraz
"remote-upgrade-all" do głównej części PEAR.

Aby skorzystać z tej funkcjonalności, konieczne jest posiadanie pliku
konfiguracyjnego na zdalnym serwerze oraz możliwość tworzenia i
usuwania na nim plików. Polecenie "config-create" może być użyte, aby
rozpocząć, a w zmiennej remote_config powinna znajdować się pełna
ścieżka (URL), np:
- ftp://ftp.example.com/path/to/pear.ini,
- ftps://user:pass@ftp.example.com/path/to/pear.ini,
- ssh2.sftp://user:pass@ftp.example.com/path/to/pear.ini"

Gdy to będzie zrobione, możliwa jest instalacja/aktualizacja przy
użyciu poleceń remote* tak jakby operacje przeprowadzane były na
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
