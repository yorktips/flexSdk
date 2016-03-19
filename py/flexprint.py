import requests
import json
import urllib2
from flexswitch import FlexSwitch

class FlexPrint( object):
    def  __init__ (self, ip, port):
        self.swtch = FlexSwitch(ip, port)

    def printRoutes(self):
        routes = self.swtch.getObjects('IPv4RouteStates')
        if len(routes):
            print '\n\n---- Routes ----'
            print 'Network            Mask         NextHop         Cost       Protocol   IfType IfIndex'
        for rt in routes:
            print '%s %s %s %4d   %9s    %5s   %4s' %(rt['DestinationNw'].ljust(15), 
                                                            rt['NetworkMask'].ljust(15),
                                                            rt['NextHopIp'].ljust(15), 
                                                            rt['Cost'], 
                                                            rt['Protocol'], 
                                                            rt['OutgoingIntfType'], 
                                                            rt['OutgoingInterface'])

    def printPolicyStates (self) :
        policies = self.swtch.getObjects('PolicyDefinitionStates')
        if len(policies) :
            print '\n\n---- Policies----'
            print 'Name            Hit Counter     Affected Routes'
        for plcy in policies:
            routes=''
            for route in plcy['IpPrefixList']:
                routes = routes + '  ' +route
            print '%s       %s          %s ' %(plcy['Name'], 
                                plcy['HitCounter'],
                                routes)
                                
    def printDHCPHostStates (self) :
        hosts = self.swtch.getObjects('DhcpRelayHostDhcpStates')
        if len(hosts) :
            print '\n\n---- Hosts ----'
            print 'MacAddress  ServerIP   DiscoverSent@   OfferReceived@  RequestSent@  AckReceived@   OfferedIP   RequestedIP   AcceptedIP    GWIP   ClntTx  ClntRx  SvrRx  SvrTx'
        for host in hosts:
            print '%s   %s  %s   %s     %s   %s  %s   %s     %s   %s  %s   %s   %s  %s' %(
                        host['MacAddr'],
                        host['ServerIp'],
                        host['ClientDiscover'],
                        host['ServerOffer'],
                        host['ClientRequest'],
                        host['ServerAck'],
                        host['OfferedIp'],
                        host['RequestedIp'],
                        host['AcceptedIp'],
                        host['GatewayIp'],
                        host['ClientRequests'],
                        host['ClientResponses'],
                        host['ServerRequests'],
                        host['ServerResponses'])




    def printVlans (self):
        vlans = self.swtch.getObjects('Vlans')
        if len(vlans):
            print '\n\n---- Vlans ----'
            print 'VlanId  Name   IfIndex   TaggedPorts     UntaggedPorts       Status'
        for vlan in vlans:
            print '%s   %s  %s  %s   %s  %s' %(vlan ['VlanId'],
                                               vlan ['VlanName'],
                                               vlan ['IfIndex'],
                                               vlan ['IfIndexList'],
                                               vlan ['UntagIfIndexList'],
                                               vlan ['OperState'])

    def printVrrpIntfState (self):
        vrids = self.swtch.getObjects('VrrpIntfStates')
        '''
	entry.IfIndex = gblInfo.IntfConfig.IfIndex
	entry.VRID = gblInfo.IntfConfig.VRID
	entry.IntfIpAddr = gblInfo.IpAddr
	entry.Priority = gblInfo.IntfConfig.Priority
	entry.VirtualIPv4Addr = gblInfo.IntfConfig.VirtualIPv4Addr
	entry.AdvertisementInterval = gblInfo.IntfConfig.AdvertisementInterval
	entry.PreemptMode = gblInfo.IntfConfig.PreemptMode
	entry.VirtualRouterMACAddress = gblInfo.IntfConfig.VirtualRouterMACAddress
	entry.SkewTime = gblInfo.SkewTime
	entry.MasterDownInterval = gblInfo.MasterDownInterval
        '''
        if len(vrids):
            print ''
            print 'IfIndex   VRID    Vip     Priority   State     ViMac              IntfIp      Preempt  Advertise    Skew  Master_Down'
            print '================================================================================================================'
            for fObject in vrids:
                entry = fObject['ConfigObj']
                print '%s   %s  %s     %s   %s   %s      %s   %s    %s            %s      %s' %(entry ['IfIndex'],
                                                                   entry ['VRID'],
                                                                   entry ['VirtualIPv4Addr'],
                                                                   entry ['Priority'],
                                                                   entry ['VrrpState'],
                                                                   entry ['VirtualRouterMACAddress'],
                                                                   entry ['IntfIpAddr'],
                                                                   entry ['PreemptMode'],
                                                                   entry ['AdvertisementInterval'],
                                                                   entry ['SkewTime'],
                                                                   entry ['MasterDownTimer'])
            print ''

    def printOspfLsdb(self) :
        lsas = self.swtch.getObjects('OspfLsdbEntryStates')
        if len(lsas) :
            print '\n\n---- Link State DB----'
            print 'LSA Type LS Checksum     LS Age      LS AreaId       LS ID       LS Sequence     LS RouterId     LS Advertisement'
        count = 0
        for lsa in lsas:
            count = count + 1
            print 'LS Database Entry Number:', count
            #print '%s           %s          %s          %s      %s      %s      %s      %s' %(lsa ['LsdbType'],
             #                                                               lsa ['LsdbChecksum'],
             #                                                               lsa ['LsdbAge'],
             #                                                               lsa ['LsdbAreaId'],
             #                                                               lsa ['LsdbLsid'],
             #                                                               lsa ['LsdbSequence'],
             #                                                               lsa ['LsdbRouterId'],
              #                                                              lsa ['LsdbAdvertisement'])
            adv = lsa['LsdbAdvertisement'].split(':')
            #print adv
            if lsa['LsdbType'] == 1 :
                print "LS Type: Router LSA"
            elif lsa['LsdbType'] == 2 :
                print "LS Type: Network LSA"
            elif lsa['LsdbType'] == 3 :
                print "LS Type: Summary Type 3 LSA"
            elif lsa['LsdbType'] == 4 :
                print "LS Type: Summary Type 4 LSA"
            elif lsa['LsdbType'] == 5 :
                print "LS Type: AS External LSA"

            print 'LS Age:', lsa ['LsdbAge']
            print 'Link State Id:', lsa ['LsdbLsid']
            print 'Advertising Router:', lsa ['LsdbRouterId']
            print 'LS Sequence Number:', lsa ['LsdbSequence']
            print 'LS Checksum:', lsa ['LsdbChecksum']
            if lsa['LsdbType'] == 1 :
                options = int(adv[0])
                if options & 0x1 :
                    print 'Bit B : true'
                else :
                    print 'Bit B : false'
                if options & 0x2 :
                    print 'Bit E : true'
                else :
                    print 'Bit E : false'
                if options & 0x4 :
                    print 'Bit V : true'
                else :
                    print 'Bit V : false'
                numOfLinks = int(adv[2]) << 8 | int(adv[3])
                print 'Number of Links:', numOfLinks
                for i in range(0, numOfLinks) :
                    print '         Link Number:', i+1
                    linkId = adv[4 + (i * 12)] + '.' + adv[4 + (i * 12) + 1] + '.' + adv[4 + (i * 12) + 2] + '.' + adv[4 + (i * 12) + 3]
                    print '         Link ID:', linkId
                    linkData = adv[4 + (i * 12) + 4] + '.' + adv[4 + (i * 12) + 5] + '.' + adv[4 + (i * 12) + 6] + '.' + adv[4 + (i * 12) + 7]
                    print '         Link Data:', linkData
                    linkType = ""
                    lType = adv[4 + (i * 12) + 8]
                    if lType == '1' :
                        linkType = "Point-to-Point Connection"
                    elif lType == '2' :
                        linkType = "Transit Link" 
                    elif lType == '3' :
                        linkType = "Stub Link" 
                    elif lType == '4' :
                        linkType = "Virtual Link" 
                    print '         Link Type:', linkType
                    numOfTOS = int(adv[4 + (i * 12) + 9])
                    print '         Number of TOS:', numOfTOS
                    metric = int(adv[4 + (i * 12) + 10]) << 8 | int(adv[4 + (i * 12) + 11])
                    print '         Metric:', metric
                    print ''
            elif lsa['LsdbType'] == 2 :
                netmask = adv[0] + '.' + adv[1] + '.' + adv[2] + '.' + adv[3]
                print 'Netmask:', netmask
                for i in range(0, (len(adv) - 4) / 4) :
                    attachedRtr = adv[4 + i * 4] + '.' + adv[5 + i * 4] + '.' + adv[6 + i * 4] + '.' + adv[3 + i * 4]
                    print '         Attached Router:', attachedRtr
                    
            print ''

                                
if __name__=='__main__':
    pass
