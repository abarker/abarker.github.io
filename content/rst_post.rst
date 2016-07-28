RST example
###########

:date: 2016-06-16 14:13
:modified: 2016-06-16 14:13
:category: misc
:tags: first, misc
:authors: Allen Barker
:summary: An rst article.

.. :slug: Another-post

Some math :math:`A_\text{c} = (\pi/4) d^2` and a 
code example to consider::

   for f in fruits:
       print("The fruit is", f)

Some inline Python: :code:`for i in egg: break i`.

.. default-role:: code

Some default inline Python: `import j; print("x")`.

.. code-block:: python

   for f in fruits:
       print("The fruit is", f)

And some inline math:

.. math::

   x_i = \int_0^{1000} \sin(x) \mathrm{d}x

Some links `a relative link, relative to the current file <{filename}./another_post.md>`_
and `an "absolute" link, relative to the content root <{filename}/another_post.md>`_.

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

