%define module  XML-DBMS
%define name    perl-%{module}
%define version 1.03
%define release %mkrel 15

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        XML-DBMS perl module
License:        Public Domain
Group:          Development/Perl
URL:            http://www.rpbourret.com/xmldbms/index.htm
Source0:        ftp://ftp.rpbourret.com/perl-xml-dbms-%{version}.tar.bz2
Requires:       perl-libxml-perl
Requires:       perl-XML-LibXML
Requires:       perl-TimeDate
BuildRequires:  perl-devel >= 5.6
BuildRequires:  perl-libxml-perl
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Common)
BuildRequires:  perl-TimeDate
BuildRequires:  perl(DBI)
BuildArch:      noarch

%description
XML-DBMS is middleware for transferring data between XML documents and
relational databases. It maps the XML document to the database according
to an object-relational mapping in which element types are generally
viewed as classes and attributes and PCDATA as properties of those
classes. An XML-based mapping language allows the user to specify
customize this mapping.

%prep
%setup -q -n %{module}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf samples/CVS

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README samples xmldbms.dtd
%{perl_vendorlib}/XML

