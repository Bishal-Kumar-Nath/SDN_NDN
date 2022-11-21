"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.link import TCLink
class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        Host1 = self.addHost( 'h1', mac='00:00:00:00:00:01' )
        Host2 = self.addHost( 'h2', mac='00:00:00:00:00:02' )
        Host3 = self.addHost( 'h3', mac='00:00:00:00:00:03' )

        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host3, Switch1 )
        self.addLink( Host2, Switch3)
        
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch2, Switch3 )
        #self.addLink( Host2, Switch2, cls=TCLink, bw=2 )  # bw in Mbps
        #self.addLink( Host2, Switch2, cls=TCLink )
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
