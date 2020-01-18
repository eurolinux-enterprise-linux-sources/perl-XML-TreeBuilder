Summary:	Parser that builds a tree of XML::Element objects
Name:		perl-XML-TreeBuilder
Version:	4.2
Release:	1%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/XML-TreeBuilder/
Source:		http://www.cpan.org/modules/by-authors/id/J/JF/JFEARN/XML-TreeBuilder-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Devel::Cover)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:	perl(HTML::Element) >= 4.1
BuildRequires:	perl(HTML::Tagset)
BuildRequires:	perl(XML::Parser)
Requires:	perl(HTML::Element) >= 4.1 perl(HTML::Tagset) perl(XML::Parser)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
perl-XML-TreeBuilder is a Perl module that implements a parser
that builds a tree of XML::Element objects.

%prep
%setup -q -n XML-TreeBuilder-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

### Clean up buildroot
find $RPM_BUILD_ROOT -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc Changes README
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/XML/

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.2-1
- Mass rebuild 2013-12-27

* Mon Jul 15 2013 Jeff Fearn <jfearn@redhat.com> 4.2-0
- New upstream with CDATA support.

* Wed Aug 15 2012 Daniel Mach <dmach@redhat.com> - 4.0-8.1
- Rebuild for perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 4.0-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 4.0-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 4 2011 Rüdiger Landmann <r.landmann@redhat.com> - 4.0-3
- Add Test::More to build requires

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.0-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 02 2010 Jeff Fearn <jfearn@redhat.com> - 4.0-1
- New upstream

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.09-19
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.09-18
- rebuild against perl 5.10.1

* Mon Nov 16 2009 Jeff Fearn <jfearn@redhat.com> - 3.09-17
- Fix Requires

* Tue Sep 29 2009  Jeff Fearn <jfearn@redhat.com> - 3.09-16
- Stupid man! Don't eat entities :(

* Mon Sep 28 2009  Jeff Fearn <jfearn@redhat.com> - 3.09-15
- Always remove NoExpand and ErrorContext from output

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jeff Fearn <jfearn@redhat.com> - 3.09-13
- Remove NoExpand and ErrorContext from output if they aren't set.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 15 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-11
- Add ErrorContext pass through
- Fix crash on Entity declaration. BZ #461557

* Thu May 29 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-10
- Rebuild for docs

* Fri Jan 18 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-9
- Missed one 3.10

* Fri Jan 18 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-8
- Pretend 3.10 never happened

* Thu Jan 17 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-7
- Trimmed Summary

* Fri Jan 11 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-6
- Fixed test
- Fixed Source URL
- Added %%check

* Tue Jan 08 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-5
- Changed Development/Languages to Development/Libraries

* Tue Jan 08 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-4
- Remove %%doc from man files, used glob
- Simplify XML in filelist
- Remove OPTIMIZE setting from make call
- Change buildroot to fedora style
- Remove unused defines

* Mon Jan 07 2008 Jeff Fearn <jfearn@redhat.com> - 3.09-3
- Tidy spec file

* Wed Dec 12 2007 Jeff Fearn <jfearn@redhat.com> - 3.09-2
- Add dist param
- Add NoExpand to allow entities to pass thru un-expanded

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 3.09-1
- Initial package. (using DAR)
