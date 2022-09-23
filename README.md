# tutobooks

**Note: All code credit to Francois Chollet, I simply bundled this into a pip package because I wanted to use it for more than keras.io**

Taken from [keras-io/scripts](https://github.com/keras-team/keras-io).

## Overview

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
Title:
Author: (could be `Authors`: as well, and may contain markdown links)
Date created: (date in yyyy/mm/dd format)
Last modified: (date in yyyy/mm/dd format)
Description: (one-line text description)
```
You would typically start from an existing notebook.

Save it to disk (let's say as `path_to_your_nb.ipynb`).

Then run:

```
tutobooks nb2py path_to_your_nb.ipynb your_example.py
```

This will create the file `your_example.py`. Open it,
fill in the headers, and generally edit it so that it looks nice.

You can then preview what it looks like when converted back again
to ipynb by running:

```
python tutobooks py2nb your_example.py preview.ipynb
```

Open the generated `preview.ipynb` and make sure it looks like what
you expect. If not, keep editing `your_example.py` until it does.

## Usage

Conversion to markdown:

```bash
tutobooks nb2md mypath.ipynb mypath.md
```

Conversion to python:

```bash
tutobooks nb2py mypath.ipynb mypath.py
```

Conversion to markdown from python:

```bash
tutobooks py2md mypath.py mypath.md
```

