# Copyright (c) 2011-2012 Martin Ueding <dev@martin-ueding.de>

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see http://www.gnu.org/licenses/.

all: doc/git-changelog.1

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
	$(RM) git-changelog*.tar.gz

install:
	install -d "$(DESTDIR)/usr/share/man/man1/"
	gzip --stdout doc/git-changelog.1 > "$(DESTDIR)/usr/share/man/man1/git-changelog.1.gz"
	python setup.py install --root "$(DESTDIR)"

%.1: %.1.rst
	rst2man $< $@
