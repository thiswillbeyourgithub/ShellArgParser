
# ShellArgParser
A simple python tool to parse any arg / kwarg arguments in a manner that is easy to parse for the linux shell.

## I don't understand
For example:
```sh
uvx ShellArgParser@latest --test=something -a -b -no-c
```
Will print this text:
```sh
ARGS_A=1
ARGS_B=1
ARGS_C=0
ARGS_TEST="something"
```

So running this:
```sh
eval $(uvx ShellArgParser@latest --test=something -a -b -no-c)
```
Will parse the args and kwargs as shell environment variables, handy for use in the shell:
```sh
echo $ARGS_TEST  # outputs 'something'
```

## Notes:
- `-something` is parsed as `ARGS_SOMETHING=1`
- `-no-something` is parsed as `ARGS_SOMETHING=0`
- `-no_something` is parsed as `ARGS_SOMETHING=0`
- Any `None` python value is parsed as `0`
- A prototype 'pure shell' version of this script can be found in `./ShellArgParser.sh`

# Getting started
* From pypi:
    * As a uv tool: `uvx ShellArgParser@latest --help`
    * Via uv: `uv pip install ShellArgParser`
    * Via pip: `pip install ShellArgParser`
* From github:
    * Clone this repo then `pip install .`
