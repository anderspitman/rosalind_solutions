#!/usr/bin/env python

import sys

if __name__ == '__main__':
    
    symbol_counts = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0,
    }

    text = ''

    for line in sys.stdin:
        text += line
    for symbol in text:
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
    for symbol in sorted(symbol_counts.keys()):
        print(symbol_counts[symbol]),

