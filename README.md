httpheaders.cgi
===============

A simple CGI script for printing out the HTTP headers sent to a web server. Useful for checking if an ISP is inserting 'supercookies' into HTTP requests (supercookies are injected by adding a HTTP header called `X-UIDH`).

Installation:
-------------

Assuming you have a web server with a `cgi-bin` folder configured and Perl installed with the required modules available (see below), all you have to do is copy `httpheaders.cgi` into the `cgi-bin` folder.

Required Modules:
* [CGI](http://search.cpan.org/perldoc?CGI) 
* [CGI::Carp](http://search.cpan.org/perldoc?CGI%3A%3ACarp)
* [String::Util](http://search.cpan.org/perldoc?String%3A%3AUtil)
* [DateTime](http://search.cpan.org/perldoc?DateTime)
