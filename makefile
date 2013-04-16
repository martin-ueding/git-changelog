# Copyright © 2011-2013 Martin Ueding <dev@martin-ueding.de>

all: doc/git-changelog.1

install:
	install -d "$(DESTDIR)/usr/share/man/man1/"
	gzip --stdout doc/git-changelog.1 > "$(DESTDIR)/usr/share/man/man1/git-changelog.1.gz"
	./setup.py install --prefix "$(DESTDIR)/usr" --install-layout deb

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.orig
	$(RM) *.pyc
	$(RM) -r build
	$(RM) -r dist
	$(RM) -r html
	$(RM) -r __pycache__
	$(RM) CHANGELOG
	$(RM) doc/git-changelog.1
	$(RM) git-changelog*.tar.gz

%.1: %.1.rst
	rst2man $< $@
