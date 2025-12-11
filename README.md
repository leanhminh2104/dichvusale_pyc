# dichvusale-pyc


Small package to allow importing `.pyc` files as modules (fallback when `.py` is missing) and to compile `.py` files to `.pyc`.


**Copyright (c) 2025 dichvusale.io.vn**


## Features


- Installable import hook that finds literal `module.pyc` or `__pycache__/module.*.pyc` and loads it
- Utilities to compile a single file or whole directories
- Lightweight CLI: `dichvusale-pyc install | compile | compiledir`


## Install


Build and install locally:


```bash
python -m build
pip install dist/dichvusale_pyc-0
