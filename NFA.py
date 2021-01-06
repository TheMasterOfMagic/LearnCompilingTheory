from functools import reduce
from typing import Set, Dict

Node = int
def is_node(node) -> bool:
    return isinstance(node, Node)
def node_to_str(node: Node) -> str:
    assert is_node(node)
    return str(node)
def str_to_node(s: str) -> Node:
    assert isinstance(s, str)
    assert s.isdecimal()
    return Node(s)

NodeSet = Set[Node]
def is_node_set(node_set) -> bool:
    return isinstance(node_set, set) and all(map(is_node, node_set))
def node_set_to_str(node_set: NodeSet) -> str:
    assert is_node_set(node_set)
    rv = ','.join(list(map(node_to_str, node_set)))
    return f'[{rv}]'

Symbol = str
def is_symbol(symbol) -> bool:
    return isinstance(symbol, Symbol)
def symbol_to_str(symbol: Symbol) -> str:
    assert is_symbol(symbol)
    return str(symbol)
def str_to_symbol(s: str) -> Symbol:
    assert isinstance(s, str)
    assert len(s) == 1 and s.isprintable() and s not in "()|*"
    return Symbol(s)

OutEdges = Dict[Symbol, NodeSet]
def is_out_edges(out_edges) -> bool:
    return isinstance(out_edges, dict) and all(map(is_symbol, out_edges.keys())) and all(map(is_node_set, out_edges.values()))
def out_edges_to_str(out_edges: OutEdges) -> str:
    assert is_out_edges(out_edges)
    rv = ','.join(list(f'({symbol},{node_set_to_str(node_set)})' for symbol, node_set in out_edges.items()))
    return f'[{rv}]'

NFATable = Dict[Node, OutEdges]
def is_nfa_table(nfa_table) -> bool:
     return isinstance(nfa_table, dict) and all(map(is_node, nfa_table.keys())) and all(map(is_out_edges, nfa_table.values()))
def nfa_table_to_str(nfa_table: NFATable) -> str:
    assert is_nfa_table(nfa_table)
    rv = ','.join(list(f'({prev},{out_edges_to_str(out_edges)})' for prev, out_edges in nfa_table.items()))
    return f'[{rv}]'

class NFA:
    def __init__(self):
        self.nfa_table = dict()

    def __str__(self):
        return nfa_table_to_str(self.nfa_table)

    def link(self, prev: Node, symbol: Symbol, next: Node) -> None:
        assert is_node(prev)
        assert is_symbol(symbol)
        assert is_node(next)
        self.nfa_table.setdefault(prev, dict())
        self.nfa_table[prev].setdefault(symbol, set())
        self.nfa_table[prev][symbol].add(next)
