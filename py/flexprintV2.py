#!/usr/bin/python                                                                                                       
import requests
import json
import urllib2
from flexswitchV2 import FlexSwitch
from tablePrint import *
                                                                                                                        
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}                                          
class FlexSwitchShow( object):
    httpSuccessCodes = [200, 201, 202, 204]
    def  __init__ (self, ip, port):
        self.swtch = FlexSwitch(ip, port)

    def tblPrintObject(self, objName, headers, valuesList):
        '''
        Prints the data in a table format
        objName - Object which is being printed
        keys - This will be the attributes of the obj and column names
        valueList - List of tuples containing the data to be put into
                    the rows.  Each attribute must be in string format
        '''

        def terminal_size():
            import fcntl, termios, struct
            h, w, hp, wp = struct.unpack('HHHH',
                fcntl.ioctl(0, termios.TIOCGWINSZ,
                struct.pack('HHHH', 0, 0, 0, 0)))
            return h, w

        labels = headers
        rows=valuesList

        height, width = terminal_size()
        if labels:
            width = (width / len(labels)) + 5
            print indent([labels]+rows, hasHeader=True, separateRows=True,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                 wrapfunc=lambda x: wrap_onspace_strict(x,width))
        elif rows:
            width = (width / len(rows[0])) + 5
            print indent(rows, hasHeader=False, separateRows=True,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                 wrapfunc=lambda x: wrap_onspace_strict(x,width))
        else:
            print 'No Data To Display for %s' %(objName)


    def printArpEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Intf')
            header.append('ExpiryTimeLeft')

        objs = self.swtch.getAllArpEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Intf'])
            values.append('%s' % o['ExpiryTimeLeft'])
            rows.append(values)
        self.tblPrintObject('ArpEntryState', header, rows)


    def printOspfIPv4RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestId')
            header.append('DestType')
            header.append('AddrMask')
            header.append('OptCapabilities')
            header.append('AreaId')
            header.append('PathType')
            header.append('Cost')
            header.append('Type2Cost')
            header.append('NumOfPaths')
            header.append('NextHops')
            header.append('LSOrigin')

        objs = self.swtch.getAllOspfIPv4RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestId'])
            values.append('%s' % o['DestType'])
            values.append('%s' % o['AddrMask'])
            values.append('%s' % o['OptCapabilities'])
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['PathType'])
            values.append('%s' % o['Cost'])
            values.append('%s' % o['Type2Cost'])
            values.append('%s' % o['NumOfPaths'])
            values.append('%s' % o['NextHops'])
            values.append('%s' % o['LSOrigin'])
            rows.append(values)
        self.tblPrintObject('OspfIPv4RouteState', header, rows)


    def printOspfIfMetricEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfMetricAddressLessIf')
            header.append('IfMetricTOS')
            header.append('IfMetricIpAddress')
            header.append('IfMetricValue')

        objs = self.swtch.getAllOspfIfMetricEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfMetricAddressLessIf'])
            values.append('%s' % o['IfMetricTOS'])
            values.append('%s' % o['IfMetricIpAddress'])
            values.append('%s' % o['IfMetricValue'])
            rows.append(values)
        self.tblPrintObject('OspfIfMetricEntry', header, rows)


    def printNdpEntryHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Port')

        objs = self.swtch.getAllNdpEntryHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Port'])
            rows.append(values)
        self.tblPrintObject('NdpEntryHwState', header, rows)


    def printPolicyStmts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Conditions')
            header.append('Action')
            header.append('MatchConditions')

        objs = self.swtch.getAllPolicyStmts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['MatchConditions'])
            rows.append(values)
        self.tblPrintObject('PolicyStmt', header, rows)


    def printVlans(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VlanId')
            header.append('IntfList')
            header.append('UntagIntfList')

        objs = self.swtch.getAllVlans()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['IntfList'])
            values.append('%s' % o['UntagIntfList'])
            rows.append(values)
        self.tblPrintObject('Vlan', header, rows)


    def printDWDMModuleNwIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NwIntfId')
            header.append('ModuleId')
            header.append('ClntIntfIdToTributary0Map')
            header.append('ClntIntfIdToTributary1Map')
            header.append('EnableRxPRBSChecker')
            header.append('TxPulseShapeFltrRollOff')
            header.append('TxPower')
            header.append('RxPRBSInvertPattern')
            header.append('EnableTxPRBS')
            header.append('TxPRBSInvertPattern')
            header.append('AdminState')
            header.append('ChannelNumber')
            header.append('FECMode')
            header.append('ModulationFmt')
            header.append('TxPulseShapeFltrType')
            header.append('RxPRBSPattern')
            header.append('TxPRBSPattern')
            header.append('DiffEncoding')

        objs = self.swtch.getAllDWDMModuleNwIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ClntIntfIdToTributary0Map'])
            values.append('%s' % o['ClntIntfIdToTributary1Map'])
            values.append('%s' % o['EnableRxPRBSChecker'])
            values.append('%s' % o['TxPulseShapeFltrRollOff'])
            values.append('%s' % o['TxPower'])
            values.append('%s' % o['RxPRBSInvertPattern'])
            values.append('%s' % o['EnableTxPRBS'])
            values.append('%s' % o['TxPRBSInvertPattern'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['ChannelNumber'])
            values.append('%s' % o['FECMode'])
            values.append('%s' % o['ModulationFmt'])
            values.append('%s' % o['TxPulseShapeFltrType'])
            values.append('%s' % o['RxPRBSPattern'])
            values.append('%s' % o['TxPRBSPattern'])
            values.append('%s' % o['DiffEncoding'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntf', header, rows)


    def printComponentLoggings(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Module')
            header.append('Level')

        objs = self.swtch.getAllComponentLoggings()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Module'])
            values.append('%s' % o['Level'])
            rows.append(values)
        self.tblPrintObject('ComponentLogging', header, rows)


    def printFans(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FanId')
            header.append('AdminState')
            header.append('AdminSpeed')

        objs = self.swtch.getAllFans()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FanId'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['AdminSpeed'])
            rows.append(values)
        self.tblPrintObject('Fan', header, rows)


    def printIPv4EventStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventInfo')

        objs = self.swtch.getAllIPv4EventStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
        self.tblPrintObject('IPv4EventState', header, rows)


    def printSubIPv6Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('Type')
            header.append('MacAddr')
            header.append('Enable')

        objs = self.swtch.getAllSubIPv6Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('SubIPv6Intf', header, rows)


    def printIPv6RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')

        objs = self.swtch.getAllIPv6RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            rows.append(values)
        self.tblPrintObject('IPv6RouteState', header, rows)


    def printPsus(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('PsuId')
            header.append('AdminState')

        objs = self.swtch.getAllPsus()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['PsuId'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('Psu', header, rows)


    def printBGPv4NeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('Messages')
            header.append('Queues')

        objs = self.swtch.getAllBGPv4NeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            rows.append(values)
        self.tblPrintObject('BGPv4NeighborState', header, rows)


    def printOspfAreaEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AreaId')
            header.append('AuthType')
            header.append('ImportAsExtern')
            header.append('AreaSummary')
            header.append('AreaNssaTranslatorRole')
            header.append('StubDefaultCost')

        objs = self.swtch.getAllOspfAreaEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['ImportAsExtern'])
            values.append('%s' % o['AreaSummary'])
            values.append('%s' % o['AreaNssaTranslatorRole'])
            values.append('%s' % o['StubDefaultCost'])
            rows.append(values)
        self.tblPrintObject('OspfAreaEntry', header, rows)


    def printVxlanVtepInstances(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Intf')
            header.append('IntfRef')
            header.append('Vni')
            header.append('DstIp')
            header.append('VlanId')
            header.append('TOS')
            header.append('Mtu')
            header.append('InnerVlanHandlingMode')
            header.append('TTL')
            header.append('SrcIp')
            header.append('DstUDP')

        objs = self.swtch.getAllVxlanVtepInstances()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Intf'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Vni'])
            values.append('%s' % o['DstIp'])
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['TOS'])
            values.append('%s' % o['Mtu'])
            values.append('%s' % o['InnerVlanHandlingMode'])
            values.append('%s' % o['TTL'])
            values.append('%s' % o['SrcIp'])
            values.append('%s' % o['DstUDP'])
            rows.append(values)
        self.tblPrintObject('VxlanVtepInstance', header, rows)


    def printLaPortChannelStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LagId')
            header.append('IfIndex')
            header.append('Name')
            header.append('LagType')
            header.append('MinLinks')
            header.append('SystemIdMac')
            header.append('SystemPriority')
            header.append('AdminState')
            header.append('OperState')
            header.append('Members')
            header.append('MembersUpInBundle')
            header.append('Interval')
            header.append('LagHash')
            header.append('LacpMode')

        objs = self.swtch.getAllLaPortChannelStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LagId'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['LagType'])
            values.append('%s' % o['MinLinks'])
            values.append('%s' % o['SystemIdMac'])
            values.append('%s' % o['SystemPriority'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['Members'])
            values.append('%s' % o['MembersUpInBundle'])
            values.append('%s' % o['Interval'])
            values.append('%s' % o['LagHash'])
            values.append('%s' % o['LacpMode'])
            rows.append(values)
        self.tblPrintObject('LaPortChannelState', header, rows)


    def printDhcpGlobalConfigs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DhcpConfigKey')
            header.append('Enable')
            header.append('DefaultLeaseTime')
            header.append('MaxLeaseTime')

        objs = self.swtch.getAllDhcpGlobalConfigs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DhcpConfigKey'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['DefaultLeaseTime'])
            values.append('%s' % o['MaxLeaseTime'])
            rows.append(values)
        self.tblPrintObject('DhcpGlobalConfig', header, rows)


    def printDhcpRelayIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('Enable')
            header.append('ServerIp')

        objs = self.swtch.getAllDhcpRelayIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['ServerIp'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntf', header, rows)


    def printBGPv4Neighbors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('BfdEnable')
            header.append('MultiHopTTL')
            header.append('LocalAS')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixesDisconnect')
            header.append('PeerAS')
            header.append('AddPathsMaxTx')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('BfdSessionParam')
            header.append('HoldTime')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv4Neighbors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['BfdEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['BfdSessionParam'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv4Neighbor', header, rows)


    def printStpPortStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('BrgIfIndex')
            header.append('IfIndex')
            header.append('Priority')
            header.append('PathCost')
            header.append('PathCost32')
            header.append('State')
            header.append('DesignatedRoot')
            header.append('DesignatedCost')
            header.append('DesignatedBridge')
            header.append('DesignatedPort')
            header.append('ForwardTransitions')
            header.append('AdminEdgePort')
            header.append('AdminPathCost')
            header.append('OperEdgePort')
            header.append('OperPointToPoint')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('ForwardDelay')
            header.append('BridgeAssurance')
            header.append('BridgeAssuranceInconsistant')
            header.append('BpduGuard')
            header.append('BpduGuardDetected')
            header.append('StpInPkts')
            header.append('StpOutPkts')
            header.append('RstpInPkts')
            header.append('RstpOutPkts')
            header.append('TcInPkts')
            header.append('TcOutPkts')
            header.append('TcAckInPkts')
            header.append('TcAckOutPkts')
            header.append('PvstInPkts')
            header.append('PvstOutPkts')
            header.append('BpduInPkts')
            header.append('BpduOutPkts')
            header.append('PimPrevState')
            header.append('PimCurrState')
            header.append('PrtmPrevState')
            header.append('PrtmCurrState')
            header.append('PrxmPrevState')
            header.append('PrxmCurrState')
            header.append('PstmPrevState')
            header.append('PstmCurrState')
            header.append('TcmPrevState')
            header.append('TcmCurrState')
            header.append('PpmPrevState')
            header.append('PpmCurrState')
            header.append('PtxmPrevState')
            header.append('PtxmCurrState')
            header.append('PtimPrevState')
            header.append('PtimCurrState')
            header.append('BdmPrevState')
            header.append('BdmCurrState')
            header.append('EdgeDelayWhile')
            header.append('FdWhile')
            header.append('HelloWhen')
            header.append('MdelayWhile')
            header.append('RbWhile')
            header.append('RcvdInfoWhile')
            header.append('RrWhile')
            header.append('TcWhile')
            header.append('BaWhile')
            header.append('Enable')
            header.append('BpduGuardInterval')

        objs = self.swtch.getAllStpPortStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['BrgIfIndex'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['PathCost'])
            values.append('%s' % o['PathCost32'])
            values.append('%s' % o['State'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['DesignatedCost'])
            values.append('%s' % o['DesignatedBridge'])
            values.append('%s' % o['DesignatedPort'])
            values.append('%s' % o['ForwardTransitions'])
            values.append('%s' % o['AdminEdgePort'])
            values.append('%s' % o['AdminPathCost'])
            values.append('%s' % o['OperEdgePort'])
            values.append('%s' % o['OperPointToPoint'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeAssurance'])
            values.append('%s' % o['BridgeAssuranceInconsistant'])
            values.append('%s' % o['BpduGuard'])
            values.append('%s' % o['BpduGuardDetected'])
            values.append('%s' % o['StpInPkts'])
            values.append('%s' % o['StpOutPkts'])
            values.append('%s' % o['RstpInPkts'])
            values.append('%s' % o['RstpOutPkts'])
            values.append('%s' % o['TcInPkts'])
            values.append('%s' % o['TcOutPkts'])
            values.append('%s' % o['TcAckInPkts'])
            values.append('%s' % o['TcAckOutPkts'])
            values.append('%s' % o['PvstInPkts'])
            values.append('%s' % o['PvstOutPkts'])
            values.append('%s' % o['BpduInPkts'])
            values.append('%s' % o['BpduOutPkts'])
            values.append('%s' % o['PimPrevState'])
            values.append('%s' % o['PimCurrState'])
            values.append('%s' % o['PrtmPrevState'])
            values.append('%s' % o['PrtmCurrState'])
            values.append('%s' % o['PrxmPrevState'])
            values.append('%s' % o['PrxmCurrState'])
            values.append('%s' % o['PstmPrevState'])
            values.append('%s' % o['PstmCurrState'])
            values.append('%s' % o['TcmPrevState'])
            values.append('%s' % o['TcmCurrState'])
            values.append('%s' % o['PpmPrevState'])
            values.append('%s' % o['PpmCurrState'])
            values.append('%s' % o['PtxmPrevState'])
            values.append('%s' % o['PtxmCurrState'])
            values.append('%s' % o['PtimPrevState'])
            values.append('%s' % o['PtimCurrState'])
            values.append('%s' % o['BdmPrevState'])
            values.append('%s' % o['BdmCurrState'])
            values.append('%s' % o['EdgeDelayWhile'])
            values.append('%s' % o['FdWhile'])
            values.append('%s' % o['HelloWhen'])
            values.append('%s' % o['MdelayWhile'])
            values.append('%s' % o['RbWhile'])
            values.append('%s' % o['RcvdInfoWhile'])
            values.append('%s' % o['RrWhile'])
            values.append('%s' % o['TcWhile'])
            values.append('%s' % o['BaWhile'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['BpduGuardInterval'])
            rows.append(values)
        self.tblPrintObject('StpPortState', header, rows)


    def printFMgrGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllFMgrGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('FMgrGlobal', header, rows)


    def printNotifierEnables(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AlarmEnable')
            header.append('FaultEnable')
            header.append('EventEnable')

        objs = self.swtch.getAllNotifierEnables()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AlarmEnable'])
            values.append('%s' % o['FaultEnable'])
            values.append('%s' % o['EventEnable'])
            rows.append(values)
        self.tblPrintObject('NotifierEnable', header, rows)


    def printLaPortChannels(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LagId')
            header.append('Members')
            header.append('SystemIdMac')
            header.append('MinLinks')
            header.append('SystemPriority')
            header.append('Interval')
            header.append('LagHash')
            header.append('AdminState')
            header.append('LagType')
            header.append('LacpMode')

        objs = self.swtch.getAllLaPortChannels()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LagId'])
            values.append('%s' % o['Members'])
            values.append('%s' % o['SystemIdMac'])
            values.append('%s' % o['MinLinks'])
            values.append('%s' % o['SystemPriority'])
            values.append('%s' % o['Interval'])
            values.append('%s' % o['LagHash'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['LagType'])
            values.append('%s' % o['LacpMode'])
            rows.append(values)
        self.tblPrintObject('LaPortChannel', header, rows)


    def printBGPPolicyConditionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')

        objs = self.swtch.getAllBGPPolicyConditionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyConditionState', header, rows)


    def printIPv4RouteHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NextHopIps')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')

        objs = self.swtch.getAllIPv4RouteHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NextHopIps'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            rows.append(values)
        self.tblPrintObject('IPv4RouteHwState', header, rows)


    def printBfdSessionParams(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('RequiredMinRxInterval')
            header.append('AuthData')
            header.append('DemandEnabled')
            header.append('AuthKeyId')
            header.append('AuthType')
            header.append('DesiredMinTxInterval')
            header.append('AuthenticationEnabled')
            header.append('RequiredMinEchoRxInterval')
            header.append('LocalMultiplier')

        objs = self.swtch.getAllBfdSessionParams()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['AuthData'])
            values.append('%s' % o['DemandEnabled'])
            values.append('%s' % o['AuthKeyId'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['AuthenticationEnabled'])
            values.append('%s' % o['RequiredMinEchoRxInterval'])
            values.append('%s' % o['LocalMultiplier'])
            rows.append(values)
        self.tblPrintObject('BfdSessionParam', header, rows)


    def printBfdSessionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('SessionId')
            header.append('ParamName')
            header.append('IfIndex')
            header.append('InterfaceSpecific')
            header.append('IfName')
            header.append('PerLinkSession')
            header.append('LocalMacAddr')
            header.append('RemoteMacAddr')
            header.append('RegisteredProtocols')
            header.append('SessionState')
            header.append('RemoteSessionState')
            header.append('LocalDiscriminator')
            header.append('RemoteDiscriminator')
            header.append('LocalDiagType')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RemoteMinRxInterval')
            header.append('DetectionMultiplier')
            header.append('RemoteDetectionMultiplier')
            header.append('DemandMode')
            header.append('RemoteDemandMode')
            header.append('AuthSeqKnown')
            header.append('AuthType')
            header.append('ReceivedAuthSeq')
            header.append('SentAuthSeq')
            header.append('NumTxPackets')
            header.append('NumRxPackets')

        objs = self.swtch.getAllBfdSessionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['SessionId'])
            values.append('%s' % o['ParamName'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['InterfaceSpecific'])
            values.append('%s' % o['IfName'])
            values.append('%s' % o['PerLinkSession'])
            values.append('%s' % o['LocalMacAddr'])
            values.append('%s' % o['RemoteMacAddr'])
            values.append('%s' % o['RegisteredProtocols'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['RemoteSessionState'])
            values.append('%s' % o['LocalDiscriminator'])
            values.append('%s' % o['RemoteDiscriminator'])
            values.append('%s' % o['LocalDiagType'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RemoteMinRxInterval'])
            values.append('%s' % o['DetectionMultiplier'])
            values.append('%s' % o['RemoteDetectionMultiplier'])
            values.append('%s' % o['DemandMode'])
            values.append('%s' % o['RemoteDemandMode'])
            values.append('%s' % o['AuthSeqKnown'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['ReceivedAuthSeq'])
            values.append('%s' % o['SentAuthSeq'])
            values.append('%s' % o['NumTxPackets'])
            values.append('%s' % o['NumRxPackets'])
            rows.append(values)
        self.tblPrintObject('BfdSessionState', header, rows)


    def printDWDMModuleStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('ModuleState')
            header.append('ModuleVoltage')
            header.append('ModuleTemp')
            header.append('Populated')
            header.append('VendorName')
            header.append('VendorPartNum')
            header.append('VendorSerialNum')
            header.append('VendorDateCode')
            header.append('ModuleHWVersion')
            header.append('ModuleFWAVersion')
            header.append('ModuleFWBVersion')

        objs = self.swtch.getAllDWDMModuleStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ModuleState'])
            values.append('%s' % o['ModuleVoltage'])
            values.append('%s' % o['ModuleTemp'])
            values.append('%s' % o['Populated'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorPartNum'])
            values.append('%s' % o['VendorSerialNum'])
            values.append('%s' % o['VendorDateCode'])
            values.append('%s' % o['ModuleHWVersion'])
            values.append('%s' % o['ModuleFWAVersion'])
            values.append('%s' % o['ModuleFWBVersion'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleState', header, rows)


    def printDhcpRelayIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfId')
            header.append('TotalDrops')
            header.append('TotalDhcpClientRx')
            header.append('TotalDhcpClientTx')
            header.append('TotalDhcpServerRx')
            header.append('TotalDhcpServerTx')

        objs = self.swtch.getAllDhcpRelayIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfId'])
            values.append('%s' % o['TotalDrops'])
            values.append('%s' % o['TotalDhcpClientRx'])
            values.append('%s' % o['TotalDhcpClientTx'])
            values.append('%s' % o['TotalDhcpServerRx'])
            values.append('%s' % o['TotalDhcpServerTx'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntfState', header, rows)


    def printDhcpRelayGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DhcpRelay')
            header.append('Enable')

        objs = self.swtch.getAllDhcpRelayGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DhcpRelay'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayGlobal', header, rows)


    def printPlatformStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ObjName')
            header.append('ProductName')
            header.append('SerialNum')
            header.append('Manufacturer')
            header.append('Vendor')
            header.append('Release')
            header.append('PlatformName')
            header.append('Version')

        objs = self.swtch.getAllPlatformStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ObjName'])
            values.append('%s' % o['ProductName'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Manufacturer'])
            values.append('%s' % o['Vendor'])
            values.append('%s' % o['Release'])
            values.append('%s' % o['PlatformName'])
            values.append('%s' % o['Version'])
            rows.append(values)
        self.tblPrintObject('PlatformState', header, rows)


    def printBfdSessionParamStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('NumSessions')
            header.append('LocalMultiplier')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RequiredMinEchoRxInterval')
            header.append('DemandEnabled')
            header.append('AuthenticationEnabled')
            header.append('AuthenticationType')
            header.append('AuthenticationKeyId')
            header.append('AuthenticationData')

        objs = self.swtch.getAllBfdSessionParamStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['NumSessions'])
            values.append('%s' % o['LocalMultiplier'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RequiredMinEchoRxInterval'])
            values.append('%s' % o['DemandEnabled'])
            values.append('%s' % o['AuthenticationEnabled'])
            values.append('%s' % o['AuthenticationType'])
            values.append('%s' % o['AuthenticationKeyId'])
            values.append('%s' % o['AuthenticationData'])
            rows.append(values)
        self.tblPrintObject('BfdSessionParamState', header, rows)


    def printOspfLsdbEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LsdbType')
            header.append('LsdbAreaId')
            header.append('LsdbLsid')
            header.append('LsdbRouterId')
            header.append('LsdbSequence')
            header.append('LsdbAge')
            header.append('LsdbChecksum')
            header.append('LsdbAdvertisement')

        objs = self.swtch.getAllOspfLsdbEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LsdbType'])
            values.append('%s' % o['LsdbAreaId'])
            values.append('%s' % o['LsdbLsid'])
            values.append('%s' % o['LsdbRouterId'])
            values.append('%s' % o['LsdbSequence'])
            values.append('%s' % o['LsdbAge'])
            values.append('%s' % o['LsdbChecksum'])
            values.append('%s' % o['LsdbAdvertisement'])
            rows.append(values)
        self.tblPrintObject('OspfLsdbEntryState', header, rows)


    def printArpLinuxEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('HWType')
            header.append('MacAddr')
            header.append('IfName')

        objs = self.swtch.getAllArpLinuxEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['HWType'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['IfName'])
            rows.append(values)
        self.tblPrintObject('ArpLinuxEntryState', header, rows)


    def printStpBridgeStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('IfIndex')
            header.append('Address')
            header.append('Priority')
            header.append('ProtocolSpecification')
            header.append('TimeSinceTopologyChange')
            header.append('TopChanges')
            header.append('DesignatedRoot')
            header.append('RootCost')
            header.append('RootPort')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('HoldTime')
            header.append('ForwardDelay')
            header.append('BridgeMaxAge')
            header.append('BridgeHelloTime')
            header.append('BridgeHoldTime')
            header.append('BridgeForwardDelay')
            header.append('TxHoldCount')

        objs = self.swtch.getAllStpBridgeStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Address'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['ProtocolSpecification'])
            values.append('%s' % o['TimeSinceTopologyChange'])
            values.append('%s' % o['TopChanges'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['RootCost'])
            values.append('%s' % o['RootPort'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeMaxAge'])
            values.append('%s' % o['BridgeHelloTime'])
            values.append('%s' % o['BridgeHoldTime'])
            values.append('%s' % o['BridgeForwardDelay'])
            values.append('%s' % o['TxHoldCount'])
            rows.append(values)
        self.tblPrintObject('StpBridgeState', header, rows)


    def printBGPPolicyConditions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionType')
            header.append('IpPrefix')
            header.append('MaskLengthRange')

        objs = self.swtch.getAllBGPPolicyConditions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionType'])
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['MaskLengthRange'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyCondition', header, rows)


    def printOspfGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('AdminStat')
            header.append('ASBdrRtrStatus')
            header.append('RestartSupport')
            header.append('RestartInterval')
            header.append('TOSSupport')
            header.append('ReferenceBandwidth')

        objs = self.swtch.getAllOspfGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['AdminStat'])
            values.append('%s' % o['ASBdrRtrStatus'])
            values.append('%s' % o['RestartSupport'])
            values.append('%s' % o['RestartInterval'])
            values.append('%s' % o['TOSSupport'])
            values.append('%s' % o['ReferenceBandwidth'])
            rows.append(values)
        self.tblPrintObject('OspfGlobal', header, rows)


    def printDhcpRelayHostDhcpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('MacAddr')
            header.append('ServerIp')
            header.append('OfferedIp')
            header.append('GatewayIp')
            header.append('AcceptedIp')
            header.append('RequestedIp')
            header.append('ClientDiscover')
            header.append('ClientRequest')
            header.append('ClientRequests')
            header.append('ClientResponses')
            header.append('ServerOffer')
            header.append('ServerAck')
            header.append('ServerRequests')
            header.append('ServerResponses')

        objs = self.swtch.getAllDhcpRelayHostDhcpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['ServerIp'])
            values.append('%s' % o['OfferedIp'])
            values.append('%s' % o['GatewayIp'])
            values.append('%s' % o['AcceptedIp'])
            values.append('%s' % o['RequestedIp'])
            values.append('%s' % o['ClientDiscover'])
            values.append('%s' % o['ClientRequest'])
            values.append('%s' % o['ClientRequests'])
            values.append('%s' % o['ClientResponses'])
            values.append('%s' % o['ServerOffer'])
            values.append('%s' % o['ServerAck'])
            values.append('%s' % o['ServerRequests'])
            values.append('%s' % o['ServerResponses'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayHostDhcpState', header, rows)


    def printDhcpRelayIntfServerStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfId')
            header.append('ServerIp')
            header.append('Request')
            header.append('Responses')

        objs = self.swtch.getAllDhcpRelayIntfServerStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfId'])
            values.append('%s' % o['ServerIp'])
            values.append('%s' % o['Request'])
            values.append('%s' % o['Responses'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntfServerState', header, rows)


    def printLLDPIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('Enable')
            header.append('LocalPort')
            header.append('PeerMac')
            header.append('PeerPort')
            header.append('PeerHostName')
            header.append('HoldTime')
            header.append('SystemCapabilities')
            header.append('EnabledCapabilities')

        objs = self.swtch.getAllLLDPIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['LocalPort'])
            values.append('%s' % o['PeerMac'])
            values.append('%s' % o['PeerPort'])
            values.append('%s' % o['PeerHostName'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['SystemCapabilities'])
            values.append('%s' % o['EnabledCapabilities'])
            rows.append(values)
        self.tblPrintObject('LLDPIntfState', header, rows)


    def printLeds(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LedId')
            header.append('LedAdmin')
            header.append('LedSetColor')

        objs = self.swtch.getAllLeds()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LedId'])
            values.append('%s' % o['LedAdmin'])
            values.append('%s' % o['LedSetColor'])
            rows.append(values)
        self.tblPrintObject('Led', header, rows)


    def printPolicyDefinitions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Priority')
            header.append('StatementList')
            header.append('MatchType')
            header.append('PolicyType')

        objs = self.swtch.getAllPolicyDefinitions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['StatementList'])
            values.append('%s' % o['MatchType'])
            values.append('%s' % o['PolicyType'])
            rows.append(values)
        self.tblPrintObject('PolicyDefinition', header, rows)


    def printOspfVirtNbrEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VirtNbrRtrId')
            header.append('VirtNbrArea')
            header.append('VirtNbrIpAddr')
            header.append('VirtNbrOptions')
            header.append('VirtNbrState')
            header.append('VirtNbrEvents')
            header.append('VirtNbrHelloSuppressed')

        objs = self.swtch.getAllOspfVirtNbrEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VirtNbrRtrId'])
            values.append('%s' % o['VirtNbrArea'])
            values.append('%s' % o['VirtNbrIpAddr'])
            values.append('%s' % o['VirtNbrOptions'])
            values.append('%s' % o['VirtNbrState'])
            values.append('%s' % o['VirtNbrEvents'])
            values.append('%s' % o['VirtNbrHelloSuppressed'])
            rows.append(values)
        self.tblPrintObject('OspfVirtNbrEntryState', header, rows)


    def printDWDMModuleClntIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ClntIntfId')
            header.append('ModuleId')
            header.append('PRBSTxErrCntLane0')
            header.append('PRBSTxErrCntLane1')
            header.append('PRBSTxErrCntLane2')
            header.append('PRBSTxErrCntLane3')

        objs = self.swtch.getAllDWDMModuleClntIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ClntIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['PRBSTxErrCntLane0'])
            values.append('%s' % o['PRBSTxErrCntLane1'])
            values.append('%s' % o['PRBSTxErrCntLane2'])
            values.append('%s' % o['PRBSTxErrCntLane3'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleClntIntfState', header, rows)


    def printRouteStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('TotalRouteCount')
            header.append('ECMPRouteCount')
            header.append('V4RouteCount')
            header.append('V6RouteCount')
            header.append('PerProtocolRouteCountList')

        objs = self.swtch.getAllRouteStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['TotalRouteCount'])
            values.append('%s' % o['ECMPRouteCount'])
            values.append('%s' % o['V4RouteCount'])
            values.append('%s' % o['V6RouteCount'])
            values.append('%s' % o['PerProtocolRouteCountList'])
            rows.append(values)
        self.tblPrintObject('RouteStatState', header, rows)


    def printRouteDistanceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('Distance')

        objs = self.swtch.getAllRouteDistanceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['Distance'])
            rows.append(values)
        self.tblPrintObject('RouteDistanceState', header, rows)


    def printLogicalIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Type')

        objs = self.swtch.getAllLogicalIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Type'])
            rows.append(values)
        self.tblPrintObject('LogicalIntf', header, rows)


    def printBGPv6NeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('Messages')
            header.append('Queues')

        objs = self.swtch.getAllBGPv6NeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            rows.append(values)
        self.tblPrintObject('BGPv6NeighborState', header, rows)


    def printMacTableEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('MacAddr')
            header.append('Port')
            header.append('VlanId')

        objs = self.swtch.getAllMacTableEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Port'])
            values.append('%s' % o['VlanId'])
            rows.append(values)
        self.tblPrintObject('MacTableEntryState', header, rows)


    def printBGPPeerGroups(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('Description')
            header.append('MaxPrefixesRestartTimer')
            header.append('RouteReflectorClient')
            header.append('MultiHopTTL')
            header.append('MaxPrefixesDisconnect')
            header.append('LocalAS')
            header.append('KeepaliveTime')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixes')
            header.append('AddPathsMaxTx')
            header.append('MultiHopEnable')
            header.append('AddPathsRx')
            header.append('MaxPrefixesThresholdPct')
            header.append('HoldTime')
            header.append('PeerAS')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPPeerGroups()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPPeerGroup', header, rows)


    def printSystemParams(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('MgmtIp')
            header.append('Hostname')
            header.append('Version')
            header.append('SwitchMac')
            header.append('Description')

        objs = self.swtch.getAllSystemParams()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['MgmtIp'])
            values.append('%s' % o['Hostname'])
            values.append('%s' % o['Version'])
            values.append('%s' % o['SwitchMac'])
            values.append('%s' % o['Description'])
            rows.append(values)
        self.tblPrintObject('SystemParam', header, rows)


    def printBfdGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllBfdGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('BfdGlobal', header, rows)


    def printAlarmStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('EventId')
            header.append('EventName')
            header.append('SrcObjName')
            header.append('OwnerName')
            header.append('OwnerId')
            header.append('Severity')
            header.append('Description')
            header.append('OccuranceTime')
            header.append('SrcObjKey')
            header.append('SrcObjUUID')
            header.append('ResolutionTime')
            header.append('ResolutionReason')

        objs = self.swtch.getAllAlarmStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['EventId'])
            values.append('%s' % o['EventName'])
            values.append('%s' % o['SrcObjName'])
            values.append('%s' % o['OwnerName'])
            values.append('%s' % o['OwnerId'])
            values.append('%s' % o['Severity'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['OccuranceTime'])
            values.append('%s' % o['SrcObjKey'])
            values.append('%s' % o['SrcObjUUID'])
            values.append('%s' % o['ResolutionTime'])
            values.append('%s' % o['ResolutionReason'])
            rows.append(values)
        self.tblPrintObject('AlarmState', header, rows)


    def printBGPPolicyStmts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Actions')

        objs = self.swtch.getAllBGPPolicyStmts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Actions'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyStmt', header, rows)


    def printArpGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Timeout')

        objs = self.swtch.getAllArpGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Timeout'])
            rows.append(values)
        self.tblPrintObject('ArpGlobal', header, rows)


    def printBGPPolicyStmtStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Actions')

        objs = self.swtch.getAllBGPPolicyStmtStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Actions'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyStmtState', header, rows)


    def printBGPv4PeerGroups(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('Description')
            header.append('MaxPrefixesRestartTimer')
            header.append('RouteReflectorClient')
            header.append('MultiHopTTL')
            header.append('MaxPrefixesDisconnect')
            header.append('LocalAS')
            header.append('KeepaliveTime')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixes')
            header.append('AddPathsMaxTx')
            header.append('MultiHopEnable')
            header.append('AddPathsRx')
            header.append('MaxPrefixesThresholdPct')
            header.append('HoldTime')
            header.append('PeerAS')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv4PeerGroups()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv4PeerGroup', header, rows)


    def printIPv4RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')

        objs = self.swtch.getAllIPv4RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            rows.append(values)
        self.tblPrintObject('IPv4RouteState', header, rows)


    def printBGPIPv6Aggregates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpPrefix')
            header.append('SendSummaryOnly')
            header.append('GenerateASSet')

        objs = self.swtch.getAllBGPIPv6Aggregates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['SendSummaryOnly'])
            values.append('%s' % o['GenerateASSet'])
            rows.append(values)
        self.tblPrintObject('BGPIPv6Aggregate', header, rows)


    def printBGPAggregates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpPrefix')
            header.append('SendSummaryOnly')
            header.append('GenerateASSet')

        objs = self.swtch.getAllBGPAggregates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['SendSummaryOnly'])
            values.append('%s' % o['GenerateASSet'])
            rows.append(values)
        self.tblPrintObject('BGPAggregate', header, rows)


    def printBfdGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('NumTotalSessions')
            header.append('NumUpSessions')
            header.append('NumDownSessions')
            header.append('NumAdminDownSessions')

        objs = self.swtch.getAllBfdGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['NumTotalSessions'])
            values.append('%s' % o['NumUpSessions'])
            values.append('%s' % o['NumDownSessions'])
            values.append('%s' % o['NumAdminDownSessions'])
            rows.append(values)
        self.tblPrintObject('BfdGlobalState', header, rows)


    def printFanStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FanId')
            header.append('OperMode')
            header.append('OperSpeed')
            header.append('OperDirection')
            header.append('Status')
            header.append('Model')
            header.append('SerialNum')
            header.append('LedId')

        objs = self.swtch.getAllFanStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FanId'])
            values.append('%s' % o['OperMode'])
            values.append('%s' % o['OperSpeed'])
            values.append('%s' % o['OperDirection'])
            values.append('%s' % o['Status'])
            values.append('%s' % o['Model'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['LedId'])
            rows.append(values)
        self.tblPrintObject('FanState', header, rows)


    def printBGPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('AS')
            header.append('UseMultiplePaths')
            header.append('EBGPMaxPaths')
            header.append('EBGPAllowMultipleAS')
            header.append('IBGPMaxPaths')
            header.append('TotalPaths')
            header.append('TotalPrefixes')

        objs = self.swtch.getAllBGPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['AS'])
            values.append('%s' % o['UseMultiplePaths'])
            values.append('%s' % o['EBGPMaxPaths'])
            values.append('%s' % o['EBGPAllowMultipleAS'])
            values.append('%s' % o['IBGPMaxPaths'])
            values.append('%s' % o['TotalPaths'])
            values.append('%s' % o['TotalPrefixes'])
            rows.append(values)
        self.tblPrintObject('BGPGlobalState', header, rows)


    def printOspfEventStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventType')
            header.append('EventInfo')

        objs = self.swtch.getAllOspfEventStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventType'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
        self.tblPrintObject('OspfEventState', header, rows)


    def printLLDPIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('Enable')

        objs = self.swtch.getAllLLDPIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('LLDPIntf', header, rows)


    def printBufferGlobalStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DeviceId')
            header.append('BufferStat')
            header.append('EgressBufferStat')
            header.append('IngressBufferStat')

        objs = self.swtch.getAllBufferGlobalStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DeviceId'])
            values.append('%s' % o['BufferStat'])
            values.append('%s' % o['EgressBufferStat'])
            values.append('%s' % o['IngressBufferStat'])
            rows.append(values)
        self.tblPrintObject('BufferGlobalStatState', header, rows)


    def printIPv6IntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')

        objs = self.swtch.getAllIPv6IntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            rows.append(values)
        self.tblPrintObject('IPv6IntfState', header, rows)


    def printIPv4Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')

        objs = self.swtch.getAllIPv4Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            rows.append(values)
        self.tblPrintObject('IPv4Intf', header, rows)


    def printPolicyStmtStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Action')
            header.append('PolicyList')

        objs = self.swtch.getAllPolicyStmtStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['PolicyList'])
            rows.append(values)
        self.tblPrintObject('PolicyStmtState', header, rows)


    def printIPv6Routes(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NetworkMask')
            header.append('NextHop')
            header.append('Protocol')
            header.append('NullRoute')
            header.append('Cost')

        objs = self.swtch.getAllIPv6Routes()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NetworkMask'])
            values.append('%s' % o['NextHop'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['NullRoute'])
            values.append('%s' % o['Cost'])
            rows.append(values)
        self.tblPrintObject('IPv6Route', header, rows)


    def printNDPEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Intf')
            header.append('ExpiryTimeLeft')

        objs = self.swtch.getAllNDPEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Intf'])
            values.append('%s' % o['ExpiryTimeLeft'])
            rows.append(values)
        self.tblPrintObject('NDPEntryState', header, rows)


    def printDWDMModuleClntIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ClntIntfId')
            header.append('ModuleId')
            header.append('NwLaneTributaryToClntIntfMap')
            header.append('HostTxEqDfe')
            header.append('HostRxSerializerTap1Gain')
            header.append('RxPRBSPattern')
            header.append('HostRxSerializerTap2Delay')
            header.append('HostRxSerializerTap2Gain')
            header.append('HostRxSerializerTap0Delay')
            header.append('HostTxEqCtle')
            header.append('TxPRBSPattern')
            header.append('HostTxEqLfCtle')
            header.append('AdminState')
            header.append('RXFECDecDisable')
            header.append('EnableTxPRBSChecker')
            header.append('EnableHostLoopback')
            header.append('HostRxSerializerTap0Gain')
            header.append('TXFECDecDisable')
            header.append('EnableRxPRBS')
            header.append('EnableIntSerdesNWLoopback')

        objs = self.swtch.getAllDWDMModuleClntIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ClntIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['NwLaneTributaryToClntIntfMap'])
            values.append('%s' % o['HostTxEqDfe'])
            values.append('%s' % o['HostRxSerializerTap1Gain'])
            values.append('%s' % o['RxPRBSPattern'])
            values.append('%s' % o['HostRxSerializerTap2Delay'])
            values.append('%s' % o['HostRxSerializerTap2Gain'])
            values.append('%s' % o['HostRxSerializerTap0Delay'])
            values.append('%s' % o['HostTxEqCtle'])
            values.append('%s' % o['TxPRBSPattern'])
            values.append('%s' % o['HostTxEqLfCtle'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['RXFECDecDisable'])
            values.append('%s' % o['EnableTxPRBSChecker'])
            values.append('%s' % o['EnableHostLoopback'])
            values.append('%s' % o['HostRxSerializerTap0Gain'])
            values.append('%s' % o['TXFECDecDisable'])
            values.append('%s' % o['EnableRxPRBS'])
            values.append('%s' % o['EnableIntSerdesNWLoopback'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleClntIntf', header, rows)


    def printRouteStatsPerInterfaceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Intfref')
            header.append('V4Routes')
            header.append('V6Routes')

        objs = self.swtch.getAllRouteStatsPerInterfaceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Intfref'])
            values.append('%s' % o['V4Routes'])
            values.append('%s' % o['V6Routes'])
            rows.append(values)
        self.tblPrintObject('RouteStatsPerInterfaceState', header, rows)


    def printDhcpIntfConfigs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Subnet')
            header.append('SubnetMask')
            header.append('IPAddrRange')
            header.append('BroadcastAddr')
            header.append('RouterAddr')
            header.append('DNSServerAddr')
            header.append('DomainName')
            header.append('Enable')

        objs = self.swtch.getAllDhcpIntfConfigs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Subnet'])
            values.append('%s' % o['SubnetMask'])
            values.append('%s' % o['IPAddrRange'])
            values.append('%s' % o['BroadcastAddr'])
            values.append('%s' % o['RouterAddr'])
            values.append('%s' % o['DNSServerAddr'])
            values.append('%s' % o['DomainName'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('DhcpIntfConfig', header, rows)


    def printVrrpIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('IntfIpAddr')
            header.append('Priority')
            header.append('VirtualIPv4Addr')
            header.append('AdvertisementInterval')
            header.append('PreemptMode')
            header.append('VirtualRouterMACAddress')
            header.append('SkewTime')
            header.append('MasterDownTimer')
            header.append('VrrpState')

        objs = self.swtch.getAllVrrpIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IntfIpAddr'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['VirtualIPv4Addr'])
            values.append('%s' % o['AdvertisementInterval'])
            values.append('%s' % o['PreemptMode'])
            values.append('%s' % o['VirtualRouterMACAddress'])
            values.append('%s' % o['SkewTime'])
            values.append('%s' % o['MasterDownTimer'])
            values.append('%s' % o['VrrpState'])
            rows.append(values)
        self.tblPrintObject('VrrpIntfState', header, rows)


    def printOspfNbrEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NbrIpAddr')
            header.append('NbrAddressLessIndex')
            header.append('NbrRtrId')
            header.append('NbrOptions')
            header.append('NbrState')
            header.append('NbrEvents')
            header.append('NbrHelloSuppressed')

        objs = self.swtch.getAllOspfNbrEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NbrIpAddr'])
            values.append('%s' % o['NbrAddressLessIndex'])
            values.append('%s' % o['NbrRtrId'])
            values.append('%s' % o['NbrOptions'])
            values.append('%s' % o['NbrState'])
            values.append('%s' % o['NbrEvents'])
            values.append('%s' % o['NbrHelloSuppressed'])
            rows.append(values)
        self.tblPrintObject('OspfNbrEntryState', header, rows)


    def printSystemStatusStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Ready')
            header.append('Reason')
            header.append('UpTime')
            header.append('NumCreateCalls')
            header.append('NumDeleteCalls')
            header.append('NumUpdateCalls')
            header.append('NumGetCalls')
            header.append('NumActionCalls')
            header.append('FlexDaemons')

        objs = self.swtch.getAllSystemStatusStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Ready'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['UpTime'])
            values.append('%s' % o['NumCreateCalls'])
            values.append('%s' % o['NumDeleteCalls'])
            values.append('%s' % o['NumUpdateCalls'])
            values.append('%s' % o['NumGetCalls'])
            values.append('%s' % o['NumActionCalls'])
            values.append('%s' % o['FlexDaemons'])
            rows.append(values)
        self.tblPrintObject('SystemStatusState', header, rows)


    def printIpTableAcls(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Action')
            header.append('IpAddr')
            header.append('Protocol')
            header.append('Port')
            header.append('PhysicalPort')

        objs = self.swtch.getAllIpTableAcls()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['Port'])
            values.append('%s' % o['PhysicalPort'])
            rows.append(values)
        self.tblPrintObject('IpTableAcl', header, rows)


    def printDWDMModuleNwIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NwIntfId')
            header.append('ModuleId')
            header.append('TxChanGridSpacing')
            header.append('CurrentBER')
            header.append('MinBEROverPMInterval')
            header.append('AvgBEROverPMInterval')
            header.append('MaxBEROverPMInterval')
            header.append('CurrUncorrectableFECBlkCnt')
            header.append('UncorrectableFECBlkCntOverPMInt')
            header.append('PRBSRxErrCnt')

        objs = self.swtch.getAllDWDMModuleNwIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['TxChanGridSpacing'])
            values.append('%s' % o['CurrentBER'])
            values.append('%s' % o['MinBEROverPMInterval'])
            values.append('%s' % o['AvgBEROverPMInterval'])
            values.append('%s' % o['MaxBEROverPMInterval'])
            values.append('%s' % o['CurrUncorrectableFECBlkCnt'])
            values.append('%s' % o['UncorrectableFECBlkCntOverPMInt'])
            values.append('%s' % o['PRBSRxErrCnt'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntfState', header, rows)


    def printOspfIfEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIpAddress')
            header.append('AddressLessIf')
            header.append('IfAdminStat')
            header.append('IfAreaId')
            header.append('IfType')
            header.append('IfRtrPriority')
            header.append('IfTransitDelay')
            header.append('IfRetransInterval')
            header.append('IfPollInterval')
            header.append('IfAuthKey')
            header.append('IfAuthType')
            header.append('IfHelloInterval')
            header.append('IfRtrDeadInterval')

        objs = self.swtch.getAllOspfIfEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIpAddress'])
            values.append('%s' % o['AddressLessIf'])
            values.append('%s' % o['IfAdminStat'])
            values.append('%s' % o['IfAreaId'])
            values.append('%s' % o['IfType'])
            values.append('%s' % o['IfRtrPriority'])
            values.append('%s' % o['IfTransitDelay'])
            values.append('%s' % o['IfRetransInterval'])
            values.append('%s' % o['IfPollInterval'])
            values.append('%s' % o['IfAuthKey'])
            values.append('%s' % o['IfAuthType'])
            values.append('%s' % o['IfHelloInterval'])
            values.append('%s' % o['IfRtrDeadInterval'])
            rows.append(values)
        self.tblPrintObject('OspfIfEntry', header, rows)


    def printBufferPortStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('EgressPort')
            header.append('IngressPort')
            header.append('PortBufferStat')

        objs = self.swtch.getAllBufferPortStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['EgressPort'])
            values.append('%s' % o['IngressPort'])
            values.append('%s' % o['PortBufferStat'])
            rows.append(values)
        self.tblPrintObject('BufferPortStatState', header, rows)


    def printBGPGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('ASNum')
            header.append('RouterId')
            header.append('UseMultiplePaths')
            header.append('EBGPMaxPaths')
            header.append('EBGPAllowMultipleAS')
            header.append('IBGPMaxPaths')
            header.append('Redistribution')

        objs = self.swtch.getAllBGPGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['ASNum'])
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['UseMultiplePaths'])
            values.append('%s' % o['EBGPMaxPaths'])
            values.append('%s' % o['EBGPAllowMultipleAS'])
            values.append('%s' % o['IBGPMaxPaths'])
            values.append('%s' % o['Redistribution'])
            rows.append(values)
        self.tblPrintObject('BGPGlobal', header, rows)


    def printOspfAreaEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AreaId')
            header.append('SpfRuns')
            header.append('AreaBdrRtrCount')
            header.append('AsBdrRtrCount')
            header.append('AreaLsaCount')

        objs = self.swtch.getAllOspfAreaEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['SpfRuns'])
            values.append('%s' % o['AreaBdrRtrCount'])
            values.append('%s' % o['AsBdrRtrCount'])
            values.append('%s' % o['AreaLsaCount'])
            rows.append(values)
        self.tblPrintObject('OspfAreaEntryState', header, rows)


    def printNDPGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllNDPGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('NDPGlobal', header, rows)


    def printPsuStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('PsuId')
            header.append('AdminState')
            header.append('ModelNum')
            header.append('SerialNum')
            header.append('Vin')
            header.append('Vout')
            header.append('Iin')
            header.append('Iout')
            header.append('Pin')
            header.append('Pout')
            header.append('Fan')
            header.append('FanId')
            header.append('LedId')

        objs = self.swtch.getAllPsuStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['PsuId'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['ModelNum'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Vin'])
            values.append('%s' % o['Vout'])
            values.append('%s' % o['Iin'])
            values.append('%s' % o['Iout'])
            values.append('%s' % o['Pin'])
            values.append('%s' % o['Pout'])
            values.append('%s' % o['Fan'])
            values.append('%s' % o['FanId'])
            values.append('%s' % o['LedId'])
            rows.append(values)
        self.tblPrintObject('PsuState', header, rows)


    def printBfdSessions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('Interface')
            header.append('Owner')
            header.append('PerLink')
            header.append('ParamName')

        objs = self.swtch.getAllBfdSessions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Interface'])
            values.append('%s' % o['Owner'])
            values.append('%s' % o['PerLink'])
            values.append('%s' % o['ParamName'])
            rows.append(values)
        self.tblPrintObject('BfdSession', header, rows)


    def printPolicyConditionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')

        objs = self.swtch.getAllPolicyConditionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
        self.tblPrintObject('PolicyConditionState', header, rows)


    def printVrrpIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('VirtualIPv4Addr')
            header.append('PreemptMode')
            header.append('Priority')
            header.append('AdvertisementInterval')
            header.append('AcceptMode')

        objs = self.swtch.getAllVrrpIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['VirtualIPv4Addr'])
            values.append('%s' % o['PreemptMode'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['AdvertisementInterval'])
            values.append('%s' % o['AcceptMode'])
            rows.append(values)
        self.tblPrintObject('VrrpIntf', header, rows)


    def printLLDPGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllLLDPGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('LLDPGlobal', header, rows)


    def printSubIPv4Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('Type')
            header.append('MacAddr')
            header.append('Enable')

        objs = self.swtch.getAllSubIPv4Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('SubIPv4Intf', header, rows)


    def printSfpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SfpId')
            header.append('SfpSpeed')
            header.append('SfpLOS')
            header.append('SfpPresent')
            header.append('SfpType')
            header.append('SerialNum')
            header.append('EEPROM')

        objs = self.swtch.getAllSfpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['SfpId'])
            values.append('%s' % o['SfpSpeed'])
            values.append('%s' % o['SfpLOS'])
            values.append('%s' % o['SfpPresent'])
            values.append('%s' % o['SfpType'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['EEPROM'])
            rows.append(values)
        self.tblPrintObject('SfpState', header, rows)


    def printPolicyDefinitionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IpPrefixList')

        objs = self.swtch.getAllPolicyDefinitionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IpPrefixList'])
            rows.append(values)
        self.tblPrintObject('PolicyDefinitionState', header, rows)


    def printVlanStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VlanId')
            header.append('VlanName')
            header.append('OperState')
            header.append('IfIndex')

        objs = self.swtch.getAllVlanStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['VlanName'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfIndex'])
            rows.append(values)
        self.tblPrintObject('VlanState', header, rows)


    def printLogicalIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IfIndex')
            header.append('SrcMac')
            header.append('OperState')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')

        objs = self.swtch.getAllLogicalIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SrcMac'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            rows.append(values)
        self.tblPrintObject('LogicalIntfState', header, rows)


    def printThermalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ThermalId')
            header.append('Location')
            header.append('Temperature')
            header.append('LowerWatermarkTemperature')
            header.append('UpperWatermarkTemperature')
            header.append('ShutdownTemperature')

        objs = self.swtch.getAllThermalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ThermalId'])
            values.append('%s' % o['Location'])
            values.append('%s' % o['Temperature'])
            values.append('%s' % o['LowerWatermarkTemperature'])
            values.append('%s' % o['UpperWatermarkTemperature'])
            values.append('%s' % o['ShutdownTemperature'])
            rows.append(values)
        self.tblPrintObject('ThermalState', header, rows)


    def printBGPNeighbors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NeighborAddress')
            header.append('IfIndex')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('Description')
            header.append('PeerGroup')
            header.append('BfdEnable')
            header.append('MultiHopTTL')
            header.append('LocalAS')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixesDisconnect')
            header.append('PeerAS')
            header.append('AddPathsMaxTx')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('BfdSessionParam')
            header.append('HoldTime')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPNeighbors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['BfdEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['BfdSessionParam'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPNeighbor', header, rows)


    def printStpBridgeInstances(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('HelloTime')
            header.append('ForwardDelay')
            header.append('MaxAge')
            header.append('TxHoldCount')
            header.append('Priority')
            header.append('ForceVersion')
            header.append('Address')

        objs = self.swtch.getAllStpBridgeInstances()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['TxHoldCount'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['ForceVersion'])
            values.append('%s' % o['Address'])
            rows.append(values)
        self.tblPrintObject('StpBridgeInstance', header, rows)


    def printLaPortChannelMemberStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('LagId')
            header.append('OperState')
            header.append('LagIfIndex')
            header.append('Activity')
            header.append('Timeout')
            header.append('Synchronization')
            header.append('Aggregatable')
            header.append('Collecting')
            header.append('Distributing')
            header.append('Defaulted')
            header.append('SystemId')
            header.append('OperKey')
            header.append('PartnerId')
            header.append('PartnerKey')
            header.append('DebugId')
            header.append('RxMachine')
            header.append('RxTime')
            header.append('MuxMachine')
            header.append('MuxReason')
            header.append('ActorChurnMachine')
            header.append('PartnerChurnMachine')
            header.append('ActorChurnCount')
            header.append('PartnerChurnCount')
            header.append('ActorSyncTransitionCount')
            header.append('PartnerSyncTransitionCount')
            header.append('ActorChangeCount')
            header.append('PartnerChangeCount')
            header.append('ActorCdsChurnMachine')
            header.append('PartnerCdsChurnMachine')
            header.append('ActorCdsChurnCount')
            header.append('PartnerCdsChurnCount')
            header.append('LacpInPkts')
            header.append('LacpOutPkts')
            header.append('LacpRxErrors')
            header.append('LacpTxErrors')
            header.append('LacpUnknownErrors')
            header.append('LacpErrors')
            header.append('LampInPdu')
            header.append('LampInResponsePdu')
            header.append('LampOutPdu')
            header.append('LampOutResponsePdu')

        objs = self.swtch.getAllLaPortChannelMemberStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['LagId'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['LagIfIndex'])
            values.append('%s' % o['Activity'])
            values.append('%s' % o['Timeout'])
            values.append('%s' % o['Synchronization'])
            values.append('%s' % o['Aggregatable'])
            values.append('%s' % o['Collecting'])
            values.append('%s' % o['Distributing'])
            values.append('%s' % o['Defaulted'])
            values.append('%s' % o['SystemId'])
            values.append('%s' % o['OperKey'])
            values.append('%s' % o['PartnerId'])
            values.append('%s' % o['PartnerKey'])
            values.append('%s' % o['DebugId'])
            values.append('%s' % o['RxMachine'])
            values.append('%s' % o['RxTime'])
            values.append('%s' % o['MuxMachine'])
            values.append('%s' % o['MuxReason'])
            values.append('%s' % o['ActorChurnMachine'])
            values.append('%s' % o['PartnerChurnMachine'])
            values.append('%s' % o['ActorChurnCount'])
            values.append('%s' % o['PartnerChurnCount'])
            values.append('%s' % o['ActorSyncTransitionCount'])
            values.append('%s' % o['PartnerSyncTransitionCount'])
            values.append('%s' % o['ActorChangeCount'])
            values.append('%s' % o['PartnerChangeCount'])
            values.append('%s' % o['ActorCdsChurnMachine'])
            values.append('%s' % o['PartnerCdsChurnMachine'])
            values.append('%s' % o['ActorCdsChurnCount'])
            values.append('%s' % o['PartnerCdsChurnCount'])
            values.append('%s' % o['LacpInPkts'])
            values.append('%s' % o['LacpOutPkts'])
            values.append('%s' % o['LacpRxErrors'])
            values.append('%s' % o['LacpTxErrors'])
            values.append('%s' % o['LacpUnknownErrors'])
            values.append('%s' % o['LacpErrors'])
            values.append('%s' % o['LampInPdu'])
            values.append('%s' % o['LampInResponsePdu'])
            values.append('%s' % o['LampOutPdu'])
            values.append('%s' % o['LampOutResponsePdu'])
            rows.append(values)
        self.tblPrintObject('LaPortChannelMemberState', header, rows)


    def printOspfVirtIfEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VirtIfNeighbor')
            header.append('VirtIfAreaId')
            header.append('VirtIfTransitDelay')
            header.append('VirtIfRetransInterval')
            header.append('VirtIfHelloInterval')
            header.append('VirtIfRtrDeadInterval')
            header.append('VirtIfAuthKey')
            header.append('VirtIfAuthType')

        objs = self.swtch.getAllOspfVirtIfEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VirtIfNeighbor'])
            values.append('%s' % o['VirtIfAreaId'])
            values.append('%s' % o['VirtIfTransitDelay'])
            values.append('%s' % o['VirtIfRetransInterval'])
            values.append('%s' % o['VirtIfHelloInterval'])
            values.append('%s' % o['VirtIfRtrDeadInterval'])
            values.append('%s' % o['VirtIfAuthKey'])
            values.append('%s' % o['VirtIfAuthType'])
            rows.append(values)
        self.tblPrintObject('OspfVirtIfEntry', header, rows)


    def printSystemLoggings(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Logging')

        objs = self.swtch.getAllSystemLoggings()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Logging'])
            rows.append(values)
        self.tblPrintObject('SystemLogging', header, rows)


    def printBGPPolicyActionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ActionInfo')
            header.append('PolicyStmtList')

        objs = self.swtch.getAllBGPPolicyActionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ActionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyActionState', header, rows)


    def printVxlanInstances(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vni')
            header.append('VlanId')

        objs = self.swtch.getAllVxlanInstances()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vni'])
            values.append('%s' % o['VlanId'])
            rows.append(values)
        self.tblPrintObject('VxlanInstance', header, rows)


    def printBGPPolicyDefinitionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HitCounter')
            header.append('IpPrefixList')

        objs = self.swtch.getAllBGPPolicyDefinitionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HitCounter'])
            values.append('%s' % o['IpPrefixList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyDefinitionState', header, rows)


    def printLedStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LedId')
            header.append('LedIdentify')
            header.append('LedState')
            header.append('LedColor')

        objs = self.swtch.getAllLedStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LedId'])
            values.append('%s' % o['LedIdentify'])
            values.append('%s' % o['LedState'])
            values.append('%s' % o['LedColor'])
            rows.append(values)
        self.tblPrintObject('LedState', header, rows)


    def printIPv4IntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')

        objs = self.swtch.getAllIPv4IntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            rows.append(values)
        self.tblPrintObject('IPv4IntfState', header, rows)


    def printPortStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('Name')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('Pvid')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')
            header.append('ErrDisableReason')
            header.append('PresentInHW')

        objs = self.swtch.getAllPortStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['Pvid'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            values.append('%s' % o['ErrDisableReason'])
            values.append('%s' % o['PresentInHW'])
            rows.append(values)
        self.tblPrintObject('PortState', header, rows)


    def printSfps(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SfpId')
            header.append('AdminState')

        objs = self.swtch.getAllSfps()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['SfpId'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('Sfp', header, rows)


    def printBGPPolicyActions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ActionType')
            header.append('GenerateASSet')
            header.append('SendSummaryOnly')

        objs = self.swtch.getAllBGPPolicyActions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ActionType'])
            values.append('%s' % o['GenerateASSet'])
            values.append('%s' % o['SendSummaryOnly'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyAction', header, rows)


    def printSystemSwVersionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FlexswitchVersion')
            header.append('Repos')

        objs = self.swtch.getAllSystemSwVersionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FlexswitchVersion'])
            values.append('%s' % o['Repos'])
            rows.append(values)
        self.tblPrintObject('SystemSwVersionState', header, rows)


    def printDaemonStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Enable')
            header.append('State')
            header.append('Reason')
            header.append('StartTime')
            header.append('KeepAlive')
            header.append('RestartCount')
            header.append('RestartTime')
            header.append('RestartReason')

        objs = self.swtch.getAllDaemonStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['State'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['StartTime'])
            values.append('%s' % o['KeepAlive'])
            values.append('%s' % o['RestartCount'])
            values.append('%s' % o['RestartTime'])
            values.append('%s' % o['RestartReason'])
            rows.append(values)
        self.tblPrintObject('DaemonState', header, rows)


    def printSystemParamStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('MgmtIp')
            header.append('Hostname')
            header.append('Version')
            header.append('SwitchMac')
            header.append('Description')

        objs = self.swtch.getAllSystemParamStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['MgmtIp'])
            values.append('%s' % o['Hostname'])
            values.append('%s' % o['Version'])
            values.append('%s' % o['SwitchMac'])
            values.append('%s' % o['Description'])
            rows.append(values)
        self.tblPrintObject('SystemParamState', header, rows)


    def printDWDMModuleNwIntfPMStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('NwIntfId')
            header.append('Type')
            header.append('Class')
            header.append('ModuleId')
            header.append('Data')

        objs = self.swtch.getAllDWDMModuleNwIntfPMStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntfPMState', header, rows)


    def printDWDMModules(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('EnableExtPMTickSrc')
            header.append('PMInterval')
            header.append('AdminState')
            header.append('IndependentLaneMode')

        objs = self.swtch.getAllDWDMModules()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['EnableExtPMTickSrc'])
            values.append('%s' % o['PMInterval'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['IndependentLaneMode'])
            rows.append(values)
        self.tblPrintObject('DWDMModule', header, rows)


    def printBGPv6Neighbors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('UpdateSource')
            header.append('BfdEnable')
            header.append('MultiHopTTL')
            header.append('LocalAS')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixesDisconnect')
            header.append('PeerAS')
            header.append('AddPathsMaxTx')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('BfdSessionParam')
            header.append('HoldTime')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv6Neighbors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['BfdEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['BfdSessionParam'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv6Neighbor', header, rows)


    def printStpPorts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('BrgIfIndex')
            header.append('IfIndex')
            header.append('BpduGuardInterval')
            header.append('PathCost')
            header.append('Priority')
            header.append('AdminEdgePort')
            header.append('Enable')
            header.append('ProtocolMigration')
            header.append('BridgeAssurance')
            header.append('BpduGuard')
            header.append('AdminPointToPoint')
            header.append('AdminPathCost')
            header.append('PathCost32')

        objs = self.swtch.getAllStpPorts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['BrgIfIndex'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['BpduGuardInterval'])
            values.append('%s' % o['PathCost'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['AdminEdgePort'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['ProtocolMigration'])
            values.append('%s' % o['BridgeAssurance'])
            values.append('%s' % o['BpduGuard'])
            values.append('%s' % o['AdminPointToPoint'])
            values.append('%s' % o['AdminPathCost'])
            values.append('%s' % o['PathCost32'])
            rows.append(values)
        self.tblPrintObject('StpPort', header, rows)


    def printBGPRouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('CIDRLen')
            header.append('Network')
            header.append('Paths')

        objs = self.swtch.getAllBGPRouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['CIDRLen'])
            values.append('%s' % o['Network'])
            values.append('%s' % o['Paths'])
            rows.append(values)
        self.tblPrintObject('BGPRouteState', header, rows)


    def printIPv4Routes(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NetworkMask')
            header.append('NextHop')
            header.append('Protocol')
            header.append('NullRoute')
            header.append('Cost')

        objs = self.swtch.getAllIPv4Routes()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NetworkMask'])
            values.append('%s' % o['NextHop'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['NullRoute'])
            values.append('%s' % o['Cost'])
            rows.append(values)
        self.tblPrintObject('IPv4Route', header, rows)


    def printBGPv6PeerGroups(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('UpdateSource')
            header.append('Description')
            header.append('MaxPrefixesRestartTimer')
            header.append('RouteReflectorClient')
            header.append('MultiHopTTL')
            header.append('MaxPrefixesDisconnect')
            header.append('LocalAS')
            header.append('KeepaliveTime')
            header.append('RouteReflectorClusterId')
            header.append('AddPathsMaxTx')
            header.append('MultiHopEnable')
            header.append('AddPathsRx')
            header.append('MaxPrefixesThresholdPct')
            header.append('HoldTime')
            header.append('MaxPrefixes')
            header.append('PeerAS')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv6PeerGroups()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv6PeerGroup', header, rows)


    def printArpEntryHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Port')

        objs = self.swtch.getAllArpEntryHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Port'])
            rows.append(values)
        self.tblPrintObject('ArpEntryHwState', header, rows)


    def printOspfGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('VersionNumber')
            header.append('AreaBdrRtrStatus')
            header.append('ExternLsaCount')
            header.append('OpaqueLsaSupport')
            header.append('RestartExitReason')

        objs = self.swtch.getAllOspfGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['VersionNumber'])
            values.append('%s' % o['AreaBdrRtrStatus'])
            values.append('%s' % o['ExternLsaCount'])
            values.append('%s' % o['OpaqueLsaSupport'])
            values.append('%s' % o['RestartExitReason'])
            rows.append(values)
        self.tblPrintObject('OspfGlobalState', header, rows)


    def printBGPNeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NeighborAddress')
            header.append('IfIndex')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('PeerType')
            header.append('AuthPassword')
            header.append('Description')
            header.append('SessionState')
            header.append('Messages')
            header.append('Queues')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('PeerGroup')
            header.append('BfdNeighborState')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')

        objs = self.swtch.getAllBGPNeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            rows.append(values)
        self.tblPrintObject('BGPNeighborState', header, rows)


    def printIPv6Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('LinkIp')

        objs = self.swtch.getAllIPv6Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['LinkIp'])
            rows.append(values)
        self.tblPrintObject('IPv6Intf', header, rows)


    def printRouteStatsPerProtocolStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('V4Routes')
            header.append('V6Routes')

        objs = self.swtch.getAllRouteStatsPerProtocolStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['V4Routes'])
            values.append('%s' % o['V6Routes'])
            rows.append(values)
        self.tblPrintObject('RouteStatsPerProtocolState', header, rows)


    def printVrrpVridStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('AdverRx')
            header.append('AdverTx')
            header.append('LastAdverRx')
            header.append('LastAdverTx')
            header.append('MasterIp')
            header.append('CurrentState')
            header.append('PreviousState')
            header.append('TransitionReason')

        objs = self.swtch.getAllVrrpVridStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['AdverRx'])
            values.append('%s' % o['AdverTx'])
            values.append('%s' % o['LastAdverRx'])
            values.append('%s' % o['LastAdverTx'])
            values.append('%s' % o['MasterIp'])
            values.append('%s' % o['CurrentState'])
            values.append('%s' % o['PreviousState'])
            values.append('%s' % o['TransitionReason'])
            rows.append(values)
        self.tblPrintObject('VrrpVridState', header, rows)


    def printFaultStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('EventId')
            header.append('EventName')
            header.append('SrcObjName')
            header.append('OwnerName')
            header.append('OwnerId')
            header.append('Description')
            header.append('OccuranceTime')
            header.append('SrcObjKey')
            header.append('SrcObjUUID')
            header.append('ResolutionTime')
            header.append('ResolutionReason')

        objs = self.swtch.getAllFaultStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['EventId'])
            values.append('%s' % o['EventName'])
            values.append('%s' % o['SrcObjName'])
            values.append('%s' % o['OwnerName'])
            values.append('%s' % o['OwnerId'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['OccuranceTime'])
            values.append('%s' % o['SrcObjKey'])
            values.append('%s' % o['SrcObjUUID'])
            values.append('%s' % o['ResolutionTime'])
            values.append('%s' % o['ResolutionReason'])
            rows.append(values)
        self.tblPrintObject('FaultState', header, rows)


    def printBGPPolicyDefinitions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Precedence')
            header.append('MatchType')
            header.append('StatementList')

        objs = self.swtch.getAllBGPPolicyDefinitions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Precedence'])
            values.append('%s' % o['MatchType'])
            values.append('%s' % o['StatementList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyDefinition', header, rows)


    def printPolicyConditions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionType')
            header.append('Protocol')
            header.append('IpPrefix')
            header.append('MaskLengthRange')

        objs = self.swtch.getAllPolicyConditions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionType'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['MaskLengthRange'])
            rows.append(values)
        self.tblPrintObject('PolicyCondition', header, rows)


    def printPorts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('PhyIntfType')
            header.append('MacAddr')
            header.append('Speed')
            header.append('Duplex')
            header.append('MediaType')
            header.append('Mtu')
            header.append('BreakOutMode')
            header.append('Description')
            header.append('AdminState')
            header.append('Autoneg')

        objs = self.swtch.getAllPorts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['PhyIntfType'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Speed'])
            values.append('%s' % o['Duplex'])
            values.append('%s' % o['MediaType'])
            values.append('%s' % o['Mtu'])
            values.append('%s' % o['BreakOutMode'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['Autoneg'])
            rows.append(values)
        self.tblPrintObject('Port', header, rows)


    def printOspfIfEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIpAddress')
            header.append('AddressLessIf')
            header.append('IfState')
            header.append('IfDesignatedRouter')
            header.append('IfBackupDesignatedRouter')
            header.append('IfEvents')
            header.append('IfLsaCount')
            header.append('IfDesignatedRouterId')
            header.append('IfBackupDesignatedRouterId')

        objs = self.swtch.getAllOspfIfEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIpAddress'])
            values.append('%s' % o['AddressLessIf'])
            values.append('%s' % o['IfState'])
            values.append('%s' % o['IfDesignatedRouter'])
            values.append('%s' % o['IfBackupDesignatedRouter'])
            values.append('%s' % o['IfEvents'])
            values.append('%s' % o['IfLsaCount'])
            values.append('%s' % o['IfDesignatedRouterId'])
            values.append('%s' % o['IfBackupDesignatedRouterId'])
            rows.append(values)
        self.tblPrintObject('OspfIfEntryState', header, rows)


    def printRIBEventStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventInfo')

        objs = self.swtch.getAllRIBEventStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
        self.tblPrintObject('RIBEventState', header, rows)

