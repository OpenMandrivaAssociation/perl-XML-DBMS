%define module  XML-DBMS
%define name    perl-%{module}
%define version 1.03
%define release %mkrel 18

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
BuildRoot:      %{_tmppath}/%{name}-%{version}

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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.03-18mdv2010.0
+ Revision: 430662
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.03-17mdv2009.0
+ Revision: 242197
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-15mdv2008.0
+ Revision: 87082
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-14mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-13mdk
- Fix According to perl Policy
    - BuildRequires

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-12mdk
- Fix BuildRequires

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.03-11mdk 
- remove MANIFEST

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.03-10mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.03-9mdk 
- rebuild

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.03-8mdk
- fixed dir ownership (distlint)
- %%makeinstall_std macro

