"""
Tools for simulating a network of bitcoin miners.
"""

from collections.abc import Sequence


class Minernet(Sequence):

    def __init__(self, n):
        nodes = [x for x in range(n)]
        peers = {k:{} for k in nodes}

        self.delay = dict()
        self.nodes = nodes
        self.peers = peers
        self.pool = set()
        self.tick = 0

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, i):
        return self.nodes[i]

    def __repr__(self):
        return f"<Minernet with {len(self)} nodes>"

