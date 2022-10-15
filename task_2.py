#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set(input("Введите первое множество: "))
    b = set(input("Введите второе множество: "))

    c = a.intersection(b)
    print(c)