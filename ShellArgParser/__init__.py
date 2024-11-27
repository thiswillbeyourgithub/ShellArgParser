
import sys
import fire

from .ShellArgParser import ShellArgParser

__all__ = ["ShellArgParser"]

__VERSION__ = ShellArgParser.__VERSION__

def cli_launcher() -> None:
    if sys.argv[-1] ==  "--version":
        return(f"ShellArgParser version: {__VERSION__}")
    fire.Fire(ShellArgParser)

if __name__ == "__main__":
    cli_launcher()