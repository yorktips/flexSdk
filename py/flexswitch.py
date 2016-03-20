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
        return r.json()

    def createBfdGlobal(self, bfd_type, bfd_enable):
    	obj =  {
        		'Bfd': bfd_type, 
        		'Enable': bfd_enable
        		}
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()    
        		
    def createBfdintf(self, ifindex, multiplier, mintx_int, minrx_int, minrx_echo, demand, auth, auth_type, auth_key, auth_data):
    	obj =  {
        		'IfIndex': ifindex,
    			'LocalMultiplier': multiplier, 
    			'DesiredMinTxInterval': mintx_int, 
    			'RequiredMinRxInterval': minrx_int, 
    			'RequiredMinEchoRxInterval': minrx_echo, 
    			'DemandEnabled': demand, 
    			'AuthenticationEnabled': auth, 
    			'AuthenticationType': auth_type, 
    			'AuthenticationKeyId': auth_key, 
    			'AuthenticationData': auth_data
    			}
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() 

    def createBfdSession(self, ipaddr, perlink, owner):
    	obj =  {
 				'IpAddr': ipaddr, 
 				'PerLink': perlink, 
 				'Owner': owner, 
    			}
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json() 

      
    def createBgpGlobal(self, asnum, rtrid, usemp, ebgpmp, ibgpmp):
        obj =  { 
                'ASNum'         : asnum,
                'RouterId'   : rtrid,  
                'UseMultiplePaths': usemp, 
				'EBGPMaxPaths': ebgpmp, 
				'IBGPMaxPaths': ibgpmp  
               }
 
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createBgpPeerGroup(self, name, desc, CRT, HT, KpAT, RRClustID=0, RRClient=False):
        obj =  { 
        		'Name' : name,
                'ConnectRetryTime': CRT, 
                'HoldTime'         : HT,
                'KeepaliveTime'    : KpAT,
                'Description'      : desc,
                'RouteReflectorClusterId' : RRClustID,
                'RouteReflectorClient': RRClient,
                
               }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()

    def createBgpPeer(self, nbrIp, peeras, peergroup, desc, bfd):
        obj =  { 
                'PeerAS'         : peeras,
                'AuthPassword'   : '',
                'Description'      : desc ,
                'PeerGroup'		: peergroup,
                'NeighborAddress' : nbrIp,
                'BfdEnable'	: bfd
               }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()

    def createBgpPeerLocAs(self, nbrIp, peeras, localas, peergroup, desc, bfd):
        obj =  { 
                'PeerAS'         : peeras,
                'LocalAS'        : localas,
                'AuthPassword'   : '',
                'Description'      : desc ,
                'PeerGroup'		: peergroup,
                'NeighborAddress' : nbrIp,
                'BfdEnable'	: bfd
               }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createOspfGlobal(self, rtrid='10.0.1.1'):
        obj =  { 
                'RouterIdKey' : rtrid,
               }
        reqUrl =  self.urlBase+'OspfGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicyCondition(self, condition ):
        obj = condition 
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicyAction (self, action):
        obj = action
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicyStatement (self, stmt):
        obj = stmt 
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def createPolicy(self, policy ):
        obj = policy 
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
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
        reqUrl =  self.urlBase+'OspfIfEntry'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
		
    def createRedistributionPolicy(self):
        obj = {'Name'           :'RedistributeConnectedToBGP', 
          'MatchPrefixSet': {'PrefixSet' :'', 'MatchSetOptions' : 0}, 
          'InstallProtocolEq':'Connected', 
          'RouteDisposition': '', 
          'Redistribute':True, 
          'RedistributeTargetProtocol':'BGP'}

        reqUrl =  self.urlBase+'PolicyDefinitionStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers)
        return r.json()
        
    def enableGlobalDHCPRelay (self) :
        obj =  { 
        		'DhcpRelay': 'Test',
                'Enable' : True
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
        print obj["NameKey"], r.__dict__
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
        return r.json()
        
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
        for vlan in self.getObjects('Vlans'):
            #print vlan
            if vlan['ConfigObj']['VlanId'] == vlanId:
                return int(vlan['ConfigObj']['IfIndex'])
                
####################################################################               
#################### DELETE OPERATIONS #############################
####################################################################               

    def deleteIPv4Address( self, uuid) :
        reqUrl =  self.urlBase+'IPv4Intf/'+ uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
      
    def deleteVlan (self, uuid):
        reqUrl =  self.urlBase+'Vlan/' + uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
    
    def deleteBfdGlobal(self, uuid):
        reqUrl =  self.urlBase+'BfdGlobalConfig/' + uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()    
        
    def deleteBfdintf(self, uuid):
        reqUrl =  self.urlBase+'BfdIntfConfig/' + uuid
        r = requests.post(reqUrl,  headers=headers)
        return r.json() 
    
    def deleteBfdSession(self, uuid):
        reqUrl =  self.urlBase+'BfdSessionConfig/' + uuid
        r = requests.post(reqUrl,  headers=headers)
        return r.json() 
      
    def deleteBgpGlobal(self, uuid):
        reqUrl =  self.urlBase+'BGPGlobalConfig/' + uuid
        r = requests.post(reqUrl,  headers=headers)
        return r.json()
        
    def deleteBgpPeerGroup(self, uuid):
        reqUrl =  self.urlBase+'BGPPeerGroup/' + uuid
        r = requests.post(reqUrl,  headers=headers)
        return r.json()
    
    def deleteBgpPeer(self, uuid):
        reqUrl =  self.urlBase+'BGPNeighborConfig/' + uuid
        r = requests.post(reqUrl,  headers=headers)
        return r.json()
    
    def deleteOspfGlobal(self, uuid):
        reqUrl =  self.urlBase+'OspfGlobalConfig/'+ uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
        
    def deletePolicyCondition(self, uuid ):
        reqUrl =  self.urlBase+'PolicyConditionConfig/'+ uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
        
    def deletePolicyAction (self, uuid):
        reqUrl =  self.urlBase+'PolicyActionConfig/'+ uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
        
    def deletePolicyStatement (self, uuid):
        reqUrl =  self.urlBase+'PolicyStmtConfig/'+ uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
        
    def deletePolicy(self, uuid ):
        reqUrl =  self.urlBase+'PolicyDefinitionConfig/'+ uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
    
    def deleteOspfIntf(self, uuid):
        reqUrl =  self.urlBase+'OspfIfEntryConfig/' + uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
    	
        
    def deleteGlobalDHCPRelay (self, uuid):
        reqUrl =  self.urlBase+'DhcpRelayGlobalConfig/' + uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()
        
    def deleteIntfDHCPRelay (self, uuid):
        reqUrl =  self.urlBase+'DhcpRelayIntfConfig/' + uuid
        r = requests.delete(reqUrl,  headers=headers)
        return r.json()      
			

if __name__=='__main__':
    pass
