#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use CGI::Carp;
use String::Util 'trim';
use DateTime;

#==============================================================================#
# HTTP Response Header Printer
#==============================================================================#
#
# This very simple CGI script prints all the HTTP request headers received.
#
# Optionally specific headers can be highlighted by adding them to the 
# @HIGHLIGHT_HEADERS array.
#
# Copyright (c) 2014, Bart Busschots T/A Bartificer Web Solutions All rights
# reserved. This code is released under the BSD License:
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#==============================================================================#

#
# === Define Variables (edit this seciton to tweak behaviour)===================
#

# headers to highlight (array of scalars)
my @HIGHLIGHT_HEADERS = qw(X-UIDH);

#
# === Print The Headers (no need to edit anything below here) ==================
#

my $q = CGI->new;
my %headers = map { $_ => $q->http($_) } $q->http();

print $q->header(-type => 'text/html',
                 -expires => '+1s',
                 -Pragma => 'no-cache'
                 );

print <<'ENDPAGESTART';
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>HTTP Request Headers</title>
</head>
<body>
<h1>HTTP Request Headers Received:</h1>
<p>Below is a sorted list of the HTTP request headers received by this server:</p>
<blockquote>
ENDPAGESTART

foreach my $header (sort keys %headers){
	my $do_highlight = do_highlight($header);
    print '<code>';
    print '<strong style="color:red">' if $do_highlight;
    print "$header: $headers{$header}";
    print '</strong>' if $do_highlight;
    print "</code><br />\n";
}

my $timestamp = DateTime->now()->iso8601();
print <<"ENDPAGEEND";
</blockquote>
<p style="font-style:italic">(Generated at $timestamp)</p>
</body>
</html>
ENDPAGEEND

#
# === Helper Functions =========================================================
#

#####-SUB-######################################################################
# Type       : SUBROUTINE
# Purpose    : Test if a given header needs to be highlighted or not
# Returns    : 1 if the header should be highlighted, 0 otherwise
# Arguments  : 1. the header to test as a scalar
# Throws     : Carps on invalid args, then returns 0
# Notes      :
# See Also   :
sub do_highlight{
	my $header = shift;
	my $cleaned_header = trim(uc $header);
	
	# validate args
	unless(defined $header && ref $header eq q{} && length $header){
		carp((caller 0)[3].'() - invalid args, no (or invalid) header passed');
	}
	
	# check for a case-insensitive match agaise all highlight headers
	foreach my $highlight_header (@HIGHLIGHT_HEADERS){
		if($cleaned_header eq uc $highlight_header){
			return 1;
		}
	}
	
	# if we got here there was no match, so return 0
	return 0;
}
