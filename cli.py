"""Small CLI so users can compile files or install the import hook via console.


Entry point defined in pyproject.toml as `dichvusale-pyc`.
"""


import argparse
import sys
from . import install as install_hook
from .util import compile_file, compile_directory




def main(argv=None):
argv = argv if argv is not None else sys.argv[1:]
p = argparse.ArgumentParser(prog="dichvusale-pyc", description="dichvusale .pyc importer and compiler")
sub = p.add_subparsers(dest="cmd")


install = sub.add_parser("install", help="Install the .pyc import hook for the running interpreter")
install.set_defaults(func=lambda args: install_hook() or print("hook installed"))


comp = sub.add_parser("compile", help="Compile a single .py file to .pyc")
comp.add_argument("src", help="Source .py file")
comp.add_argument("-o", "--out", dest="out", help="Output .pyc path (optional)")
comp.set_defaults(func=lambda args: print(compile_file(args.src, args.out)))


compdir = sub.add_parser("compiledir", help="Compile whole directory recursively")
compdir.add_argument("path", help="Directory path")
compdir.add_argument("-f", "--force", action="store_true", help="Force recompilation")
compdir.set_defaults(func=lambda args: print(compile_directory(args.path, args.force)))


args = p.parse_args(argv)
if not hasattr(args, "func"):
p.print_help()
return 1
try:
args.func(args)
except Exception as e:
print("Error:", e, file=sys.stderr)
return 2
return 0




if __name__ == "__main__":
raise SystemExit(main())
