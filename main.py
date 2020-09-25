# trt v1.1
# Translate in Terminal
# trt: A command-line script to translate text, by opening a web page
# with a specific url at "translate.google.com".
#
# Written in python.
# GITHUB
#
# Check "constant.py" for supported languages and supported actions

import sys
import pyperclip as pype
import webbrowser as web
import traceback

from arg_parser import parse
from constant import main_address


def main():

    try:
        # storing an object that contains the arguments and the action to performing on them
        args = parse(sys.argv[1:])
        source_lan = args.lan_args[0][1:]
        target_lan = args.lan_args[1][1:]

        if args.action == "TRANSLATE_CLIPBOARD":
            text = "%0A".join(pype.paste().split("\n"))
            web.open(main_address.format(source_lan, target_lan, text))
            sys.exit(0)

        if args.action == "TRANSLATE_COMMANDLINE":
            arg = args.args_word
            text = "%0A".join(arg)
            web.open(main_address.format(source_lan, target_lan, text))
            sys.exit(0)

        if args.action == "TRANSLATE_INPUT":
            arg = []
            # while there is at least one character in input, keep getting input from user.
            while "" not in arg:
                arg.append(input("> "))
            text = "%0A".join(arg)
            web.open(main_address.format(source_lan, target_lan, text))
            sys.exit(0)

    except KeyboardInterrupt:
        print()
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
