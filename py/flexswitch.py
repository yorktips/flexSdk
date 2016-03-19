#!/usr/bin/python
import requests
import json
import urllib2

SUCCESS_STATUS_CODE = 201

headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
class FlexSwitch( object):
    def  __init__ (self, ip, port):
        self.ip    = ip
        self.port  = port 
        self.urlBase = 'http://%s:%s/public/v1/'%(ip,str(port))

    def createVlanInterface( self, intfIp, vlanId) :
        obj =  { 'IpAddr'   : intfIp,
                 'IfIndex' : self.getVlanInfo(vlanId),
               }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def createPhyInterface( self, intfIp, ifindex) :
        obj =  { 'IpAddr'   : intfIp,
                 'IfIndex' : ifindex,
               }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def createVlan (self, vlanId, ports, taggedports):
        obj =  { 'VlanId': int(vlanId),
                 'IfIndexList' : ports,
                 'UntagIfIndexList': taggedports 
               }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj["VlanId"], r.__dict__
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def deleteVlan(self, vlanId, ports, taggedports):
        obj =  { 'VlanId': int(vlanId),
                 'IfIndexList' : ports,
                 'UntagIfIndexList': taggedports
               }

    def deleteVlanByUuid(self, uuid):
        reqUrl =  self.urlBase+'Vlan'+'/'+ uuid
        r = requests.delete(reqUrl, headers=headers)

    def createBgpGlobal(self, asnum, rtrid, usemp=False, ebgpmp=1, ibgpmp=1):
        obj =  { 
                'ASNum'         : asnum,
                'RouterId'   : rtrid,  
                'UseMultiplePaths': usemp, 
		'EBGPMaxPaths': ebgpmp, 
		'IBGPMaxPaths': ibgpmp  
               }
 
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
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
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
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
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def createOspfGlobal(self, rtrid='10.0.1.1'):
        obj =  { 
                'RouterIdKey' : rtrid,
               }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def createPolicyCondition(self, condition ):
        obj = condition 
        reqUrl =  self.urlBase+'PolicyConditionConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def createPolicyAction (self, action):
        obj = action
        reqUrl =  self.urlBase+'PolicyActionConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def createPolicyStatement (self, stmt):
        obj = stmt 
        reqUrl =  self.urlBase+'PolicyStmtConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def createPolicy(self, policy ):
        obj = policy 
        reqUrl =  self.urlBase+'PolicyConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print r.__dict__
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None


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
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
    
    def createRedistributionPolicy(self):
        obj = {'Name'           :'RedistributeConnectedToBGP', 
          'MatchPrefixSet': {'PrefixSet' :'', 'MatchSetOptions' : 0}, 
          'InstallProtocolEq':'Connected', 
          'RouteDisposition': '', 
          'Redistribute':True, 
          'RedistributeTargetProtocol':'BGP'}

        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def enableGlobalDHCPRelay (self) :
        obj =  { 
                'Enable' : True,
               }
        reqUrl =  self.urlBase+'DhcpRelayGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
        
    def enableIntfDHCPRelay (self, ifIndex, svrIp ):
        obj =  {  
                'IfIndex' : ifIndex,
                'Enable' : True,
                'ServerIp': svrIp
                }

        reqUrl =  self.urlBase+'DhcpRelayIntfConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    # configure lag group
    # id - lag id # will be converted to aggId-<id>
    # type - 0 == LACP, 1 == STATIC
    # mode - 0 == ACTIVE, 1 == PASSIVE
    # period - 0 == SLOW, 1 == FAST
    # sysmac - format 'XX:XX:XX:XX:XX:XX'

    def createLag(self, lagId, lagType, sysmac, sysprio, mode, period, hashmode):
        obj = {
            'NameKey' : "aggId-%s" %lagId,
            'LagType' : lagType,
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
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
    
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
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

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

    def createStpBridge(self, vlan, mac, prio, age, hellotime, forwarddelay):
        obj = {
            "Address" : mac, #string `SNAPROUTE: KEY`
            "Priority": prio,  #int32 `SNAPROUTE: KEY`
            "MaxAge": age, # int32
            "HelloTime": hellotime, # int32
            "ForwardDelay": forwarddelay, # int32
            "ForceVersion": 2, # int32 0 STP compatibility, 2 default mode
            "TxHoldCount": 6, # int32 valid values 1-10s
            "Vlan": vlan,
        }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def deleteStpBridge(self, vlan, mac, prio, age, hellotime, forwarddelay):
        obj = {
            "Address" : mac,
            "Priority": prio,
            "MaxAge": age, # int32
            "HelloTime": hellotime, # int32
            "ForwardDelay": forwarddelay, # int32
            "ForceVersion": 2, # int32 0 STP compatibility, 2 default mode
            "TxHoldCount": 6, # int32 valid values 1-10s
            "Vlan": vlan, # SNAPROUTE KEY
        }

    def deleteStpBridgeByUuid(self, uuid):
        reqUrl =  self.urlBase+'StpBridgeInstance'+'/'+uuid
        r = requests.delete(reqUrl, headers=headers)

    def createStpPortEntry(self, port, brg, prio, ena, pathcost, protomigra, adminp2p, adminedge, adminpathcost, brgassurance):

        obj = {
            "IfIndex": port, # int32 `SNAPROUTE: KEY`
            "Priority": prio, # int32
            "Enable": ena, # int32
            "PathCost": pathcost, # int32
            "PathCost32": pathcost, # int32
            "ProtocolMigration": protomigra, # int32
            "PointToPoint": adminp2p, # int32
            "AdminEdgePort": adminedge, # int32
            "AdminPathCost": adminpathcost, # int32
            "BrgIfIndex": brg, # int32
            "BridgeAssurance":brgassurance, #int32
            "BpduGuard": 1 if adminedge else 0,
        }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None


    def deleteStpPortEntry(self, port, brg, prio, ena, pathcost, protomigra, adminp2p, adminedge, adminpathcost, brgassurance):

        obj = {
            "IfIndex": port, # int32 `SNAPROUTE: KEY`
            "Priority": prio, # int32
            "Enable": ena, # int32
            "PathCost": pathcost, # int32
            "PathCost32": pathcost, # int32
            "ProtocolMigration": protomigra, # int32
            "AdminPointToPoint": adminp2p, # int32
            "AdminEdgePort": adminedge, # int32
            "AdminPathCost": adminpathcost, # int32
            "BrgIfIndex": brg, # int32
            "BridgeAssurance":brgassurance, #int32
            "BpduGuard": 1 if adminedge else 0,
        }


    def deleteStpPortEntryByUuid(self, uuid):
        reqUrl =  self.urlBase+'StpPort'+'/'+uuid
        r = requests.delete(reqUrl, headers=headers)

    def createVxlanEntry(self, vni, vlanId, GroupIp, MTU):
        obj = {
            "VxlanId" :  vni, # key
	        "Group" : "", # UNSUPPORTED
	        "VlanId" : vlanId,
            "Mtu" : MTU,
        }
        reqUrl =  self.urlBase+'VxlanInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj, r.__dict__
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def deleteVxlanEntryByUuid(self, uuid):
        reqUrl =  self.urlBase+'VxlanInstance'+'/'+uuid
        r = requests.delete(reqUrl, headers=headers)

    def createVtepEntry(self, vtepId, vxlanId, srcifindex, udp, srcmac, tunnelsrcip, tunneldstip, ttl, tos):
        obj = {
           "VtepId" : vtepId, #key
           "VtepName" : "vtep%s" %(vtepId),
	       "VxlanId" : vxlanId, # key
	       "SrcIfIndex" : srcifindex,
	       "UDP" : udp,
	       "TTL" : ttl,
	       "TOS" : tos,
	       "TunnelSourceIp" : tunnelsrcip,
	       "TunnelDestinationIp" : tunneldstip,
	       "SrcMac" : srcmac,
        }
        reqUrl =  self.urlBase+'VxlanVtepInstances'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj, r.__dict__
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def deleteVtepEntryByUuid(self, uuid):
        reqUrl =  self.urlBase+'VxlanVtepInstances'+'/'+uuid
        r = requests.delete(reqUrl, headers=headers)

    def createLogicalIntf(self, name, type):
        obj = {
            "Name" : name,
	        "Type" : type,
        }
        reqUrl =  self.urlBase+'LogicalIntfConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj, r.__dict__
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def deleteLogicalIntf(self, uuid):
        reqUrl =  self.urlBase+'LogicalIntfConfig'+'/'+uuid
        r = requests.delete(reqUrl, headers=headers)

    def createIpV4Intf(self, ip, ifindex):
        obj = {
            "IpAddr" : ip,
	        "IfIndex" : ifindex,
        }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        print obj, r.__dict__
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def deleteIpV4Intf(self, uuid):
        reqUrl =  self.urlBase+'IPv4Intf'+'/'+uuid
        r = requests.delete(reqUrl, headers=headers)

    def portAdminStateSet(self, uuid, enable):
        obj = {
            	'AdminState' : "ON" if enable else "OFF"
        }
        reqUrl =  self.urlBase+'PortConfig' + '/' + ouid
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None

    def portSpeedSet(self, ouid, speed):
        obj = {
            'Speed' : speed
        }
        reqUrl =  self.urlBase+'PortConfig' + '/' + ouid
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() if r.status_code == SUCCESS_STATUS_CODE else None
    
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
        for vlanObj in self.getObjects ('Vlans'):
            vlan = vlanObj['Object']
            if vlan['VlanId'] == vlanId:
                return int(vlan['IfIndex'])
			

if __name__=='__main__':
    pass
