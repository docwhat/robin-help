#!/usr/local/bin/python3

import sys


class Robin(object):
    def __init__(self):
        self.some_variable = 10

    def __str__(self):
        return "Bloop! %d" % self.some_variable


class Oscar(Robin):
    pass


if __name__ == "__main__":
    r = Oscar()
    print("Hello, Fishy!")
    print(str(r))

    sys.stdout.write("STDOUT!\n")

# EOF
