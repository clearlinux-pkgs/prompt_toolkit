#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prompt_toolkit
Version  : 1.0.15
Release  : 8
URL      : https://pypi.debian.net/prompt_toolkit/prompt_toolkit-1.0.15.tar.gz
Source0  : https://pypi.debian.net/prompt_toolkit/prompt_toolkit-1.0.15.tar.gz
Summary  : Library for building powerful interactive command lines in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: prompt_toolkit-python
Requires: Pygments
Requires: six
Requires: wcwidth
BuildRequires : Pygments
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : wcwidth

%description
=====================
        
        |Build Status|  |PyPI|
        
        ``prompt_toolkit`` is a library for building powerful interactive command lines
        and terminal applications in Python.
        
        Read the `documentation on readthedocs

%package python
Summary: python components for the prompt_toolkit package.
Group: Default

%description python
python components for the prompt_toolkit package.


%prep
%setup -q -n prompt_toolkit-1.0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505403803
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
