#!/usr/bin/env python
"""
Goldilocks' Bear Necessities
"""
from __future__ import print_function
import sys

if __name__ == "__main__":
    line_counter = 0
    seats = []
    for line in sys.stdin:
        w, t = [int(s) for s in line.split()]
        if line_counter == 0:
            wm = w
            tm = t
            line_counter += 1
            continue
        if w > wm and t < tm:
            seats.append(str(line_counter))
        line_counter += 1
    print(" ".join(seats))

        
