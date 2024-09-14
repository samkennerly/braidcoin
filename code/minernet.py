"""
Tools for simulating a network of bitcoin miners.
"""

from collections.abc import Iterable

from numpy import random
from pandas import DataFrame


# initialize numpy random number generator
rng = random.default_rng()


def random_links(n_nodes, n_peers, mu, sigma):
    nodes = list(range(n_nodes))

    for node in nodes:
        peers = [x for x in nodes if x != node]
        peers = rng.choice(peers, size=n_peers, replace=False)
        peers = map(int, peers)
        for peer in peers:
            yield node, peer, rng.lognormal(mu, sigma)


class Minernet(Iterable):

    def __init__(self, n_nodes, n_peers=4, mu=1, sigma=0.5):
        cols = "node peer latency".split()
        links = random_links(n_nodes, n_peers, mu, sigma)
        links = DataFrame(links, columns=cols)

        self.links = links
        self.pool = set()
        self.tick = 0

    @property
    def nodes(self):
        """numpy.array: Distinct, sorted nodes."""
        return sorted(int(x) for x in self.links["node"].unique())

    def __len__(self):
        return len(self.links)

    def __iter__(self):
        return self.links.itertuples(index=False, name="Link")

    def __repr__(self):
        return f"<Minernet with {len(self)} links and {len(self.nodes)} nodes>"
