from __future__ import annotations

from enum import Enum


class EdgeType(Enum):
    LEFT = 1
    RIGHT = 2
    UNDIRECTED = 3


class PathPattern:
    def __init__(self, chain: list[NodePattern | EdgePattern]):
        for a, b in zip(chain, chain[1:]):
            if type(a) is type(b):
                raise ValueError(
                    f'chain must be alternating between NodePattern and EdgePattern'
                )
        self.chain = chain

    def __str__(self) -> str:
        return ''.join(str(x) for x in self.chain)


class NodeSpec:
    def __str__(self) -> str:
        return f''


class NodePattern:
    def __init__(self, spec: NodeSpec) -> None:
        self.spec = spec

    def __str__(self) -> str:
        return f'[{self.spec}]'


class EdgeSpec:
    def __str__(self) -> str:
        return f''


class EdgePattern:
    def __init__(self, spec: EdgeSpec, edge_type: set[EdgeType] | EdgeType) -> None:
        if isinstance(edge_type, EdgeType):
            self.edge_type = set([edge_type])
        else:
            self.edge_type = edge_type
        self.spec = spec

    def __str__(self) -> str:
        if (
            EdgeType.LEFT in self.edge_type
            and EdgeType.RIGHT in self.edge_type
            and EdgeType.UNDIRECTED in self.edge_type
        ):
            return f'-[{self.spec}]-'
        if EdgeType.LEFT in self.edge_type and EdgeType.RIGHT in self.edge_type:
            return f'<-[{self.spec}]->'
        if EdgeType.LEFT in self.edge_type and EdgeType.UNDIRECTED in self.edge_type:
            return f'<~[{self.spec}]~'
        if EdgeType.RIGHT in self.edge_type and EdgeType.UNDIRECTED in self.edge_type:
            return f'~[{self.spec}]~>'
        if EdgeType.LEFT in self.edge_type:
            return f'<-[{self.spec}]'
        if EdgeType.RIGHT in self.edge_type:
            return f'-[{self.spec}]->'
        if EdgeType.UNDIRECTED in self.edge_type:
            return f'~[{self.spec}]~'
        raise ValueError(f'Unknown edge type: {self.edge_type}')
