#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prompt_toolkit
Version  : 2.0.9
Release  : 35
URL      : https://files.pythonhosted.org/packages/94/a0/57dc47115621d9b3fcc589848cdbcbb6c4c130186e8fc4c4704766a7a699/prompt_toolkit-2.0.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/a0/57dc47115621d9b3fcc589848cdbcbb6c4c130186e8fc4c4704766a7a699/prompt_toolkit-2.0.9.tar.gz
Summary  : Library for building powerful interactive command lines in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: prompt_toolkit-license = %{version}-%{release}
Requires: prompt_toolkit-python = %{version}-%{release}
Requires: prompt_toolkit-python3 = %{version}-%{release}
Requires: Pygments
Requires: six
Requires: wcwidth
BuildRequires : Pygments
BuildRequires : buildreq-distutils3
BuildRequires : six
BuildRequires : wcwidth

%description
=====================
        
        |Build Status|  |AppVeyor|  |PyPI|  |RTD|  |License|  |Codecov|

%package license
Summary: license components for the prompt_toolkit package.
Group: Default

%description license
license components for the prompt_toolkit package.


%package python
Summary: python components for the prompt_toolkit package.
Group: Default
Requires: prompt_toolkit-python3 = %{version}-%{release}

%description python
python components for the prompt_toolkit package.


%package python3
Summary: python3 components for the prompt_toolkit package.
Group: Default
Requires: python3-core

%description python3
python3 components for the prompt_toolkit package.


%prep
%setup -q -n prompt_toolkit-2.0.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550703172
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/prompt_toolkit
cp LICENSE %{buildroot}/usr/share/package-licenses/prompt_toolkit/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/prompt_toolkit/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
