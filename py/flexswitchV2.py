#!/usr/bin/python                                                                                                       
import requests                                                                                                         
import json                                                                                                             
import urllib2                                                                                                          
                                                                                                                        
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}                                          

def processReturnCode (method) :
    def returnDetails (self, *args, **kwargs) :
        r = method(self, *args, **kwargs)
        if r.status_code in self.httpSuccessCodes:
            return (r.json(), None)
        else:
            print 'Error in executing request. Error code %s, Error Message ' %(r.status_code) 
            return ({}, "Error")
    return returnDetails

class FlexSwitch( object):                                                                                              
    httpSuccessCodes = [200, 201, 202, 204]
    def  __init__ (self, ip, port):                                                                                     
        self.ip    = ip                                                                                                 
        self.port  = port                                                                                               
        self.urlBase = 'http://%s:%s/public/v1/'%(ip,str(port))                                                         

    def getObjects(self, objName):                                                                                         
        currentMarker = 0                                                                                                  
        nextMarker = 0                                                                                                     
        count = 10                                                                                                         
        more = True                                                                                                        
        entries = []                                                                                                       
        while more == True:                                                                                                
            qry = 'http://%s:8080/public/v1/%ss?CurrentMarker=%d&NextMarker=%d&Count=%d' %(self.ip, objName, currentMarker, nextMarker, count)
            response = requests.get(qry)                                                                                   
            data = response.json()                                                                                         
            more =  data['MoreExist']                                                                                      
            currentMarker =  data['NextMarker']                                                                            
            NextMarker    =  data['NextMarker']                                                                            
            if data['StateObjects'] != None:                                                                               
                entries.extend(data['StateObjects'])                                                                       
        return entries

    @processReturnCode
    def createArpConfig(self,
                        ArpConfigKey,
                        Timeout):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey,
                'Timeout' : int(Timeout),
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateArpConfig(self,
                        ArpConfigKey,
                        Timeout = None):
        obj =  {}
        if ArpConfigKey != None :
            obj['ArpConfigKey'] = ArpConfigKey

        if Timeout != None :
            obj['Timeout'] = int(Timeout)

        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateArpConfigById(self,
                             objectId,
                             Timeout = None):
        obj =  {'objectId': objectId }
        if Timeout !=  None:
            obj['Timeout'] = Timeout

        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteArpConfig(self,
                        ArpConfigKey):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey,
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteArpConfigById(self, objectId ):
        reqUrl =  self.urlBase+'ArpConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getArpConfig(self,
                     ArpConfigKey):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey,
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getArpConfigById(self, objectId ):
        reqUrl =  self.urlBase+'ArpConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpConfigs(self):
        return self.getObjects( 'ArpConfig') 


    @processReturnCode
    def createBGPPeerGroup(self,
                           Name,
                           PeerAS,
                           RouteReflectorClusterId=0,
                           RouteReflectorClient=False,
                           Description='',
                           MultiHopTTL=0,
                           LocalAS=0,
                           KeepaliveTime=60,
                           AddPathsMaxTx=0,
                           MultiHopEnable=False,
                           AddPathsRx=False,
                           HoldTime=180,
                           AuthPassword='',
                           ConnectRetryTime=60):
        obj =  { 
                'Name' : Name,
                'PeerAS' : int(PeerAS),
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'Description' : Description,
                'MultiHopTTL' : int(MultiHopTTL),
                'LocalAS' : int(LocalAS),
                'KeepaliveTime' : int(KeepaliveTime),
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'AddPathsRx' : True if AddPathsRx else False,
                'HoldTime' : int(HoldTime),
                'AuthPassword' : AuthPassword,
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPeerGroup(self,
                           Name,
                           PeerAS = None,
                           RouteReflectorClusterId = None,
                           RouteReflectorClient = None,
                           Description = None,
                           MultiHopTTL = None,
                           LocalAS = None,
                           KeepaliveTime = None,
                           AddPathsMaxTx = None,
                           MultiHopEnable = None,
                           AddPathsRx = None,
                           HoldTime = None,
                           AuthPassword = None,
                           ConnectRetryTime = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if PeerAS != None :
            obj['PeerAS'] = int(PeerAS)

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if Description != None :
            obj['Description'] = Description

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if LocalAS != None :
            obj['LocalAS'] = int(LocalAS)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if AuthPassword != None :
            obj['AuthPassword'] = AuthPassword

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPeerGroupById(self,
                                objectId,
                                PeerAS = None,
                                RouteReflectorClusterId = None,
                                RouteReflectorClient = None,
                                Description = None,
                                MultiHopTTL = None,
                                LocalAS = None,
                                KeepaliveTime = None,
                                AddPathsMaxTx = None,
                                MultiHopEnable = None,
                                AddPathsRx = None,
                                HoldTime = None,
                                AuthPassword = None,
                                ConnectRetryTime = None):
        obj =  {'objectId': objectId }
        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if Description !=  None:
            obj['Description'] = Description

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if AuthPassword !=  None:
            obj['AuthPassword'] = AuthPassword

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPeerGroup(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPeerGroupById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPeerGroup'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPPeerGroup(self,
                        Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPeerGroupById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPeerGroup'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPeerGroups(self):
        return self.getObjects( 'BGPPeerGroup') 


    @processReturnCode
    def getBGPGlobalState(self,
                          RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.urlBase+'BGPGlobalState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPGlobalStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPGlobalState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPGlobalStates(self):
        return self.getObjects( 'BGPGlobalState') 


    @processReturnCode
    def getDhcpRelayIntfState(self,
                              IntfId):
        obj =  { 
                'IntfId' : IntfId,
                }
        reqUrl =  self.urlBase+'DhcpRelayIntfState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayIntfStateById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntfState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayIntfStates(self):
        return self.getObjects( 'DhcpRelayIntfState') 


    @processReturnCode
    def createOspfAreaAggregateEntryConfig(self,
                                           AreaAggregateLsdbType,
                                           AreaAggregateMask,
                                           AreaAggregateAreaID,
                                           AreaAggregateNet,
                                           AreaAggregateEffect,
                                           AreaAggregateExtRouteTag):
        obj =  { 
                'AreaAggregateLsdbType' : int(AreaAggregateLsdbType),
                'AreaAggregateMask' : AreaAggregateMask,
                'AreaAggregateAreaID' : AreaAggregateAreaID,
                'AreaAggregateNet' : AreaAggregateNet,
                'AreaAggregateEffect' : int(AreaAggregateEffect),
                'AreaAggregateExtRouteTag' : int(AreaAggregateExtRouteTag),
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfAreaAggregateEntryConfig(self,
                                           AreaAggregateLsdbType,
                                           AreaAggregateMask,
                                           AreaAggregateAreaID,
                                           AreaAggregateNet,
                                           AreaAggregateEffect = None,
                                           AreaAggregateExtRouteTag = None):
        obj =  {}
        if AreaAggregateLsdbType != None :
            obj['AreaAggregateLsdbType'] = int(AreaAggregateLsdbType)

        if AreaAggregateMask != None :
            obj['AreaAggregateMask'] = AreaAggregateMask

        if AreaAggregateAreaID != None :
            obj['AreaAggregateAreaID'] = AreaAggregateAreaID

        if AreaAggregateNet != None :
            obj['AreaAggregateNet'] = AreaAggregateNet

        if AreaAggregateEffect != None :
            obj['AreaAggregateEffect'] = int(AreaAggregateEffect)

        if AreaAggregateExtRouteTag != None :
            obj['AreaAggregateExtRouteTag'] = int(AreaAggregateExtRouteTag)

        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfAreaAggregateEntryConfigById(self,
                                                objectId,
                                                AreaAggregateEffect = None,
                                                AreaAggregateExtRouteTag = None):
        obj =  {'objectId': objectId }
        if AreaAggregateEffect !=  None:
            obj['AreaAggregateEffect'] = AreaAggregateEffect

        if AreaAggregateExtRouteTag !=  None:
            obj['AreaAggregateExtRouteTag'] = AreaAggregateExtRouteTag

        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfAreaAggregateEntryConfig(self,
                                           AreaAggregateLsdbType,
                                           AreaAggregateMask,
                                           AreaAggregateAreaID,
                                           AreaAggregateNet):
        obj =  { 
                'AreaAggregateLsdbType' : AreaAggregateLsdbType,
                'AreaAggregateMask' : AreaAggregateMask,
                'AreaAggregateAreaID' : AreaAggregateAreaID,
                'AreaAggregateNet' : AreaAggregateNet,
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfAreaAggregateEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaAggregateEntryConfig(self,
                                        AreaAggregateLsdbType,
                                        AreaAggregateMask,
                                        AreaAggregateAreaID,
                                        AreaAggregateNet):
        obj =  { 
                'AreaAggregateLsdbType' : AreaAggregateLsdbType,
                'AreaAggregateMask' : AreaAggregateMask,
                'AreaAggregateAreaID' : AreaAggregateAreaID,
                'AreaAggregateNet' : AreaAggregateNet,
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaAggregateEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaAggregateEntryConfigs(self):
        return self.getObjects( 'OspfAreaAggregateEntryConfig') 


    @processReturnCode
    def createDhcpRelayGlobal(self,
                              DhcpRelay,
                              Enable):
        obj =  { 
                'DhcpRelay' : DhcpRelay,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateDhcpRelayGlobal(self,
                              DhcpRelay,
                              Enable = None):
        obj =  {}
        if DhcpRelay != None :
            obj['DhcpRelay'] = DhcpRelay

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateDhcpRelayGlobalById(self,
                                   objectId,
                                   Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteDhcpRelayGlobal(self,
                              DhcpRelay):
        obj =  { 
                'DhcpRelay' : DhcpRelay,
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayGlobal(self,
                           DhcpRelay):
        obj =  { 
                'DhcpRelay' : DhcpRelay,
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayGlobals(self):
        return self.getObjects( 'DhcpRelayGlobal') 


    @processReturnCode
    def createIpTableAcl(self,
                         Name,
                         Action,
                         IpAddr,
                         Protocol,
                         Port='all',
                         PhysicalPort='all'):
        obj =  { 
                'Name' : Name,
                'Action' : Action,
                'IpAddr' : IpAddr,
                'Protocol' : Protocol,
                'Port' : Port,
                'PhysicalPort' : PhysicalPort,
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIpTableAcl(self,
                         Name,
                         Action = None,
                         IpAddr = None,
                         Protocol = None,
                         Port = None,
                         PhysicalPort = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Action != None :
            obj['Action'] = Action

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Protocol != None :
            obj['Protocol'] = Protocol

        if Port != None :
            obj['Port'] = Port

        if PhysicalPort != None :
            obj['PhysicalPort'] = PhysicalPort

        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIpTableAclById(self,
                              objectId,
                              Action = None,
                              IpAddr = None,
                              Protocol = None,
                              Port = None,
                              PhysicalPort = None):
        obj =  {'objectId': objectId }
        if Action !=  None:
            obj['Action'] = Action

        if IpAddr !=  None:
            obj['IpAddr'] = IpAddr

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if Port !=  None:
            obj['Port'] = Port

        if PhysicalPort !=  None:
            obj['PhysicalPort'] = PhysicalPort

        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIpTableAcl(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIpTableAclById(self, objectId ):
        reqUrl =  self.urlBase+'IpTableAcl'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getIpTableAcl(self,
                      Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getIpTableAclById(self, objectId ):
        reqUrl =  self.urlBase+'IpTableAcl'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIpTableAcls(self):
        return self.getObjects( 'IpTableAcl') 


    @processReturnCode
    def createStpBridgeInstance(self,
                                Vlan,
                                Address,
                                Priority,
                                MaxAge,
                                HelloTime,
                                ForwardDelay,
                                ForceVersion,
                                TxHoldCount):
        obj =  { 
                'Vlan' : Vlan,
                'Address' : Address,
                'Priority' : int(Priority),
                'MaxAge' : int(MaxAge),
                'HelloTime' : int(HelloTime),
                'ForwardDelay' : int(ForwardDelay),
                'ForceVersion' : int(ForceVersion),
                'TxHoldCount' : int(TxHoldCount),
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateStpBridgeInstance(self,
                                Vlan,
                                Address = None,
                                Priority = None,
                                MaxAge = None,
                                HelloTime = None,
                                ForwardDelay = None,
                                ForceVersion = None,
                                TxHoldCount = None):
        obj =  {}
        if Vlan != None :
            obj['Vlan'] = Vlan

        if Address != None :
            obj['Address'] = Address

        if Priority != None :
            obj['Priority'] = int(Priority)

        if MaxAge != None :
            obj['MaxAge'] = int(MaxAge)

        if HelloTime != None :
            obj['HelloTime'] = int(HelloTime)

        if ForwardDelay != None :
            obj['ForwardDelay'] = int(ForwardDelay)

        if ForceVersion != None :
            obj['ForceVersion'] = int(ForceVersion)

        if TxHoldCount != None :
            obj['TxHoldCount'] = int(TxHoldCount)

        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateStpBridgeInstanceById(self,
                                     objectId,
                                     Address = None,
                                     Priority = None,
                                     MaxAge = None,
                                     HelloTime = None,
                                     ForwardDelay = None,
                                     ForceVersion = None,
                                     TxHoldCount = None):
        obj =  {'objectId': objectId }
        if Address !=  None:
            obj['Address'] = Address

        if Priority !=  None:
            obj['Priority'] = Priority

        if MaxAge !=  None:
            obj['MaxAge'] = MaxAge

        if HelloTime !=  None:
            obj['HelloTime'] = HelloTime

        if ForwardDelay !=  None:
            obj['ForwardDelay'] = ForwardDelay

        if ForceVersion !=  None:
            obj['ForceVersion'] = ForceVersion

        if TxHoldCount !=  None:
            obj['TxHoldCount'] = TxHoldCount

        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteStpBridgeInstance(self,
                                Vlan):
        obj =  { 
                'Vlan' : Vlan,
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.urlBase+'StpBridgeInstance'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getStpBridgeInstance(self,
                             Vlan):
        obj =  { 
                'Vlan' : Vlan,
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.urlBase+'StpBridgeInstance'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpBridgeInstances(self):
        return self.getObjects( 'StpBridgeInstance') 


    @processReturnCode
    def createOspfAreaEntryConfig(self,
                                  AreaId,
                                  AuthType,
                                  ImportAsExtern,
                                  AreaSummary,
                                  AreaNssaTranslatorRole,
                                  AreaNssaTranslatorStabilityInterval):
        obj =  { 
                'AreaId' : AreaId,
                'AuthType' : int(AuthType),
                'ImportAsExtern' : int(ImportAsExtern),
                'AreaSummary' : int(AreaSummary),
                'AreaNssaTranslatorRole' : int(AreaNssaTranslatorRole),
                'AreaNssaTranslatorStabilityInterval' : int(AreaNssaTranslatorStabilityInterval),
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfAreaEntryConfig(self,
                                  AreaId,
                                  AuthType = None,
                                  ImportAsExtern = None,
                                  AreaSummary = None,
                                  AreaNssaTranslatorRole = None,
                                  AreaNssaTranslatorStabilityInterval = None):
        obj =  {}
        if AreaId != None :
            obj['AreaId'] = AreaId

        if AuthType != None :
            obj['AuthType'] = int(AuthType)

        if ImportAsExtern != None :
            obj['ImportAsExtern'] = int(ImportAsExtern)

        if AreaSummary != None :
            obj['AreaSummary'] = int(AreaSummary)

        if AreaNssaTranslatorRole != None :
            obj['AreaNssaTranslatorRole'] = int(AreaNssaTranslatorRole)

        if AreaNssaTranslatorStabilityInterval != None :
            obj['AreaNssaTranslatorStabilityInterval'] = int(AreaNssaTranslatorStabilityInterval)

        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfAreaEntryConfigById(self,
                                       objectId,
                                       AuthType = None,
                                       ImportAsExtern = None,
                                       AreaSummary = None,
                                       AreaNssaTranslatorRole = None,
                                       AreaNssaTranslatorStabilityInterval = None):
        obj =  {'objectId': objectId }
        if AuthType !=  None:
            obj['AuthType'] = AuthType

        if ImportAsExtern !=  None:
            obj['ImportAsExtern'] = ImportAsExtern

        if AreaSummary !=  None:
            obj['AreaSummary'] = AreaSummary

        if AreaNssaTranslatorRole !=  None:
            obj['AreaNssaTranslatorRole'] = AreaNssaTranslatorRole

        if AreaNssaTranslatorStabilityInterval !=  None:
            obj['AreaNssaTranslatorStabilityInterval'] = AreaNssaTranslatorStabilityInterval

        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfAreaEntryConfig(self,
                                  AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaEntryConfig(self,
                               AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaEntryConfigs(self):
        return self.getObjects( 'OspfAreaEntryConfig') 


    @processReturnCode
    def createLLDPIntf(self,
                       IfIndex,
                       Enable):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.urlBase+'LLDPIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateLLDPIntf(self,
                       IfIndex,
                       Enable = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.urlBase+'LLDPIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateLLDPIntfById(self,
                            objectId,
                            Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.urlBase+'LLDPIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteLLDPIntf(self,
                       IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'LLDPIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteLLDPIntfById(self, objectId ):
        reqUrl =  self.urlBase+'LLDPIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getLLDPIntf(self,
                    IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'LLDPIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getLLDPIntfById(self, objectId ):
        reqUrl =  self.urlBase+'LLDPIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLLDPIntfs(self):
        return self.getObjects( 'LLDPIntf') 


    @processReturnCode
    def getLaPortChannelMemberState(self,
                                    IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'LaPortChannelMemberState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getLaPortChannelMemberStateById(self, objectId ):
        reqUrl =  self.urlBase+'LaPortChannelMemberState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLaPortChannelMemberStates(self):
        return self.getObjects( 'LaPortChannelMemberState') 


    @processReturnCode
    def getOspfHostEntryState(self,
                              HostTOS,
                              HostIpAddress):
        obj =  { 
                'HostTOS' : HostTOS,
                'HostIpAddress' : HostIpAddress,
                }
        reqUrl =  self.urlBase+'OspfHostEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfHostEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfHostEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfHostEntryStates(self):
        return self.getObjects( 'OspfHostEntryState') 


    @processReturnCode
    def getOspfLsdbEntryState(self,
                              LsdbType,
                              LsdbAreaId,
                              LsdbLsid,
                              LsdbRouterId):
        obj =  { 
                'LsdbType' : LsdbType,
                'LsdbAreaId' : LsdbAreaId,
                'LsdbLsid' : LsdbLsid,
                'LsdbRouterId' : LsdbRouterId,
                }
        reqUrl =  self.urlBase+'OspfLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfLsdbEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfLsdbEntryStates(self):
        return self.getObjects( 'OspfLsdbEntryState') 


    @processReturnCode
    def createIPv4Intf(self,
                       IpAddr,
                       IfIndex):
        obj =  { 
                'IpAddr' : IpAddr,
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIPv4Intf(self,
                       IpAddr,
                       IfIndex = None):
        obj =  {}
        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIPv4IntfById(self,
                            objectId,
                            IfIndex = None):
        obj =  {'objectId': objectId }
        if IfIndex !=  None:
            obj['IfIndex'] = IfIndex

        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIPv4Intf(self,
                       IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIPv4IntfById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getIPv4Intf(self,
                    IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getIPv4IntfById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4Intfs(self):
        return self.getObjects( 'IPv4Intf') 


    @processReturnCode
    def getPolicyStmtState(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyStmtState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyStmtStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyStmtState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyStmtStates(self):
        return self.getObjects( 'PolicyStmtState') 


    @processReturnCode
    def createOspfAreaRangeEntryConfig(self,
                                       AreaRangeNet,
                                       AreaRangeAreaId,
                                       AreaRangeMask,
                                       AreaRangeEffect):
        obj =  { 
                'AreaRangeNet' : AreaRangeNet,
                'AreaRangeAreaId' : AreaRangeAreaId,
                'AreaRangeMask' : AreaRangeMask,
                'AreaRangeEffect' : int(AreaRangeEffect),
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfAreaRangeEntryConfig(self,
                                       AreaRangeNet,
                                       AreaRangeAreaId,
                                       AreaRangeMask = None,
                                       AreaRangeEffect = None):
        obj =  {}
        if AreaRangeNet != None :
            obj['AreaRangeNet'] = AreaRangeNet

        if AreaRangeAreaId != None :
            obj['AreaRangeAreaId'] = AreaRangeAreaId

        if AreaRangeMask != None :
            obj['AreaRangeMask'] = AreaRangeMask

        if AreaRangeEffect != None :
            obj['AreaRangeEffect'] = int(AreaRangeEffect)

        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfAreaRangeEntryConfigById(self,
                                            objectId,
                                            AreaRangeMask = None,
                                            AreaRangeEffect = None):
        obj =  {'objectId': objectId }
        if AreaRangeMask !=  None:
            obj['AreaRangeMask'] = AreaRangeMask

        if AreaRangeEffect !=  None:
            obj['AreaRangeEffect'] = AreaRangeEffect

        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfAreaRangeEntryConfig(self,
                                       AreaRangeNet,
                                       AreaRangeAreaId):
        obj =  { 
                'AreaRangeNet' : AreaRangeNet,
                'AreaRangeAreaId' : AreaRangeAreaId,
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfAreaRangeEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaRangeEntryConfig(self,
                                    AreaRangeNet,
                                    AreaRangeAreaId):
        obj =  { 
                'AreaRangeNet' : AreaRangeNet,
                'AreaRangeAreaId' : AreaRangeAreaId,
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaRangeEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaRangeEntryConfigs(self):
        return self.getObjects( 'OspfAreaRangeEntryConfig') 


    @processReturnCode
    def getOspfExtLsdbEntryState(self,
                                 ExtLsdbLsid,
                                 ExtLsdbRouterId,
                                 ExtLsdbType):
        obj =  { 
                'ExtLsdbLsid' : ExtLsdbLsid,
                'ExtLsdbRouterId' : ExtLsdbRouterId,
                'ExtLsdbType' : ExtLsdbType,
                }
        reqUrl =  self.urlBase+'OspfExtLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfExtLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfExtLsdbEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfExtLsdbEntryStates(self):
        return self.getObjects( 'OspfExtLsdbEntryState') 


    @processReturnCode
    def createBfdInterface(self,
                           IfIndex,
                           RequiredMinRxInterval=1000,
                           AuthData='snaproute',
                           DemandEnabled=False,
                           AuthKeyId=1,
                           AuthType='simple',
                           DesiredMinTxInterval=1000,
                           AuthenticationEnabled=False,
                           RequiredMinEchoRxInterval=0,
                           LocalMultiplier=3):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'RequiredMinRxInterval' : int(RequiredMinRxInterval),
                'AuthData' : AuthData,
                'DemandEnabled' : True if DemandEnabled else False,
                'AuthKeyId' : int(AuthKeyId),
                'AuthType' : AuthType,
                'DesiredMinTxInterval' : int(DesiredMinTxInterval),
                'AuthenticationEnabled' : True if AuthenticationEnabled else False,
                'RequiredMinEchoRxInterval' : int(RequiredMinEchoRxInterval),
                'LocalMultiplier' : int(LocalMultiplier),
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBfdInterface(self,
                           IfIndex,
                           RequiredMinRxInterval = None,
                           AuthData = None,
                           DemandEnabled = None,
                           AuthKeyId = None,
                           AuthType = None,
                           DesiredMinTxInterval = None,
                           AuthenticationEnabled = None,
                           RequiredMinEchoRxInterval = None,
                           LocalMultiplier = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if RequiredMinRxInterval != None :
            obj['RequiredMinRxInterval'] = int(RequiredMinRxInterval)

        if AuthData != None :
            obj['AuthData'] = AuthData

        if DemandEnabled != None :
            obj['DemandEnabled'] = True if DemandEnabled else False

        if AuthKeyId != None :
            obj['AuthKeyId'] = int(AuthKeyId)

        if AuthType != None :
            obj['AuthType'] = AuthType

        if DesiredMinTxInterval != None :
            obj['DesiredMinTxInterval'] = int(DesiredMinTxInterval)

        if AuthenticationEnabled != None :
            obj['AuthenticationEnabled'] = True if AuthenticationEnabled else False

        if RequiredMinEchoRxInterval != None :
            obj['RequiredMinEchoRxInterval'] = int(RequiredMinEchoRxInterval)

        if LocalMultiplier != None :
            obj['LocalMultiplier'] = int(LocalMultiplier)

        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBfdInterfaceById(self,
                                objectId,
                                RequiredMinRxInterval = None,
                                AuthData = None,
                                DemandEnabled = None,
                                AuthKeyId = None,
                                AuthType = None,
                                DesiredMinTxInterval = None,
                                AuthenticationEnabled = None,
                                RequiredMinEchoRxInterval = None,
                                LocalMultiplier = None):
        obj =  {'objectId': objectId }
        if RequiredMinRxInterval !=  None:
            obj['RequiredMinRxInterval'] = RequiredMinRxInterval

        if AuthData !=  None:
            obj['AuthData'] = AuthData

        if DemandEnabled !=  None:
            obj['DemandEnabled'] = DemandEnabled

        if AuthKeyId !=  None:
            obj['AuthKeyId'] = AuthKeyId

        if AuthType !=  None:
            obj['AuthType'] = AuthType

        if DesiredMinTxInterval !=  None:
            obj['DesiredMinTxInterval'] = DesiredMinTxInterval

        if AuthenticationEnabled !=  None:
            obj['AuthenticationEnabled'] = AuthenticationEnabled

        if RequiredMinEchoRxInterval !=  None:
            obj['RequiredMinEchoRxInterval'] = RequiredMinEchoRxInterval

        if LocalMultiplier !=  None:
            obj['LocalMultiplier'] = LocalMultiplier

        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBfdInterface(self,
                           IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBfdInterfaceById(self, objectId ):
        reqUrl =  self.urlBase+'BfdInterface'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBfdInterface(self,
                        IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBfdInterfaceById(self, objectId ):
        reqUrl =  self.urlBase+'BfdInterface'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdInterfaces(self):
        return self.getObjects( 'BfdInterface') 


    @processReturnCode
    def getStpBridgeState(self,
                          Vlan):
        obj =  { 
                'Vlan' : Vlan,
                }
        reqUrl =  self.urlBase+'StpBridgeState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getStpBridgeStateById(self, objectId ):
        reqUrl =  self.urlBase+'StpBridgeState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpBridgeStates(self):
        return self.getObjects( 'StpBridgeState') 


    @processReturnCode
    def createSystemLogging(self,
                            SRLogger,
                            SystemLogging='on'):
        obj =  { 
                'SRLogger' : SRLogger,
                'SystemLogging' : SystemLogging,
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateSystemLogging(self,
                            SRLogger,
                            SystemLogging = None):
        obj =  {}
        if SRLogger != None :
            obj['SRLogger'] = SRLogger

        if SystemLogging != None :
            obj['SystemLogging'] = SystemLogging

        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateSystemLoggingById(self,
                                 objectId,
                                 SystemLogging = None):
        obj =  {'objectId': objectId }
        if SystemLogging !=  None:
            obj['SystemLogging'] = SystemLogging

        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteSystemLogging(self,
                            SRLogger):
        obj =  { 
                'SRLogger' : SRLogger,
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteSystemLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'SystemLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getSystemLogging(self,
                         SRLogger):
        obj =  { 
                'SRLogger' : SRLogger,
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getSystemLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'SystemLogging'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSystemLoggings(self):
        return self.getObjects( 'SystemLogging') 


    @processReturnCode
    def createBGPPolicyCondition(self,
                                 Name,
                                 ConditionType,
                                 IpPrefix,
                                 MaskLengthRange):
        obj =  { 
                'Name' : Name,
                'ConditionType' : ConditionType,
                'IpPrefix' : IpPrefix,
                'MaskLengthRange' : MaskLengthRange,
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyCondition(self,
                                 Name,
                                 ConditionType = None,
                                 IpPrefix = None,
                                 MaskLengthRange = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ConditionType != None :
            obj['ConditionType'] = ConditionType

        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange != None :
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyConditionById(self,
                                      objectId,
                                      ConditionType = None,
                                      IpPrefix = None,
                                      MaskLengthRange = None):
        obj =  {'objectId': objectId }
        if ConditionType !=  None:
            obj['ConditionType'] = ConditionType

        if IpPrefix !=  None:
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange !=  None:
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyCondition(self,
                                 Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyConditions(self):
        return self.getObjects( 'BGPPolicyCondition') 


    @processReturnCode
    def createOspfGlobalConfig(self,
                               RouterId,
                               AdminStat,
                               ASBdrRtrStatus,
                               TOSSupport,
                               ExtLsdbLimit,
                               MulticastExtensions,
                               ExitOverflowInterval,
                               DemandExtensions,
                               RFC1583Compatibility,
                               ReferenceBandwidth,
                               RestartSupport,
                               RestartInterval,
                               RestartStrictLsaChecking,
                               StubRouterAdvertisement):
        obj =  { 
                'RouterId' : RouterId,
                'AdminStat' : int(AdminStat),
                'ASBdrRtrStatus' : True if ASBdrRtrStatus else False,
                'TOSSupport' : True if TOSSupport else False,
                'ExtLsdbLimit' : int(ExtLsdbLimit),
                'MulticastExtensions' : int(MulticastExtensions),
                'ExitOverflowInterval' : int(ExitOverflowInterval),
                'DemandExtensions' : True if DemandExtensions else False,
                'RFC1583Compatibility' : True if RFC1583Compatibility else False,
                'ReferenceBandwidth' : int(ReferenceBandwidth),
                'RestartSupport' : int(RestartSupport),
                'RestartInterval' : int(RestartInterval),
                'RestartStrictLsaChecking' : True if RestartStrictLsaChecking else False,
                'StubRouterAdvertisement' : int(StubRouterAdvertisement),
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfGlobalConfig(self,
                               RouterId,
                               AdminStat = None,
                               ASBdrRtrStatus = None,
                               TOSSupport = None,
                               ExtLsdbLimit = None,
                               MulticastExtensions = None,
                               ExitOverflowInterval = None,
                               DemandExtensions = None,
                               RFC1583Compatibility = None,
                               ReferenceBandwidth = None,
                               RestartSupport = None,
                               RestartInterval = None,
                               RestartStrictLsaChecking = None,
                               StubRouterAdvertisement = None):
        obj =  {}
        if RouterId != None :
            obj['RouterId'] = RouterId

        if AdminStat != None :
            obj['AdminStat'] = int(AdminStat)

        if ASBdrRtrStatus != None :
            obj['ASBdrRtrStatus'] = True if ASBdrRtrStatus else False

        if TOSSupport != None :
            obj['TOSSupport'] = True if TOSSupport else False

        if ExtLsdbLimit != None :
            obj['ExtLsdbLimit'] = int(ExtLsdbLimit)

        if MulticastExtensions != None :
            obj['MulticastExtensions'] = int(MulticastExtensions)

        if ExitOverflowInterval != None :
            obj['ExitOverflowInterval'] = int(ExitOverflowInterval)

        if DemandExtensions != None :
            obj['DemandExtensions'] = True if DemandExtensions else False

        if RFC1583Compatibility != None :
            obj['RFC1583Compatibility'] = True if RFC1583Compatibility else False

        if ReferenceBandwidth != None :
            obj['ReferenceBandwidth'] = int(ReferenceBandwidth)

        if RestartSupport != None :
            obj['RestartSupport'] = int(RestartSupport)

        if RestartInterval != None :
            obj['RestartInterval'] = int(RestartInterval)

        if RestartStrictLsaChecking != None :
            obj['RestartStrictLsaChecking'] = True if RestartStrictLsaChecking else False

        if StubRouterAdvertisement != None :
            obj['StubRouterAdvertisement'] = int(StubRouterAdvertisement)

        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfGlobalConfigById(self,
                                    objectId,
                                    AdminStat = None,
                                    ASBdrRtrStatus = None,
                                    TOSSupport = None,
                                    ExtLsdbLimit = None,
                                    MulticastExtensions = None,
                                    ExitOverflowInterval = None,
                                    DemandExtensions = None,
                                    RFC1583Compatibility = None,
                                    ReferenceBandwidth = None,
                                    RestartSupport = None,
                                    RestartInterval = None,
                                    RestartStrictLsaChecking = None,
                                    StubRouterAdvertisement = None):
        obj =  {'objectId': objectId }
        if AdminStat !=  None:
            obj['AdminStat'] = AdminStat

        if ASBdrRtrStatus !=  None:
            obj['ASBdrRtrStatus'] = ASBdrRtrStatus

        if TOSSupport !=  None:
            obj['TOSSupport'] = TOSSupport

        if ExtLsdbLimit !=  None:
            obj['ExtLsdbLimit'] = ExtLsdbLimit

        if MulticastExtensions !=  None:
            obj['MulticastExtensions'] = MulticastExtensions

        if ExitOverflowInterval !=  None:
            obj['ExitOverflowInterval'] = ExitOverflowInterval

        if DemandExtensions !=  None:
            obj['DemandExtensions'] = DemandExtensions

        if RFC1583Compatibility !=  None:
            obj['RFC1583Compatibility'] = RFC1583Compatibility

        if ReferenceBandwidth !=  None:
            obj['ReferenceBandwidth'] = ReferenceBandwidth

        if RestartSupport !=  None:
            obj['RestartSupport'] = RestartSupport

        if RestartInterval !=  None:
            obj['RestartInterval'] = RestartInterval

        if RestartStrictLsaChecking !=  None:
            obj['RestartStrictLsaChecking'] = RestartStrictLsaChecking

        if StubRouterAdvertisement !=  None:
            obj['StubRouterAdvertisement'] = StubRouterAdvertisement

        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfGlobalConfig(self,
                               RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfGlobalConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfGlobalConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfGlobalConfig(self,
                            RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfGlobalConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfGlobalConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfGlobalConfigs(self):
        return self.getObjects( 'OspfGlobalConfig') 


    @processReturnCode
    def getDhcpRelayHostDhcpState(self,
                                  MacAddr):
        obj =  { 
                'MacAddr' : MacAddr,
                }
        reqUrl =  self.urlBase+'DhcpRelayHostDhcpState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayHostDhcpStateById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayHostDhcpState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayHostDhcpStates(self):
        return self.getObjects( 'DhcpRelayHostDhcpState') 


    @processReturnCode
    def getDhcpRelayIntfServerState(self,
                                    IntfId):
        obj =  { 
                'IntfId' : IntfId,
                }
        reqUrl =  self.urlBase+'DhcpRelayIntfServerState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayIntfServerStateById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntfServerState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayIntfServerStates(self):
        return self.getObjects( 'DhcpRelayIntfServerState') 


    @processReturnCode
    def getBGPPolicyActionState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyActionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyActionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyActionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyActionStates(self):
        return self.getObjects( 'BGPPolicyActionState') 


    @processReturnCode
    def createBGPPolicyDefinition(self,
                                  Name,
                                  Precedence,
                                  MatchType,
                                  StatementList):
        obj =  { 
                'Name' : Name,
                'Precedence' : int(Precedence),
                'MatchType' : MatchType,
                'StatementList' : StatementList,
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyDefinition(self,
                                  Name,
                                  Precedence = None,
                                  MatchType = None,
                                  StatementList = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Precedence != None :
            obj['Precedence'] = int(Precedence)

        if MatchType != None :
            obj['MatchType'] = MatchType

        if StatementList != None :
            obj['StatementList'] = StatementList

        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyDefinitionById(self,
                                       objectId,
                                       Precedence = None,
                                       MatchType = None,
                                       StatementList = None):
        obj =  {'objectId': objectId }
        if Precedence !=  None:
            obj['Precedence'] = Precedence

        if MatchType !=  None:
            obj['MatchType'] = MatchType

        if StatementList !=  None:
            obj['StatementList'] = StatementList

        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyDefinition(self,
                                  Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyDefinitions(self):
        return self.getObjects( 'BGPPolicyDefinition') 


    @processReturnCode
    def getVrrpIntfState(self,
                         VRID,
                         IfIndex):
        obj =  { 
                'VRID' : VRID,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'VrrpIntfState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVrrpIntfStateById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpIntfState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVrrpIntfStates(self):
        return self.getObjects( 'VrrpIntfState') 


    @processReturnCode
    def getOspfAsLsdbEntryState(self,
                                AsLsdbLsid,
                                AsLsdbRouterId,
                                AsLsdbType):
        obj =  { 
                'AsLsdbLsid' : AsLsdbLsid,
                'AsLsdbRouterId' : AsLsdbRouterId,
                'AsLsdbType' : AsLsdbType,
                }
        reqUrl =  self.urlBase+'OspfAsLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfAsLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAsLsdbEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAsLsdbEntryStates(self):
        return self.getObjects( 'OspfAsLsdbEntryState') 


    @processReturnCode
    def createVxlanInstance(self,
                            VxlanId,
                            McDestIp,
                            VlanId,
                            Mtu):
        obj =  { 
                'VxlanId' : int(VxlanId),
                'McDestIp' : McDestIp,
                'VlanId' : VlanId,
                'Mtu' : int(Mtu),
                }
        reqUrl =  self.urlBase+'VxlanInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVxlanInstance(self,
                            VxlanId,
                            McDestIp = None,
                            VlanId = None,
                            Mtu = None):
        obj =  {}
        if VxlanId != None :
            obj['VxlanId'] = int(VxlanId)

        if McDestIp != None :
            obj['McDestIp'] = McDestIp

        if VlanId != None :
            obj['VlanId'] = VlanId

        if Mtu != None :
            obj['Mtu'] = int(Mtu)

        reqUrl =  self.urlBase+'VxlanInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVxlanInstanceById(self,
                                 objectId,
                                 McDestIp = None,
                                 VlanId = None,
                                 Mtu = None):
        obj =  {'objectId': objectId }
        if McDestIp !=  None:
            obj['McDestIp'] = McDestIp

        if VlanId !=  None:
            obj['VlanId'] = VlanId

        if Mtu !=  None:
            obj['Mtu'] = Mtu

        reqUrl =  self.urlBase+'VxlanInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVxlanInstance(self,
                            VxlanId):
        obj =  { 
                'VxlanId' : VxlanId,
                }
        reqUrl =  self.urlBase+'VxlanInstance'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVxlanInstanceById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanInstance'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getVxlanInstance(self,
                         VxlanId):
        obj =  { 
                'VxlanId' : VxlanId,
                }
        reqUrl =  self.urlBase+'VxlanInstance'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVxlanInstanceById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanInstance'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVxlanInstances(self):
        return self.getObjects( 'VxlanInstance') 


    @processReturnCode
    def createPolicyDefinition(self,
                               Name,
                               Precedence,
                               MatchType,
                               StatementList):
        obj =  { 
                'Name' : Name,
                'Precedence' : int(Precedence),
                'MatchType' : MatchType,
                'StatementList' : StatementList,
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyDefinition(self,
                               Name,
                               Precedence = None,
                               MatchType = None,
                               StatementList = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Precedence != None :
            obj['Precedence'] = int(Precedence)

        if MatchType != None :
            obj['MatchType'] = MatchType

        if StatementList != None :
            obj['StatementList'] = StatementList

        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyDefinitionById(self,
                                    objectId,
                                    Precedence = None,
                                    MatchType = None,
                                    StatementList = None):
        obj =  {'objectId': objectId }
        if Precedence !=  None:
            obj['Precedence'] = Precedence

        if MatchType !=  None:
            obj['MatchType'] = MatchType

        if StatementList !=  None:
            obj['StatementList'] = StatementList

        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getPolicyDefinition(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyDefinitions(self):
        return self.getObjects( 'PolicyDefinition') 


    @processReturnCode
    def createOspfNbrEntryConfig(self,
                                 NbrIpAddr,
                                 NbrAddressLessIndex,
                                 NbrPriority):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr,
                'NbrAddressLessIndex' : int(NbrAddressLessIndex),
                'NbrPriority' : int(NbrPriority),
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfNbrEntryConfig(self,
                                 NbrIpAddr,
                                 NbrAddressLessIndex,
                                 NbrPriority = None):
        obj =  {}
        if NbrIpAddr != None :
            obj['NbrIpAddr'] = NbrIpAddr

        if NbrAddressLessIndex != None :
            obj['NbrAddressLessIndex'] = int(NbrAddressLessIndex)

        if NbrPriority != None :
            obj['NbrPriority'] = int(NbrPriority)

        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfNbrEntryConfigById(self,
                                      objectId,
                                      NbrPriority = None):
        obj =  {'objectId': objectId }
        if NbrPriority !=  None:
            obj['NbrPriority'] = NbrPriority

        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfNbrEntryConfig(self,
                                 NbrIpAddr,
                                 NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr,
                'NbrAddressLessIndex' : NbrAddressLessIndex,
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfNbrEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfNbrEntryConfig(self,
                              NbrIpAddr,
                              NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr,
                'NbrAddressLessIndex' : NbrAddressLessIndex,
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfNbrEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfNbrEntryConfigs(self):
        return self.getObjects( 'OspfNbrEntryConfig') 


    @processReturnCode
    def createVlan(self,
                   VlanId,
                   IfIndexList,
                   UntagIfIndexList):
        obj =  { 
                'VlanId' : int(VlanId),
                'IfIndexList' : IfIndexList,
                'UntagIfIndexList' : UntagIfIndexList,
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVlan(self,
                   VlanId,
                   IfIndexList = None,
                   UntagIfIndexList = None):
        obj =  {}
        if VlanId != None :
            obj['VlanId'] = int(VlanId)

        if IfIndexList != None :
            obj['IfIndexList'] = IfIndexList

        if UntagIfIndexList != None :
            obj['UntagIfIndexList'] = UntagIfIndexList

        reqUrl =  self.urlBase+'Vlan'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVlanById(self,
                        objectId,
                        IfIndexList = None,
                        UntagIfIndexList = None):
        obj =  {'objectId': objectId }
        if IfIndexList !=  None:
            obj['IfIndexList'] = IfIndexList

        if UntagIfIndexList !=  None:
            obj['UntagIfIndexList'] = UntagIfIndexList

        reqUrl =  self.urlBase+'Vlan'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVlan(self,
                   VlanId):
        obj =  { 
                'VlanId' : VlanId,
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVlanById(self, objectId ):
        reqUrl =  self.urlBase+'Vlan'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getVlan(self,
                VlanId):
        obj =  { 
                'VlanId' : VlanId,
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVlanById(self, objectId ):
        reqUrl =  self.urlBase+'Vlan'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVlans(self):
        return self.getObjects( 'Vlan') 


    @processReturnCode
    def getOspfLocalLsdbEntryState(self,
                                   LocalLsdbAddressLessIf,
                                   LocalLsdbIpAddress,
                                   LocalLsdbRouterId,
                                   LocalLsdbLsid,
                                   LocalLsdbType):
        obj =  { 
                'LocalLsdbAddressLessIf' : LocalLsdbAddressLessIf,
                'LocalLsdbIpAddress' : LocalLsdbIpAddress,
                'LocalLsdbRouterId' : LocalLsdbRouterId,
                'LocalLsdbLsid' : LocalLsdbLsid,
                'LocalLsdbType' : LocalLsdbType,
                }
        reqUrl =  self.urlBase+'OspfLocalLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfLocalLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfLocalLsdbEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfLocalLsdbEntryStates(self):
        return self.getObjects( 'OspfLocalLsdbEntryState') 


    @processReturnCode
    def createOspfIfMetricEntryConfig(self,
                                      IfMetricAddressLessIf,
                                      IfMetricTOS,
                                      IfMetricIpAddress,
                                      IfMetricValue):
        obj =  { 
                'IfMetricAddressLessIf' : int(IfMetricAddressLessIf),
                'IfMetricTOS' : int(IfMetricTOS),
                'IfMetricIpAddress' : IfMetricIpAddress,
                'IfMetricValue' : int(IfMetricValue),
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfIfMetricEntryConfig(self,
                                      IfMetricAddressLessIf,
                                      IfMetricTOS,
                                      IfMetricIpAddress,
                                      IfMetricValue = None):
        obj =  {}
        if IfMetricAddressLessIf != None :
            obj['IfMetricAddressLessIf'] = int(IfMetricAddressLessIf)

        if IfMetricTOS != None :
            obj['IfMetricTOS'] = int(IfMetricTOS)

        if IfMetricIpAddress != None :
            obj['IfMetricIpAddress'] = IfMetricIpAddress

        if IfMetricValue != None :
            obj['IfMetricValue'] = int(IfMetricValue)

        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfIfMetricEntryConfigById(self,
                                           objectId,
                                           IfMetricValue = None):
        obj =  {'objectId': objectId }
        if IfMetricValue !=  None:
            obj['IfMetricValue'] = IfMetricValue

        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfIfMetricEntryConfig(self,
                                      IfMetricAddressLessIf,
                                      IfMetricTOS,
                                      IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf,
                'IfMetricTOS' : IfMetricTOS,
                'IfMetricIpAddress' : IfMetricIpAddress,
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfIfMetricEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfIfMetricEntryConfig(self,
                                   IfMetricAddressLessIf,
                                   IfMetricTOS,
                                   IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf,
                'IfMetricTOS' : IfMetricTOS,
                'IfMetricIpAddress' : IfMetricIpAddress,
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfIfMetricEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIfMetricEntryConfigs(self):
        return self.getObjects( 'OspfIfMetricEntryConfig') 


    @processReturnCode
    def getOspfVirtNbrEntryState(self,
                                 VirtNbrRtrId,
                                 VirtNbrArea):
        obj =  { 
                'VirtNbrRtrId' : VirtNbrRtrId,
                'VirtNbrArea' : VirtNbrArea,
                }
        reqUrl =  self.urlBase+'OspfVirtNbrEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfVirtNbrEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtNbrEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfVirtNbrEntryStates(self):
        return self.getObjects( 'OspfVirtNbrEntryState') 


    @processReturnCode
    def createComponentLogging(self,
                               Module,
                               Level='info'):
        obj =  { 
                'Module' : Module,
                'Level' : Level,
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateComponentLogging(self,
                               Module,
                               Level = None):
        obj =  {}
        if Module != None :
            obj['Module'] = Module

        if Level != None :
            obj['Level'] = Level

        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateComponentLoggingById(self,
                                    objectId,
                                    Level = None):
        obj =  {'objectId': objectId }
        if Level !=  None:
            obj['Level'] = Level

        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteComponentLogging(self,
                               Module):
        obj =  { 
                'Module' : Module,
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteComponentLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'ComponentLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getComponentLogging(self,
                            Module):
        obj =  { 
                'Module' : Module,
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getComponentLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'ComponentLogging'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllComponentLoggings(self):
        return self.getObjects( 'ComponentLogging') 


    @processReturnCode
    def createIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp,
                        OutgoingIntfType,
                        OutgoingInterface,
                        Protocol,
                        Cost=0):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHopIp' : NextHopIp,
                'OutgoingIntfType' : OutgoingIntfType,
                'OutgoingInterface' : OutgoingInterface,
                'Protocol' : Protocol,
                'Cost' : int(Cost),
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp,
                        OutgoingIntfType = None,
                        OutgoingInterface = None,
                        Protocol = None,
                        Cost = None):
        obj =  {}
        if DestinationNw != None :
            obj['DestinationNw'] = DestinationNw

        if NetworkMask != None :
            obj['NetworkMask'] = NetworkMask

        if NextHopIp != None :
            obj['NextHopIp'] = NextHopIp

        if OutgoingIntfType != None :
            obj['OutgoingIntfType'] = OutgoingIntfType

        if OutgoingInterface != None :
            obj['OutgoingInterface'] = OutgoingInterface

        if Protocol != None :
            obj['Protocol'] = Protocol

        if Cost != None :
            obj['Cost'] = int(Cost)

        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIPv4RouteById(self,
                             objectId,
                             OutgoingIntfType = None,
                             OutgoingInterface = None,
                             Protocol = None,
                             Cost = None):
        obj =  {'objectId': objectId }
        if OutgoingIntfType !=  None:
            obj['OutgoingIntfType'] = OutgoingIntfType

        if OutgoingInterface !=  None:
            obj['OutgoingInterface'] = OutgoingInterface

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if Cost !=  None:
            obj['Cost'] = Cost

        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHopIp' : NextHopIp,
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIPv4RouteById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getIPv4Route(self,
                     DestinationNw,
                     NetworkMask,
                     NextHopIp):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHopIp' : NextHopIp,
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getIPv4RouteById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4Routes(self):
        return self.getObjects( 'IPv4Route') 


    @processReturnCode
    def getVlanState(self,
                     VlanId):
        obj =  { 
                'VlanId' : VlanId,
                }
        reqUrl =  self.urlBase+'VlanState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVlanStateById(self, objectId ):
        reqUrl =  self.urlBase+'VlanState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVlanStates(self):
        return self.getObjects( 'VlanState') 


    @processReturnCode
    def createBGPPolicyAction(self,
                              Name,
                              ActionType,
                              GenerateASSet,
                              SendSummaryOnly):
        obj =  { 
                'Name' : Name,
                'ActionType' : ActionType,
                'GenerateASSet' : True if GenerateASSet else False,
                'SendSummaryOnly' : True if SendSummaryOnly else False,
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyAction(self,
                              Name,
                              ActionType = None,
                              GenerateASSet = None,
                              SendSummaryOnly = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ActionType != None :
            obj['ActionType'] = ActionType

        if GenerateASSet != None :
            obj['GenerateASSet'] = True if GenerateASSet else False

        if SendSummaryOnly != None :
            obj['SendSummaryOnly'] = True if SendSummaryOnly else False

        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyActionById(self,
                                   objectId,
                                   ActionType = None,
                                   GenerateASSet = None,
                                   SendSummaryOnly = None):
        obj =  {'objectId': objectId }
        if ActionType !=  None:
            obj['ActionType'] = ActionType

        if GenerateASSet !=  None:
            obj['GenerateASSet'] = GenerateASSet

        if SendSummaryOnly !=  None:
            obj['SendSummaryOnly'] = SendSummaryOnly

        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyAction(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyAction(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyActions(self):
        return self.getObjects( 'BGPPolicyAction') 


    @processReturnCode
    def createPolicyStmt(self,
                         Name,
                         MatchConditions,
                         Conditions,
                         Actions):
        obj =  { 
                'Name' : Name,
                'MatchConditions' : MatchConditions,
                'Conditions' : Conditions,
                'Actions' : Actions,
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyStmt(self,
                         Name,
                         MatchConditions = None,
                         Conditions = None,
                         Actions = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if MatchConditions != None :
            obj['MatchConditions'] = MatchConditions

        if Conditions != None :
            obj['Conditions'] = Conditions

        if Actions != None :
            obj['Actions'] = Actions

        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyStmtById(self,
                              objectId,
                              MatchConditions = None,
                              Conditions = None,
                              Actions = None):
        obj =  {'objectId': objectId }
        if MatchConditions !=  None:
            obj['MatchConditions'] = MatchConditions

        if Conditions !=  None:
            obj['Conditions'] = Conditions

        if Actions !=  None:
            obj['Actions'] = Actions

        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getPolicyStmt(self,
                      Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyStmts(self):
        return self.getObjects( 'PolicyStmt') 


    @processReturnCode
    def getRouteDistanceState(self,
                              Protocol):
        obj =  { 
                'Protocol' : Protocol,
                }
        reqUrl =  self.urlBase+'RouteDistanceState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getRouteDistanceStateById(self, objectId ):
        reqUrl =  self.urlBase+'RouteDistanceState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllRouteDistanceStates(self):
        return self.getObjects( 'RouteDistanceState') 


    @processReturnCode
    def getIPv4EventState(self,
                          Index):
        obj =  { 
                'Index' : Index,
                }
        reqUrl =  self.urlBase+'IPv4EventState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getIPv4EventStateById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4EventState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4EventStates(self):
        return self.getObjects( 'IPv4EventState') 


    @processReturnCode
    def createLogicalIntf(self,
                          Name,
                          Type):
        obj =  { 
                'Name' : Name,
                'Type' : Type,
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateLogicalIntf(self,
                          Name,
                          Type = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Type != None :
            obj['Type'] = Type

        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateLogicalIntfById(self,
                               objectId,
                               Type = None):
        obj =  {'objectId': objectId }
        if Type !=  None:
            obj['Type'] = Type

        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteLogicalIntf(self,
                          Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteLogicalIntfById(self, objectId ):
        reqUrl =  self.urlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getLogicalIntf(self,
                       Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getLogicalIntfById(self, objectId ):
        reqUrl =  self.urlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLogicalIntfs(self):
        return self.getObjects( 'LogicalIntf') 


    @processReturnCode
    def getOspfGlobalState(self,
                           RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.urlBase+'OspfGlobalState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfGlobalStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfGlobalState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfGlobalStates(self):
        return self.getObjects( 'OspfGlobalState') 


    @processReturnCode
    def createStpPort(self,
                      BrgIfIndex,
                      IfIndex,
                      Priority,
                      Enable,
                      PathCost,
                      PathCost32,
                      ProtocolMigration,
                      AdminPointToPoint,
                      AdminEdgePort,
                      AdminPathCost,
                      BpduGuard,
                      BpduGuardInterval,
                      BridgeAssurance):
        obj =  { 
                'BrgIfIndex' : int(BrgIfIndex),
                'IfIndex' : int(IfIndex),
                'Priority' : int(Priority),
                'Enable' : int(Enable),
                'PathCost' : int(PathCost),
                'PathCost32' : int(PathCost32),
                'ProtocolMigration' : int(ProtocolMigration),
                'AdminPointToPoint' : int(AdminPointToPoint),
                'AdminEdgePort' : int(AdminEdgePort),
                'AdminPathCost' : int(AdminPathCost),
                'BpduGuard' : int(BpduGuard),
                'BpduGuardInterval' : int(BpduGuardInterval),
                'BridgeAssurance' : int(BridgeAssurance),
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateStpPort(self,
                      BrgIfIndex,
                      IfIndex,
                      Priority = None,
                      Enable = None,
                      PathCost = None,
                      PathCost32 = None,
                      ProtocolMigration = None,
                      AdminPointToPoint = None,
                      AdminEdgePort = None,
                      AdminPathCost = None,
                      BpduGuard = None,
                      BpduGuardInterval = None,
                      BridgeAssurance = None):
        obj =  {}
        if BrgIfIndex != None :
            obj['BrgIfIndex'] = int(BrgIfIndex)

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if Priority != None :
            obj['Priority'] = int(Priority)

        if Enable != None :
            obj['Enable'] = int(Enable)

        if PathCost != None :
            obj['PathCost'] = int(PathCost)

        if PathCost32 != None :
            obj['PathCost32'] = int(PathCost32)

        if ProtocolMigration != None :
            obj['ProtocolMigration'] = int(ProtocolMigration)

        if AdminPointToPoint != None :
            obj['AdminPointToPoint'] = int(AdminPointToPoint)

        if AdminEdgePort != None :
            obj['AdminEdgePort'] = int(AdminEdgePort)

        if AdminPathCost != None :
            obj['AdminPathCost'] = int(AdminPathCost)

        if BpduGuard != None :
            obj['BpduGuard'] = int(BpduGuard)

        if BpduGuardInterval != None :
            obj['BpduGuardInterval'] = int(BpduGuardInterval)

        if BridgeAssurance != None :
            obj['BridgeAssurance'] = int(BridgeAssurance)

        reqUrl =  self.urlBase+'StpPort'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateStpPortById(self,
                           objectId,
                           Priority = None,
                           Enable = None,
                           PathCost = None,
                           PathCost32 = None,
                           ProtocolMigration = None,
                           AdminPointToPoint = None,
                           AdminEdgePort = None,
                           AdminPathCost = None,
                           BpduGuard = None,
                           BpduGuardInterval = None,
                           BridgeAssurance = None):
        obj =  {'objectId': objectId }
        if Priority !=  None:
            obj['Priority'] = Priority

        if Enable !=  None:
            obj['Enable'] = Enable

        if PathCost !=  None:
            obj['PathCost'] = PathCost

        if PathCost32 !=  None:
            obj['PathCost32'] = PathCost32

        if ProtocolMigration !=  None:
            obj['ProtocolMigration'] = ProtocolMigration

        if AdminPointToPoint !=  None:
            obj['AdminPointToPoint'] = AdminPointToPoint

        if AdminEdgePort !=  None:
            obj['AdminEdgePort'] = AdminEdgePort

        if AdminPathCost !=  None:
            obj['AdminPathCost'] = AdminPathCost

        if BpduGuard !=  None:
            obj['BpduGuard'] = BpduGuard

        if BpduGuardInterval !=  None:
            obj['BpduGuardInterval'] = BpduGuardInterval

        if BridgeAssurance !=  None:
            obj['BridgeAssurance'] = BridgeAssurance

        reqUrl =  self.urlBase+'StpPort'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteStpPort(self,
                      BrgIfIndex,
                      IfIndex):
        obj =  { 
                'BrgIfIndex' : BrgIfIndex,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteStpPortById(self, objectId ):
        reqUrl =  self.urlBase+'StpPort'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getStpPort(self,
                   BrgIfIndex,
                   IfIndex):
        obj =  { 
                'BrgIfIndex' : BrgIfIndex,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getStpPortById(self, objectId ):
        reqUrl =  self.urlBase+'StpPort'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpPorts(self):
        return self.getObjects( 'StpPort') 


    @processReturnCode
    def getOspfNbrEntryState(self,
                             NbrIpAddr,
                             NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr,
                'NbrAddressLessIndex' : NbrAddressLessIndex,
                }
        reqUrl =  self.urlBase+'OspfNbrEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfNbrEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfNbrEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfNbrEntryStates(self):
        return self.getObjects( 'OspfNbrEntryState') 


    @processReturnCode
    def getBfdInterfaceState(self,
                             IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'BfdInterfaceState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBfdInterfaceStateById(self, objectId ):
        reqUrl =  self.urlBase+'BfdInterfaceState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdInterfaceStates(self):
        return self.getObjects( 'BfdInterfaceState') 


    @processReturnCode
    def getBGPPolicyStmtState(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyStmtState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyStmtStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyStmtState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyStmtStates(self):
        return self.getObjects( 'BGPPolicyStmtState') 


    @processReturnCode
    def createBfdGlobal(self,
                        Bfd,
                        Enable=True):
        obj =  { 
                'Bfd' : Bfd,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBfdGlobal(self,
                        Bfd,
                        Enable = None):
        obj =  {}
        if Bfd != None :
            obj['Bfd'] = Bfd

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBfdGlobalById(self,
                             objectId,
                             Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBfdGlobal(self,
                        Bfd):
        obj =  { 
                'Bfd' : Bfd,
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBfdGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBfdGlobal(self,
                     Bfd):
        obj =  { 
                'Bfd' : Bfd,
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBfdGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdGlobals(self):
        return self.getObjects( 'BfdGlobal') 


    @processReturnCode
    def getLaPortChannelState(self,
                              LagId):
        obj =  { 
                'LagId' : LagId,
                }
        reqUrl =  self.urlBase+'LaPortChannelState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getLaPortChannelStateById(self, objectId ):
        reqUrl =  self.urlBase+'LaPortChannelState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLaPortChannelStates(self):
        return self.getObjects( 'LaPortChannelState') 


    @processReturnCode
    def createBGPGlobal(self,
                        RouterId,
                        ASNum,
                        EBGPMaxPaths=0,
                        EBGPAllowMultipleAS=False,
                        IBGPMaxPaths=0,
                        UseMultiplePaths=False):
        obj =  { 
                'RouterId' : RouterId,
                'ASNum' : int(ASNum),
                'EBGPMaxPaths' : int(EBGPMaxPaths),
                'EBGPAllowMultipleAS' : True if EBGPAllowMultipleAS else False,
                'IBGPMaxPaths' : int(IBGPMaxPaths),
                'UseMultiplePaths' : True if UseMultiplePaths else False,
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPGlobal(self,
                        RouterId,
                        ASNum = None,
                        EBGPMaxPaths = None,
                        EBGPAllowMultipleAS = None,
                        IBGPMaxPaths = None,
                        UseMultiplePaths = None):
        obj =  {}
        if RouterId != None :
            obj['RouterId'] = RouterId

        if ASNum != None :
            obj['ASNum'] = int(ASNum)

        if EBGPMaxPaths != None :
            obj['EBGPMaxPaths'] = int(EBGPMaxPaths)

        if EBGPAllowMultipleAS != None :
            obj['EBGPAllowMultipleAS'] = True if EBGPAllowMultipleAS else False

        if IBGPMaxPaths != None :
            obj['IBGPMaxPaths'] = int(IBGPMaxPaths)

        if UseMultiplePaths != None :
            obj['UseMultiplePaths'] = True if UseMultiplePaths else False

        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPGlobalById(self,
                             objectId,
                             ASNum = None,
                             EBGPMaxPaths = None,
                             EBGPAllowMultipleAS = None,
                             IBGPMaxPaths = None,
                             UseMultiplePaths = None):
        obj =  {'objectId': objectId }
        if ASNum !=  None:
            obj['ASNum'] = ASNum

        if EBGPMaxPaths !=  None:
            obj['EBGPMaxPaths'] = EBGPMaxPaths

        if EBGPAllowMultipleAS !=  None:
            obj['EBGPAllowMultipleAS'] = EBGPAllowMultipleAS

        if IBGPMaxPaths !=  None:
            obj['IBGPMaxPaths'] = IBGPMaxPaths

        if UseMultiplePaths !=  None:
            obj['UseMultiplePaths'] = UseMultiplePaths

        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPGlobal(self,
                        RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPGlobal(self,
                     RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPGlobals(self):
        return self.getObjects( 'BGPGlobal') 


    @processReturnCode
    def createOspfIfEntryConfig(self,
                                IfIpAddress,
                                AddressLessIf,
                                IfAreaId,
                                IfType,
                                IfAdminStat,
                                IfRtrPriority,
                                IfTransitDelay,
                                IfRetransInterval,
                                IfHelloInterval,
                                IfRtrDeadInterval,
                                IfPollInterval,
                                IfAuthKey,
                                IfMulticastForwarding,
                                IfDemand,
                                IfAuthType):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                'IfAreaId' : IfAreaId,
                'IfType' : int(IfType),
                'IfAdminStat' : int(IfAdminStat),
                'IfRtrPriority' : int(IfRtrPriority),
                'IfTransitDelay' : int(IfTransitDelay),
                'IfRetransInterval' : int(IfRetransInterval),
                'IfHelloInterval' : int(IfHelloInterval),
                'IfRtrDeadInterval' : int(IfRtrDeadInterval),
                'IfPollInterval' : int(IfPollInterval),
                'IfAuthKey' : IfAuthKey,
                'IfMulticastForwarding' : int(IfMulticastForwarding),
                'IfDemand' : True if IfDemand else False,
                'IfAuthType' : int(IfAuthType),
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfIfEntryConfig(self,
                                IfIpAddress,
                                AddressLessIf,
                                IfAreaId = None,
                                IfType = None,
                                IfAdminStat = None,
                                IfRtrPriority = None,
                                IfTransitDelay = None,
                                IfRetransInterval = None,
                                IfHelloInterval = None,
                                IfRtrDeadInterval = None,
                                IfPollInterval = None,
                                IfAuthKey = None,
                                IfMulticastForwarding = None,
                                IfDemand = None,
                                IfAuthType = None):
        obj =  {}
        if IfIpAddress != None :
            obj['IfIpAddress'] = IfIpAddress

        if AddressLessIf != None :
            obj['AddressLessIf'] = int(AddressLessIf)

        if IfAreaId != None :
            obj['IfAreaId'] = IfAreaId

        if IfType != None :
            obj['IfType'] = int(IfType)

        if IfAdminStat != None :
            obj['IfAdminStat'] = int(IfAdminStat)

        if IfRtrPriority != None :
            obj['IfRtrPriority'] = int(IfRtrPriority)

        if IfTransitDelay != None :
            obj['IfTransitDelay'] = int(IfTransitDelay)

        if IfRetransInterval != None :
            obj['IfRetransInterval'] = int(IfRetransInterval)

        if IfHelloInterval != None :
            obj['IfHelloInterval'] = int(IfHelloInterval)

        if IfRtrDeadInterval != None :
            obj['IfRtrDeadInterval'] = int(IfRtrDeadInterval)

        if IfPollInterval != None :
            obj['IfPollInterval'] = int(IfPollInterval)

        if IfAuthKey != None :
            obj['IfAuthKey'] = IfAuthKey

        if IfMulticastForwarding != None :
            obj['IfMulticastForwarding'] = int(IfMulticastForwarding)

        if IfDemand != None :
            obj['IfDemand'] = True if IfDemand else False

        if IfAuthType != None :
            obj['IfAuthType'] = int(IfAuthType)

        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfIfEntryConfigById(self,
                                     objectId,
                                     IfAreaId = None,
                                     IfType = None,
                                     IfAdminStat = None,
                                     IfRtrPriority = None,
                                     IfTransitDelay = None,
                                     IfRetransInterval = None,
                                     IfHelloInterval = None,
                                     IfRtrDeadInterval = None,
                                     IfPollInterval = None,
                                     IfAuthKey = None,
                                     IfMulticastForwarding = None,
                                     IfDemand = None,
                                     IfAuthType = None):
        obj =  {'objectId': objectId }
        if IfAreaId !=  None:
            obj['IfAreaId'] = IfAreaId

        if IfType !=  None:
            obj['IfType'] = IfType

        if IfAdminStat !=  None:
            obj['IfAdminStat'] = IfAdminStat

        if IfRtrPriority !=  None:
            obj['IfRtrPriority'] = IfRtrPriority

        if IfTransitDelay !=  None:
            obj['IfTransitDelay'] = IfTransitDelay

        if IfRetransInterval !=  None:
            obj['IfRetransInterval'] = IfRetransInterval

        if IfHelloInterval !=  None:
            obj['IfHelloInterval'] = IfHelloInterval

        if IfRtrDeadInterval !=  None:
            obj['IfRtrDeadInterval'] = IfRtrDeadInterval

        if IfPollInterval !=  None:
            obj['IfPollInterval'] = IfPollInterval

        if IfAuthKey !=  None:
            obj['IfAuthKey'] = IfAuthKey

        if IfMulticastForwarding !=  None:
            obj['IfMulticastForwarding'] = IfMulticastForwarding

        if IfDemand !=  None:
            obj['IfDemand'] = IfDemand

        if IfAuthType !=  None:
            obj['IfAuthType'] = IfAuthType

        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfIfEntryConfig(self,
                                IfIpAddress,
                                AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : AddressLessIf,
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfIfEntryConfig(self,
                             IfIpAddress,
                             AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : AddressLessIf,
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIfEntryConfigs(self):
        return self.getObjects( 'OspfIfEntryConfig') 


    @processReturnCode
    def getOspfAreaEntryState(self,
                              AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.urlBase+'OspfAreaEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaEntryStates(self):
        return self.getObjects( 'OspfAreaEntryState') 


    @processReturnCode
    def getOspfAreaLsaCountEntryState(self,
                                      AreaLsaCountAreaId,
                                      AreaLsaCountLsaType):
        obj =  { 
                'AreaLsaCountAreaId' : AreaLsaCountAreaId,
                'AreaLsaCountLsaType' : AreaLsaCountLsaType,
                }
        reqUrl =  self.urlBase+'OspfAreaLsaCountEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfAreaLsaCountEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaLsaCountEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaLsaCountEntryStates(self):
        return self.getObjects( 'OspfAreaLsaCountEntryState') 


    @processReturnCode
    def getPortState(self,
                     PortNum):
        obj =  { 
                'PortNum' : PortNum,
                }
        reqUrl =  self.urlBase+'PortState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPortStateById(self, objectId ):
        reqUrl =  self.urlBase+'PortState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPortStates(self):
        return self.getObjects( 'PortState') 


    @processReturnCode
    def createDhcpRelayIntf(self,
                            IfIndex,
                            Enable,
                            ServerIp):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'Enable' : True if Enable else False,
                'ServerIp' : ServerIp,
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateDhcpRelayIntf(self,
                            IfIndex,
                            Enable = None,
                            ServerIp = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if Enable != None :
            obj['Enable'] = True if Enable else False

        if ServerIp != None :
            obj['ServerIp'] = ServerIp

        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateDhcpRelayIntfById(self,
                                 objectId,
                                 Enable = None,
                                 ServerIp = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        if ServerIp !=  None:
            obj['ServerIp'] = ServerIp

        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteDhcpRelayIntf(self,
                            IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayIntf(self,
                         IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayIntfs(self):
        return self.getObjects( 'DhcpRelayIntf') 


    @processReturnCode
    def createOspfHostEntryConfig(self,
                                  HostTOS,
                                  HostIpAddress,
                                  HostMetric,
                                  HostCfgAreaID):
        obj =  { 
                'HostTOS' : int(HostTOS),
                'HostIpAddress' : HostIpAddress,
                'HostMetric' : int(HostMetric),
                'HostCfgAreaID' : HostCfgAreaID,
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfHostEntryConfig(self,
                                  HostTOS,
                                  HostIpAddress,
                                  HostMetric = None,
                                  HostCfgAreaID = None):
        obj =  {}
        if HostTOS != None :
            obj['HostTOS'] = int(HostTOS)

        if HostIpAddress != None :
            obj['HostIpAddress'] = HostIpAddress

        if HostMetric != None :
            obj['HostMetric'] = int(HostMetric)

        if HostCfgAreaID != None :
            obj['HostCfgAreaID'] = HostCfgAreaID

        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfHostEntryConfigById(self,
                                       objectId,
                                       HostMetric = None,
                                       HostCfgAreaID = None):
        obj =  {'objectId': objectId }
        if HostMetric !=  None:
            obj['HostMetric'] = HostMetric

        if HostCfgAreaID !=  None:
            obj['HostCfgAreaID'] = HostCfgAreaID

        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfHostEntryConfig(self,
                                  HostTOS,
                                  HostIpAddress):
        obj =  { 
                'HostTOS' : HostTOS,
                'HostIpAddress' : HostIpAddress,
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfHostEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfHostEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfHostEntryConfig(self,
                               HostTOS,
                               HostIpAddress):
        obj =  { 
                'HostTOS' : HostTOS,
                'HostIpAddress' : HostIpAddress,
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfHostEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfHostEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfHostEntryConfigs(self):
        return self.getObjects( 'OspfHostEntryConfig') 


    @processReturnCode
    def getPolicyConditionState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyConditionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyConditionStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyConditionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyConditionStates(self):
        return self.getObjects( 'PolicyConditionState') 


    @processReturnCode
    def createBGPPolicyStmt(self,
                            Name,
                            MatchConditions,
                            Conditions,
                            Actions):
        obj =  { 
                'Name' : Name,
                'MatchConditions' : MatchConditions,
                'Conditions' : Conditions,
                'Actions' : Actions,
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyStmt(self,
                            Name,
                            MatchConditions = None,
                            Conditions = None,
                            Actions = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if MatchConditions != None :
            obj['MatchConditions'] = MatchConditions

        if Conditions != None :
            obj['Conditions'] = Conditions

        if Actions != None :
            obj['Actions'] = Actions

        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPPolicyStmtById(self,
                                 objectId,
                                 MatchConditions = None,
                                 Conditions = None,
                                 Actions = None):
        obj =  {'objectId': objectId }
        if MatchConditions !=  None:
            obj['MatchConditions'] = MatchConditions

        if Conditions !=  None:
            obj['Conditions'] = Conditions

        if Actions !=  None:
            obj['Actions'] = Actions

        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyStmt(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyStmts(self):
        return self.getObjects( 'BGPPolicyStmt') 


    @processReturnCode
    def createOspfVirtIfEntryConfig(self,
                                    VirtIfNeighbor,
                                    VirtIfAreaId,
                                    VirtIfTransitDelay,
                                    VirtIfRetransInterval,
                                    VirtIfHelloInterval,
                                    VirtIfRtrDeadInterval,
                                    VirtIfAuthKey,
                                    VirtIfAuthType):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                'VirtIfTransitDelay' : int(VirtIfTransitDelay),
                'VirtIfRetransInterval' : int(VirtIfRetransInterval),
                'VirtIfHelloInterval' : int(VirtIfHelloInterval),
                'VirtIfRtrDeadInterval' : int(VirtIfRtrDeadInterval),
                'VirtIfAuthKey' : VirtIfAuthKey,
                'VirtIfAuthType' : int(VirtIfAuthType),
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfVirtIfEntryConfig(self,
                                    VirtIfNeighbor,
                                    VirtIfAreaId,
                                    VirtIfTransitDelay = None,
                                    VirtIfRetransInterval = None,
                                    VirtIfHelloInterval = None,
                                    VirtIfRtrDeadInterval = None,
                                    VirtIfAuthKey = None,
                                    VirtIfAuthType = None):
        obj =  {}
        if VirtIfNeighbor != None :
            obj['VirtIfNeighbor'] = VirtIfNeighbor

        if VirtIfAreaId != None :
            obj['VirtIfAreaId'] = VirtIfAreaId

        if VirtIfTransitDelay != None :
            obj['VirtIfTransitDelay'] = int(VirtIfTransitDelay)

        if VirtIfRetransInterval != None :
            obj['VirtIfRetransInterval'] = int(VirtIfRetransInterval)

        if VirtIfHelloInterval != None :
            obj['VirtIfHelloInterval'] = int(VirtIfHelloInterval)

        if VirtIfRtrDeadInterval != None :
            obj['VirtIfRtrDeadInterval'] = int(VirtIfRtrDeadInterval)

        if VirtIfAuthKey != None :
            obj['VirtIfAuthKey'] = VirtIfAuthKey

        if VirtIfAuthType != None :
            obj['VirtIfAuthType'] = int(VirtIfAuthType)

        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfVirtIfEntryConfigById(self,
                                         objectId,
                                         VirtIfTransitDelay = None,
                                         VirtIfRetransInterval = None,
                                         VirtIfHelloInterval = None,
                                         VirtIfRtrDeadInterval = None,
                                         VirtIfAuthKey = None,
                                         VirtIfAuthType = None):
        obj =  {'objectId': objectId }
        if VirtIfTransitDelay !=  None:
            obj['VirtIfTransitDelay'] = VirtIfTransitDelay

        if VirtIfRetransInterval !=  None:
            obj['VirtIfRetransInterval'] = VirtIfRetransInterval

        if VirtIfHelloInterval !=  None:
            obj['VirtIfHelloInterval'] = VirtIfHelloInterval

        if VirtIfRtrDeadInterval !=  None:
            obj['VirtIfRtrDeadInterval'] = VirtIfRtrDeadInterval

        if VirtIfAuthKey !=  None:
            obj['VirtIfAuthKey'] = VirtIfAuthKey

        if VirtIfAuthType !=  None:
            obj['VirtIfAuthType'] = VirtIfAuthType

        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfVirtIfEntryConfig(self,
                                    VirtIfNeighbor,
                                    VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfVirtIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfVirtIfEntryConfig(self,
                                 VirtIfNeighbor,
                                 VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfVirtIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfVirtIfEntryConfigs(self):
        return self.getObjects( 'OspfVirtIfEntryConfig') 


    @processReturnCode
    def createOspfStubAreaEntryConfig(self,
                                      StubTOS,
                                      StubAreaId,
                                      StubMetric,
                                      StubMetricType):
        obj =  { 
                'StubTOS' : int(StubTOS),
                'StubAreaId' : StubAreaId,
                'StubMetric' : int(StubMetric),
                'StubMetricType' : int(StubMetricType),
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfStubAreaEntryConfig(self,
                                      StubTOS,
                                      StubAreaId,
                                      StubMetric = None,
                                      StubMetricType = None):
        obj =  {}
        if StubTOS != None :
            obj['StubTOS'] = int(StubTOS)

        if StubAreaId != None :
            obj['StubAreaId'] = StubAreaId

        if StubMetric != None :
            obj['StubMetric'] = int(StubMetric)

        if StubMetricType != None :
            obj['StubMetricType'] = int(StubMetricType)

        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateOspfStubAreaEntryConfigById(self,
                                           objectId,
                                           StubMetric = None,
                                           StubMetricType = None):
        obj =  {'objectId': objectId }
        if StubMetric !=  None:
            obj['StubMetric'] = StubMetric

        if StubMetricType !=  None:
            obj['StubMetricType'] = StubMetricType

        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfStubAreaEntryConfig(self,
                                      StubTOS,
                                      StubAreaId):
        obj =  { 
                'StubTOS' : StubTOS,
                'StubAreaId' : StubAreaId,
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteOspfStubAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getOspfStubAreaEntryConfig(self,
                                   StubTOS,
                                   StubAreaId):
        obj =  { 
                'StubTOS' : StubTOS,
                'StubAreaId' : StubAreaId,
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfStubAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfStubAreaEntryConfigs(self):
        return self.getObjects( 'OspfStubAreaEntryConfig') 


    @processReturnCode
    def getPolicyActionState(self,
                             Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyActionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyActionStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyActionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyActionStates(self):
        return self.getObjects( 'PolicyActionState') 


    @processReturnCode
    def createVrrpIntf(self,
                       VRID,
                       IfIndex,
                       VirtualIPv4Addr,
                       PreemptMode=True,
                       Priority=100,
                       AdvertisementInterval=1,
                       AcceptMode=False):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                'VirtualIPv4Addr' : VirtualIPv4Addr,
                'PreemptMode' : True if PreemptMode else False,
                'Priority' : int(Priority),
                'AdvertisementInterval' : int(AdvertisementInterval),
                'AcceptMode' : True if AcceptMode else False,
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVrrpIntf(self,
                       VRID,
                       IfIndex,
                       VirtualIPv4Addr = None,
                       PreemptMode = None,
                       Priority = None,
                       AdvertisementInterval = None,
                       AcceptMode = None):
        obj =  {}
        if VRID != None :
            obj['VRID'] = int(VRID)

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if VirtualIPv4Addr != None :
            obj['VirtualIPv4Addr'] = VirtualIPv4Addr

        if PreemptMode != None :
            obj['PreemptMode'] = True if PreemptMode else False

        if Priority != None :
            obj['Priority'] = int(Priority)

        if AdvertisementInterval != None :
            obj['AdvertisementInterval'] = int(AdvertisementInterval)

        if AcceptMode != None :
            obj['AcceptMode'] = True if AcceptMode else False

        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVrrpIntfById(self,
                            objectId,
                            VirtualIPv4Addr = None,
                            PreemptMode = None,
                            Priority = None,
                            AdvertisementInterval = None,
                            AcceptMode = None):
        obj =  {'objectId': objectId }
        if VirtualIPv4Addr !=  None:
            obj['VirtualIPv4Addr'] = VirtualIPv4Addr

        if PreemptMode !=  None:
            obj['PreemptMode'] = PreemptMode

        if Priority !=  None:
            obj['Priority'] = Priority

        if AdvertisementInterval !=  None:
            obj['AdvertisementInterval'] = AdvertisementInterval

        if AcceptMode !=  None:
            obj['AcceptMode'] = AcceptMode

        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVrrpIntf(self,
                       VRID,
                       IfIndex):
        obj =  { 
                'VRID' : VRID,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVrrpIntfById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getVrrpIntf(self,
                    VRID,
                    IfIndex):
        obj =  { 
                'VRID' : VRID,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVrrpIntfById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVrrpIntfs(self):
        return self.getObjects( 'VrrpIntf') 


    @processReturnCode
    def getBGPNeighborState(self,
                            IfIndex,
                            NeighborAddress):
        obj =  { 
                'IfIndex' : IfIndex,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.urlBase+'BGPNeighborState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPNeighborStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPNeighborState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPNeighborStates(self):
        return self.getObjects( 'BGPNeighborState') 


    @processReturnCode
    def createVxlanVtepInstances(self,
                                 VtepId,
                                 VxlanId,
                                 VtepName,
                                 SrcIfIndex,
                                 UDP,
                                 TTL,
                                 TOS,
                                 InnerVlanHandlingMode,
                                 Learning,
                                 Rsc,
                                 L2miss,
                                 L3miss,
                                 DstIp,
                                 DstMac,
                                 VlanId):
        obj =  { 
                'VtepId' : int(VtepId),
                'VxlanId' : int(VxlanId),
                'VtepName' : VtepName,
                'SrcIfIndex' : int(SrcIfIndex),
                'UDP' : UDP,
                'TTL' : TTL,
                'TOS' : TOS,
                'InnerVlanHandlingMode' : int(InnerVlanHandlingMode),
                'Learning' : int(Learning),
                'Rsc' : int(Rsc),
                'L2miss' : int(L2miss),
                'L3miss' : int(L3miss),
                'DstIp' : DstIp,
                'DstMac' : DstMac,
                'VlanId' : VlanId,
                }
        reqUrl =  self.urlBase+'VxlanVtepInstances'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVxlanVtepInstances(self,
                                 VtepId,
                                 VxlanId,
                                 VtepName = None,
                                 SrcIfIndex = None,
                                 UDP = None,
                                 TTL = None,
                                 TOS = None,
                                 InnerVlanHandlingMode = None,
                                 Learning = None,
                                 Rsc = None,
                                 L2miss = None,
                                 L3miss = None,
                                 DstIp = None,
                                 DstMac = None,
                                 VlanId = None):
        obj =  {}
        if VtepId != None :
            obj['VtepId'] = int(VtepId)

        if VxlanId != None :
            obj['VxlanId'] = int(VxlanId)

        if VtepName != None :
            obj['VtepName'] = VtepName

        if SrcIfIndex != None :
            obj['SrcIfIndex'] = int(SrcIfIndex)

        if UDP != None :
            obj['UDP'] = UDP

        if TTL != None :
            obj['TTL'] = TTL

        if TOS != None :
            obj['TOS'] = TOS

        if InnerVlanHandlingMode != None :
            obj['InnerVlanHandlingMode'] = int(InnerVlanHandlingMode)

        if Learning != None :
            obj['Learning'] = int(Learning)

        if Rsc != None :
            obj['Rsc'] = int(Rsc)

        if L2miss != None :
            obj['L2miss'] = int(L2miss)

        if L3miss != None :
            obj['L3miss'] = int(L3miss)

        if DstIp != None :
            obj['DstIp'] = DstIp

        if DstMac != None :
            obj['DstMac'] = DstMac

        if VlanId != None :
            obj['VlanId'] = VlanId

        reqUrl =  self.urlBase+'VxlanVtepInstances'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateVxlanVtepInstancesById(self,
                                      objectId,
                                      VtepName = None,
                                      SrcIfIndex = None,
                                      UDP = None,
                                      TTL = None,
                                      TOS = None,
                                      InnerVlanHandlingMode = None,
                                      Learning = None,
                                      Rsc = None,
                                      L2miss = None,
                                      L3miss = None,
                                      DstIp = None,
                                      DstMac = None,
                                      VlanId = None):
        obj =  {'objectId': objectId }
        if VtepName !=  None:
            obj['VtepName'] = VtepName

        if SrcIfIndex !=  None:
            obj['SrcIfIndex'] = SrcIfIndex

        if UDP !=  None:
            obj['UDP'] = UDP

        if TTL !=  None:
            obj['TTL'] = TTL

        if TOS !=  None:
            obj['TOS'] = TOS

        if InnerVlanHandlingMode !=  None:
            obj['InnerVlanHandlingMode'] = InnerVlanHandlingMode

        if Learning !=  None:
            obj['Learning'] = Learning

        if Rsc !=  None:
            obj['Rsc'] = Rsc

        if L2miss !=  None:
            obj['L2miss'] = L2miss

        if L3miss !=  None:
            obj['L3miss'] = L3miss

        if DstIp !=  None:
            obj['DstIp'] = DstIp

        if DstMac !=  None:
            obj['DstMac'] = DstMac

        if VlanId !=  None:
            obj['VlanId'] = VlanId

        reqUrl =  self.urlBase+'VxlanVtepInstances'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVxlanVtepInstances(self,
                                 VtepId,
                                 VxlanId):
        obj =  { 
                'VtepId' : VtepId,
                'VxlanId' : VxlanId,
                }
        reqUrl =  self.urlBase+'VxlanVtepInstances'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteVxlanVtepInstancesById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVtepInstances'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getVxlanVtepInstances(self,
                              VtepId,
                              VxlanId):
        obj =  { 
                'VtepId' : VtepId,
                'VxlanId' : VxlanId,
                }
        reqUrl =  self.urlBase+'VxlanVtepInstances'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVxlanVtepInstancesById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVtepInstances'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVxlanVtepInstancess(self):
        return self.getObjects( 'VxlanVtepInstances') 


    @processReturnCode
    def createBfdSession(self,
                         IpAddr,
                         Owner='user',
                         PerLink=False):
        obj =  { 
                'IpAddr' : IpAddr,
                'Owner' : Owner,
                'PerLink' : True if PerLink else False,
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBfdSession(self,
                         IpAddr,
                         Owner = None,
                         PerLink = None):
        obj =  {}
        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Owner != None :
            obj['Owner'] = Owner

        if PerLink != None :
            obj['PerLink'] = True if PerLink else False

        reqUrl =  self.urlBase+'BfdSession'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBfdSessionById(self,
                              objectId,
                              Owner = None,
                              PerLink = None):
        obj =  {'objectId': objectId }
        if Owner !=  None:
            obj['Owner'] = Owner

        if PerLink !=  None:
            obj['PerLink'] = PerLink

        reqUrl =  self.urlBase+'BfdSession'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBfdSession(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBfdSessionById(self, objectId ):
        reqUrl =  self.urlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBfdSession(self,
                      IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBfdSessionById(self, objectId ):
        reqUrl =  self.urlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdSessions(self):
        return self.getObjects( 'BfdSession') 


    @processReturnCode
    def createPolicyAction(self,
                           Name,
                           ActionType,
                           SetAdminDistanceValue,
                           Accept,
                           Reject,
                           RedistributeAction,
                           RedistributeTargetProtocol,
                           NetworkStatementTargetProtocol):
        obj =  { 
                'Name' : Name,
                'ActionType' : ActionType,
                'SetAdminDistanceValue' : int(SetAdminDistanceValue),
                'Accept' : True if Accept else False,
                'Reject' : True if Reject else False,
                'RedistributeAction' : RedistributeAction,
                'RedistributeTargetProtocol' : RedistributeTargetProtocol,
                'NetworkStatementTargetProtocol' : NetworkStatementTargetProtocol,
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyAction(self,
                           Name,
                           ActionType = None,
                           SetAdminDistanceValue = None,
                           Accept = None,
                           Reject = None,
                           RedistributeAction = None,
                           RedistributeTargetProtocol = None,
                           NetworkStatementTargetProtocol = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ActionType != None :
            obj['ActionType'] = ActionType

        if SetAdminDistanceValue != None :
            obj['SetAdminDistanceValue'] = int(SetAdminDistanceValue)

        if Accept != None :
            obj['Accept'] = True if Accept else False

        if Reject != None :
            obj['Reject'] = True if Reject else False

        if RedistributeAction != None :
            obj['RedistributeAction'] = RedistributeAction

        if RedistributeTargetProtocol != None :
            obj['RedistributeTargetProtocol'] = RedistributeTargetProtocol

        if NetworkStatementTargetProtocol != None :
            obj['NetworkStatementTargetProtocol'] = NetworkStatementTargetProtocol

        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyActionById(self,
                                objectId,
                                ActionType = None,
                                SetAdminDistanceValue = None,
                                Accept = None,
                                Reject = None,
                                RedistributeAction = None,
                                RedistributeTargetProtocol = None,
                                NetworkStatementTargetProtocol = None):
        obj =  {'objectId': objectId }
        if ActionType !=  None:
            obj['ActionType'] = ActionType

        if SetAdminDistanceValue !=  None:
            obj['SetAdminDistanceValue'] = SetAdminDistanceValue

        if Accept !=  None:
            obj['Accept'] = Accept

        if Reject !=  None:
            obj['Reject'] = Reject

        if RedistributeAction !=  None:
            obj['RedistributeAction'] = RedistributeAction

        if RedistributeTargetProtocol !=  None:
            obj['RedistributeTargetProtocol'] = RedistributeTargetProtocol

        if NetworkStatementTargetProtocol !=  None:
            obj['NetworkStatementTargetProtocol'] = NetworkStatementTargetProtocol

        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyAction(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getPolicyAction(self,
                        Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyAction'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyActions(self):
        return self.getObjects( 'PolicyAction') 


    @processReturnCode
    def getStpPortState(self,
                        BrgIfIndex,
                        IfIndex):
        obj =  { 
                'BrgIfIndex' : BrgIfIndex,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'StpPortState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getStpPortStateById(self, objectId ):
        reqUrl =  self.urlBase+'StpPortState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpPortStates(self):
        return self.getObjects( 'StpPortState') 


    @processReturnCode
    def getOspfIfEntryState(self,
                            IfIpAddress,
                            AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : AddressLessIf,
                }
        reqUrl =  self.urlBase+'OspfIfEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfIfEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIfEntryStates(self):
        return self.getObjects( 'OspfIfEntryState') 


    @processReturnCode
    def getIPv4RouteState(self,
                          DestinationNw,
                          NextHopIp):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NextHopIp' : NextHopIp,
                }
        reqUrl =  self.urlBase+'IPv4RouteState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getIPv4RouteStateById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4RouteState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4RouteStates(self):
        return self.getObjects( 'IPv4RouteState') 


    @processReturnCode
    def getVrrpVridState(self,
                         VRID,
                         IfIndex):
        obj =  { 
                'VRID' : VRID,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.urlBase+'VrrpVridState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getVrrpVridStateById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpVridState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVrrpVridStates(self):
        return self.getObjects( 'VrrpVridState') 


    @processReturnCode
    def createLaPortChannel(self,
                            LagId,
                            LagType,
                            MinLinks,
                            Interval,
                            LacpMode,
                            SystemIdMac,
                            SystemPriority,
                            LagHash,
                            AdminState,
                            Members):
        obj =  { 
                'LagId' : int(LagId),
                'LagType' : int(LagType),
                'MinLinks' : MinLinks,
                'Interval' : int(Interval),
                'LacpMode' : int(LacpMode),
                'SystemIdMac' : SystemIdMac,
                'SystemPriority' : SystemPriority,
                'LagHash' : int(LagHash),
                'AdminState' : AdminState,
                'Members' : Members,
                }
        reqUrl =  self.urlBase+'LaPortChannel'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateLaPortChannel(self,
                            LagId,
                            LagType = None,
                            MinLinks = None,
                            Interval = None,
                            LacpMode = None,
                            SystemIdMac = None,
                            SystemPriority = None,
                            LagHash = None,
                            AdminState = None,
                            Members = None):
        obj =  {}
        if LagId != None :
            obj['LagId'] = int(LagId)

        if LagType != None :
            obj['LagType'] = int(LagType)

        if MinLinks != None :
            obj['MinLinks'] = MinLinks

        if Interval != None :
            obj['Interval'] = int(Interval)

        if LacpMode != None :
            obj['LacpMode'] = int(LacpMode)

        if SystemIdMac != None :
            obj['SystemIdMac'] = SystemIdMac

        if SystemPriority != None :
            obj['SystemPriority'] = SystemPriority

        if LagHash != None :
            obj['LagHash'] = int(LagHash)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if Members != None :
            obj['Members'] = Members

        reqUrl =  self.urlBase+'LaPortChannel'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateLaPortChannelById(self,
                                 objectId,
                                 LagType = None,
                                 MinLinks = None,
                                 Interval = None,
                                 LacpMode = None,
                                 SystemIdMac = None,
                                 SystemPriority = None,
                                 LagHash = None,
                                 AdminState = None,
                                 Members = None):
        obj =  {'objectId': objectId }
        if LagType !=  None:
            obj['LagType'] = LagType

        if MinLinks !=  None:
            obj['MinLinks'] = MinLinks

        if Interval !=  None:
            obj['Interval'] = Interval

        if LacpMode !=  None:
            obj['LacpMode'] = LacpMode

        if SystemIdMac !=  None:
            obj['SystemIdMac'] = SystemIdMac

        if SystemPriority !=  None:
            obj['SystemPriority'] = SystemPriority

        if LagHash !=  None:
            obj['LagHash'] = LagHash

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if Members !=  None:
            obj['Members'] = Members

        reqUrl =  self.urlBase+'LaPortChannel'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteLaPortChannel(self,
                            LagId):
        obj =  { 
                'LagId' : LagId,
                }
        reqUrl =  self.urlBase+'LaPortChannel'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteLaPortChannelById(self, objectId ):
        reqUrl =  self.urlBase+'LaPortChannel'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getLaPortChannel(self,
                         LagId):
        obj =  { 
                'LagId' : LagId,
                }
        reqUrl =  self.urlBase+'LaPortChannel'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getLaPortChannelById(self, objectId ):
        reqUrl =  self.urlBase+'LaPortChannel'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLaPortChannels(self):
        return self.getObjects( 'LaPortChannel') 


    @processReturnCode
    def createSubIPv4Intf(self,
                          IfIndex,
                          IpAddr,
                          Type,
                          MacAddr,
                          Enable=False):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'IpAddr' : IpAddr,
                'Type' : Type,
                'MacAddr' : MacAddr,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.urlBase+'SubIPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateSubIPv4Intf(self,
                          IfIndex,
                          IpAddr,
                          Type = None,
                          MacAddr = None,
                          Enable = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Type != None :
            obj['Type'] = Type

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.urlBase+'SubIPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateSubIPv4IntfById(self,
                               objectId,
                               Type = None,
                               MacAddr = None,
                               Enable = None):
        obj =  {'objectId': objectId }
        if Type !=  None:
            obj['Type'] = Type

        if MacAddr !=  None:
            obj['MacAddr'] = MacAddr

        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.urlBase+'SubIPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteSubIPv4Intf(self,
                          IfIndex,
                          IpAddr):
        obj =  { 
                'IfIndex' : IfIndex,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'SubIPv4Intf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteSubIPv4IntfById(self, objectId ):
        reqUrl =  self.urlBase+'SubIPv4Intf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getSubIPv4Intf(self,
                       IfIndex,
                       IpAddr):
        obj =  { 
                'IfIndex' : IfIndex,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'SubIPv4Intf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getSubIPv4IntfById(self, objectId ):
        reqUrl =  self.urlBase+'SubIPv4Intf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSubIPv4Intfs(self):
        return self.getObjects( 'SubIPv4Intf') 


    @processReturnCode
    def getPolicyDefinitionState(self,
                                 Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyDefinitionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyDefinitionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyDefinitionStates(self):
        return self.getObjects( 'PolicyDefinitionState') 


    @processReturnCode
    def getBfdGlobalState(self,
                          Bfd):
        obj =  { 
                'Bfd' : Bfd,
                }
        reqUrl =  self.urlBase+'BfdGlobalState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBfdGlobalStateById(self, objectId ):
        reqUrl =  self.urlBase+'BfdGlobalState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdGlobalStates(self):
        return self.getObjects( 'BfdGlobalState') 


    @processReturnCode
    def getOspfVirtLocalLsdbEntryState(self,
                                       VirtLocalLsdbLsid,
                                       VirtLocalLsdbType,
                                       VirtLocalLsdbNeighbor,
                                       VirtLocalLsdbRouterId,
                                       VirtLocalLsdbTransitArea):
        obj =  { 
                'VirtLocalLsdbLsid' : VirtLocalLsdbLsid,
                'VirtLocalLsdbType' : VirtLocalLsdbType,
                'VirtLocalLsdbNeighbor' : VirtLocalLsdbNeighbor,
                'VirtLocalLsdbRouterId' : VirtLocalLsdbRouterId,
                'VirtLocalLsdbTransitArea' : VirtLocalLsdbTransitArea,
                }
        reqUrl =  self.urlBase+'OspfVirtLocalLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getOspfVirtLocalLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtLocalLsdbEntryState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfVirtLocalLsdbEntryStates(self):
        return self.getObjects( 'OspfVirtLocalLsdbEntryState') 


    @processReturnCode
    def getBGPPolicyConditionState(self,
                                   Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyConditionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyConditionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyConditionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyConditionStates(self):
        return self.getObjects( 'BGPPolicyConditionState') 


    @processReturnCode
    def getArpEntry(self,
                    IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.urlBase+'ArpEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getArpEntryById(self, objectId ):
        reqUrl =  self.urlBase+'ArpEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpEntrys(self):
        return self.getObjects( 'ArpEntry') 


    @processReturnCode
    def getBGPRoute(self,
                    Network,
                    NextHop,
                    CIDRLen):
        obj =  { 
                'Network' : Network,
                'NextHop' : NextHop,
                'CIDRLen' : CIDRLen,
                }
        reqUrl =  self.urlBase+'BGPRoute'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPRouteById(self, objectId ):
        reqUrl =  self.urlBase+'BGPRoute'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPRoutes(self):
        return self.getObjects( 'BGPRoute') 


    @processReturnCode
    def getBGPPolicyDefinitionState(self,
                                    Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinitionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyDefinitionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyDefinitionStates(self):
        return self.getObjects( 'BGPPolicyDefinitionState') 


    @processReturnCode
    def getBfdSessionState(self,
                           SessionId):
        obj =  { 
                'SessionId' : SessionId,
                }
        reqUrl =  self.urlBase+'BfdSessionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBfdSessionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BfdSessionState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdSessionStates(self):
        return self.getObjects( 'BfdSessionState') 


    @processReturnCode
    def getLogicalIntfState(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'LogicalIntfState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getLogicalIntfStateById(self, objectId ):
        reqUrl =  self.urlBase+'LogicalIntfState'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLogicalIntfStates(self):
        return self.getObjects( 'LogicalIntfState') 


    @processReturnCode
    def createPolicyCondition(self,
                              Name,
                              ConditionType,
                              MatchProtocol,
                              IpPrefix,
                              MaskLengthRange):
        obj =  { 
                'Name' : Name,
                'ConditionType' : ConditionType,
                'MatchProtocol' : MatchProtocol,
                'IpPrefix' : IpPrefix,
                'MaskLengthRange' : MaskLengthRange,
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyCondition(self,
                              Name,
                              ConditionType = None,
                              MatchProtocol = None,
                              IpPrefix = None,
                              MaskLengthRange = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ConditionType != None :
            obj['ConditionType'] = ConditionType

        if MatchProtocol != None :
            obj['MatchProtocol'] = MatchProtocol

        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange != None :
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePolicyConditionById(self,
                                   objectId,
                                   ConditionType = None,
                                   MatchProtocol = None,
                                   IpPrefix = None,
                                   MaskLengthRange = None):
        obj =  {'objectId': objectId }
        if ConditionType !=  None:
            obj['ConditionType'] = ConditionType

        if MatchProtocol !=  None:
            obj['MatchProtocol'] = MatchProtocol

        if IpPrefix !=  None:
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange !=  None:
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getPolicyCondition(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyConditions(self):
        return self.getObjects( 'PolicyCondition') 


    @processReturnCode
    def createPort(self,
                   PortNum,
                   PhyIntfType,
                   AdminState,
                   MacAddr,
                   Speed,
                   Duplex,
                   Autoneg,
                   MediaType,
                   Mtu,
                   Description='FP Port'):
        obj =  { 
                'PortNum' : int(PortNum),
                'PhyIntfType' : PhyIntfType,
                'AdminState' : AdminState,
                'MacAddr' : MacAddr,
                'Speed' : int(Speed),
                'Duplex' : Duplex,
                'Autoneg' : Autoneg,
                'MediaType' : MediaType,
                'Mtu' : int(Mtu),
                'Description' : Description,
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePort(self,
                   PortNum,
                   PhyIntfType = None,
                   AdminState = None,
                   MacAddr = None,
                   Speed = None,
                   Duplex = None,
                   Autoneg = None,
                   MediaType = None,
                   Mtu = None,
                   Description = None):
        obj =  {}
        if PortNum != None :
            obj['PortNum'] = int(PortNum)

        if PhyIntfType != None :
            obj['PhyIntfType'] = PhyIntfType

        if AdminState != None :
            obj['AdminState'] = AdminState

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Speed != None :
            obj['Speed'] = int(Speed)

        if Duplex != None :
            obj['Duplex'] = Duplex

        if Autoneg != None :
            obj['Autoneg'] = Autoneg

        if MediaType != None :
            obj['MediaType'] = MediaType

        if Mtu != None :
            obj['Mtu'] = int(Mtu)

        if Description != None :
            obj['Description'] = Description

        reqUrl =  self.urlBase+'Port'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updatePortById(self,
                        objectId,
                        PhyIntfType = None,
                        AdminState = None,
                        MacAddr = None,
                        Speed = None,
                        Duplex = None,
                        Autoneg = None,
                        MediaType = None,
                        Mtu = None,
                        Description = None):
        obj =  {'objectId': objectId }
        if PhyIntfType !=  None:
            obj['PhyIntfType'] = PhyIntfType

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if MacAddr !=  None:
            obj['MacAddr'] = MacAddr

        if Speed !=  None:
            obj['Speed'] = Speed

        if Duplex !=  None:
            obj['Duplex'] = Duplex

        if Autoneg !=  None:
            obj['Autoneg'] = Autoneg

        if MediaType !=  None:
            obj['MediaType'] = MediaType

        if Mtu !=  None:
            obj['Mtu'] = Mtu

        if Description !=  None:
            obj['Description'] = Description

        reqUrl =  self.urlBase+'Port'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePort(self,
                   PortNum):
        obj =  { 
                'PortNum' : PortNum,
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deletePortById(self, objectId ):
        reqUrl =  self.urlBase+'Port'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getPort(self,
                PortNum):
        obj =  { 
                'PortNum' : PortNum,
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getPortById(self, objectId ):
        reqUrl =  self.urlBase+'Port'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPorts(self):
        return self.getObjects( 'Port') 


    @processReturnCode
    def createBGPNeighbor(self,
                          IfIndex,
                          NeighborAddress,
                          PeerAS,
                          BfdEnable=False,
                          RouteReflectorClusterId=0,
                          PeerGroup='',
                          Description='',
                          MultiHopTTL=0,
                          LocalAS=0,
                          KeepaliveTime=60,
                          AddPathsMaxTx=0,
                          MultiHopEnable=False,
                          RouteReflectorClient=False,
                          AddPathsRx=False,
                          HoldTime=180,
                          AuthPassword='',
                          ConnectRetryTime=60):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'NeighborAddress' : NeighborAddress,
                'PeerAS' : int(PeerAS),
                'BfdEnable' : True if BfdEnable else False,
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'PeerGroup' : PeerGroup,
                'Description' : Description,
                'MultiHopTTL' : int(MultiHopTTL),
                'LocalAS' : int(LocalAS),
                'KeepaliveTime' : int(KeepaliveTime),
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'AddPathsRx' : True if AddPathsRx else False,
                'HoldTime' : int(HoldTime),
                'AuthPassword' : AuthPassword,
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPNeighbor(self,
                          IfIndex,
                          NeighborAddress,
                          PeerAS = None,
                          BfdEnable = None,
                          RouteReflectorClusterId = None,
                          PeerGroup = None,
                          Description = None,
                          MultiHopTTL = None,
                          LocalAS = None,
                          KeepaliveTime = None,
                          AddPathsMaxTx = None,
                          MultiHopEnable = None,
                          RouteReflectorClient = None,
                          AddPathsRx = None,
                          HoldTime = None,
                          AuthPassword = None,
                          ConnectRetryTime = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if NeighborAddress != None :
            obj['NeighborAddress'] = NeighborAddress

        if PeerAS != None :
            obj['PeerAS'] = int(PeerAS)

        if BfdEnable != None :
            obj['BfdEnable'] = True if BfdEnable else False

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if PeerGroup != None :
            obj['PeerGroup'] = PeerGroup

        if Description != None :
            obj['Description'] = Description

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if LocalAS != None :
            obj['LocalAS'] = int(LocalAS)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if AuthPassword != None :
            obj['AuthPassword'] = AuthPassword

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateBGPNeighborById(self,
                               objectId,
                               PeerAS = None,
                               BfdEnable = None,
                               RouteReflectorClusterId = None,
                               PeerGroup = None,
                               Description = None,
                               MultiHopTTL = None,
                               LocalAS = None,
                               KeepaliveTime = None,
                               AddPathsMaxTx = None,
                               MultiHopEnable = None,
                               RouteReflectorClient = None,
                               AddPathsRx = None,
                               HoldTime = None,
                               AuthPassword = None,
                               ConnectRetryTime = None):
        obj =  {'objectId': objectId }
        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if BfdEnable !=  None:
            obj['BfdEnable'] = BfdEnable

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if PeerGroup !=  None:
            obj['PeerGroup'] = PeerGroup

        if Description !=  None:
            obj['Description'] = Description

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if AuthPassword !=  None:
            obj['AuthPassword'] = AuthPassword

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPNeighbor(self,
                          IfIndex,
                          NeighborAddress):
        obj =  { 
                'IfIndex' : IfIndex,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteBGPNeighborById(self, objectId ):
        reqUrl =  self.urlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getBGPNeighbor(self,
                       IfIndex,
                       NeighborAddress):
        obj =  { 
                'IfIndex' : IfIndex,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getBGPNeighborById(self, objectId ):
        reqUrl =  self.urlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPNeighbors(self):
        return self.getObjects( 'BGPNeighbor') 

