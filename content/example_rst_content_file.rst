Example RST content
###################

:date: 2016-06-16 14:13
:modified: 2016-06-16 14:13
:category: misc
:tags: misc
:authors: Allen Barker
:summary: An example rst article.

Examples to look at.

Math
----

Some math :math:`A_\text{c} = (\pi/4) d^2`.

And some inline math:

.. math::

   x_i = \int_0^{1000} \sin(x) \mathrm{d}x

Inline code
-----------

A code example to consider, uses only two colons at end::

   for f in fruits:
       print("The fruit is", f)


Some inline Python: :code:`for i in egg: break i`.  Note that variable :code:`egg`
is used.  Using double backtics instead of inline code gives ``egg`` as the variable name.

.. default-role:: code

Some default inline Python with single backtics but after setting code as default role: `import j; print("x")`.

.. code-block:: python

   for f in fruits:
       print("The fruit is", f)

Some Bash code:

.. code-block:: bash

   for i in *
   do
      echo "$i"
   done


Images and figures
------------------

A picture `here is a lovely picture <{filename}/images/oldguitar.jpg>`_

Here is an inline image:

.. image:: {filename}/images/oldguitar.jpg
    :width: 200px
    :align: center
    :alt: alternate text

And here is a figure:

.. figure:: {filename}/images/oldguitar.jpg
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

Some links `a relative link, relative to the current file
<{filename}./example_markdown_content_file_DRAFT.md>`_ and `an "absolute" link,
relative to the content root
<{filename}/example_markdown_content_file_DRAFT.md>`_.

Examples of a URL, one in text and another defined: `Python
<http://www.python.org/>`_ and Python_.

For more links, see http://docutils.sourceforge.net/docs/user/rst/quickref.html#external-hyperlink-targets
