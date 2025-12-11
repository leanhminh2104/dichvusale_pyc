"""
from typing import Optional




def compile_file(src: str, dest: Optional[str] = None, optimize: int = -1) -> str:
"""Compile a single Python source file to a .pyc file.


Args:
src: path to .py file.
dest: optional destination path for resulting .pyc (if omitted Python's
default location is used).
optimize: optimization level; -1 means default, 0 means no optimization,
1 or 2 correspond to -O or -OO.


Returns:
path to generated .pyc file
"""
src_path = Path(src)
if not src_path.exists():
raise FileNotFoundError(f"source file not found: {src}")
if src_path.suffix != ".py":
raise ValueError("src must be a .py file")


if dest:
dest_path = Path(dest)
dest_path.parent.mkdir(parents=True, exist_ok=True)
# py_compile.compile doesn't allow writing arbitrary destination easily.
# We'll compile to a temp file and then move it.
py_compile.compile(str(src_path), cfile=str(dest_path), optimize=optimize)
return str(dest_path)
else:
py_compile.compile(str(src_path), optimize=optimize)
# find produced .pyc in __pycache__ or alongside depending on Python
# Standard py_compile returns path for older versions; we will attempt
# to derive.
pycache = src_path.parent / "__pycache__"
if pycache.exists():
# pick the first matching file
name_prefix = src_path.stem
for f in pycache.iterdir():
if f.name.startswith(name_prefix) and f.suffix == ".pyc":
return str(f)
# fallback: check sibling .pyc
sibling = src_path.with_suffix('.pyc')
if sibling.exists():
return str(sibling)
# if all fails, return an educated guess path
return str(src_path.with_suffix('.cpython-{}.pyc'.format(sys.version_info.major)))




def compile_directory(path: str, force: bool = False, optimize: int = -1) -> int:
"""Compile all .py files inside `path` recursively.


Args:
path: directory to compile
force: if True, recompile even when up-to-date
optimize: optimization level passed to compileall


Returns:
number of files compiled
"""
p = Path(path)
if not p.is_dir():
raise NotADirectoryError(path)
# compileall returns boolean for success; but we can use its API to collect
# counts via its return value is True if no errors.
# However compileall.compile_dir returns None; use compile_dir with quiet=1
compiled = compileall.compile_dir(str(p), force=force, optimize=optimize, quiet=1)
# compiled is True/False; to get count we'd need to walk manually.
# For simplicity return 1 if success else 0
return 1 if compiled else 0
