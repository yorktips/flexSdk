import requests
import json
import urllib2
from flexswitchV2 import FlexSwitch
from tablePrint import *

def getLagGroups(ip, port):
        currentMarker = 0
        nextMarker = 0
        count = 5
        more = True

        while more == True:
            qry = 'http://%s:%s/public/v1/AggregationLacpStates?CurrentMarker=%d&NextMarker=%d&Count=%d' %(ip, port, currentMarker, nextMarker, count)
            response = requests.get(qry)
            data = response.json()
            if currentMarker == 0: #Print the header only for first iteration
                print 'Name      Ifindex      LagType   Description      Enabled   MinLinks   Interval   Mode          SystemIdMac            SystemPriority    HASH'


            more =  data['MoreExist']
            currentMarker =  data['NextMarker']
            NextMarker    =  data['NextMarker']
            if data['StateObjects']:
                for d in data['StateObjects']:
                    print '%7s  %7s    %7s  %15s    %8s   %2s     %8s      %6s   %20s         %s              %s' %(d['NameKey'],
                                                                    d['Ifindex'],
                                                                    "LACP" if int(d['LagType']) == 0 else "STATIC",
                                                                    d['Description'],
                                                                    "Enabled" if bool(d['Enabled']) else "Disabled",
                                                                    d['MinLinks'],
                                                                    "FAST" if int(d['Interval']) == 0 else "SLOW",
                                                                    "ACTIVE" if int(d['LacpMode']) == 0 else "PASSIVE",
                                                                    d['SystemIdMac'],
                                                                    d['SystemPriority'],
                                                                    d['LagHash'])
            #import ipdb;ipdb.set_trace()



class FlexPrint( object):
    def  __init__ (self, ip, port):
        self.swtch = FlexSwitch(ip, port)

    def printPortState(self, IntfRef):

        self.printPortStates(IntfRef=int(IntfRef))

    def printPortStates(self, IntfRef=None):

        ports = self.swtch.getAllPortStates()
        for port in ports:

            p = port['Object']
            if IntfRef == None or IntfRef == p['IntfRef']:
                print "PortNum : ", p['IntfRef'], "IfIndex: ", p['IfIndex'], "Name: ", p['Name']
                print "OperState: ", p['OperState']
                print "NumUpEvents: ", p['NumUpEvents'],
                print "LastUpEventTime: ", p['LastUpEventTime'],
                print "NumDownEvents: ", p['NumDownEvents'],
                print "LastDownEventTime: ", p["LastDownEventTime"],
                print "Pvid: ", p["Pvid"]
                print "Counters:"
                print "\tIfInOctets:    ", p['IfInOctets']
                print "\tIfInUcastPkts: ", p['IfInUcastPkts']
                print "\tIfInDiscards: ", p['IfInDiscards']
                print "\tIfInErrors: ", p['IfInErrors']
                print "\tIfInUnknownProtos: ", p['IfInUnknownProtos']
                print "\tIfOutOctets: ", p['IfOutOctets']
                print "\tIfOutUcastPkts: ", p['IfOutUcastPkts']
                print "\tIfOutDiscards: ", p['IfOutDiscards']
                print "\tIfOutErrors: ", p['IfOutErrors']

                print 'Err-disable-Reason: ', p['ErrDisableReason']
                print 'PresentInHW', p['PresentInHW']
                print '------------------------------------------------------------------------------'

    def printIPv4RouteStates(self):
        routes = self.swtch.getAllIPv4RouteStates()
        print '\n\n---- Routes ----'
        labels = ('Network', 'NextHop', 'Protocol', 'Reachability', 'Creation Time', 'Update Time', 'PolicyList')
        rows = []
        for r in routes:
            rt = r['Object']
            rows.append(("%s" %(rt['DestinationNw']),
                        "%s" %(rt['NextHopList']),
                        "%s" %(rt['Protocol']),
                        "%s" %(rt['IsNetworkReachable']),
                        "%s" %(rt['RouteCreatedTime']),
                        "%s" %(rt['RouteUpdatedTime']),
                        "%s" %(rt['PolicyList'])))
        width = 30
        print indent([labels]+rows, hasHeader=True, separateRows=False,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                     wrapfunc=lambda x: wrap_onspace_strict(x,width))

    def printIPv4IntfStates(self, IntfRef=None):
        ipv4intfs = self.swtch.getAllIPv4IntfStates()
        if len(ipv4intfs):
            print '------Ip Info------\n'
        for ipv4intf in ipv4intfs:
            if ipv4intf == IntfRef or IntfRef is None:
                print 'address: %s' %(ipv4intf['IntfRef'])

    def printIPv4IntfState(self, IntfRef):
        self.printIPv4IntfStates(IntfRef)

    def printVlanState(self, VlanId):

        found = self.printVlanStates(int(VlanId))
        if not found:
            print "VlanId %d NOT FOUND" % (VlanId,)

    def printVlanStates(self, VlanId=None):
        vlans = self.swtch.getAllVlanStates()
        if len(vlans):
            print '\n\n\t\t---- Vlans ----'
            print '%13s%12s%15s%10s' %('Vlan','Name','OperState','IfIndex')
        else:
            return 0
        for v in vlans:
            vlan = v['Object']
            if VlanId == None or vlan['VlanId'] == int(VlanId):
                print '%13s%12s%15s%10s\n' %(vlan['VlanId'], vlan['VlanName'], vlan['OperState'], vlan['IfIndex'])

        return 1

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
                entry = fObject['Object']
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

    def printStpBridges(self):

        brgs = self.swtch.getObjects('StpBridgeStates')

        if len(brgs):
            print '\n\n---- STP Bridge DB----'

            count = 0
            for data in brgs:
                obj = data['Object']
                print "BrgIfIndex: ", obj["IfIndex"]
                #print "Version: ", obj["ForceVersion"]
                print "Bridge Id: ", obj["Address"]
                print "Bridge Hello time: ", obj["BridgeHelloTime"]
                print "Bridge TxHold: ", obj["TxHoldCount"]
                print "Bridge Forwarding Delay: ", obj["BridgeForwardDelay"]
                print "Bridge Max Age: ", obj["BridgeMaxAge"]
                print "Bridge Priority: ", obj["Priority"]
                print "Time Since Topology Change: UNSUPPORTED" #nextStpBridgeState.Dot1dStpTimeSinceTopologyChange uint32 //The time (in hundredths of a second) since the last time a topology change was detected by the bridge entity. For RSTP, this reports the time since the tcWhile timer for any port on this Bridge was nonzero.
                print "Topology Changes: UNSUPPORTED" #nextStpBridgeState.Dot1dStpTopChanges              uint32 //The total number of topology changes detected by this bridge since the management entity was last reset or initialized.
                print "Root Bridge Id: ", obj["DesignatedRoot"]
                print "Root Cost: ", obj["RootCost"]
                print "Root Port: ", obj["RootPort"]
                print "Max Age: ", obj["MaxAge"]
                print "Hello Time: ", obj["HelloTime"]
                print "Hold Time: UNSUPPORTED" #Dot1dStpHoldTime = int32(b.TxHoldCount)
                print "Forwarding Delay: ", obj["ForwardDelay"]
                print "Bridge Vlan: ", obj["Vlan"] if obj["Vlan"] != 0 else "DEFAULT"
                print "=====================================================================================\n\n"

    def printStpPorts(self):
        stateDict = {
            1 : "Disabled",
            2 : "Blocked",
            3 : "Listening",
            4 : "Learning",
            5 : "Forwarding",
            6 : "Broken",
        }
        linkTypeDict = {
            0 : "LAN",
            1 : "P2P",
        }

        ports = self.swtch.getObjects('StpPortStates')

        if len(ports):
            print '\n\n---- STP PORT DB----'
            for data in ports:
                obj = data['Object']
                bainconsistant = "(inconsistant)" if obj["BridgeAssuranceInconsistant"] else ""
                print "IfIndex %s of BrgIfIndex %s is %s %s" %(obj["IfIndex"], obj["BrgIfIndex"], stateDict[obj["State"]], bainconsistant)
                #print "Enabled %s, Protocol Migration %s" %(obj["Enable"], obj["ProtocolMigration"])
                print "Enabled %s" %(obj["Enable"],)
                print "Port path cost %s, Port priority %s, Port Identifier %s" %(obj["PathCost32"], obj["Priority"], obj["IfIndex"])
                print "Designated root has bridge id %s" %(obj["DesignatedRoot"])
                print "Designated bridge has bridge id %s" %(obj["DesignatedBridge"])
                print "Designated port id %s, designated path cost %s admin path cost %s" %(obj["DesignatedPort"], obj["DesignatedCost"], obj["AdminPathCost"])
                print "Root Timers: max age %s, forward delay %s, hello %s" %(obj["MaxAge"],obj["ForwardDelay"],obj["HelloTime"],)
                print "Number of transitions to forwarding state: %s" %(obj["ForwardTransitions"],)
                print "AdminEdge %s OperEdge %s" %(obj["AdminEdgePort"], obj["OperEdgePort"])
                print "Bridge Assurance %s Bpdu Guard %s" %(obj["BridgeAssurance"], obj["BpduGuard"])
                print "Link Type %s" %("UNSUPPORTED",)
                print "\nPort Timers: (current tick(seconds) count)"
                print "EdgeDelayWhile:\t", obj["EdgeDelayWhile"]
                print "FdWhile:       \t", obj["FdWhile"]
                print "HelloWhen:     \t", obj["HelloWhen"]
                print "MdelayWhile:   \t", obj["MdelayWhile"]
                print "RbWhile:       \t", obj["RbWhile"]
                print "RcvdInfoWhile  \t", obj["RcvdInfoWhile"]
                print "RrWhile:       \t", obj["RrWhile"]
                print "TcWhile:       \t", obj["TcWhile"]
                print "\nCounters:"
                print "        %13s%13s" %("RX", "TX")
                print "BPDU    %13s%13s" %(obj["BpduInPkts"], obj["BpduOutPkts"])
                print "STP     %13s%13s" %(obj["StpInPkts"], obj["StpOutPkts"])
                print "TC      %13s%13s" %(obj["TcInPkts"], obj["TcOutPkts"])
                print "TC ACK  %13s%13s" %(obj["TcAckInPkts"], obj["TcAckOutPkts"])
                print "RSTP    %13s%13s" %(obj["RstpInPkts"], obj["RstpOutPkts"])
                print "PVST    %13s%13s" %(obj["PvstInPkts"], obj["PvstOutPkts"])
                print "\nFSM States:"
                print "PIM - Port Information, PRTM - Port Role Transition, PRXM - Port Receive"
                print "PSTM - Port State Transition, PPM - Port Protocol Migration, PTXM - Port Transmit"
                print "PTIM - Port Timer, BDM - Bridge Detection, TCM - Topology Change"
                print "MACHINE       %20s%20s" %("CURRENT", "PREVIOUS")
                print "PIM           %20s%20s" %(obj["PimCurrState"], obj["PimPrevState"])
                print "PRTM          %20s%20s" %(obj["PrtmCurrState"], obj["PrtmPrevState"])
                print "PRXM          %20s%20s" %(obj["PrxmCurrState"], obj["PrxmPrevState"])
                print "PSTM          %20s%20s" %(obj["PstmCurrState"], obj["PstmPrevState"])
                print "PPM           %20s%20s" %(obj["PpmCurrState"], obj["PpmPrevState"])
                print "PTXM          %20s%20s" %(obj["PtxmCurrState"], obj["PtxmPrevState"])
                print "PTIM          %20s%20s" %(obj["PtimCurrState"], obj["PtimPrevState"])
                print "BDM           %20s%20s" %(obj["BdmCurrState"], obj["BdmPrevState"])
                print "TCM           %20s%20s" %(obj["TcmCurrState"], obj["TcmPrevState"])
                print "====================================================================="


    def printLaPortChannelMembers(self):

        # YANG MODEL REPRESENTATION
        RxMachineStateDict = {
            0 : "RX_CURRENT",
            1 : "RX_EXPIRED",
            2 : "RX_DEFAULTED",
            3 : "RX_INITIALIZE",
            4 : "RX_LACP_DISABLED",
            5 : "RX_PORT_DISABLE",
        }

        MuxMachineStateDict = {
            0 : "MUX_DETACHED",
            1 : "MUX_WAITING",
            2 : "MUX_ATTACHED",
            3 : "MUX_COLLECTING",
            4 : "MUX_DISTRIBUTING",
            5 : "MUX_COLLECTING_DISTRIBUTING",
        }

        ChurnMachineStateDict = {
            0 : "CDM_NO_CHURN",
            1 : "CDM_CHURN",
        }

        '''
        //Collecting bool
        // parent leaf
        //OperKey uint16
        // parent leaf
        //PartnerId string
        // parent leaf
        //Interface string
        // parent leaf
        //Synchronization int32
        // parent leaf
        //Aggregatable bool
        // parent leaf
        Mtu uint16
        // parent leaf
        //LacpMode int32
        // parent leaf
        //PartnerKey uint16
        // parent leaf
        Description string
        // parent leaf
        //SystemIdMac string
        // parent leaf
        //LagType int32
        // parent leaf
        //SystemId string
        // parent leaf
        //Interval int32
        // parent leaf
        //Enabled bool
        // parent leaf
        //NameKey string `SNAPROUTE: KEY`
        // parent leaf
        //Distributing bool
        // parent leaf
        //Timeout int32
        // parent leaf
        //Activity int32
        // parent leaf
        //SystemPriority uint16
        // parent leaf
        Type string
        // parent leaf
        MinLinks uint16
        //yang_name: lacp-in-pkts class: leaf
        //LacpInPkts uint64
        //yang_name: lacp-out-pkts class: leaf
        //LacpOutPkts uint64
        //yang_name: lacp-rx-errors class: leaf
        //LacpRxErrors uint64
        //yang_name: lacp-tx-errors class: leaf
        //LacpTxErrors uint64
        //yang_name: lacp-unknown-errors class: leaf
        //LacpUnknownErrors uint64
        //yang_name: lacp-errors class: leaf
        //LacpErrors uint64
        '''

        members = self.swtch.getAllLaPortChannelMemberStates()

        for data in members:
            d = data['Object']

            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'
            print 'IfIndex: ' + "%s" % d['IfIndex'] + 'LagId: ' + "%s" %d['LagId'] + 'LagIfIndex: ' + "%s" %d['LagIfIndex']
            print 'OperState: ' + d['OperState']
            #print 'lagtype: ' + ('LACP' if not d['LagType'] else 'STATIC')
            print 'operkey: %s' % d['OperKey']
            #print 'mode: ' + ('ACTIVE' if not d['LacpMode'] else 'PASSIVE')
            #print 'interval: %s' % (('SLOW' if d['Interval'] else 'FAST'))
            #print 'system:\n'
            #print '\tsystemmac: %s' % d['SystemIdMac']
            #print '\tsysteprio: %s' % d['SystemPriority']
            #print '\tsystemId: %s' % d['SystemId']
            print 'actor:'
            stateStr = '\tstate: '
            for s in ('Activity', 'Timeout', 'Aggregatable', 'Synchronization', 'Collecting', 'Distributing', 'Defaulted'):
                if s == 'Synchronization' and not d[s]:
                    stateStr += s + ', '
                elif s == 'Activity' and not d[s]:
                    stateStr += s + ', '
                elif s in ('Activity', 'Synchronization'):
                    continue
                elif d[s]:
                    stateStr += s + ', '
            print stateStr.rstrip(',')

            print '\tstats:'
            for s in ('LacpInPkts', 'LacpOutPkts', 'LacpRxErrors', 'LacpTxErrors', 'LacpUnknownErrors', 'LacpErrors', 'LampInPdu', 'LampOutPdu', 'LampInResponsePdu', 'LampOutResponsePdu'):
                print '\t' + s, ': ', d[s]

            print 'partner:\n'
            print '\t' + 'key: %s' % d['PartnerKey']
            print '\t' + 'partnerid: ' + d['PartnerId']

            print 'debug:\n'
            try:
                print '\t' + 'debugId: %s' % d['DebugId']
                print '\t' + 'RxMachineState: %s' % RxMachineStateDict[d['RxMachine']]
                print '\t' + 'RxTime (rx pkt rcv): %s' % d['RxTime']
                print '\t' + 'MuxMachineState: %s' % MuxMachineStateDict[d['MuxMachine']]
                print '\t' + 'MuxReason: %s' % d['MuxReason']
                print '\t' + 'Actor Churn State: %s' % ChurnMachineStateDict[d['ActorChurnMachine']]
                print '\t' + 'Partner Churn State: %s' % ChurnMachineStateDict[d['PartnerChurnMachine']]
                print '\t' + 'Actor Churn Count: %s' % d['ActorChurnCount']
                print '\t' + 'Partner Churn Count: %s' % d['PartnerChurnCount']
                print '\t' + 'Actor Sync Transition Count: %s' % d['ActorSyncTransitionCount']
                print '\t' + 'Partner Sync Transition Count: %s' % d['PartnerSyncTransitionCount']
                print '\t' + 'Actor LAG ID change Count: %s' % d['ActorChangeCount']
                print '\t' + 'Partner LAG ID change Count: %s' % d['PartnerChangeCount']
            except Exception as e:
                print e


    # TODO fix cli so that the name is better
    def printBGPRouteStates(self, ):
        routes = self.swtch.getAllBGPRouteStates()
        print '\n\n---- BGP Routes ----'
        labels = ('Network', 'Mask', 'NextHop', 'Metric', 'LocalPref', 'Updated', 'Path')
        rows = []
        for r in routes:
            rt = r['Object']
            rows.append((rt['Network'],
                        "%s" %(rt['CIDRLen']),
                        "%s" %(rt['NextHop']),
                        "%s" %(rt['Metric']),
                        "%s" %(rt['LocalPref']),
                        "%s" %(rt['UpdatedDuration'].split(".")[0]),
                        "%s" %(rt['Path'])))
        width = 30
        print indent([labels]+rows, hasHeader=True, separateRows=False,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                     wrapfunc=lambda x: wrap_onspace_strict(x,width))

    def printIPv4IntfStates(self,):
        ipintfs = self.swtch.getAllIPv4IntfStates()
        print '\n\n---- IP Interfaces ----'
        labels = ('Interface', 'IfIndex', 'Address', 'OperState', 'L2IntfType', 'L2IntfId')
        rows = []
        for i in ipintfs:
            ip = i['Object']
            rows.append((ip['IntfRef'],
                        "%s" %(ip['IfIndex']),
                        "%s" %(ip['IpAddr']),
                        "%s" %(ip['OperState']),
                        "%s" %(ip['L2IntfType']),
                        "%s" %(ip['L2IntfId'])))
        width = 20
        print indent([labels]+rows, hasHeader=True, separateRows=False,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                     wrapfunc=lambda x: wrap_onspace_strict(x,width))

        labels = ('NumUpEvents', 'LastUpEventTime', 'NumDownEvents', 'LastDownEventtime')
        rows = []
        for i in ipintfs:
            ip = i['Object']
            rows.append(("%s" %(ip['NumUpEvents']),
                        "%s" %(ip['LastUpEventTime']),
                        "%s" %(ip['NumDownEvents']),
                        "%s" %(ip['LastDownEventTime'])))
        width = 20
        print indent([labels]+rows, hasHeader=True, separateRows=False,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                     wrapfunc=lambda x: wrap_onspace_strict(x,width))


    def printBGPNeighborStates(self):	   
		   sessionState=  {  1: "Idle",
				     2: "Connect",
				     3: "Active",
				     4: "OpenSent",
				     5: "OpenConfirm",
				     6: "Established"
				   } 
	
		   peers = self.swtch.getAllBGPNeighborStates()
		   if len(peers)>=0: 
			   print '\n'
			   labels = ('Neighbor','LocalAS','PeerAS','State','RxMsg','TxMsg','Description','TotalPrefixes')
			   for p in peers:
			       pr = p['Object']
			       RXmsg = (pr['Messages']['Received']['Notification']) + (pr['Messages']['Received']['Update'])
			       TXmsg = (pr['Messages']['Sent']['Notification']) + (pr['Messages']['Sent']['Update'])
			       rows.append( (pr['NeighborAddress'],
						 "%s" %(pr['LocalAS']),
						 "%s" %(pr['PeerAS']),
						 "%s" %(sessionState[pr['SessionState']]),
						 "%s" %(RXmsg),
						 "%s" %(TXmsg),
						 "%s" %(pr['Description']),
						 "%s" %(pr['TotalPrefixes'])))
					
					 

if __name__=='__main__':
    pass
