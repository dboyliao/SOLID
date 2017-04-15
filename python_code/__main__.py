#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from .good import __all__ as all_submodules
import sys

def main(argv):
    if len(argv) > 1 and argv[1] in ["-l", "--list"]:
        print("Available submodules: ")
        for i, submodule in enumerate(all_submodules, 1):
            print("{}. good.{} / bad.{}".format(i, submodule, submodule))

if __name__ == "__main__":

    main(sys.argv)
