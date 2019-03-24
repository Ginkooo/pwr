from dataclasses import dataclass
import string


@dataclass
class Node:
    visited: bool = False


p_idx = string.ascii_lowercase.find('p')

node_names = string.ascii_lowercase[:p_idx+1]
for name in node_names:
    globals()[name] = Node()

unvisited = {}
