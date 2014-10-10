%define upstream_name    MooseX-SemiAffordanceAccessor
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Names accessors in a semi-affordance style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module does not provide any methods. Simply loading it changes the
default naming policy for the loading class so that accessors are separated
into get and set methods. The get methods have the same name as the
accessor, while set methods are prefixed with "set_".

If you define an attribute with a leading underscore, then the set method
will start with "_set_".

If you explicitly set a "reader" or "writer" name when creating an
attribute, then that attribute's naming scheme is left unchanged.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 657454
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 643410
- update to new version 0.09

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 561039
- update to 0.08

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 553963
- update to 0.07

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 396751
- forgot to commit new source tarball
- update to 0.05

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 394961
- update to 0.04

* Wed Jun 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 384756
- import perl-MooseX-SemiAffordanceAccessor


* Wed Jun 10 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist

