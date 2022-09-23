# tutobooks

**Note: All code credit to Francois Chollet, I simply bundled this into a pip package because I wanted to use it for more than keras.io**

Taken from [keras-io/scripts](https://github.com/keras-team/keras-io).

A tutobook is a tutorial available simultaneously as a notebook,
as a Python script, and as a nicely rendered webpage.

Its source-of-truth (for manual edition and version control) is
its Python script form, but you can also create one by starting
from a notebook and converting it with the command `nb2py`.

Text cells are stored in markdown-formatted comment blocks.
the first line (starting with " * 3) may optionally contain a special
annotation, one of:

- invisible: do not render this block.
- shell: execute this block while prefixing each line with `!`.

The script form should start with a header with the following fields:

```
Title:<br>
Author: (could be `Authors`: as well, and may contain markdown links)<br>
Date created: (date in yyyy/mm/dd format)<br>
Last modified: (date in yyyy/mm/dd format)<br>
Description: (one-line text description)<br>
```
You would typically start from an existing notebook.

Save it to disk (let's say as `path_to_your_nb.ipynb`).

Then run:

```
python tutobooks nb2py path_to_your_nb.ipynb ../examples/your_example.py
```

This will create the file `examples/your_example.py`. Open it,
fill in the headers, and generally edit it so that it looks nice.

NOTE THAT THE CONVERSION SCRIPT MAY MAKE MISTAKES IN ITS ATTEMPTS
TO SHORTEN LINES. MAKE SURE TO PROOFREAD THE GENERATED .py IN FULL.
Or alternatively, make sure to keep your lines reasonably-sized (<90 char)
to start with, so that the script won't have to shorten them.

You can then preview what it looks like when converted back again
to ipynb by running:

```
python tutobooks py2nb ../examples/your_example.py preview.ipynb
```

NOTE THAT THIS COMMAND WILL ERROR OUT IF ANY CELLS TAKES TOO LONG
TO EXECUTE. In that case, make your code lighter/faster.
Remember that examples are meant to demonstrate workflows, not
train state-of-the-art models. They should
stay very lightweight.

Open the generated `preview.ipynb` and make sure it looks like what
you expect. If not, keep editing `your_example.py` until it does.

Finally, submit a PR adding `examples/your_example.py`.
"""
