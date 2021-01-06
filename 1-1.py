#!/usr/bin/env python3

import NFA
import sys

if __name__ == '__main__':
    nfa = NFA.NFA()
    for line in sys.stdin:
        line = line.strip()
        parts = list(filter(bool, line.split(' ')))
        assert len(parts) == 3
        prev, symbol, next = parts
        prev, symbol, node = NFA.str_to_node(prev), NFA.str_to_symbol(symbol), NFA.str_to_node(next)
        nfa.link(prev, symbol, node)
    print(nfa)
