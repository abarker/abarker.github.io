Understanding Python Imports
############################

:date: 2019-07-12 14:13
:modified: 2019-07-12 14:13
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

Python has many strong points and tends to have a learning curve that is
friendly to beginners.  The import system, however, is one part of the
language which can be confusing.  There are a few possible sources of
confusion:

* Certain import statements which work in modules inside packages do not work
  in modules which are not in packages, and vice versa.

* Some of the import syntax does not generalize in the way one might first
  expect it does.

* Modules run as scripts have some special properties which can affect imports.

* Lack of familiarity with the Python package mechanism in general.
 
* Old documentation can come up in searches.  (For example, Python 2 had
  something called implicit relative import which Python 3 does not have.  If
  you're still using Python 2, disable implicit relative imports by using `from
  __future__ import absolute_import` as the first import.)

This article only discusses modern Python imports (Python versions >3.0).
Basic familiarity with the concepts of files and directories/folders is
assumed.  Before imports are discussed Python modules and packages will be
briefly reviewed.

Review of Python modules and packages
=====================================

The Python module and package system is closely tied to the directories and
files in the underlying filesystem.  Understanding the correspondence is
important in understanding the Python import system.  The basic correspondence
can be summarized as follows:

.. math::

   \textrm{python modules} \Longleftrightarrow \textrm{files with}\; \texttt{.py}\; \textrm{extension} \\

   \textrm{python packages} \Longleftrightarrow \substack{\textrm{directory subtrees where each} \\
   \textrm{directory has an}\; \texttt{__init.py__}\; \textrm{file}}

A file containing Python code is always a module.  Such files usually end with
the `.py` extension.  All Python programs are composed of one or more modules.

Packages are collections of modules organized in a certain way.  Any Python
module/file which is inside a directory containing an `__init__.py` module
(which may or may not be an empty file) is by definition part of the package
associated with that `__init__.py` file.  Otherwise a module is not part of any
package.  Subpackages are defined similarly, as subdirectories of a package
directory which also contain `__init__.py` files, and so forth.  (Formally
packages are a special kind of module, but in this context they can and will be
considered to be distinct things.)

Consider this example directory structure, which will be used throughout the
article:

::

   my_project
   │ 
   ├── bin
   │   └── my_script.py
   │ 
   └── src
       ├── my_standalone_module.py
       │ 
       └── my_package
           ├── __init__.py
           ├── foo.py
           ├── bar.py
           └── my_subpackage
               ├── __init__.py
               └── baz.py

This is the skeleton of a project called `my_project` which contains one script
called `my_script` in its `bin` directory and a package called `my_package` in
its `src` directory.  (Some people prefer not to have a separate `src`
directory, but there are some `good
<https://hynek.me/articles/testing-packaging/>`_ `reasons
<https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_ to include it.)  There
is also a module named `my_standalone_module` in the `src` directory.

The `__init__.py` files in the directories are essentially the modules for the
corresponding packages or subpackages.  Whenever a package or subpackage is
imported its `__init__.py` is implicitly imported and executed.  It is easy to
underestimate `__init__.py` files, since they are often empty files, but they
are quite important as far as how Python packages work.

The package's namespace is the same as the namespace of its `__init__.py` file.
This includes any names which are explicitly imported into the `__init__.py`
file.  Whenever a subpackages is imported its name is automatically added to
the namespace of `__init__.py` (and hence the package namespace).  The
top-level packages namespace is the main user interface for Python packages, so
names which should be accessible there should be imported into the
`__init__.py` file.

Subpackages are imported (and their `__init__.py` files are run) when they are
either 1) explicitly imported or 2) automatically imported just before a module
or subpackage contained within that subpackage is imported.  As noted above,
the subpackage module is also added to the top-level package namespace (under
its module name).

Python `import` statements always contain a specifier for a module or a package
to import.  Equivalently, they always contain a specifier for the corresponding
file or a directory.  While Python's import statements never use the `.py` file
extension for naming modules, other than that the names of modules, packages,
and subpackages correspond directly with filesystem objects (files and
directories) and their filesystem names.

The Python path-search list: `sys.path`
=======================================

The `sys.path` list is the root of all imports in Python (excepting the
system library modules such as `math`, which are always found in their usual
location).

The list `sys.path` (in the `sys` module of the Python library) tells the
Python import system where to look for packages and modules to import.  It is
just a list containing directory pathnames, represented as strings.
Understanding `sys.path` is important in understanding Python imports.  **If
the pathname of the directory containing a module's file or else containing the
package directory is not on the** `sys.path` **list then Python will not
be able to import the respective module or package.**  Note that when
adding external packages with `pip` or similar programs they are placed in
the system ``site-packages`` directory which is on `sys.path` by default.

Ordering in the `sys.path` list is important: The first match found in the
list is the one that is used.  The paths themselves are strings which can
represent relative or absolute pathnames for the underlying operating system.
Relative pathnames in `sys.path` (such as `".."`) are interpreted relative to
Python's current working directory (CWD).  The CWD is initially set to the
command shell's notion of current directory (the directory you are in when you
invoke the `python` command), but it can be changed by calls to
`os.setcwd()`.

Directories can also be added to the `sys.path` list from from command shells
like Bash by adding their pathnames to the `PYTHONPATH` environment variable.
This is usually not the recommended way, however.

It is simple to importing a package or a module not part of a package which is
located in a directory on the `sys.path` list: just import the package
directory name or the module name without the `.py` extension.  For example,
assuming that `my_project/src` is on `sys.path`, the following imports can
be used:

.. code-block:: python

   import my_package
   import my_standalone_module

These statements import the package `my_package` in the directory of that same
name and then import the module `my_standalone_module` with code located in the
file `my_standalone_module.py`.

The `as` keyword can also be used to rename the import under an alias:

.. code-block:: python

   import my_package as mp
   import my_standalone_module as msm

The `as` keyword can be used anywhere in an import statement where a name
is created in the namespace in order to rename the variable.

The `from` statement can be used to import particular attributes from within a
package or module:

.. code-block:: python

   from my_package import my_package_var as mpv, my_subpackage as msp
   from my_standalone_module import my_standalone_module_var

These statements first import the attribute `my_package_var` from the package
namespace of `my_package`, renaming it as `mpv`.  The subpackage
`my_subpackage` is similarly imported and renamed to `msp`.  Finally, the
attribute `my_standalone_module_var` is imported from `my_standalone_module`.

Absolute imports
================

We have already seen one kind of absolute import, which is the import of a
module or package from a directory on the `sys.path` list.  There is one more
kind of absolute import which has not yet been covered.  These are used to
import modules and subpackages which are located inside packages.  This kind of
import cannot be done correctly simply by placing the directory on `sys.path`
and then importing the module or subpackage.  (In fact, a package directory or
subdirectory, i.e., a directory with an `__init__.py` file, should *never*
appear in the `sys.path` list.  Doing that can introduce subtle bugs which can
be difficult to find.  Only the *parent* directory of the package should ever
appear in `sys.path`.)

Absolute imports *require* that the directory containing either the module or
the top-level directory of the package being imported be discoverable on the
`sys.path` list.  Absolute imports can always be used, in any Python module,
regardless of whether it is inside a package or outside of a package.

Absolute imports for modules inside packages use a dotted-path syntax, e.g.,

.. code-block:: python

   import my_package.foo

This statement would import the module `foo` from the `foo.py` file under the
name `my_package.foo` (an `as` statement could be used to create an alias).
The next subsection covers the relation of these dotted-paths to the filesystem
objects.  Then absolute imports of subpackages and modules in packages will be
discussed further.

Absolute dotted paths and the filesystem
----------------------------------------

For any package which can be found via `sys.path` (i.e., for which the root
directory of the package subtree is found inside some directory on the
`sys.path` list) there is an alternate way to specify modules (files) and
subpackages (subdirectories) located inside the package (in the package's
directory subtree).  The slashes in operating-system pathnames are essentially
replaced with dots.  These dotted paths are relative to the top-level package
directory (i.e., the top directory containing an `__init__.py` file):

.. math::

   \scriptstyle\texttt{src/my_package} \;\Longleftrightarrow\; \texttt{mypackage} \\

   \scriptstyle\texttt{src/my_package/foo.py} \;\Longleftrightarrow\; \texttt{mypackage.foo} \\

   \scriptstyle\texttt{src/my_package/foo.py/my_subpackage} \;\Longleftrightarrow\; \texttt{mypackage.foo.my_subpackage} \\

   \scriptstyle\texttt{src/my_package/foo.py/my_subpackage/baz.py} \;\Longleftrightarrow\; \texttt{mypackage.foo.my_subpackage.baz}

Note that the `.py` extension is omitted, but other than that the
correspondence is fairly simple.  These dotted paths *always* refer to objects
on the filesystem.

Absolute imports of subpackages and modules in packages
-------------------------------------------------------

Now that dotted paths have been covered the discussion of importing modules
that are inside packages is fairly simple: just put the dotted path after the
import statement.  The first component of the dotted path is *always* the
top-level package name (i.e., the name of the directory which is the root of
the package subtree).  For package `my_package` as given above these are
all allowable imports using `import` directly:

.. code-block:: python

   import my_package
   import my_package.foo
   import my_package.my_subpackage
   import my_package.my_subpackage.baz

These are all allowable imports using `from` imports:

.. code-block:: python

   from my_package import foo
   from my_package import my_subpackage
   from my_package.my_subpackage import baz

Possible confusions in import syntax
------------------------------------

One possibly confusing aspect of Python imports is that the dot symbol is
overloaded.  In the general language the dot is used for attribute access, such
as in `my_class.my_attribute`.  But in the dotted-paths of import statements
the dot essentially means "subdirectory" and should be thought of more as a "/"
character in a pathname.

Consider these valid import statements, assuming that `foo_var` is a variable
assigned in `foo.py`:

.. code-block:: python

    import my_package
    import my_package.foo
    from my_package.foo import foo_var

After the first import the statement `my_package.foo` is valid in the Python
code, since `my_package` is a `module` object with submodule `foo` as a `module`
attribute.  In that context the dot symbol is attribute access (unlike in the
second import above).

After the second import above the statement `my_package.foo.foo_var` is
similarly valid Python code, with the dots again representing attribute access
on `module` objects.

In the third import the relation between `my_package.foo` and `foo_var`, using
the `from` statement is actually attribute access, since `foo_var` is an
attribute of the `foo` module.

Given the cases above the following seems like it should work, but it is not
allowed:

.. code-block:: python

    import my_package
    import my_package.foo.foo_var # FAILS!
    import my_package.foo.foo_var as fv # Also FAILS!

Another thing that you cannot do is to assign Python variables as aliases to dotted
paths.  So, while it seems like it would be convenient, this code does not work:

.. code-block:: python

    import my_package.foo as mpf
    from mpf import foo_var # FAILS!  Only dotted paths directly after from statements.

While the module attribute-access pattern mimicks the dotted-path syntax, they
are not the same thing.  Because module objects cannot be used in import
statements, the full dotted paths must always be entered.  Relative dotted
paths, to be covered later, can simplify some cases of having to write out the
full dotted paths.

To avoid these possible confusions, remember that dotted paths in Python import
statements always refer to filesystem objects (either directories or `.py`
files).  The first specifier in any import statement, whether a bare `import`
or a `from` statement, can *only* be a dotted path.  In bare `import`
statements the dotted path then becomes a module in the namespace of the Python
code.  In a `from` import only the final specifier(s) after `import` become
namespace objects, and they are not restricted to only be module objects.

Imports in scripts
------------------

A **script** is any Python module which is directly run by the Python
interpreter.  This can be done from the command line with the `python` command,
by clicking an icon, or via some other invocation method such as from a menu.
Every Python application must be started by running a module run as a script
(except packages which are directly executed as packages such as by using
`python -m`).

For the time being scripts will be assumed to always be located outside of
packages, i.e., they reside in a directory without an `__init__.py` file.
Scripts inside modules are also possible, but they introduce extra
complications and are discussed in a separate section near the end.

Scripts have a few unique properties not shared by other modules:

1. The directory containing the script file is automatically added to
   `sys.path` when the script is run by the Python interpreter.  

2. The `__name__` attribute of the script's module is always set to
   `"__main__"` when it is run as a script, regardless of the file's name.

Property 2 is what allows the use of the common idiom `if __name__ ==
"__main__":` in Python files.  Code in that section then only executes when the
module is directly run as a script and not when the module is imported from
another Python module (some modules are meant to be used both ways).

Scripts can only import modules and packages which are found in directories on
the `sys.path` list.  These are called **absolute imports**.  For example,
the import

.. code-block:: python

   import my_package

must correspond to a file `my_package.py` that is located in some directory on the
`sys.path` list.

Relative imports
================

We saw earlier that dotted paths in import statements must be typed out in
full.  In the case of **intra-package imports**, i.e., importing a module of
subpackage from another module inside the same package, **relative imports**
can often be used to simplify the dotted-path expressions.  Note that relative
imports are *only* allowed for intra-package imports; all other imports must
use absolute imports.

Relative imports are to absolute imports as relative filename paths are to
absolute filename paths.  They allow for shortened expressions relative to
another directory.  First we will extend the definition of dotted paths to
allow for relative dotted paths.

Relative dotted paths
---------------------

A **relative dotted path** is similar to an absolute dotted path except that it
always starts with a dot symbol.

Relative dotted paths have different meanings depending on the location of the
module in which they occur.  They are interpreted relative to the directory
containing the module in which they occur.  (If you are familiar with relative
paths in a Unix-style shell such as Bash, the syntax is similar.)

* A single dot refers to the directory containing the module.  It can occur
  alone or at the beginning of a longer dotted path.  As an example, the
  following correspondences hold inside the `foo` module:

.. math::

  \scriptstyle\texttt{my_package/bar.py} \;\Longleftrightarrow\; \texttt{.bar} \\

  \scriptstyle\texttt{my_package/my_subpackage/baz.py} \;\Longleftrightarrow\; \texttt{.my_subpackage.baz} 

* Two dots refer to the parent directory of the directory containing the
  module.  They can occur alone or at the beginning of a longer dotted path.
  The following correspondence holds inside the `baz` module:

.. math::

  \scriptstyle\texttt{my_package/bar.py} \;\Longleftrightarrow\; \texttt{..bar}

* Each additional dot goes up one more directory level.

If there were another subpackage named `sibling` at the same level as `my_subpackage` then
a module `cousin` in it could be imported from `baz` by going up and then down as follows:

.. math::

  \scriptstyle\texttt{my_package/sibling/cousin} \;\Longleftrightarrow\; \texttt{..sibling.cousin}

Relative imports
----------------

Now that relative dotted paths have been covered, relative imports are
straightforward: just use a relative dotted path instead of an absolute dotted
path (but remember that they are only allowed for intra-package imports).

There is one important restriction on relative imports: **A relative
dotted-path can only appear after a** `from` **statement.**  It seems like you
should be able to write imports such as `import .bar` from the `foo` module and
`import ..bar` from `baz` module, but those are syntax errors.  The reason this
is not allowed is that the expressions after the bare `import` statement (such
as `.bar`) are not valid Python names and so cannot be added to the namespace
as in the case of absolute imports.

The following are valid relative imports from the `foo` module:

.. code-block:: python

   from . import bar
   from .bar import bar_var
   from . import my_subpackage
   from .my_subpackage import baz
   from .my_subpackage.baz import baz_var

These relative imports are all valid in the `baz` module:

.. code-block:: python

   from .. import bar
   from ..bar import bar_var

Note that importing from dot-paths alone, such as from `.` and `..`, allows you
to import from the package or subpackage namespace (i.e., the `__init__.py`
namespace of that directory) as well as to import modules and subpackages in the
directory.  Same as absolute imports from `my_package` package.

Running modules inside packages as scripts
==========================================

Scripts were previously assumed to always be located outside of packages, but
scripts inside packages will also run just fine.  At this point, however,
another property needs to be added to the special properties of modules run as
scripts:

3. By default a script is not run as part of a package, even if there is
   an `__init__.py` in its directory.

As long as only absolute imports are used then scripts inside packages should
run as normal.  Relative imports do not work, however, because the module is
not run as part of the package and the package itself is not automatically
imported when a script inside it is run.  In order for a script inside a
package directory structure to import modules from that package it would need
to load the package and then only use absolute imports, from the package root.

There is an additional danger that can arise from running a script inside a
package.  Recall special property 1 of scripts: the script's home directory is
always added to `sys.path`.  This means that absolute imports from within the
directory will *seem* to work; they might work correctly or they might not.
Since the current directory is on `sys.path`, any absolute imports with the
same name as a module or subpackage in the directory will be imported that
individual module or subpackage, i.e., not as part of the full package.  So 1)
the package initialization is not run, and 2) any relative imports inside the
imported module will cause a syntax error.   If the package is also loaded as a
package then there is also a danger of double imports.  (The script could
remove its own directory from `sys.path` to avoid these particular problems.)

To get around these problems and still run scripts inside packages what is
needed is a way to automatically load the package and to run the script as a
part of the package.  There are several possible ways to do this:

1. Invoke the script using `python -m <fullyQualifiedName>`, where
   `<fullyQualifiedName>` is the fully-qualified name of the module inside the
   package (i.e., the absolute dotted path).  Note that the directory
   containing the package's root directory must also be in `sys.path` or the
   command will fail.  A fancier shell script could be defined to set
   `PYTHONPATH` and calculate the qualified name, etc., but generally the
   invocation differs from that of other Python scripts.

2. Set the `__package__` attribute of the script to the fully-qualified name
   and then import the package in the correct way (which is more complex than
   you might expect).  Fortunately there is a `package on PyPI
   <https://abarker.github.io/set-package-attribute/>`_ which can do this for
   you automatically (and optionally also remove the directory's `sys.path`
   entry).

3. Create a `setup.py` file and `create an entry point for it
   <http://www.python.org/>`_ via `console_scripts`.  For development this
   requires setting up the project with a `setup.py` and then `pip` installing
   it in development mode by running `pip install -e .` in the project root
   directory.  To add or remove entry points the `setup.py` file must be
   modified and the package reinstalled.  An advantage of this approach is that
   it creates commands which are directly executable in the shell (under the
   name specified in `setup.py`).  A similar thing can be done in the
   more-recent `pyproject.toml` files if you use that method to set up projects
   rather than `setup.py`.

Not covered
===========

A few important import variations are not covered above.  They tend to only be
used in special or advanced cases.

**pth files**: Pth files are special files which contain the pathnames of
packages or modules to import.  Using pth files only works in the special
system `site-packages` directory.

**Namespace packages**: Namespace packages allow one or more toplevel
directories having the same: directory name, but without `__init__.py` files,
to be used like a common namespace for all the modules and packages in all
the directories.  This can: be useful for large distributions, but there are
also drawbacks.  Most people should continue to use `__init__.py` files to
create packages.

**Star imports**: By default, the statement `from my_module import *` imports
all the names in the `my_module` namespace which do not start with the
underscore character.  If `__all__` is defined in `my_module` as a list of
string variable names then only those names will be imported by `*` imports
from the module.  Anything else must be imported explicitly.  The `__all__`
list can also contain the names of modules and subpackages to import.

**Importing from zip files**: Python allows modules to be imported from
zipfiles, provided the `.zip` archive file is located on `sys.path`.   The
directory structure in the zip file then acts as a regular directory.

Further reading
===============

* The official Python documentation on `imports
  <https://docs.python.org/3/reference/import.html>`_ and
  `modules <https://docs.python.org/3.7/tutorial/modules.html>`_. 

* `Another guide to Python imports
  <https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html>`_ by Chris Yeh.

* An `introduction to absolute vs. relative imports
  <https://realpython.com/absolute-vs-relative-python-imports>`_, including a discussion
  of formatting style.   By Mbithe Nzomo.

* A discussion of some of the often subtle `import traps
  <http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html>`_
  which can arise, by Nick Coghlan.

