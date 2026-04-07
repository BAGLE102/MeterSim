#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.node import RemoteController, OVSSwitch

def main():
	OFSwitchList = []
	HostList = []
	net = Mininet(controller = None, link = TCLink)
	Controller = RemoteController( 'Controller', ip='127.0.0.1', port=6633)

#	for i in xrange(10):
	for i in range(1):
		OFSwitchList.append(net.addSwitch("s%s"%str(i+1), cls = OVSSwitch))
		
#	for i in xrange(4):
	for i in range(2):
		HostList.append(net.addHost("h%s"%str(i+1), ip = "10.0.0.%s/24"%str(i+10), mac = "00:04:00:00:00:%s"%str(i+1)))

	net.addLink(HostList[0], OFSwitchList[0])
	net.addLink(HostList[1], OFSwitchList[0])

	net.start()
	for x in range(1):
		net.get("s%s"%str(x+1)).start([Controller])
	CLI(net)
	net.stop()

if __name__ == "__main__":
	setLogLevel( "info" )
	main()
