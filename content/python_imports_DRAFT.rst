Understanding Modern Python Imports
###################################

:date: 2016-08-16 14:13
:modified: 2016-08-16 14:13
:category: programming, python
:tags: programming, python, imports, packages, scripts
:authors: Allen Barker
:summary: Description of modern Python imports.
:slug: understanding_python_imports

.. default-role:: code

.. |nbsp| unicode:: 0xA0 
   :trim:

.. |emsp| unicode:: 0x2003

.. contents::
    :depth: 2

Python has many strong points, and tends to have a learning curve that is
friendly to beginners.  The Python import system, however, is one part of the
language which can be confusing.  This article will discuss modern Python
imports, why they can be confusing, and how to use them correctly.

This article turned out to be longer than I thought it would be.  To
get the short summary, here is a diagram: TODO or DELETE

Old-style import rules versus new-style ones
============================================

One reason Python's import system is confusing, especially when searching for
tutorials and examples online, is that there are different versions of it which
work in different ways.  This article only discusses the modern imports, the
way current code should be written.  If you are using Python 3 then you are
already required to use the newer import system.  Python 2, however, does not
do this by default.

If you are still using Python 2 you should import `absolute_import` from the
`__future__` module in order to get the modern import system.  This is highly
recommended, and will make moving to Python 3 much easier.  While you're at it,
importing `division` and `print_function` from that module is also a good idea.
Just use this import before any of the others:

.. code-block:: python

    from __future__ import division, print_function, absolute_import

The remainder of this article will assume a modern Python import system.

Review of Python modules and packages
=====================================

The Python package and module system is closely tied to the directories and
files in the underlying filesystem.  Understanding the correspondence is
important in understanding the Python import system.  The correspondence is as
follows:

* python modules |emsp| <--> |emsp| files with `.py` extension

* python packages |emsp| <--> |emsp| directory subtrees where each directory
  has an `__init__.py` file

Any Python module/file which is inside a directory which contains an
`__init__.py` (which may or may not be an empty file) is by definition part of
a package.  Inside Python the `.py` file extension is never used to name
modules -- it is simply omitted -- but otherwise (with exception of script!
TODO) the names of modules, packages, and subpackages are in one-to-one
correspondence with filesystem objects and their filesystem names.

Note importance of root of package... TODO

The list `sys.path` (in the `sys` module of the Python library) tells the
Python import system where to look for packages and modules to import.  It is
just a list containing directory pathnames, represented as strings.
Understanding `sys.path` is important in understanding Python imports.  **If
the pathname of the directory containing a module's file or else containing the
package's root directory is not on the** `sys.path` **list then Python will not
be able to import the respective module or package.**  Ordering in the
`sys.path` list is important: The first match found in the list is the one that
is used.

As a side note, directories can also be added to the `sys.path` list from
command shells, by adding the pathnames to the `PYTHONPATH` environment
variable.

Dotted paths and the filesystem
===============================

For any package which can be found via `sys.path` (i.e., for which the root
directory of the package subtree is found inside some directory on the
`sys.path` list) there is an alternate way to specify modules (files) and
subpackages (subdirectories) located inside the package (in the package's
directory subtree).  This is a **dotted module or package list**.  For lack of
a better term these will be referred to as **dotpaths**.  These lists **always
refer to objects on the filesystem**.  The correspondence is fairly simple,
with an important exception mentioned below.  Dots in dotted module or package
list correspond one-to-one to slashes in filesystem pathnames:

Absolute dotted paths
---------------------

**Absolute dotted paths** always start with a package name corresponding to
some directory locatable inside some directory on the `sys.path` list.  They
are called absolute, but they are really relative to the root of the package
subdirectory.  To convert an absolute dotted path to a filesystem pathname
you do the following:

1. Change all the dots in the path into slashes (forward slashes except for
   Windows, where backslashes are used).

2. Prepend the path of the root directory of the package.

3. Add the `.py` extension if the object being imported is a module.

Although the dots look like the same dots which are used to access attributes
of Python objects, **the dots in dotted paths are not the same as attribute
access dots**.  This overloading of the dot symbol can cause confusion.
Dotted paths only refer to filesystem objects, and the two sorts of dots
cannot be mixed together in an import statement.  No object attribute dots
can appear in an import statement or a from statement.

* `p_name1.sp_name2.m_name3` |emsp| <--> |emsp| `"${P_NAME1_DIR}/p_name1/sp_name2/m_name3.py"`

After an import of a dotted path without an `as` renaming every package,
subpackage or module which is a prefix of the dotted path path *is* available
in the local namespace as a module.   The dotted path then works, but now the
dots really are attribute access (in a chain of modules containing modules).

It is convenient to think of a dotted path to a package or subpackage as simply
being a shorthand for the longer dotted path to the corresponding `__init__.py`
file which is inside the directory.  The effect of importing a directory is
to import the `__init__.py` file inside that directory.

Relative dotted paths
---------------------

A **relative dotted path** is similar to an absolute dotted path except that it
always starts with a dot or period symbol.  The use of relative dotted paths is
also more restricted (they can only appear immediately after a `from`
statement, and they only work within the same package).

Relative dotted paths are relative to the directory containing the module in
which they occur.  A single dot at the beginning of a relative dotted path
refers to the directory of the module.  Two dots refer to the parent directory,
and every dot after that goes up another level.

* `....p_name1.sp_name2.m_name3` |emsp| <--> |emsp| `"/../../../name1.name2.name3.py"` CWD???


Imports in scripts <-- actually, also non-package modules...
============================================================

TODO: Another split: inside a package or not inside a package.

A **script** is any Python module which is directly run by the Python
interpreter.  This can be done from the command line with the `python` command,
via clicking an icon, or by some other invocation method, such as a menu.
Every Python application must be started up from a script module.  Most modules
inside packages are not intended to be directly run as scripts, but they can
be, and then they are also scripts.

Scripts have a couple of unique properties, not shared by other modules:

1. The directory containing the script file is automatically added to
   `sys.path` when the script is run by the Python interpreter.  

2. The `__name__` attribute of the script's module is always `"__main__"`,
   regardless of the file name.

Property 2 is what allows the use of the common idiom `if __name__ ==
"__main__":` in Python files.

Another confusing thing about the Python import system is that **scripts and
packages have completely different import rules**.

Scripts cannot use any form of explicit relative import unless they are
explicitly run as part of a package (via `python -m` or by setting the
`__package__` attribute).

Scripts outside packages can *only* import modules and packages which are found
on the `sys.path` list.

implicit relative, older way, now forbidden
explicit relative, forbidden for scripts without special techniques

To avoid problems with imports you should always know if the module is
1) part of a package or not, and 2) going to be run as a script or not.

Imports in packages
===================

extra-package
   absolute

intra-package
   relative or absolute

Packages have some unique properties which are important in the context of
imports:

1. Importing a package (directory name) has the effect of importing and running
   the code inside any `__init__.py`.  The directory containing the top-level
   package directory **must** be found on the `sys.path` list) file contained
   in the directory.

2. Importing any file/module within a package will, by default, import and initialize
   every `__init__.py` file from the root of the package down to the directory


It is easy to underestimate `__init__.py` files, since they are often empty
files, but they are quite important as far as how Python packages work.

Imports can be done AS PACKAGES or AS MODULES.  It is perfectly OK to import
a module inside a package without importing the package **as long as it does
not import anything else from within the same package using relative imports
and as long as the package is on** `sys.path` **for absolute imports.**

Running modules inside packages as scripts
==========================================

Scripts are not part of any package, but there are ways to run files inside modules as 
if they were scripts.  One way is by setting the `__package__` attribute.
Another is to run them with the `-m` command-line option to the Python interpreter.



