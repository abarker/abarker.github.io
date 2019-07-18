Incremental Package Development
###############################

:date: 2019-08-16 14:13
:modified: 2019-08-16 14:13
:category: programming
:tags: programming, python
:authors: Allen Barker
:summary: Developing packages incrementally.
:slug: incremental_development

.. default-role:: code

.. |nbsp| unicode:: 0xA0 
   :trim:

.. |emsp| unicode:: 0x2003

.. contents::
    :depth: 2

Not everyone's way to develop, but I often start with a rough
script and it evolves to the point where it should be a package,
but then imports, scripts inside, etc...

Eventually you start separating out into different modules, and some end up
being library-type modules, while others are scripts that use the library-type
modules.

Especially for scientific stuff.

Usual way: work for a while in a non-package and eventually decide
to convert to a package.  Change all local imports to be relative.
Move all scripts and tests to external directory.  Hassle.

---> Also incorporate the notes in quantum directory.

Developing in the same directory
================================


Scripts meant to live inside the package directory
--------------------------------------------------

Scripts which will later be moved outside the package directory
---------------------------------------------------------------

If a script is intended to be run from outside the package directory at some
point then it should only use absolute imports from the package.  So, for
example, use `import foo` and `from foo import foo_var` rather than `from .
import foo_bar` to import from package `foo`.  All the dotted import paths
should start with `foo`.  These imports will work in both cases.  Instead of
using long dotted-names you can instead import the names into the `__init__.py`
module's namespace if they are generally useful for the package's exposed
interface.

As long as the script is inside the package it needs to be run as part of the
package, using one of the methods discussed earlier.  When it moves out of the
package this is no longer required and any extra code to set the `__package__`
attribute should be removed.  Remember that the `foo` package will need to be
discoverable on the script's `sys.path`.  This is commonly done with `pip` and
a `setup.py`, using `pip install -e .` in the project root directory containing
`setup.py`.

Alternatives
============

TODO:  not just entry points, but scripts can be specified.  It is `scripts`
vs. the `console_scripts` entry point.
https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html

Alternative: use something like cookiecutter and make a full project structure
for everything.  But some things just stay rough, and do not get developed
further...  Also a pain to deal with widely-separated things in the early
stages and when development is heavy.  IDEs might make it easer for some, but
there is still the separation into package/non-package to deal with.

