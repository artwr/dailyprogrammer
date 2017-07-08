#!/usr/bin/env python
"""
ASCII Histogram Maker: Part 1 - The Simple Bar Chart
"""
from __future__ import print_function
import sys

def format_axis_val(value):


if __name__ == "__main__":
    line_counter = 0
    data = []
    for line in sys.stdin:
        if line_counter == 0:
            setup = [int(c) for c in line.split()]
            minx, maxx, miny , maxy = setup
            line_counter += 1
            continue
        else:
            parsed_line = [int(c) for c in line.split()]
            data.append((parsed_line[0], parsed_line[1], parsed_line[2]))
        
            '{value:{fill}{align}{width}}'.format(message='Hi', fill=' ', align='<', width=16)

        
