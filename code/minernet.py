"""
Tools for simulating a network of bitcoin miners.
"""

from collections import namedtuple
from dataclasses import dataclass, field
from itertools import count

from numpy import random
from pandas import DataFrame


# initialize numpy random number generator
rng = random.default_rng()


def braid(beads):
    raise NotImplementedError


def random_links(n_nodes, n_peers):
    for node in range(n_nodes):
        peers = [x for x in range(n_nodes) if x != node]
        peers = rng.choice(peers, size=n_peers, replace=False)
        peers = map(int, peers)
        for peer in peers:
            yield node, peer


@dataclass(frozen=True, slots=True)
class Bead:
    uid: int = field(default_factory=count().__next__)
    tick: int = 0
    parents: frozenset = frozenset()
    creator: int = 0


class Minernet:

    def __init__(self, mu=1, sigma=0.5):
        links = random_links(**kwargs)
        links = DataFrame(links, columns="node peer".split())
        links["lag"] = rng.lognormal(mean=mu, sigma=sigma, size=len(links))

        bead0 = Bead()
        beads = [[bead0] for _ in links["node"].unique()]

        self.beads = beads
        self.links = links
        self.pool = set()
        self.tick = 0

    @property
    def nodes(self):
        """list: Distinct, sorted node ids."""
        return sorted(int(x) for x in self.links["node"].unique())

    @property
    def genesis(self):
        """Bead: First bead created when network was initialized."""
        return self.beads[0][0]

    def __len__(self):
        return len(self.links)

    def __iter__(self):
        return self.links.itertuples(index=False, name="Link")

    def __repr__(self):
        return f"<GraphFrame with {len(self)} links>"
