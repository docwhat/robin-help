def f(n, first, last):
    if n == 0:
        return
    print("  %d %s %s" % (n, first, last))
    f(n - 1, last, first)


f(7, "a", "z")
# n=4, first=z, last=a

# f(3, "a", "z")
# n=3, first="a", last="z" => print("3 a z")

# f(2, z, a)
# n=2, first="z", last="a" => print("2 z a")

# f(1, a, z)
# n=1, first="a", last="z" => print("1 a z")

# f(0, z, a)
# n=0, first="z", last="a" => return


# EOF
