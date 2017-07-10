#!/usr/bin/env python
from __future__ import print_function

n = 4




def make_line(numbers, size=2):
    return "".join(str(n).rjust(size) for n in numbers)


if __name__ == "__main__":
    max_num = n ** 2
    numbers = range(n ** 2)
    max_size = len(str(max_num))
    print(make_line(range(1,8), size=max_size))
