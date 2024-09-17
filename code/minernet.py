"""
Tools for simulating a network of bitcoin miners.
"""

from collections import namedtuple
from dataclasses import dataclass

from numpy import random
from pandas import DataFrame


# initialize numpy random number generator
rng = random.default_rng()


def random_links(n_nodes, n_peers, mean=1, sigma=0.1):
    """generator[Tuple(int, int)]: (node, peer) pairs."""
    for node in range(n_nodes):
        peers = [x for x in range(n_nodes) if x != node]
        peers = rng.choice(peers, size=n_peers, replace=False)
        peers = map(int, peers)
        for peer in peers:
            yield node, peer, rng.lognormal(mean=mean, sigma=sigma)


@dataclass(frozen=True)
class Bead:
    creator: int = 0
    parents: frozenset = frozenset()
    tick: int = 0


class Minernet:

    def __init__(self, **kwargs):
        links = random_links(**kwargs)
        links = DataFrame(links, columns="node peer lag".split())

        bead0 = Bead()
        beads = [{bead0} for _ in links["node"].unique()]

        self.beads = beads
        self.links = links
        self.pool = set()
        self.tick = 0

    @property
    def nodes(self):
        """list: Distinct, sorted node ids."""
        return sorted(int(x) for x in self.links["node"].unique())

    def __len__(self):
        return len(self.links)

    def __iter__(self):
        return self.links.itertuples(index=False, name="Link")

    def __repr__(self):
        return f"<GraphFrame with {len(self)} links>"
