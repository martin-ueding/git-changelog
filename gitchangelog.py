#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

"""
Logic for the changelog generation.
"""

import itertools
import os
import re
import subprocess
import sys
import tempfile

__docformat__ = "restructuredtext en"

def has_git_dir():
    """
    Checks for a git directory.

    :return: Whether a git repo exists.
    :rtype: bool
    """
    with open(os.devnull, 'w') as null:
        return subprocess.call(["git", "rev-parse", "--show-toplevel"], stdout=null, stderr=null) == 0

    return True


def generate_filter_tag_function(options):
    """
    Creates a filter for tags.

    :param options: Program options.
    :return: Filter function that decides over a given string.
    :rtype: function
    """
    regex = load_regex(options.regex)

    if regex is None:
        def filter_tag(tag):
            """
            Filters tags.

            This one returns True as it does not filter any tags out.

            :param tag: Tag to filter.
            :return: True.
            """
            return True

    else:
        pattern = re.compile(regex)

        def filter_tag(tag):
            """
            Filters tags.

            If the given tag does not lie on the current branch, it is filtered
            out.

            :param tag: Tag to filter.
            :return: Whether tag is on branch.
            """
            matcher = pattern.match(tag)
            return matcher is not None

    return filter_tag


def generate_tag_list(options):
    """
    Builds a list of tags.

    The list is either from all tags or just from the current branch.

    :param options: Program options.
    :return: Filtered tag list.
    """
    # Get the tag description. Split the lines, remove the last empty line.
    all_tags = subprocess.check_output(["git", "tag"]).split(b'\n')[:-1]

    if is_list_all(options):
        tags = sorted(all_tags)[::-1]
    else:
        # The above list only gives us a list of all tags. We are interested in
        # the correct order in the repo and only the tags that are on the
        # current branch. `git log` gives that, but also branch names.
        log = subprocess.check_output(["git", "log", "--simplify-by-decoration", "--format=%d"]).split(b'\n')

        tags = []
        for log_entry in log:
            # There are a couple of empty lines there.
            if len(log_entry) == 0:
                continue

            log_entry_refs = log_entry[2:-1].split(b', ')
            for ref in log_entry_refs:
                if ref in all_tags:
                    tags.append(ref)

    return list(filter(generate_filter_tag_function(options), tags))


def generate_changelog(tags, outfile):
    """
    Generate the changelog, strip PGP signatures.

    :param tags: Tags to list.
    :type tags: list
    :param outfile: File to write changelog to.
    :type outfile: File
    """
    # Iterate through the tags.
    for tag in tags:
        # Get the description for the tag.
        git_show = subprocess.check_output(["git", "cat-file", "-p", tag]).split(b'\n')

        # If this is an annotated tag, it starts with "tag …", if it is a
        # lightweight tag, it starts with "commit …". Since lightweight tags do
        # not carry any description, we can discard them.
        if git_show[2][:3] != b"tag":
            continue

        for line, i in zip(git_show, itertools.count()):
            # If the PGP signature starts, the entry is over.
            if line == b"-----BEGIN PGP SIGNATURE-----":
                break

            # Print the line from the tag message.
            if i >= 5:
                outfile.write(b"    "+line+b"\n")

            # Print the tag name.
            elif i == 2:
                outfile.write(line[4:]+b"\n")


def is_list_all(options):
    """
    Checks whether all tags (not only current branch) should be listed.

    :param options: Program options.
    :return: Whether all tags should be listed.
    """
    if options.list_all:
        return True

    try:
        with open(os.devnull, 'w') as null:
            return subprocess.check_output(["git", "config", "--get", "changelog.listall"], stderr=null).strip() == "true"
    except subprocess.CalledProcessError as e:
        return False


def load_regex(regex = None):
    """
    Load the tag filter regex from from either command line or config.

    :param regex: RegEx to use instead.
    :return: RegEx string.
    """
    if regex != None:
        return regex

    try:
        with open(os.devnull, 'w') as null:
            return subprocess.check_output(["git", "config", "--get", "changelog.filter"], stderr=null).strip()
    except subprocess.CalledProcessError as e:
        return None
