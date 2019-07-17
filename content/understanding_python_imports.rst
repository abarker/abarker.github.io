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

* Certain import statements which work for modules inside packages do not work
  for modules outside of packages, and vice versa.

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

At some point most non-trivial projects become large enough that it makes sense
to separate the code into separate files.  In Python those separate files are
called **modules**.  The use of modules can make the codebase easier to
understand and, as the name implies, more modular.  Imports are used to allow
code in one module to access and use code from other modules.

The Python module and package system is closely tied to the directories and
files in the underlying filesystem.  Understanding the correspondence is
important in understanding the Python import system.  The basic correspondence
can be summarized as follows:

.. math::

   \textrm{files with}\; \texttt{.py}\; \textrm{extension} \;\Longrightarrow\; \textrm{python modules} \\
   
   \substack{\textrm{directory subtrees where each} \\
   \textrm{directory has an}\; \texttt{__init__.py}\; \textrm{file}} \;\Longrightarrow\; \textrm{python packages} \\

A file containing Python code is always a module and vice versa.  Such files
usually have names ending with the `.py` extension.  All Python programs are
composed of one or more modules.  **Packages** are collections of modules
organized in a certain way:
  
* Any Python module which is inside a directory containing an `__init__.py`
  file (which may or may not be an empty file) is by definition part of the
  package associated with that `__init__.py` file.  The name of the package is
  the same as the name of the directory.  (Formally, packages are just a
  special kind of module, but in this context packages and modules will be
  considered to be distinct.)

* **Subpackages** are defined similarly to packages, as subdirectories of a
  package directory which also contain an `__init__.py` file.  Subpackages can
  have their own subpackages, and so forth.

* A module with no `__init__.py` in its directory is not part of any package or
  subpackage (excepting namespace packages, an advanced topic briefly discussed
  `later <namespace-packages_>`_).

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
           │ 
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
corresponding packages or subpackages.  When a module is imported its code
is run to initialize it.  When a package or subpackage is
imported its `__init__.py` is implicitly imported and run.  It is easy to
underestimate `__init__.py` files, since they are often empty files, but they
are quite important as far as how Python packages work.

A package's namespace is by definition the namespace of the `__init__.py`
module in its directory.  This includes any names which are explicitly imported
into the `__init__.py` file.  Whenever a subpackage is imported its name is
automatically added to the namespace of `__init__.py` (and hence to the package
namespace).  The top-level namespace of a package constitutes its main
application-programmer interface (API).  Names which should be exposed by that
API must be imported into the `__init__.py` file.

Subpackages are imported (and their `__init__.py` files are run) when they are
either 1) explicitly imported or 2) automatically imported just before a module
or subpackage contained within that subpackage is imported.  As noted above,
the `module` object representing the subpackage is also added to the namespace
of the package or subpackage that imports it (under its subpackage name).

Python `import` statements always contain a specifier for a package or module
to import.  Equivalently, they always contain a specifier for the corresponding
file or a directory in the filesystem.  While Python's import statements never
use the `.py` file extension for naming modules, other than that the names of
modules, packages, and subpackages correspond directly with filesystem objects
(files and directories) and their filesystem names.

The Python path-search list: `sys.path`
=======================================

The `sys.path` list is the root of all imports in Python (excepting system
library modules such as `math`, which are always found in their usual
location).  This list tells the Python import system where to look for packages
and modules to import.  It is just a list containing directory pathnames,
represented as strings.

Understanding `sys.path` is important in understanding Python imports.  **If
the pathname of the directory containing a module's file or else containing the
package directory is not on the** `sys.path` **list then Python will not be
able to import the respective module or package.**  Note that when external
packages are installed with `pip` or similar programs they are placed in the
system ``site-packages`` directory, which is on `sys.path` by default.

Ordering in the `sys.path` list is important: The first match found in the list
is the one that is used.  The paths themselves are strings which can represent
relative or absolute pathnames for the underlying operating system.  Any
relative pathnames in `sys.path` (such as `".."`) are interpreted relative to
Python's current working directory (CWD).  The CWD is initially set to the
command shell's notion of current directory (i.e., the directory you are in
when you invoke the `python` command), but it can be changed by calls to
`os.setcwd()`.

Directories can be added to the initial `sys.path` list from command shells
like Bash by setting the `PYTHONPATH` environment variable before invoking the
`python` command.  The `PYTHONPATH` environment variable should contain a
colon-separated string of the pathnames to be added.  While this has its uses,
it is usually not the recommended way to initialize `sys.path`.

Actually importing a package which is located in a directory on the `sys.path`
list is simple: just import the package directory name.  Similarly, to import a
non-package module located in a directory on `sys.path` just import the
module's file name leaving off the `.py` extension.  For example, suppose the path
to directory `my_project/src` is in the `sys.path` list.  Then the following
imports work for the project skeleton given above:

.. code-block:: python

   import my_package
   import my_standalone_module

These statements import the package `my_package` in the directory of that same
name and then import the module `my_standalone_module` with code located in the
file `my_standalone_module.py`.  The same imports can be done with a single
statement, though that style is not generally recommended:

.. code-block:: python

   import my_package, my_standalone_module # Same as above two imports.

What is actually being imported here are two `module` objects, one representing
the package `my_package` and the other representing the module `my_module`.
For example, if you run `str(type(my_package))` the result is `"<class
'module'>"`.

All the names in the namespace of a package or module represented by a `module`
object are also attributes of that `module` object (i.e., they are in its
`__dict__`).  This is what allows those attributes to be accessed directly from
the imported module objects.  For example, assuming the `__init__.py` of
`my_package` defines the variable `init_var` and `my_standalone_module` defines
`my_standalone_module_var` expressions like `my_package.init_var` and
`my_standalone_module.my_standalone_module_var` can be used in any module that
makes the above imports.

The `as` keyword can also be used to rename an import under an alias:

.. code-block:: python

   import my_package as mp
   import my_standalone_module as msm
   import my_package as mp, my_standalone_module as msm # Same as above two.

The `as` keyword can be used anywhere in an import statement where a name in
the local namespace is being assigned a value.  It simply renames the variable
under which that package or module is imported.

Python always keeps a cache of imported packages and modules as `module`
objects, in the `sys.modules` dict, keyed by the fully-qualified name of the
package or module.  When an import statement is executed Python first looks in
that dict to see if the package or module has previously been imported.  If so
then it returns the previously-imported object.  Otherwise it tries to import
from the filesystem.  Re-importing a module requires the explicit use of the
builtin `reload` function.

The `from` statement can be used to import subpackages as well as particular
attributes defined in a package or module:

.. code-block:: python

   from my_package import init_var as iv, my_subpackage as msp
   from my_standalone_module import my_standalone_module_var

The first of these statements imports the attribute `init_var` from the
package namespace of `my_package`, renaming it as `iv`.  It also imports the
subpackage `my_subpackage`, renamed to `msp`.  The second statement imports the
attribute `my_standalone_module_var` from `my_standalone_module`.

Imports using the `from` keyword will be referred to as `from` imports, and
imports without the `from` keyword will be referred to as bare `import`
statements.

Absolute imports
================

We have already seen one kind of absolute import, which is the import of a
module or package from a directory on the `sys.path` list.  There is one more
kind of absolute import which has not yet been covered.  These are used to
import modules and subpackages which are located inside packages.  That kind of
import cannot be done correctly simply by placing the directory on `sys.path`
and then importing the module or subpackage.  (In fact, a package directory or
subdirectory, i.e., a directory with an `__init__.py` file, should *never*
appear in the `sys.path` list.  Doing that can introduce subtle bugs which can
be difficult to find.  Only the *parent* directory of the package should ever
appear in `sys.path`.)

Absolute imports *require* that the directory containing either the top-level
package directory or the non-package module being imported be discoverable on
the `sys.path` list.  Absolute imports can always be used, in any Python
module, regardless of whether it is inside a package or outside of a package.

Absolute imports for modules inside packages use a dotted-path syntax, e.g.,

.. code-block:: python

   import my_package.foo

This statement would import the module `foo` located in the `foo.py` file under
the name `my_package.foo` (an `as` keyword could be used to create an alias if
desired).  The next subsection covers the relation of these dotted paths to the
filesystem objects.  Once these dotted paths are understood absolute imports
will be much easier to discuss.

Absolute dotted paths and the filesystem
----------------------------------------

For any package which can be discovered by looking in the directories on the
`sys.path` list there is corresponding **dotted path** to specify modules
(files) and subpackages (subdirectories) located inside the package (inside the
package's directory subtree).  The slashes in operating-system pathnames are
essentially replaced with dots.  These dotted paths are always relative to the
package's top-level directory (i.e., the highest-level directory containing an
`__init__.py` file),

Here are some examples of the correspondence, based on the project skeleton
above.  The filesystem pathnames are given on the left (assuming forward
slashes), and the corresponding dotted paths are on the right:

.. math::

   \scriptstyle\texttt{src/my_package} \;\Longrightarrow\; \texttt{mypackage} \\

   \scriptstyle\texttt{src/my_package/foo.py} \;\Longrightarrow\; \texttt{mypackage.foo} \\

   \scriptstyle\texttt{src/my_package/my_subpackage} \;\Longrightarrow\; \texttt{mypackage.my_subpackage} \\

   \scriptstyle\texttt{src/my_package/my_subpackage/baz.py} \;\Longrightarrow\; \texttt{mypackage.my_subpackage.baz}

Note that the `.py` extension is omitted, but other than that the
correspondence is fairly simple.  In an import statement these dotted paths
*always* refer to objects on the filesystem.

Absolute imports of subpackages and modules in packages
-------------------------------------------------------

Now that dotted paths have been covered the discussion of importing modules
that are inside packages is fairly simple: just put the dotted path after the
import statement.  The first component of the dotted path is *always* the
top-level package name (i.e., the name of the directory which is the root of
the package subtree).  For package `my_package` as given above these are
all valid imports using `import` directly:

.. code-block:: python

   import my_package
   import my_package.foo
   import my_package.my_subpackage
   import my_package.my_subpackage as msp
   import my_package.my_subpackage.baz

All these imports result in a `module` object in the namespace which, when used
in an expression, syntactically matches the dotted path (except that the dots
are attribute accesses on `module` objects).  For example, the last import does
not actually add anything to the namespace of the module doing the import.
Instead, it adds the module attribute `baz` to the `my_subspace` namespace.
(At that point the `my_package` object is already in the namespace, and it
already has the attribute `my_subpackage`.)

This is a general property of bare `import` statements: After a bare `import`
the dotted-path used to make the import is always usable in Python expressions
in the importing module.  But in those expressions the dot symbol represents
attribute access, unlike in the import statement itself.  This will be
discussed further in the next subsection.

Python uses its `sys.modules` cache for dotted-path imports, too.  It goes down
the names on the dotted path and if it finds one that has not previously been
imported then it imports the remainder of the dotted path from the filesystem.
Any previously-imported packages or modules are taken from the cache.

Imports using `from` also work for dotted paths.  The imports below are all
valid imports for package `my_package`.  They correspond to the imports above
(except for the first one, which has no corresponding `from` import).  After
the import, though, only the package or module following the `import` keyword
is added to the namespace of the importing module (as `module` objects,
renamed in the third case):

.. code-block:: python

   from my_package import foo
   from my_package import my_subpackage
   from my_package import my_subpackage as msp
   from my_package.my_subpackage import baz

Imports using `from` can also be used to import particular attributes from the
namespaces of packages and modules.  For example, if the namespace of module
`foo` contains a variable `foo_var` then that variable can be imported with
this statement:

.. code-block:: python

   from my_package.foo import foo_var

In fact, attributes inside package and module namespaces can *only* be imported
using a `from` import statement, never with a bare `import` statement.  This is
discussed further in the next subsection.

Possible confusions in import syntax
------------------------------------

One possibly-confusing aspect of Python imports is that the dot symbol is
overloaded in Python's syntax.  In Python expressions the dot is used for
attribute access, such as in `my_class.my_attribute`.  But in the dotted paths
of import statements the dot essentially means "subdirectory" and should be
thought of more as a "/" character in a pathname.  Import statements are an
exception in that they are the only statements where the dot syntax means
something other than attribute access.  In import statements the dot can *only*
be part of a dotted path.

Consider these valid import statements, assuming that `foo_var` is a variable
assigned in `foo.py`:

.. code-block:: python

    from my_package import foo # Works.
    import my_package.foo # Works.

After the second import above the statement `my_package.foo` is definitely
usable in Python expressions, as is `my_package.foo.foo_var`.  The latter is
valid because the initial module-scope attributes of `foo` are created when it
is imported and initialized, and they are also attributes of the corresponding
`module` object.

The first import above is essentially the same as the second one except that
the `module` object for `foo` is imported to the name `foo`.

Given the apparent pattern above the following may seem like it should work,
but it is not allowed:

.. code-block:: python

    from my_package.foo import foo_var # Works.
    import my_package.foo.foo_var # FAILS!
    import my_package.foo.foo_var as fv # Also FAILS!

The first import works because `from` imports are allowed to import attributes
from the namespaces of packages and modules.  But the second import fails
because bare `import` statements cannot be used to import attributes from the
namespace of packages and modules.  Bare `import` statements can only be passed
dotted paths, which correspond to files and directories in the filesystem but
not things inside modules.  Renaming doesn't change that, so the third import
also fails.  This holds even when the expression `my_package.foo.foo_var` is
usable in Python expressions.

Another thing you cannot do is assign Python variables as aliases to dotted
paths.  So, while it seems like it would be convenient, this code does not
work:

.. code-block:: python

    import my_package.foo as mpf # Works.
    from mpf import foo_var # FAILS! Only dotted paths directly after from statements.

Although the attribute-access pattern of modules mimics the dotted-path
syntax, they are not the same thing.  The variable `mpf` is a reference
to the `module` object for `foo`.  It cannot be substituted for a dotted path.

Since references to module objects cannot be used in import statements, the full
dotted paths must always be entered.  Relative dotted paths, covered in the
next section, can simplify some cases of having to write out the full dotted
paths.

To avoid these possible confusions, remember that dotted paths in Python import
statements always refer to filesystem objects (either directories or `.py`
files).  **The first specifier in any import statement, whether a bare**
`import` **or a** `from` **import, can only be a dotted path**.

Relative imports
================

We saw in the previous section that dotted paths in absolute import statements
must always be typed out in full.  In the case of **intra-package imports**,
i.e., imports from subpackages and modules inside the same package, relative
imports can often be used to simplify the dotted-path expressions.  Keep in
mind that relative imports are *only* allowed for intra-package imports; all
other imports must use absolute imports.

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
  following correspondences hold inside the `foo` module (located in directory
  `my_package`).  The first two are equivalent filesystem paths relative to
  directory `src/my_package`, and the last one is the Python dotted path.
  (Note in the second line that while `bar` without the dot is also an
  equivalent relative pathname in a shell, as a dotted path it is *only*
  allowed as a top-level absolute import from `sys.path`.)

.. math::

   \scriptstyle\texttt{my_package} \;\Longleftrightarrow\;\; \texttt{.} \;\;\Longrightarrow\; \texttt{.} \\

   \scriptstyle\texttt{my_package/bar.py} \;\Longleftrightarrow\; \texttt{./bar.py} \;\Longrightarrow\; \texttt{.bar} \\

   \scriptstyle\texttt{my_package/my_subpackage/baz.py} \;\Longleftrightarrow\; \texttt{./my_subpackage/baz.py} \;\Longrightarrow\; \texttt{.my_subpackage.baz} \\

* Two dots refer to the parent directory of the directory containing the
  module.  They can occur alone or at the beginning of a longer dotted path.
  The following correspondence holds inside the `baz` module (which is located
  in directory `my_subpackage`).  The first two are equivalent filesystem paths
  relative to directory `src/my_package/my_subpackage` and the last one is the
  Python dotted path:

.. math::

   \scriptstyle\texttt{my_package} \;\Longleftrightarrow\;\; \texttt{..} \;\;\Longrightarrow\; \texttt{..} \\

   \scriptstyle\texttt{my_package/bar.py} \;\Longleftrightarrow\; \texttt{my_package/my_subpackage/../bar.py} \;\Longrightarrow\; \texttt{..bar}

* Each additional dot goes up one more directory level.

Suppose there were another subpackage named `sibling` at the same level as
`my_subpackage`.  Then a module `cousin` in it could be imported from `baz` by
going up and then down as follows:

.. math::

  \scriptstyle\texttt{my_package/sibling/cousin} \;\Longrightarrow\; \texttt{..sibling.cousin}

Relative imports
----------------

Now that relative dotted paths have been covered, relative imports are
straightforward: just use a relative dotted path instead of an absolute dotted
path (but remember that they are only allowed for intra-package imports).

There is another important restriction on relative imports: **A relative dotted
path can only appear after a** `from` **statement.**  It seems like you should
be able to write imports such as `import .bar` from the `foo` module and
`import ..bar` from `baz` module, but those are syntax errors.  The reason this
is not allowed is that the relative dotted paths (such as `.bar`) after bare
`import` statements are not valid Python names and therefore cannot be used in
Python expressions as attribute accesses.

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

In addition to importing modules and subpackages from the specified directory,
`from` imports using only-dot paths such as `.` and `..` can also be used to
import attributes from package and subpackage namespaces (i.e., from
`__init__.py` namespaces)  For example, this import from module `foo` would
import the variable `init_var` defined in module `my_package.__init__.py`:

.. code-block:: python

    from . import init_var

Imports in scripts
==================

A **script** is any Python module which is directly run by the Python
interpreter.  This can be done from the command line with the `python` command,
by clicking an icon, or via some other invocation method such as from a menu.
Python applications are usually started by running a Python module
as a script.

Scripts have a few unique properties not shared by other modules:

1. The directory containing the script file is automatically inserted to
   `sys.path[0]` when the script is run by the Python interpreter.   The
   absolute directory path is always added; the current working directory, in
   the shell or in Python, has no effect on this.

2. The `__name__` attribute of the script's module is always set to
   `"__main__"` when it is run as a script, regardless of the file's name.

3. By default a script is not run as part of a package, even if there happens
   to be an `__init__.py` in its directory.

Property 1 allows a script to import any package or module which is located in
its directory as an absolute, non-dotted import.  This is helpful if the
directory contains top-level packages or standalone modules that are intended
to be imported.  In some situations this can cause problems such as unintended
imports due to name shadowing and importing modules inside packages as if they
were standalone modules.

Property 2 is what allows the use of this common idiom in Python scripts:

.. code-block:: python
 
   if __name__ == "__main__":
       main() # A commonly-seen example, running function `main`.
   
Code in that conditional block only executes when the module is directly run as
a script and not when the module is imported from another Python module (some
modules are meant to be used both ways).

Scripts outside of packages
---------------------------

The standard idiom for Python scripts is that they should be located outside of
packages.  The script can then load any packages or modules it needs.  There
are some use cases for scripts inside packages, which will be covered in the
subsection after this one.

The rule for imports in scripts located outside packages is simple: scripts
outside packages can only use absolute imports.  Any absolute imports are
allowed, but of course modules inside packages should almost always be imported
as part of their package, using the dotted-path syntax relative to their
package root, rather than as a non-dotted import.  In some cases
it may be necessary to insert elements to `sys.path[1]` (after the current
directory at `sys.path[0]`) in order for Python to discover the necessary
modules and packages to import.

If you use a `setup.py` for your project then scripts outside packages `can be
added to a project
<https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html>`_
by using the `scripts` keyword argument.  For development this involves setting
up the project with a `setup.py` and then installing the project in development
mode, such as by running `pip install -e .` in the directory with `setup.py`.
(The `setup.py` file is usually placed in the project's root directory, which
is `my_project` in the project skeleton given earlier).  This provides a shell
command for running the script which is in the shell search path.  To add or
remove scripts from the project the `setup.py` must be modified and the package
reinstalled.  A similar thing can be done using the more-recent
`pyproject.toml` files if you use that method to set up projects rather than
using a `setup.py`.

Scripts inside packages
-----------------------

Scripts can also be run inside packages, but the special properties of scripts
listed above have some side-effects which need to be taken into account.

Property 3 means that the package the script is inside of is not automatically
imported when the script runs.  To import modules from the package the script
can only use non-dotted absolute imports (based on Property 1).  This only
works correctly in simple cases where the imported modules are essentially
standalone modules themselves.  Even if the script itself imports the full
package in the usual way the running script is still not correctly set up as a
module of the package.

If the script does explicitly import its containing package then dotted
absolute imports from the package will work.  But the script module itself
should never be imported by any other module in the package since it is cached
as the `__main__` module by Property 2 and a double import will result.

To get around these problems and correctly run scripts inside packages what is
needed is a way to automatically import the containing package and then run the
script as a part of the package.  There are several possible ways to do this:

1. Invoke the script using `python -m <fullyQualifiedName>`, where
   `<fullyQualifiedName>` is the fully-qualified name of the module inside the
   package (i.e., the absolute dotted path).  Note that the directory
   containing the top-level package directory must be in `sys.path` or the
   command will fail.  You could write a shell script wrapper for the `python`
   command to modify `PYTHONPATH`, calculate the qualified name, and then
   invoke `python -m`.  Generally, though, the invocation differs from that of
   other Python scripts.

2. Set the `__package__` attribute of the script to the fully-qualified name
   and then import the package in the correct way.  This is more complex than
   you might expect, but fortunately there is a `package on PyPI
   <https://abarker.github.io/set-package-attribute/>`_ which can do this for
   you automatically (and optionally also remove the directory's `sys.path`
   entry).

3. Create a `setup.py` file and `create an entry point
   <http://www.python.org/>`_ for the script via the `console_scripts` keyword.
   (This is similar to the `scripts` keyword described above, but it allows
   modules inside packages to be run via an entry-point function.)  To add or
   remove entry points the `setup.py` file must be modified and the package
   reinstalled.  This creates commands which are directly executable in the
   shell, under the name specified in `setup.py`.

Not covered
===========

This article has covered the basics of the Python import system, but some
important topics have not been discussed.  They tend to occur or be used in
special or advanced cases.

**Star imports**: By default, the statement `from my_module import *` imports
all the names in the `my_module` namespace which do not start with the
underscore character.  If `__all__` is defined in `my_module` as a list of
string variable names then `*`-imports from the module will only import those
names.  Anything else would need to be explicitly imported.  The `__all__` list
for an `__init__.py` file can also contain the names of modules and subpackages
to import: a `*`-import of the corresponding package or subpackage will then
implicitly perform the imports (which need to be done explicitly for ordinary
modules).

**Circular imports.**  This problem can arise when one module imports another
module which then imports the first module again.  The usual solution is to
reorganize the module structure or to put the problematic import inside a
function so it is not performed on module initialization.  Circular imports are
discussed in the answer to this Python FAQ question: "`What are the 'best
practices' for using import in a module?
<https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module>`_"

.. _namespace-packages:
 
**Namespace packages**: Namespace packages allow one or more toplevel
directories having the same directory name, but without `__init__.py` files, to
be used like a common namespace for all the modules and packages across all the
directories (which must all be discoverable on `sys.path`).  This can be useful
for large distributions, but there are also drawbacks such as the lack of
`__init__.py` files.  Most people should continue to use `__init__.py` files to
create single-directory packages.

**pth files**: Pth files are special files which contain the pathnames of
packages or modules to import.  Using pth files only works when they are placed
in the special system `site-packages` directory.

**Importing from zip files**: Python allows modules to be imported from
zipfiles, provided the `.zip` archive file is located on `sys.path`.   The
directory structure in the zip file then acts as a regular directory.

**Lower-level APIs of the import system.**  The `full Python import system
<https://docs.python.org/3/reference/import.html>`_ is complicated and
customizable.  There are protocols to allow it to be dynamically modified in
various ways for special applications.

Further reading
===============

* The official Python documentation on `imports
  <https://docs.python.org/3/reference/import.html>`_ and
  `modules <https://docs.python.org/3.7/tutorial/modules.html>`_. 

* A detailed `guide to Python imports
  <https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html>`_ by Chris Yeh.

* An `introduction to absolute vs. relative imports
  <https://realpython.com/absolute-vs-relative-python-imports>`_, including a discussion
  of formatting style.   By Mbithe Nzomo.

* A discussion of some of the often subtle `import traps
  <http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html>`_
  which can arise, by Nick Coghlan.

