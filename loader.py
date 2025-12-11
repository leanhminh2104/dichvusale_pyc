"""


class PycImporter:
"""A finder/loader that finds literal `.pyc` files and returns a spec with
SourcelessFileLoader so Python can load it as a normal module.


Behavior:
- When an import occurs, `find_spec` inspects the provided `path` (or sys.path if None)
for files named `<modname>.pyc`.
- If found, it returns a ModuleSpec using `SourcelessFileLoader` pointing to that file.
- This does not affect imports when a `.py` exists nearby; Python's normal import
mechanism and cached `.pyc` handling remain unchanged.
"""


def _search_paths(self, fullname: str, path: Optional[Iterable[str]]):
base_name = fullname.split(".")[-1]
if path is None:
paths = list(sys.path)
else:
paths = list(path)


for base in paths:
if not base:
base = os.getcwd()
# plain <module>.pyc
yield os.path.join(base, base_name + ".pyc")


# search __pycache__/ for compiled file matching base_name
pycache = os.path.join(base, "__pycache__")
if os.path.isdir(pycache):
for fname in os.listdir(pycache):
if fname.startswith(base_name) and fname.endswith(".pyc"):
yield os.path.join(pycache, fname)


def find_spec(self, fullname, path, target=None):
# try to find a literal .pyc to load
for candidate in self._search_paths(fullname, path):
if os.path.exists(candidate):
loader = importlib.machinery.SourcelessFileLoader(fullname, candidate)
spec = importlib.util.spec_from_loader(fullname, loader, origin=candidate)
return spec
return None




_installed = False




def install():
"""Install the PycImporter into sys.meta_path (idempotent).


Typical usage: `import dichvusale_pyc.loader` or `dichvusale_pyc.install()`
at the top of your application before importing `.pyc`-only modules.
"""
global _installed
if _installed:
return
# Insert at front to give priority when explicit .pyc files are present.
sys.meta_path.insert(0, PycImporter())
_installed = True




# Auto-install when module is imported, for convenience. Importers who prefer
# explicit control can import this module without side effects by calling
# install() only; but auto-install is helpful for the "pip-install and go" case.
install()
