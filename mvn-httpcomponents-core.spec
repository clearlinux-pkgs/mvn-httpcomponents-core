#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-httpcomponents-core
Version  : 4.0.1
Release  : 9
URL      : https://github.com/apache/httpcomponents-core/archive/4.0.1.tar.gz
Source0  : https://github.com/apache/httpcomponents-core/archive/4.0.1.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom
Source2  : https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.4.10/httpcomponents-core-4.4.10.pom
Source3  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom
Source4  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.2.1/httpcomponents-core-4.2.1.pom
Source5  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.2.2/httpcomponents-core-4.2.2.pom
Source6  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.3.2/httpcomponents-core-4.3.2.pom
Source7  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.4.4/httpcomponents-core-4.4.4.pom
Source8  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.4.5/httpcomponents-core-4.4.5.pom
Source9  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.jar
Source10  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.pom
Source11  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.jar
Source12  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.pom
Source13  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.2.2/httpcore-4.2.2.jar
Source14  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.2.2/httpcore-4.2.2.pom
Source15  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar
Source16  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.pom
Source17  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.jar
Source18  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.pom
Source19  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.4/httpcore-4.4.4.jar
Source20  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.4/httpcore-4.4.4.pom
Source21  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/4.0/project-4.0.pom
Source22  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/4.1/project-4.1.pom
Source23  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/6/project-6.pom
Source24  : https://repo1.maven.org/maven2/org/apache/httpcomponents/project/7/project-7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-httpcomponents-core-data = %{version}-%{release}
Requires: mvn-httpcomponents-core-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
Apache HttpComponents Core
==========================
Welcome to the HttpCore component of the Apache HttpComponents project.

%package data
Summary: data components for the mvn-httpcomponents-core package.
Group: Data

%description data
data components for the mvn-httpcomponents-core package.


%package license
Summary: license components for the mvn-httpcomponents-core package.
Group: Default

%description license
license components for the mvn-httpcomponents-core package.


%prep
%setup -q -n httpcomponents-core-4.0.1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-httpcomponents-core
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-httpcomponents-core/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.10/httpcomponents-core-4.4.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.2.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.2.1/httpcomponents-core-4.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.2.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.2.2/httpcomponents-core-4.2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.3.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.3.2/httpcomponents-core-4.3.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.4/httpcomponents-core-4.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.5/httpcomponents-core-4.4.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.2
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.2/httpcore-4.2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.2
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.2/httpcore-4.2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.4
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.4/httpcore-4.4.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.4
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.4/httpcore-4.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.0
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.0/project-4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.1
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.1/project-4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/6
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/6/project-6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7/project-7.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.0.1/httpcomponents-core-4.0.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.2.1/httpcomponents-core-4.2.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.2.2/httpcomponents-core-4.2.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.3.2/httpcomponents-core-4.3.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.10/httpcomponents-core-4.4.10.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.4/httpcomponents-core-4.4.4.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-core/4.4.5/httpcomponents-core-4.4.5.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.0.1/httpcore-4.0.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.2/httpcore-4.2.2.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.2.2/httpcore-4.2.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.10/httpcore-4.4.10.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.4/httpcore-4.4.4.jar
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcore/4.4.4/httpcore-4.4.4.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.0/project-4.0.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/4.1/project-4.1.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/6/project-6.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7/project-7.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-httpcomponents-core/LICENSE.txt
