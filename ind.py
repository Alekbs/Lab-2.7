#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {"b", "c", "h", "i", "j"}
    b = {"e", "h", "i", "s", "w"}
    c = {"a", "b", "j", "k", "l", "m"}
    d = {"a", "h", "i", "w", "x"}

    ab = a.union(b)
    cd = c.union(d)
    abcd = ab.union(cd)
    bb = abcd.difference(b)
    ac = a.difference(c)

    x = ac.intersection(bb)

    y = (a.intersection(bb)).union(c.difference(d))

    print(x, y)
    x = ()
