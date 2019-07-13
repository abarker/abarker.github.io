Example RST content
###################

:date: 2016-06-16 14:13
:modified: 2016-06-16 14:13
:category: misc
:tags: misc
:authors: Allen Barker
:summary: An example rst article.

.. contents::
    :depth: 2

Examples to look at.

Math
----

Some inline math :math:`A_\text{c} = (\pi/4) d^2`.

And some display math:

.. math::

   x_i = \int_0^{1000} \sin(x) \mathrm{d}x

Inline code
-----------

Some inline Python: :code:`for i in egg: break i`.  Note that variable :code:`egg`
is used.  Using double backtics instead of inline code gives ``egg`` as the variable name.

.. default-role:: code

Some default inline Python with single backtics but after setting code as default role: `import j; print("x")`.

.. code-block:: python

   class Test:
       def __init__(self):
         for f in fruits:
             print("The fruit is", f)

         if x == 4 and y != 4 and "key" in d:
             new_d = {"key" : "value"}

      @staticmethod
      def stat(arg1, arg2=False):
          return arg2 - arg1

Some Bash code:

.. code-block:: bash

   for i in *
   do
      echo "$i"
   done

A code example to consider, uses only two colons at end::

   for f in fruits:
       print("The fruit is", f)

Images and figures
------------------

A picture `here is a lovely picture <{static}/images/oldguitar.jpg>`_

Here is an inline image:

.. image:: {static}/images/oldguitar.jpg
    :width: 200px
    :align: center
    :alt: alternate text

And here is a figure:

.. figure:: {static}/images/oldguitar.jpg
    :align: center
    :width: 100px
    :alt: alternate text
    :figclass: align-center

    figure are like images but with a caption

    and whatever else you add

    .. code-block:: python

       for f in fruits: f.eat()

Links
-----

.. _Python: http://www.python.org/

Some links, first `a relative link, relative to the current file
<{filename}./example_rst_content_file.rst>`_  These links just go to the back to the same
content as an example.  Note the period before the slash.  Here is
`an "absolute" link, relative to the content root <{filename}/example_rst_content_file.rst>`_.

Examples of a URL, one in text and another defined: `Python
<http://www.python.org/>`_ and Python_.

For more links, see http://docutils.sourceforge.net/docs/user/rst/quickref.html#external-hyperlink-targets

