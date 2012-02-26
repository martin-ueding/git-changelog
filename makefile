# Copyright (c) 2011-2012 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                  Variables                                  #
###############################################################################

version := 1.3

###############################################################################
#                               Public Targets                                #
###############################################################################

all: doc/git-changelog.1 CHANGELOG

tarball:
	git archive --prefix=git-changelog-$(version)/ HEAD | gzip > git-changelog_$(version).tar.gz

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.orig
	$(RM) *.pyc
	$(RM) -r build
	$(RM) -r dist
	$(RM) -r html
	$(RM) CHANGELOG
	$(RM) doc/git-changelog.1

###############################################################################
#                               Private Targets                               #
###############################################################################

CHANGELOG:
	git changelog > $@

%.1: %.1.rst
	rst2man $< $@
