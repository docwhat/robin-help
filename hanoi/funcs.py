#!/usr/bin/python
# A version of the hanoi problem as functions.
# AKA unrolling hanoi.

import sys


def move(n, from_rod, to_rod):
    sys.stdout.write("Move disk %2d from rod %s to rod %s" % (n, from_rod, to_rod))
    sys.stdout.write((" n =  %%%ds" % (3 * n)) % n)
    sys.stdout.write("\n")


def hanoi1(from_rod, to_rod, aux_rod):
    print("hanoi1"),
    move(1, from_rod, to_rod)


def hanoi2(from_rod, to_rod, aux_rod):
    hanoi1(from_rod, aux_rod, to_rod)
    #  move(1, from_rod, aux_rod)

    print("hanoi2"),
    move(2, from_rod, to_rod)

    hanoi1(aux_rod, to_rod, from_rod)
    #  move(1, aux_rod, to_rod)


def hanoi3(from_rod, to_rod, aux_rod):
    hanoi2(from_rod, aux_rod, to_rod)

    print("hanoi3"),
    move(3, from_rod, to_rod)

    hanoi2(aux_rod, to_rod, from_rod)


hanoi3("A", "C", "B")
