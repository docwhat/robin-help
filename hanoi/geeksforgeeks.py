#!/usr/bin/python
# Recursive Python function to solve tower of hanoi

import sys


def move(n, from_rod, to_rod):  # {
    sys.stdout.write("Move disk %2d from rod %s to rod %s" % (n, from_rod, to_rod))
    sys.stdout.write((" n =  %%%ds" % (3 * n)) % n)
    sys.stdout.write("\n")

    return


# }


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):  # {
    if n == 0:  # {
        return
    # }

    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)

    move(n, from_rod, to_rod)

    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

    return


# }


# Driver code
n = 5
TowerOfHanoi(n, "A", "C", "B")

# A, C, B are the name of rods

# Contributed By Harshit Agrawal

#           4
#     3           3
#   2    2     2     2
#  1 1  1 1   1 1   1 1
