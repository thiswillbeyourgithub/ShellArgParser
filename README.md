
# ShellArgParser
A simple python tool to parse any arg / kwarg arguments in a manner that is easy to parse for the linux shell.

## I don't understand
For example:
```sh
uvx ShellArgParser@latest a_file --test=something -a -b -no-c another_file
```
Will print this text:
```sh
ARGS_1="a_file"
ARGS_2="another_file"
ARGS_TEST="something"
ARGS_A=1
ARGS_B=1
ARGS_C=0
```

So running this:
```sh
eval $(uvx ShellArgParser@latest --test=something -a -b -no-c)
```
Will parse the args and kwargs as shell environment variables, handy for use in the shell:
```sh
echo $ARGS_TEST  # outputs 'something'
```

## But why would you make this?
Handling user arguments are a major annoyance for me in shell, and in python using `fire` makes it a breeze, so it's is a great way to avoid reinventing the wheel.
Hence, when writing a small shell script, using a python cli tool oneliner makes is a real time saver for me.

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
