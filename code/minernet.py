"""
Tools for simulating a network of bitcoin miners.
"""

from dataclasses import dataclass

from networkx import bfs_layout, draw_networkx, DiGraph
from numpy import random
from matplotlib.pyplot import figure
from pandas import DataFrame

# initialize numpy random number generator
rng = random.default_rng()


def random_links(n_nodes, n_peers):
    for node in range(n_nodes):
        peers = [x for x in range(n_nodes) if x != node]
        peers = rng.choice(peers, size=n_peers, replace=False)
        peers = map(int, peers)
        for peer in peers:
            yield node, peer


@dataclass
class Bead:

    def __init__(self, index=0, creator=0, parents=(), tick=0):
        self.index = int(index)
        self.creator = int(creator)
        self.parents = frozenset(parents)
        self.tick = int(tick)


class Braid:

    def __init__(self, beads):
        self.beads = sorted(beads, key=lambda x: x.index) or [Bead()]

    def __repr__(self):
        return f"<Braid with {len(self.beads)} beads>"

    @property
    def root(self):
        return self.beads[0]

    def ancestors(self, index):
        raise NotImplementedError

    def cohorts(self):
        raise NotImplementedError

    def links(self):
        return ((y, x.index) for x in self.beads for y in x.parents)

    def tips(self):
        raise NotImplementedError

    def plot(self, figsize=(9, 3)):
        to_networkx = self.to_networkx
        root = self.root

        graph = to_networkx()
        pos = bfs_layout(graph, start=root.index)
        fig = figure(figsize=figsize)
        draw_networkx(graph, pos=pos)

        return fig

    def to_networkx(self):
        links = self.links

        graph = DiGraph()
        graph.add_edges_from(links())

        return graph


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
