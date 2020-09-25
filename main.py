# trt v1.2.0
# Translate in Terminal
# trt: A command-line script to translate text, by opening a web page
# with a specific url at "translate.google.com".
#
# Written in python.
# GITLAB: https://gitlab.com/__mr__/trt
#

import sys
import pyperclip as pype
import webbrowser as web
import traceback

import meta
from arg_parser import parse
from constant import main_address


def main():

    try:
        # storing an object that contains the arguments and the action to performing on them
        args = parse(sys.argv[1:])

        if not args.lan_args:
            if args.action == "HELP":
                meta.help()
                sys.exit(0)

            if args.action == "VERSION":
                meta.version()
                sys.exit(0)

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
                try:
                    arg.append(input("> "))
                except KeyboardInterrupt:
                    print()
                    sys.exit(0)
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
