#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

from distutils.core import setup

setup(
    author = "Martin Ueding",
    author_email = "<dev@martin-ueding.de>",
    description = "Parses annotated tags in a git repository.",
    license = "GPL2+",
    name = "gitchangelog",
    py_modules = ["gitchangelog"],
    scripts = ["git-changelog"],
    version = "1.6.1",
)
