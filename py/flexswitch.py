#!/usr/bin/python
import requests
import json
import urllib2

headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
class FlexSwitch( object):
    def  __init__ (self, ip, port):
        self.ip    = ip
        self.port  = port 
        self.urlBase = 'http://%s:%s/public/v1/'%(ip,str(port))
        self.KeyDict = {}

    def createVlanInterface( self, intfIp, vlanId) :
        obj =  { 'IpAddr'   : intfIp,
                 'IfIndex' : self.getVlanInfo(vlanId),
               }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()

    def createPhyInterface( self, intfIp, ifindex) :
        obj =  { 'IpAddr'   : intfIp,
                 'IfIndex' : ifindex,
               }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createVlan (self, vlanId, ports, taggedports):
        obj =  { 'VlanId': int(vlanId),
                 'IfIndexList' : ports,
                 'UntagIfIndexList': taggedports 
               }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj["NameKey"], r.__dict__
        self.KeyDict.update({obj['VlanId'] : r.__dict__['_content'].lstrip("{Id\":\"").rstrip("\"}")})
        return r.json()

    def deleteVlan(self, vlanId, ports, taggedports):
        obj =  { 'VlanId': int(vlanId),
                 'IfIndexList' : ports,
                 'UntagIfIndexList': taggedports
               }
        reqUrl =  self.urlBase+'EthernetConfig'+'/'+self.KeyDict[obj['VlanId']]
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers)
        del self.KeyDict[obj['VlanId']]

    def createBgpGlobal(self, asnum, rtrid):
        obj =  { 
                'ASNum'         : asnum,
                'RouterId'   : rtrid,  
                'UseMultiplePaths': usemp,
                'EBGPMaxPaths': ebgpmp,
                'IBGPMaxPaths': ibgpmp
               }
 
        reqUrl =  self.urlBase+'BGPGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createBgpPeerGroup(self, name, desc, CRT, HT, KpAT):
        obj =  { 
        	'Name' : name,
                'ConnectRetryTime': CRT, 
                'HoldTime'         : HT,
                'KeepaliveTime'    : KpAT,
                'Description'      : desc
               }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createBgpPeer(self, nbrIp, peeras, localas, peergroup=None, desc=''):
        obj =  { 
                'PeerAS'         : peeras,
                'LocalAS'        : localas,
                'AuthPassword'   : '',
                'Description'    : desc ,
                'PeerGroup'	 : peergroup,
                'NeighborAddress': nbrIp ,
                'ConnectRetryTime': 30, 
                'HoldTime'         : 3,
                'KeepaliveTime'    : 1,
               }
        reqUrl =  self.urlBase+'BGPNeighborConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createOspfGlobal(self, rtrid='10.0.1.1'):
        obj =  { 
                'RouterIdKey' : rtrid,
               }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicyCondition(self, condition ):
        obj = condition 
        reqUrl =  self.urlBase+'PolicyConditionConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicyAction (self, action):
        obj = action
        reqUrl =  self.urlBase+'PolicyActionConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicyStatement (self, stmt):
        obj = stmt 
        reqUrl =  self.urlBase+'PolicyStmtConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicy(self, policy ):
        obj = policy 
        reqUrl =  self.urlBase+'PolicyConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print r.__dict__
        return r.json()


    def createOspfIntf(self, 
                       ipaddr, 
                       ifIndex = 0,
                       areaId = '0', 
                       ifType = 1,
                       priority = 1,
                       helloIntvl = 10,
                       authKey ='',
                       authType =0
                       ):
        obj =  { 
                'IfIpAddressKey' : ipaddr,
                'AddressLessIfKey' : ifIndex,
                'IfAreaId' : areaId, 
                'IfType' :  ifType, 
                'IfAdminStat' :   1,
                'IfRtrPriority' : priority,
                'IfTransitDelay' : 0,
                'IfRetransInterval' : helloIntvl,
                'IfHelloInterval' :   helloIntvl,
                'IfRtrDeadInterval' : 4*helloIntvl, 
                'IfPollInterval' : 0, 
                'IfAuthKey' : authKey ,
                'IfAuthType' : authType
               }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()

    def createRedistributionPolicy(self):
        obj = {'Name'           :'RedistributeConnectedToBGP', 
          'MatchPrefixSet': {'PrefixSet' :'', 'MatchSetOptions' : 0}, 
          'InstallProtocolEq':'Connected', 
          'RouteDisposition': '', 
          'Redistribute':True, 
          'RedistributeTargetProtocol':'BGP'}

        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def enableGlobalDHCPRelay (self) :
        obj =  { 
                'Enable' : True,
               }
        reqUrl =  self.urlBase+'DhcpRelayGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def enableIntfDHCPRelay (self, ifIndex, svrIp ):
        obj =  {  
                'IfIndex' : ifIndex,
                'Enable' : True,
                'ServerIp': svrIp
                }

        reqUrl =  self.urlBase+'DhcpRelayIntfConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()

    # configure lag group
    # id - lag id # will be converted to aggId-<id>
    # type - 0 == LACP, 1 == STATIC
    # mode - 0 == ACTIVE, 1 == PASSIVE
    # period - 0 == SLOW, 1 == FAST
    # sysmac - format 'XX:XX:XX:XX:XX:XX'

    def createLag(self, id, type, sysmac, sysprio, mode, period, hashmode):
        obj = {
            'NameKey' : "aggId-%s" %id,
            'LagType' : type,
            'Type'    : "ETH",
            'Description' : "Test lag creation",
            'Enabled' : True,
            'Interval' : period,
            'LacpMode' : mode,
            'SystemIdMac' : sysmac,
            'SystemPriority' : sysprio,
            'MinLinks' : 1,
            'LagHash' : hashmode,
            'Mtu' : 1518
        }
        reqUrl =  self.urlBase+'AggregationLacpConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj["NameKey"], r.__dict__
        self.KeyDict.update({obj['NameKey'] : r.__dict__['_content'].lstrip("{Id\":\"").rstrip("\"}")})
        return r.json()

    # id - port number will be conververt to fpPort-<id>
    def addPortToLag(self, id, lagid):
        obj = {
            'NameKey' : 'fpPort-%s' % id,
            'Enabled' : True,
            'Description' : "Test lag port",
            'Mtu' : 1518,
            'Type' : 'ETH',
            'MacAddress' : '00:11:22:33:44:55',
            'DuplexMode' : 0,
            'Auto'       : True,
            'Speed'      : 'SPEED_1Gb',
            'EnableFlowControl' : True,
            'AggregateId' : 'aggId-%s' % lagid
        }
        reqUrl =  self.urlBase+'EthernetConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj["NameKey"], r.__dict__
        self.KeyDict.update({obj['NameKey'] : r.__dict__['_content'].lstrip("{Id\":\"").rstrip("\"}")})
        return r.json()

    def delPortFromLag(self, id, lagid):
        obj = {
            'NameKey' : 'fpPort-%s' % id,
            'Enabled' : True,
            'Description' : "Test lag port",
            'Mtu' : 1518,
            'Type' : 'ETH',
            'MacAddress' : '00:11:22:33:44:55',
            'DuplexMode' : 0,
            'Auto'       : True,
            'Speed'      : 'SPEED_1Gb',
            'EnableFlowControl' : True,
            'AggregateId' : 'aggId-%s' % lagid
        }
        reqUrl =  self.urlBase+'EthernetConfig'+'/'+self.KeyDict[obj['NameKey']]
        self.KeyDict.pop(obj['NameKey'])
        r = requests.delete(reqUrl, headers=headers)
        return r.json()

    def createStpBridge(self, mac, prio, age, hellotime, forwarddelay, vlan):
        obj = {
            "Dot1dBridgeAddress" : mac, #string `SNAPROUTE: KEY`
            "Dot1dStpPriority": prio,  #int32 `SNAPROUTE: KEY`
            "Dot1dStpBridgeMaxAge": age, # int32
            "Dot1dStpBridgeHelloTime": hellotime, # int32
            "Dot1dStpBridgeForwardDelay": forwarddelay, # int32
            "Dot1dStpBridgeForceVersion": 2, # int32 0 STP compatibility, 2 default mode
            "Dot1dStpBridgeTxHoldCount": 6, # int32 valid values 1-10s
            "Dot1dStpVlan": vlan,
        }
        reqUrl =  self.urlBase+'Dot1dStpBridgeConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        key = (obj["Dot1dStpVlan"],)
        print key, r.__dict__
        self.KeyDict.update({key : r.__dict__['_content'].lstrip("{Id\":\"").rstrip("\"}")})
        return r.json()

    def deleteStpBridge(self, mac, prio, age, hellotime, forwarddelay, vlan):
        obj = {
            "Dot1dBridgeAddress" : mac,
            "Dot1dStpPriority": prio,
            "Dot1dStpBridgeMaxAge": age, # int32
            "Dot1dStpBridgeHelloTime": hellotime, # int32
            "Dot1dStpBridgeForwardDelay": forwarddelay, # int32
            "Dot1dStpBridgeForceVersion": 2, # int32 0 STP compatibility, 2 default mode
            "Dot1dStpBridgeTxHoldCount": 6, # int32 valid values 1-10s
            "Dot1dStpVlan": vlan, # SNAPROUTE KEY
        }
        reqUrl =  self.urlBase+'Dot1dStpBridgeConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers)
        key = (obj["Dot1dStpVlan"],)
        print key, r.__dict__
        del self.KeyDict[key]

    def createStpPortEntry(self, port, brg, prio, ena, pathcost, protomigra, adminp2p, adminedge, adminpathcost, brgassurance):

        obj = {
            "Dot1dStpPort": port, # int32 `SNAPROUTE: KEY`
            "Dot1dStpPortPriority": prio, # int32
            "Dot1dStpPortEnable": ena, # int32
            "Dot1dStpPortPathCost": pathcost, # int32
            "Dot1dStpPortPathCost32": pathcost, # int32
            "Dot1dStpPortProtocolMigration": protomigra, # int32
            "Dot1dStpPortAdminPointToPoint": adminp2p, # int32
            "Dot1dStpPortAdminEdgePort": adminedge, # int32
            "Dot1dStpPortAdminPathCost": adminpathcost, # int32
            "Dot1dBrgIfIndex": brg, # int32
            "BridgeAssurance":brgassurance, #int32
        }
        reqUrl =  self.urlBase+'Dot1dStpPortEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        key = (obj['Dot1dStpPort'], obj['Dot1dBrgIfIndex'])
        print key, r.__dict__
        self.KeyDict.update({key : r.__dict__['_content'].lstrip("{Id\":\"").rstrip("\"}")})
        return r.json()


    def deleteStpPortEntry(self, port, brg, prio, ena, pathcost, protomigra, adminp2p, adminedge, adminpathcost, brgassurance):

        obj = {
            "Dot1dStpPort": port, # int32 `SNAPROUTE: KEY`
            "Dot1dStpPortPriority": prio, # int32
            "Dot1dStpPortEnable": ena, # int32
            "Dot1dStpPortPathCost": pathcost, # int32
            "Dot1dStpPortPathCost32": pathcost, # int32
            "Dot1dStpPortProtocolMigration": protomigra, # int32
            "Dot1dStpPortAdminPointToPoint": adminp2p, # int32
            "Dot1dStpPortAdminEdgePort": adminedge, # int32
            "Dot1dStpPortAdminPathCost": adminpathcost, # int32
            "Dot1dBrgIfIndex": brg, # int32
            "BridgeAssurance":brgassurance, #int32
        }
        reqUrl =  self.urlBase+'Dot1dStpPortEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers)
        key = (obj['Dot1dStpPort'], obj['Dot1dBrgIfIndex'])
        print key, r.__dict__
        del self.KeyDict[key]

    def getObjects(self, objName):
        currentMarker = 0
        nextMarker = 0
        count = 10
        more = True
        entries = []
        while more == True:
            qry = 'http://%s:8080/public/v1/%s?CurrentMarker=%d&NextMarker=%d&Count=%d' %(self.ip, objName, currentMarker, nextMarker, count)
            response = requests.get(qry)
            data = response.json()
            more =  data['MoreExist']
            currentMarker =  data['NextMarker']
            NextMarker    =  data['NextMarker']
            if data['StateObjects'] != None:
                entries.extend(data['StateObjects'])
        return entries

    def getVlanInfo (self, vlanId) :
        for vlan in self.getObjects ('Vlans'):
            if vlan['VlanId'] == vlanId:
                return int(vlan['IfIndex'])

if __name__=='__main__':
    pass
