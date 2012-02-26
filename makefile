# Copyright (c) 2011-2012 Martin Ueding <dev@martin-ueding.de>

version=1.3

all: doc/git-changelog.1 CHANGELOG

CHANGELOG:
	git changelog > $@

tarball:
	git archive --prefix=git-changelog-$(version)/ HEAD | gzip > git-changelog_$(version).tar.gz

%.1: %.1.ronn
	ronn $^ --style=toc --manual=git-changelog

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
	$(RM) doc/git-changelog.1.html
