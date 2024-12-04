import fire
import sys
import os

class ShellArgParser:
    __VERSION__: str = "0.2.1"

    def __init__(
        self,
        ) -> None:
        # redirect the sys stdout when running fire, otherwise we sometimes get a verbose print
        sys.stdout = open(os.devnull, 'w')
        try:
            args, kwargs = fire.Fire(lambda *arg, **kwargs: (arg, kwargs))
        except Exception:
            sys.stdout = sys.__stdout__
            raise
        finally:
            sys.stdout = sys.__stdout__

        output = ""

        for arg in args:
            arg = arg.upper()
            assert "=" not in arg, f"Found a '=' sign in arg: '{arg}'"
            assert f"ARGS_{arg}=" not in output, f"Arg {arg} seems already parsed! Duplicate?"
            while arg.startswith("_"):
                arg = arg[1:]

            output += f"\nARGS_{arg}=1"

        for k, v in kwargs.items():
            k = k.upper()
            while k.startswith("_"):
                k = k[1:]
            if v is True:
                v = 1
            if v in [False, None]:
                v = 0

            while str(v).startswith("'") and str(v).endswith("'"):
                v = str(v)[1:-1]

            while str(v).startswith("\"") and str(v).endswith("\""):
                v = str(v)[1:-1]

            assert f"ARGS_{k}=" not in output, f"Arg {arg} seems already parsed! Duplicate?"

            if str(v).isdigit():
                output += f"\nARGS_{k}={v}"
            else:
                output += f"\nARGS_{k}=\"{v}\""


        print(output)
