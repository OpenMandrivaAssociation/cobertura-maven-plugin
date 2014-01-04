
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		cobertura-maven-plugin
Version:	2.6
Release:	1.fc20
Summary:	javapackages-bootstrap packages
License:	GPLv3+
Source0:	cobertura-maven-plugin-2.6-1.fc20.noarch.rpm
URL:		https://abf.rosalinux.ru/openmandriva/cobertura-maven-plugin
Summary:	cobertura-maven-plugin bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1.5
Requires:	jpackage-utils
Requires:	mvn(commons-lang:commons-lang)
Requires:	mvn(net.sourceforge.cobertura:cobertura)
Requires:	mvn(net.sourceforge.cobertura:cobertura-runtime)
Requires:	mvn(org.apache.maven.reporting:maven-reporting-api)
Requires:	mvn(org.apache.maven.reporting:maven-reporting-impl)
Requires:	mvn(org.apache.maven.shared:maven-invoker)
Requires:	mvn(org.apache.maven:maven-artifact)
Requires:	mvn(org.apache.maven:maven-core)
Requires:	mvn(org.apache.maven:maven-plugin-api)
Requires:	mvn(org.apache.maven:maven-project)
Requires:	mvn(org.codehaus.plexus:plexus-utils)
Requires:	mvn(urbanophile:java-getopt)
Provides:	cobertura-maven-plugin = 2.6-1.fc20
Provides:	maven-plugin-cobertura = 2.6-1.fc20
Provides:	mvn(org.codehaus.mojo:cobertura-maven-plugin) = 2.6
Obsoletes:	maven-plugin-cobertura < 2.5.2-1

%description
cobertura-maven-plugin bootstrap version.

%files		-n cobertura-maven-plugin
/usr/share/doc/cobertura-maven-plugin
/usr/share/doc/cobertura-maven-plugin/LICENSE
/usr/share/java/cobertura-maven-plugin/cobertura-maven-plugin.jar
/usr/share/maven-effective-poms/JPP.cobertura-maven-plugin-cobertura-maven-plugin.pom
/usr/share/maven-fragments/cobertura-maven-plugin.xml
/usr/share/maven-poms/JPP.cobertura-maven-plugin-cobertura-maven-plugin.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
