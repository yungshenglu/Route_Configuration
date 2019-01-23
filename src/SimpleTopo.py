#!/usr/bin/python
#
# An exmaple of Mininet topology
# AUTHOR: David Lu (https://github.com/yungshenglu)

from mininet.topo import Topo
from mininet.link import TCLink

class Topology(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts into topology
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add switches into topology
        s1 = self.addSwitch('s1')

        # Add links into topology
        self.addLink(s1, h1, port1=1, bw=10, delay='5ms', loss=5)
        self.addLink(s1, h2, port1=2, bw=10, delay='5ms', loss=5)

topos = {
    'topo': (lambda: Topology())
}