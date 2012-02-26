=============
git-changelog
=============

displays changelog based on git tags
====================================

:Author: Martin Ueding <dev@martin-ueding.de>
:Date:   2012-02-27
:Manual section: 1


SYNOPSIS
--------
``git changelog [options]``


DESCRIPTION
-----------
Lists all annotated tags that are on a given branch and prints their message.

If you have tags like ``v1.0`` with a message like ``* New Version`` you will
get this output::

	v1.0
	    * New Version


OPTIONS
-------
``-a`` ``--all``
	Show tags from all branches.  
``--filter regex``
	Filters tags with regex.


CONFIG
------
You can set these options in your git config:

- ``changelog.filter regex``
- ``changelog.showall true|false``
