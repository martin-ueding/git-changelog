.. Copyright © 2013 Martin Ueding <dev@martin-ueding.de>

#########
Changelog
#########

v1.6.1
    - Central license file
    - Run ``setup.py`` with its own interpreter
    - Update ``make clean`` target

v1.6
    - Convert to Python 3

v1.5.4
    - Use ``--root``

v1.5.3
    - Add GPLv2+ license
    - Add install target
    - Add README
    - Add setup.py
    - Refer to manual page for the usage

v1.5.2
    - Use pipe instead of temporary file

v1.5.1
    - Fix closing of the file

v1.5
    - Use less (or git's ``core.pager``) as a pager

v1.4
    - Faster by not parsing the patch

v1.3
    - Add option to list all tags (``--all``)
    - New regex filter for tag names
    - Add manual page
    - No crash on merge commits
    - Warn if there is no git repo

v1.2
    - Handle annotated, unsigned tags correctly
    - Only show tags that are on the current branch
    - Indent with four spaces

v1.1
    - Do not crash on lightweight tags
    - Use a single Python script

v1.0
    Initial Release
