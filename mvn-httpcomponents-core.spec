#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-httpcomponents-core
Version  : 4.0.1
Release  : 4
URL      : https://github.com/apache/httpcomponents-core/archive/4.0.1.tar.gz
Source0  : https://github.com/apache/httpcomponents-core/archive/4.0.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom
Source2  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.3.2/httpcomponents-core-4.3.2.pom
Source3  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.jar
Source4  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.pom
Source5  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar
Source6  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.pom
Source7  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.jar
Source8  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.pom
Source9  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/4.0/project-4.0.pom
Source10  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/4.1/project-4.1.pom
Source11  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/7/project-7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-httpcomponents-core-data = %{version}-%{release}

%description
Apache HttpComponents Core
==========================
Welcome to the HttpCore component of the Apache HttpComponents project.

%package data
Summary: data components for the mvn-httpcomponents-core package.
Group: Data

%description data
data components for the mvn-httpcomponents-core package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.3.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.3.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.3.2/httpcomponents-core-4.3.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.0/project-4.0.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.1/project-4.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7/project-7.pom
