# Copyright (c) 2011 Martin Ueding <dev@martin-ueding.de>

all: doc/git-changelog.1

%.1: %.1.ronn
	ronn $^

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.pyc
	$(RM) *.orig
