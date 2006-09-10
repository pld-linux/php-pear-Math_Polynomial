%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Polynomial
%define		_status		beta
%define		_pearname	Math_Polynomial

Summary:	%{_pearname} - Package to represent and manipulate Polynomial equations
Summary(pl):	%{_pearname} - Pakiet do wy¶wietlania oraz obróbki równañ wielomianowych
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	21bc1af0141743e5aa3d6683b1cf40b0
URL:		http://pear.php.net/package/Math_Polynomial/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class Math_Polynomial represents Polynomial equations built from
strings or from other Polynomial objects and offers some basic
information about each Polynomial equation.

The Math_PolynomialOp class defines operations on Math_Polynomial
objects such as add, multiply, divide, etc.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa Math_Polynomial przedstawia równania wielomianowe stworzone z
³añcuchów znaków lub z innych obiektów klasy Math_Polynomial oraz
umo¿liwia wy¶wietlenie pewnych podstawowych informacji na temat
ka¿dego równania.

Klasa Math_PolynomialOp definiuje operacje takie jak dodawanie,
mno¿enie czy dzielenie na obiektach klasy Math_Polynomial.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Polynomial.php
%{php_pear_dir}/Math/PolynomialOp.php
%{php_pear_dir}/Math/doc/Polynomial_examples.php
%dir %{php_pear_dir}/Math/Polynomial
%{php_pear_dir}/Math/Polynomial/PolynomialTerm.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/Math/test/PolynomialTest.php
