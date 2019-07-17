Setting Up Spellchecking in Vim
###############################

:date: 2019-07-16 14:13
:modified: 2019-07-16 14:13
:category: vim
:tags: vim, editor
:authors: Allen Barker
:summary: Short instructions for setting up vim for spellchecking.

.. contents::
    :depth: 2

1. Create a subdirectory of your ``.vim`` directory to hold the dictionary of new words:

   .. code-block:: bash

      mkdir -p ~/.vim/spell

2. Add the following lines to your ``~/.vimrc`` file.  Change the ``en`` part if you
   are spellchecking some language other than English:

   ::

      set spelllang=en
      set spellfile=$HOME/.vim/spell/en.utf-8.add

After these steps vim is set up for spellchecking.  Open a text file in vim.  Now these
commands are available:

=====================            ==========================================================
  Command                        Action
=====================            ==========================================================
  ``:setlocal spell``            Turn on spellchecking.
  ``:set nospell``               Turn off spellchecking.
  ``]s``                         Goto next misspelled word.
  ``[s``                         Goto previous misspelled word.
  ``zg``                         Add the current "good" word to your local dictionary.
  ``z=``                         Suggest spellings (choose a number or hit enter for none).
  ``zw``                         Mark the current word as wrong.
=====================            ==========================================================

The misspelled words should be highlighted when spellchecking is turned on.

