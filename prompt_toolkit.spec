#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prompt_toolkit
Version  : 3.0.2
Release  : 42
URL      : https://files.pythonhosted.org/packages/17/83/cec3653e2c0d7997a4c25f0bf3e6fb32b142eed74d974fa79643a09a5609/prompt_toolkit-3.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/83/cec3653e2c0d7997a4c25f0bf3e6fb32b142eed74d974fa79643a09a5609/prompt_toolkit-3.0.2.tar.gz
Summary  : Library for building powerful interactive command lines in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: prompt_toolkit-license = %{version}-%{release}
Requires: prompt_toolkit-python = %{version}-%{release}
Requires: prompt_toolkit-python3 = %{version}-%{release}
Requires: Pygments
Requires: wcwidth
BuildRequires : Pygments
BuildRequires : buildreq-distutils3
BuildRequires : wcwidth

%description
Python Prompt Toolkit
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
%setup -q -n prompt_toolkit-3.0.2
cd %{_builddir}/prompt_toolkit-3.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575281376
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/prompt_toolkit
cp %{_builddir}/prompt_toolkit-3.0.2/LICENSE %{buildroot}/usr/share/package-licenses/prompt_toolkit/3f9fcc5a3e1595282b9841f8258755e753f26461
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/prompt_toolkit/3f9fcc5a3e1595282b9841f8258755e753f26461

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
