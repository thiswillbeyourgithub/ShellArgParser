#!/bin/zsh
#
# Parse arguments of script using python fire
# All -args are parsed as ARGS_i=True
# All --kwargs=bla are parsed as ARGS_key=value
# For example:
# eval $(./shell_arg_parser.sh --test=something -a -b -no-c)
# will create those variable:
# ARGS_A="1"
# ARGS_B="1"
# ARGS_C="0"
# ARGS_TEST="something"
#
# Note:
# -a is parsed as 1
# -no-a is parsed as 0
# Any None value is parsed as 0

# get arguments:
args=( $(python -c "import fire ; fire.Fire(lambda **k: ('\n'.join([f'{key.upper()}={val}' for key, val in k.items()])))" "$@") )

if [ -z "$args" ]
then
    echo "No argument were parsed"
    exit 1
fi

while IFS='=' read -r key value; do

    # Parse True, False and None
    if [[ $value == "True" ]]
    then
        value=1
    elif [[ $value == "False" ]]
    then
        value=0
    elif [[ $value == "None" ]]
    then
        value=0
    fi

    # If a -no-arg is used, then the key will not be arg but _arg
    if [[ $key = _* ]]
    then
        echo "ARGS$key=\"$value\""
    else
        echo "ARGS_$key=\"$value\""
    fi
done < <(printf '%s\n' "${args[@]}")
