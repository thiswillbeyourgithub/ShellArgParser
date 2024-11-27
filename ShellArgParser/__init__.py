
from .ShellArgParser import ShellArgParser

__all__ = ["ShellArgParser"]

__VERSION__ = ShellArgParser.__VERSION__

def cli_launcher() -> None:
    ShellArgParser()

if __name__ == "__main__":
    cli_launcher()
