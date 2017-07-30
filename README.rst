.. Copyright © 2012-2013, 2017 Martin Ueding <dev@martin-ueding.de>

#############
git-changelog
#############

For my Jscribble project, I use git. The human readable changes are stored in
the annotated tags itself. So I have a tag called ``v1.5.3`` which contains the
text that you can read in the changelog.  That way, the information is not
spread out in the git repository (the microscopic changes) and the changelog
file (the macroscopic changes) but combined in the git repository.

Each tag description is parsed, which strips all the irrelevant git
information (the commit id, the whole patch, time and author) as well as the
GnuPG signature and generates a clean changelog.

The generated changelog looks like this::

    v1.5.3
        * Add Java Webstart.
        * Create extensive manual page.
        - Fix drawing dots (broken since v1.5.2).
        - Allow movements with extra mouse buttons (enable in config).
        - Add config option to disable eraser.

It will only use the tags that are in your current branch. If you have two
branches for two versions of your program, like ``v2-series`` and
``v3-series``, you do not want the versions that start with a 3 to show up in
your other changelog.

In case you do want them all, there is an ``--all`` option.

And if you want more control, you can specify a regular expression with the
``--filter`` option.

Installation
============

The easiest way to install ``git-changelog`` is to use the ``setup.py``.

To install for all users::

    python setup.py install

To install just for yourself::

    python setup.py install --user


Manual page
-----------

To install ``git-changelog`` and the manual, use::

    make install


Usage
=====

See the manpage_.

.. _manpage: doc/git-changelog.1.rst
