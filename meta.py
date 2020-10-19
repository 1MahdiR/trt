VERSION = "2.1.0"


def help():
    """display help"""

    print()
    print("Usage:  trt [OPTIONS] [ARG]...\n")
    print("A CLI script to translate text on terminal via 'translate.google.com'\n")
    print("At least one language option must be specified.")
    print("Language options:")
    print("  {0:<14}Persian".format("-fa"))
    print("  {0:<14}English".format("-en"))
    print("  {0:<14}French".format("-fr"))
    print("  {0:<14}Dutch".format("-de"))
    print("  {0:<14}Russian".format("-ru"))
    print("  {0:<14}Chinese".format("-zh"))
    print("  {0:<14}Japanese".format("-ja"))
    print("  {0:<14}Turkish".format("-tr"))
    print("  {0:<14}Korean".format("-ko"))
    print("  {0:<14}Italian".format("-it"))
    print("  {0:<14}Spanish".format("-es"))
    print()
    print("If one language option was specified it will be set as target language\n"
          "and the source language will be set as 'auto'.\n")
    print("Options:")
    print("  {0:<14}get the arguments from clipboard".format("-c"))
    print("     {0:<14}display this help and exit".format("--help"))
    print("     {0:<14}output version information and exit".format("--version"))
    print()


def version():
    """display version information"""

    print("trt v{}".format(VERSION))
    print("Script by MR.")
    print("Source code is available on gitlab and github.")
    print("gitlab: https://gitlab.com/__mr__/trt/-/tree/trt_v2")
    print("github: https://github.com/1MahdiR/trt/tree/trt_v2")


if __name__ == "__main__":
    version()
