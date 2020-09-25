# Parsing command-line arguments and handling unsupported options

import sys

from constant import supported_languages, actions


class Args:

    def __init__(self, action, lan_args=None, args_word=None):
        # handling unsupported action
        if action not in actions:
            try:
                print("_ERROR\n Unexpected action: %s" % str(action))
                print(" Try \'trans --help\' for more information.")
                sys.exit(20)
            except:
                sys.exit(20)
        self.action = action
        self.lan_args = lan_args
        self.args_word = args_word

    def __str__(self):
        return "<Args object, action: %s, lan_args: %s>" % (self.action, self.lan_args)


def parse(args):

    opt = []
    args_word = []

    # get options and arguments from command-line
    for i in args:
        if i[0] == '-':
            opt.append(i)
        else:
            args_word.append(i)

    # get language arguments
    lan_args = [i for i in opt if i in supported_languages]

    # raising error for unsupported arguments
    supported_args = [*supported_languages, "-c", "--help", "--version"]
    for i in opt:
        if i not in supported_args:
            print("_ERROR\n Invalid option -- \'" + i[1:] + "\'")
            print(" Try \'trans --help\' for more information.")
            exit(2)

    # show help
    if "--help" in opt:
        return Args("HELP")

    # show version
    if "--version" in opt:
        return Args("VERSION")

    # raise error if there was no language option
    if not lan_args:
        print("_ERROR\n At least one language option must be set.")
        print(" Try \'trans --help\' for more information.")
        exit(3)

    # raise error if there was more than 2 language options
    if len(lan_args) > 2:
        print("_ERROR\n Too many language options.")
        print(" Try \'trans --help\' for more information.")
        exit(3)

    # if there was one language option set the first one to "auto"
    if len(lan_args) == 1:
        lan_args.insert(0, "-auto")

    # raise error if there was no language option
    if lan_args[0] == lan_args[1]:
        print("_ERROR\n Two language options cannot be the same.")
        print(" Try \'trans --help\' for more information.")
        exit(3)

    # if language option was -zh, change it to -zh-CN
    if "-zh" in lan_args:
        lan_args[lan_args.index("-zh")] = "-zh-CN"

    if "-c" in opt:
        return Args("TRANSLATE_CLIPBOARD", lan_args)

    if args_word:
        return Args("TRANSLATE_COMMANDLINE", lan_args, args_word)

    return Args("TRANSLATE_INPUT", lan_args)


if __name__ == "__main__":
    print(parse(sys.argv[1:]))
