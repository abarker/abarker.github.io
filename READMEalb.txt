#!albNotes

Note that preview does not copy the files to the `master` branch, just to the
`output` directory.  Use `publish` to also update `master` branch.

The `custom.css` file contains customizations for the Elegant theme.

## syntax highlights, pygments.css

Note that I no longer use the `pygments.css` file, and instead just append the
highlighting code (generated by the program `generate_css_and_postprocess.py`
in the $py directory) to the `custom.css`.  Note that if `alb.py` is modified
it must be copied to pygments style subpackage.  There is a script in that dir
to do the copy when run under a VENV.

# future

Automate generation more, getting closer.

Consider importing a `pygments.css` in the static dir into the `custom.css` file.
   https://stackoverflow.com/questions/147500/is-it-possible-to-include-one-css-file-in-another

