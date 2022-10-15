#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = input("Введите множество: ")
    a = set("AEIOUYaeioyФУЕЭОЯИЮауеоэюия")
    count = 0

    for i in u:
        if i in a:
            count += 1

    print(count)


