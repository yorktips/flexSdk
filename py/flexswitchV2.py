!/usr/bin/python                                                                                                       
import requests                                                                                                         
import json                                                                                                             
import urllib2                                                                                                          
                                                                                                                        
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}                                          
class FlexSwitch( object):                                                                                              
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

    def getOspfHostEntryState(self,
                              HostTOS,
                              HostIpAddress):
        obj =  { 
                'HostTOS' : HostTOS
                'HostIpAddress' : HostIpAddress
                }
        reqUrl =  self.urlBase+'OspfHostEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfHostEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfHostEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfHostEntryStates(self):
        return self.getObjects( 'OspfHostEntryState') 


    def getVxlanStateVxlanInstanceMapL3interface(self,
                                                 InterfaceName):
        obj =  { 
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanStateVxlanInstanceMapL3interface'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanStateVxlanInstanceMapL3interfaceById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanStateVxlanInstanceMapL3interface'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanStateVxlanInstanceMapL3interfaces(self):
        return self.getObjects( 'VxlanStateVxlanInstanceMapL3interface') 


    def createPolicyStmt(self,
                         Name,
                         MatchConditions,
                         Conditions,
                         Actions):
        obj =  { 
                'Name' : Name
                'MatchConditions' : MatchConditions
                'Conditions' : Conditions
                'Actions' : Actions
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyStmt(self,
                         Name,
                         MatchConditions = None,
                         Conditions = None,
                         Actions = None):
        obj =  { 
                'Name' : Name
                'MatchConditions' : MatchConditions
                'Conditions' : Conditions
                'Actions' : Actions
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyStmtById(self,
                              objectId,
                              MatchConditions = None,
                              Conditions = None,
                              Actions = None):
        obj =  { 
                'objectId': objectId
                'MatchConditions' : MatchConditions
                'Conditions' : Conditions
                'Actions' : Actions
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getPolicyStmt(self,
                      Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyStmts(self):
        return self.getObjects( 'PolicyStmt') 


    def createOspfNbrEntryConfig(self,
                                 NbrIpAddr,
                                 NbrAddressLessIndex,
                                 NbrPriority):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr
                'NbrAddressLessIndex' : NbrAddressLessIndex
                'NbrPriority' : NbrPriority
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfNbrEntryConfig(self,
                                 NbrIpAddr,
                                 NbrAddressLessIndex,
                                 NbrPriority = None):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr
                'NbrAddressLessIndex' : NbrAddressLessIndex
                'NbrPriority' : NbrPriority
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfNbrEntryConfigById(self,
                                      objectId,
                                      NbrPriority = None):
        obj =  { 
                'objectId': objectId
                'NbrPriority' : NbrPriority
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfNbrEntryConfig(self,
                                 NbrIpAddr,
                                 NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr
                'NbrAddressLessIndex' : NbrAddressLessIndex
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfNbrEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfNbrEntryConfig(self,
                              NbrIpAddr,
                              NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr
                'NbrAddressLessIndex' : NbrAddressLessIndex
                }
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfNbrEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfNbrEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfNbrEntryConfigs(self):
        return self.getObjects( 'OspfNbrEntryConfig') 


    def createVlan(self,
                   VlanId,
                   VlanName,
                   OperState,
                   IfIndex,
                   IfIndexList,
                   UntagIfIndexList):
        obj =  { 
                'VlanId' : VlanId
                'VlanName' : VlanName
                'OperState' : OperState
                'IfIndex' : IfIndex
                'IfIndexList' : IfIndexList
                'UntagIfIndexList' : UntagIfIndexList
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVlan(self,
                   VlanId,
                   VlanName = None,
                   OperState = None,
                   IfIndex = None,
                   IfIndexList = None,
                   UntagIfIndexList = None):
        obj =  { 
                'VlanId' : VlanId
                'VlanName' : VlanName
                'OperState' : OperState
                'IfIndex' : IfIndex
                'IfIndexList' : IfIndexList
                'UntagIfIndexList' : UntagIfIndexList
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVlanById(self,
                        objectId,
                        VlanName = None,
                        OperState = None,
                        IfIndex = None,
                        IfIndexList = None,
                        UntagIfIndexList = None):
        obj =  { 
                'objectId': objectId
                'VlanName' : VlanName
                'OperState' : OperState
                'IfIndex' : IfIndex
                'IfIndexList' : IfIndexList
                'UntagIfIndexList' : UntagIfIndexList
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVlan(self,
                   VlanId):
        obj =  { 
                'VlanId' : VlanId
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVlanById(self, objectId ):
        reqUrl =  self.urlBase+'Vlan'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVlan(self,
                VlanId):
        obj =  { 
                'VlanId' : VlanId
                }
        reqUrl =  self.urlBase+'Vlan'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVlanById(self, objectId ):
        reqUrl =  self.urlBase+'Vlan'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVlans(self):
        return self.getObjects( 'Vlan') 


    def getOspfLocalLsdbEntryState(self,
                                   LocalLsdbAddressLessIf,
                                   LocalLsdbType,
                                   LocalLsdbIpAddress,
                                   LocalLsdbRouterId,
                                   LocalLsdbLsid):
        obj =  { 
                'LocalLsdbAddressLessIf' : LocalLsdbAddressLessIf
                'LocalLsdbType' : LocalLsdbType
                'LocalLsdbIpAddress' : LocalLsdbIpAddress
                'LocalLsdbRouterId' : LocalLsdbRouterId
                'LocalLsdbLsid' : LocalLsdbLsid
                }
        reqUrl =  self.urlBase+'OspfLocalLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfLocalLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfLocalLsdbEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfLocalLsdbEntryStates(self):
        return self.getObjects( 'OspfLocalLsdbEntryState') 


    def createComponentLogging(self,
                               Module,
                               Level='info'):
        obj =  { 
                'Module' : Module
                'Level' : Level
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateComponentLogging(self,
                               Module,
                               Level = None):
        obj =  { 
                'Module' : Module
                'Level' : Level
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateComponentLoggingById(self,
                                    objectId,
                                    Level = None):
        obj =  { 
                'objectId': objectId
                'Level' : Level
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteComponentLogging(self,
                               Module):
        obj =  { 
                'Module' : Module
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteComponentLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'ComponentLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getComponentLogging(self,
                            Module):
        obj =  { 
                'Module' : Module
                }
        reqUrl =  self.urlBase+'ComponentLogging'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteComponentLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'ComponentLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllComponentLoggings(self):
        return self.getObjects( 'ComponentLogging') 


    def getIPv4EventState(self,
                          Index):
        obj =  { 
                'Index' : Index
                }
        reqUrl =  self.urlBase+'IPv4EventState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4EventStateById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4EventState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllIPv4EventStates(self):
        return self.getObjects( 'IPv4EventState') 


    def createDhcpRelayIntf(self,
                            IfIndex,
                            Enable,
                            ServerIp):
        obj =  { 
                'IfIndex' : IfIndex
                'Enable' : Enable
                'ServerIp' : ServerIp
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateDhcpRelayIntf(self,
                            IfIndex,
                            Enable = None,
                            ServerIp = None):
        obj =  { 
                'IfIndex' : IfIndex
                'Enable' : Enable
                'ServerIp' : ServerIp
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateDhcpRelayIntfById(self,
                                 objectId,
                                 Enable = None,
                                 ServerIp = None):
        obj =  { 
                'objectId': objectId
                'Enable' : Enable
                'ServerIp' : ServerIp
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayIntf(self,
                            IfIndex):
        obj =  { 
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getDhcpRelayIntf(self,
                         IfIndex):
        obj =  { 
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'DhcpRelayIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllDhcpRelayIntfs(self):
        return self.getObjects( 'DhcpRelayIntf') 


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
                'Name' : Name
                'ActionType' : ActionType
                'SetAdminDistanceValue' : SetAdminDistanceValue
                'Accept' : Accept
                'Reject' : Reject
                'RedistributeAction' : RedistributeAction
                'RedistributeTargetProtocol' : RedistributeTargetProtocol
                'NetworkStatementTargetProtocol' : NetworkStatementTargetProtocol
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyAction(self,
                           Name,
                           ActionType = None,
                           SetAdminDistanceValue = None,
                           Accept = None,
                           Reject = None,
                           RedistributeAction = None,
                           RedistributeTargetProtocol = None,
                           NetworkStatementTargetProtocol = None):
        obj =  { 
                'Name' : Name
                'ActionType' : ActionType
                'SetAdminDistanceValue' : SetAdminDistanceValue
                'Accept' : Accept
                'Reject' : Reject
                'RedistributeAction' : RedistributeAction
                'RedistributeTargetProtocol' : RedistributeTargetProtocol
                'NetworkStatementTargetProtocol' : NetworkStatementTargetProtocol
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyActionById(self,
                                objectId,
                                ActionType = None,
                                SetAdminDistanceValue = None,
                                Accept = None,
                                Reject = None,
                                RedistributeAction = None,
                                RedistributeTargetProtocol = None,
                                NetworkStatementTargetProtocol = None):
        obj =  { 
                'objectId': objectId
                'ActionType' : ActionType
                'SetAdminDistanceValue' : SetAdminDistanceValue
                'Accept' : Accept
                'Reject' : Reject
                'RedistributeAction' : RedistributeAction
                'RedistributeTargetProtocol' : RedistributeTargetProtocol
                'NetworkStatementTargetProtocol' : NetworkStatementTargetProtocol
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyAction(self,
                           Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getPolicyAction(self,
                        Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyAction'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyActions(self):
        return self.getObjects( 'PolicyAction') 


    def createIpTableAcl(self,
                         Name,
                         PhysicalPort='all',
                         Action,
                         IpAddr,
                         Protocol,
                         Port='all'):
        obj =  { 
                'Name' : Name
                'PhysicalPort' : PhysicalPort
                'Action' : Action
                'IpAddr' : IpAddr
                'Protocol' : Protocol
                'Port' : Port
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateIpTableAcl(self,
                         Name,
                         PhysicalPort = None,
                         Action = None,
                         IpAddr = None,
                         Protocol = None,
                         Port = None):
        obj =  { 
                'Name' : Name
                'PhysicalPort' : PhysicalPort
                'Action' : Action
                'IpAddr' : IpAddr
                'Protocol' : Protocol
                'Port' : Port
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateIpTableAclById(self,
                              objectId,
                              PhysicalPort = None,
                              Action = None,
                              IpAddr = None,
                              Protocol = None,
                              Port = None):
        obj =  { 
                'objectId': objectId
                'PhysicalPort' : PhysicalPort
                'Action' : Action
                'IpAddr' : IpAddr
                'Protocol' : Protocol
                'Port' : Port
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIpTableAcl(self,
                         Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIpTableAclById(self, objectId ):
        reqUrl =  self.urlBase+'IpTableAcl'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getIpTableAcl(self,
                      Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'IpTableAcl'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIpTableAclById(self, objectId ):
        reqUrl =  self.urlBase+'IpTableAcl'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllIpTableAcls(self):
        return self.getObjects( 'IpTableAcl') 


    def getStpPortState(self,
                        IfIndex,
                        BrgIfIndex):
        obj =  { 
                'IfIndex' : IfIndex
                'BrgIfIndex' : BrgIfIndex
                }
        reqUrl =  self.urlBase+'StpPortState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpPortStateById(self, objectId ):
        reqUrl =  self.urlBase+'StpPortState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllStpPortStates(self):
        return self.getObjects( 'StpPortState') 


    def createOspfAreaEntryConfig(self,
                                  AreaId,
                                  AuthType,
                                  ImportAsExtern,
                                  AreaSummary,
                                  AreaNssaTranslatorRole,
                                  AreaNssaTranslatorStabilityInterval):
        obj =  { 
                'AreaId' : AreaId
                'AuthType' : AuthType
                'ImportAsExtern' : ImportAsExtern
                'AreaSummary' : AreaSummary
                'AreaNssaTranslatorRole' : AreaNssaTranslatorRole
                'AreaNssaTranslatorStabilityInterval' : AreaNssaTranslatorStabilityInterval
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfAreaEntryConfig(self,
                                  AreaId,
                                  AuthType = None,
                                  ImportAsExtern = None,
                                  AreaSummary = None,
                                  AreaNssaTranslatorRole = None,
                                  AreaNssaTranslatorStabilityInterval = None):
        obj =  { 
                'AreaId' : AreaId
                'AuthType' : AuthType
                'ImportAsExtern' : ImportAsExtern
                'AreaSummary' : AreaSummary
                'AreaNssaTranslatorRole' : AreaNssaTranslatorRole
                'AreaNssaTranslatorStabilityInterval' : AreaNssaTranslatorStabilityInterval
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfAreaEntryConfigById(self,
                                       objectId,
                                       AuthType = None,
                                       ImportAsExtern = None,
                                       AreaSummary = None,
                                       AreaNssaTranslatorRole = None,
                                       AreaNssaTranslatorStabilityInterval = None):
        obj =  { 
                'objectId': objectId
                'AuthType' : AuthType
                'ImportAsExtern' : ImportAsExtern
                'AreaSummary' : AreaSummary
                'AreaNssaTranslatorRole' : AreaNssaTranslatorRole
                'AreaNssaTranslatorStabilityInterval' : AreaNssaTranslatorStabilityInterval
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaEntryConfig(self,
                                  AreaId):
        obj =  { 
                'AreaId' : AreaId
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfAreaEntryConfig(self,
                               AreaId):
        obj =  { 
                'AreaId' : AreaId
                }
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfAreaEntryConfigs(self):
        return self.getObjects( 'OspfAreaEntryConfig') 


    def getBGPPolicyConditionState(self,
                                   Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyConditionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyConditionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyConditionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyConditionStates(self):
        return self.getObjects( 'BGPPolicyConditionState') 


    def getArpEntry(self,
                    IpAddr):
        obj =  { 
                'IpAddr' : IpAddr
                }
        reqUrl =  self.urlBase+'ArpEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteArpEntryById(self, objectId ):
        reqUrl =  self.urlBase+'ArpEntry'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllArpEntrys(self):
        return self.getObjects( 'ArpEntry') 


    def createArpConfig(self,
                        ArpConfigKey,
                        Timeout):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey
                'Timeout' : Timeout
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateArpConfig(self,
                        ArpConfigKey,
                        Timeout = None):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey
                'Timeout' : Timeout
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateArpConfigById(self,
                             objectId,
                             Timeout = None):
        obj =  { 
                'objectId': objectId
                'Timeout' : Timeout
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteArpConfig(self,
                        ArpConfigKey):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteArpConfigById(self, objectId ):
        reqUrl =  self.urlBase+'ArpConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getArpConfig(self,
                     ArpConfigKey):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey
                }
        reqUrl =  self.urlBase+'ArpConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteArpConfigById(self, objectId ):
        reqUrl =  self.urlBase+'ArpConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllArpConfigs(self):
        return self.getObjects( 'ArpConfig') 


    def getOspfNbrEntryState(self,
                             NbrIpAddr,
                             NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr
                'NbrAddressLessIndex' : NbrAddressLessIndex
                }
        reqUrl =  self.urlBase+'OspfNbrEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfNbrEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfNbrEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfNbrEntryStates(self):
        return self.getObjects( 'OspfNbrEntryState') 


    def getDhcpRelayIntfState(self,
                              IntfId):
        obj =  { 
                'IntfId' : IntfId
                }
        reqUrl =  self.urlBase+'DhcpRelayIntfState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayIntfStateById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntfState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllDhcpRelayIntfStates(self):
        return self.getObjects( 'DhcpRelayIntfState') 


    def createDhcpRelayGlobal(self,
                              DhcpRelay,
                              Enable):
        obj =  { 
                'DhcpRelay' : DhcpRelay
                'Enable' : Enable
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateDhcpRelayGlobal(self,
                              DhcpRelay,
                              Enable = None):
        obj =  { 
                'DhcpRelay' : DhcpRelay
                'Enable' : Enable
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateDhcpRelayGlobalById(self,
                                   objectId,
                                   Enable = None):
        obj =  { 
                'objectId': objectId
                'Enable' : Enable
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayGlobal(self,
                              DhcpRelay):
        obj =  { 
                'DhcpRelay' : DhcpRelay
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getDhcpRelayGlobal(self,
                           DhcpRelay):
        obj =  { 
                'DhcpRelay' : DhcpRelay
                }
        reqUrl =  self.urlBase+'DhcpRelayGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllDhcpRelayGlobals(self):
        return self.getObjects( 'DhcpRelayGlobal') 


    def getOspfLsdbEntryState(self,
                              LsdbType,
                              LsdbLsid,
                              LsdbAreaId,
                              LsdbRouterId):
        obj =  { 
                'LsdbType' : LsdbType
                'LsdbLsid' : LsdbLsid
                'LsdbAreaId' : LsdbAreaId
                'LsdbRouterId' : LsdbRouterId
                }
        reqUrl =  self.urlBase+'OspfLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfLsdbEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfLsdbEntryStates(self):
        return self.getObjects( 'OspfLsdbEntryState') 


    def createVxlanVxlanInstanceAccessTypeVlanVlanList(self,
                                                       VlanId,
                                                       VxlanId):
        obj =  { 
                'VlanId' : VlanId
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceAccessTypeVlanVlanList(self,
                                                       VlanId,
                                                       VxlanId):
        obj =  { 
                'VlanId' : VlanId
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceAccessTypeVlanVlanListById(self,
                                                            objectId):
        obj =  { 
                'objectId': objectId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeVlanVlanList(self,
                                                       VlanId,
                                                       VxlanId):
        obj =  { 
                'VlanId' : VlanId
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeVlanVlanListById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVxlanVxlanInstanceAccessTypeVlanVlanList(self,
                                                    VlanId,
                                                    VxlanId):
        obj =  { 
                'VlanId' : VlanId
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeVlanVlanListById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeVlanVlanList'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanVxlanInstanceAccessTypeVlanVlanLists(self):
        return self.getObjects( 'VxlanVxlanInstanceAccessTypeVlanVlanList') 


    def createBGPPolicyCondition(self,
                                 Name,
                                 ConditionType,
                                 IpPrefix,
                                 MaskLengthRange):
        obj =  { 
                'Name' : Name
                'ConditionType' : ConditionType
                'IpPrefix' : IpPrefix
                'MaskLengthRange' : MaskLengthRange
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyCondition(self,
                                 Name,
                                 ConditionType = None,
                                 IpPrefix = None,
                                 MaskLengthRange = None):
        obj =  { 
                'Name' : Name
                'ConditionType' : ConditionType
                'IpPrefix' : IpPrefix
                'MaskLengthRange' : MaskLengthRange
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyConditionById(self,
                                      objectId,
                                      ConditionType = None,
                                      IpPrefix = None,
                                      MaskLengthRange = None):
        obj =  { 
                'objectId': objectId
                'ConditionType' : ConditionType
                'IpPrefix' : IpPrefix
                'MaskLengthRange' : MaskLengthRange
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyCondition(self,
                                 Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPPolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyConditions(self):
        return self.getObjects( 'BGPPolicyCondition') 


    def getDhcpRelayHostDhcpState(self,
                                  MacAddr):
        obj =  { 
                'MacAddr' : MacAddr
                }
        reqUrl =  self.urlBase+'DhcpRelayHostDhcpState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayHostDhcpStateById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayHostDhcpState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllDhcpRelayHostDhcpStates(self):
        return self.getObjects( 'DhcpRelayHostDhcpState') 


    def getDhcpRelayIntfServerState(self,
                                    IntfId):
        obj =  { 
                'IntfId' : IntfId
                }
        reqUrl =  self.urlBase+'DhcpRelayIntfServerState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteDhcpRelayIntfServerStateById(self, objectId ):
        reqUrl =  self.urlBase+'DhcpRelayIntfServerState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllDhcpRelayIntfServerStates(self):
        return self.getObjects( 'DhcpRelayIntfServerState') 


    def createPolicyDefinition(self,
                               Name,
                               Precedence,
                               MatchType,
                               StatementList):
        obj =  { 
                'Name' : Name
                'Precedence' : Precedence
                'MatchType' : MatchType
                'StatementList' : StatementList
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyDefinition(self,
                               Name,
                               Precedence = None,
                               MatchType = None,
                               StatementList = None):
        obj =  { 
                'Name' : Name
                'Precedence' : Precedence
                'MatchType' : MatchType
                'StatementList' : StatementList
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyDefinitionById(self,
                                    objectId,
                                    Precedence = None,
                                    MatchType = None,
                                    StatementList = None):
        obj =  { 
                'objectId': objectId
                'Precedence' : Precedence
                'MatchType' : MatchType
                'StatementList' : StatementList
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getPolicyDefinition(self,
                            Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyDefinitions(self):
        return self.getObjects( 'PolicyDefinition') 


    def getOspfVirtNbrEntryState(self,
                                 VirtNbrRtrId,
                                 VirtNbrArea):
        obj =  { 
                'VirtNbrRtrId' : VirtNbrRtrId
                'VirtNbrArea' : VirtNbrArea
                }
        reqUrl =  self.urlBase+'OspfVirtNbrEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfVirtNbrEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtNbrEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfVirtNbrEntryStates(self):
        return self.getObjects( 'OspfVirtNbrEntryState') 


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
                'BrgIfIndex' : BrgIfIndex
                'IfIndex' : IfIndex
                'Priority' : Priority
                'Enable' : Enable
                'PathCost' : PathCost
                'PathCost32' : PathCost32
                'ProtocolMigration' : ProtocolMigration
                'AdminPointToPoint' : AdminPointToPoint
                'AdminEdgePort' : AdminEdgePort
                'AdminPathCost' : AdminPathCost
                'BpduGuard' : BpduGuard
                'BpduGuardInterval' : BpduGuardInterval
                'BridgeAssurance' : BridgeAssurance
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


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
        obj =  { 
                'BrgIfIndex' : BrgIfIndex
                'IfIndex' : IfIndex
                'Priority' : Priority
                'Enable' : Enable
                'PathCost' : PathCost
                'PathCost32' : PathCost32
                'ProtocolMigration' : ProtocolMigration
                'AdminPointToPoint' : AdminPointToPoint
                'AdminEdgePort' : AdminEdgePort
                'AdminPathCost' : AdminPathCost
                'BpduGuard' : BpduGuard
                'BpduGuardInterval' : BpduGuardInterval
                'BridgeAssurance' : BridgeAssurance
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


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
        obj =  { 
                'objectId': objectId
                'Priority' : Priority
                'Enable' : Enable
                'PathCost' : PathCost
                'PathCost32' : PathCost32
                'ProtocolMigration' : ProtocolMigration
                'AdminPointToPoint' : AdminPointToPoint
                'AdminEdgePort' : AdminEdgePort
                'AdminPathCost' : AdminPathCost
                'BpduGuard' : BpduGuard
                'BpduGuardInterval' : BpduGuardInterval
                'BridgeAssurance' : BridgeAssurance
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpPort(self,
                      BrgIfIndex,
                      IfIndex):
        obj =  { 
                'BrgIfIndex' : BrgIfIndex
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpPortById(self, objectId ):
        reqUrl =  self.urlBase+'StpPort'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getStpPort(self,
                   BrgIfIndex,
                   IfIndex):
        obj =  { 
                'BrgIfIndex' : BrgIfIndex
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'StpPort'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpPortById(self, objectId ):
        reqUrl =  self.urlBase+'StpPort'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllStpPorts(self):
        return self.getObjects( 'StpPort') 


    def getRouteDistanceState(self,
                              Protocol):
        obj =  { 
                'Protocol' : Protocol
                }
        reqUrl =  self.urlBase+'RouteDistanceState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteRouteDistanceStateById(self, objectId ):
        reqUrl =  self.urlBase+'RouteDistanceState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllRouteDistanceStates(self):
        return self.getObjects( 'RouteDistanceState') 


    def createLogicalIntf(self,
                          Name,
                          Type):
        obj =  { 
                'Name' : Name
                'Type' : Type
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateLogicalIntf(self,
                          Name,
                          Type = None):
        obj =  { 
                'Name' : Name
                'Type' : Type
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateLogicalIntfById(self,
                               objectId,
                               Type = None):
        obj =  { 
                'objectId': objectId
                'Type' : Type
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteLogicalIntf(self,
                          Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteLogicalIntfById(self, objectId ):
        reqUrl =  self.urlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getLogicalIntf(self,
                       Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'LogicalIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteLogicalIntfById(self, objectId ):
        reqUrl =  self.urlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllLogicalIntfs(self):
        return self.getObjects( 'LogicalIntf') 


    def createBGPPeerGroup(self,
                           PeerAS,
                           LocalAS= 0,
                           AuthPassword='',
                           Description='',
                           Name,
                           RouteReflectorClusterId= 0,
                           RouteReflectorClient='false',
                           MultiHopEnable='false',
                           MultiHopTTL='0',
                           ConnectRetryTime= 60,
                           HoldTime= 180,
                           KeepaliveTime= 60,
                           AddPathsRx='false',
                           AddPathsMaxTx='0'):
        obj =  { 
                'PeerAS' : PeerAS
                'LocalAS' : LocalAS
                'AuthPassword' : AuthPassword
                'Description' : Description
                'Name' : Name
                'RouteReflectorClusterId' : RouteReflectorClusterId
                'RouteReflectorClient' : RouteReflectorClient
                'MultiHopEnable' : MultiHopEnable
                'MultiHopTTL' : MultiHopTTL
                'ConnectRetryTime' : ConnectRetryTime
                'HoldTime' : HoldTime
                'KeepaliveTime' : KeepaliveTime
                'AddPathsRx' : AddPathsRx
                'AddPathsMaxTx' : AddPathsMaxTx
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPeerGroup(self,
                           PeerAS = None,
                           LocalAS = None,
                           AuthPassword = None,
                           Description = None,
                           Name,
                           RouteReflectorClusterId = None,
                           RouteReflectorClient = None,
                           MultiHopEnable = None,
                           MultiHopTTL = None,
                           ConnectRetryTime = None,
                           HoldTime = None,
                           KeepaliveTime = None,
                           AddPathsRx = None,
                           AddPathsMaxTx = None):
        obj =  { 
                'PeerAS' : PeerAS
                'LocalAS' : LocalAS
                'AuthPassword' : AuthPassword
                'Description' : Description
                'Name' : Name
                'RouteReflectorClusterId' : RouteReflectorClusterId
                'RouteReflectorClient' : RouteReflectorClient
                'MultiHopEnable' : MultiHopEnable
                'MultiHopTTL' : MultiHopTTL
                'ConnectRetryTime' : ConnectRetryTime
                'HoldTime' : HoldTime
                'KeepaliveTime' : KeepaliveTime
                'AddPathsRx' : AddPathsRx
                'AddPathsMaxTx' : AddPathsMaxTx
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPeerGroupById(self,
                                objectId,
                                PeerAS = None,
                                LocalAS = None,
                                AuthPassword = None,
                                Description = None,
                                RouteReflectorClusterId = None,
                                RouteReflectorClient = None,
                                MultiHopEnable = None,
                                MultiHopTTL = None,
                                ConnectRetryTime = None,
                                HoldTime = None,
                                KeepaliveTime = None,
                                AddPathsRx = None,
                                AddPathsMaxTx = None):
        obj =  { 
                'objectId': objectId
                'PeerAS' : PeerAS
                'LocalAS' : LocalAS
                'AuthPassword' : AuthPassword
                'Description' : Description
                'RouteReflectorClusterId' : RouteReflectorClusterId
                'RouteReflectorClient' : RouteReflectorClient
                'MultiHopEnable' : MultiHopEnable
                'MultiHopTTL' : MultiHopTTL
                'ConnectRetryTime' : ConnectRetryTime
                'HoldTime' : HoldTime
                'KeepaliveTime' : KeepaliveTime
                'AddPathsRx' : AddPathsRx
                'AddPathsMaxTx' : AddPathsMaxTx
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPeerGroup(self,
                           Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPeerGroupById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPeerGroup'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPPeerGroup(self,
                        Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPeerGroup'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPeerGroupById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPeerGroup'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPeerGroups(self):
        return self.getObjects( 'BGPPeerGroup') 


    def getBfdInterfaceState(self,
                             IfIndex):
        obj =  { 
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'BfdInterfaceState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdInterfaceStateById(self, objectId ):
        reqUrl =  self.urlBase+'BfdInterfaceState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBfdInterfaceStates(self):
        return self.getObjects( 'BfdInterfaceState') 


    def createBfdGlobal(self,
                        Bfd,
                        Enable='true'):
        obj =  { 
                'Bfd' : Bfd
                'Enable' : Enable
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBfdGlobal(self,
                        Bfd,
                        Enable = None):
        obj =  { 
                'Bfd' : Bfd
                'Enable' : Enable
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBfdGlobalById(self,
                             objectId,
                             Enable = None):
        obj =  { 
                'objectId': objectId
                'Enable' : Enable
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdGlobal(self,
                        Bfd):
        obj =  { 
                'Bfd' : Bfd
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBfdGlobal(self,
                     Bfd):
        obj =  { 
                'Bfd' : Bfd
                }
        reqUrl =  self.urlBase+'BfdGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBfdGlobals(self):
        return self.getObjects( 'BfdGlobal') 


    def createVxlanVxlanInstanceVxlanEvpnVpnTargets(self,
                                                    RtValue,
                                                    VxlanId,
                                                    RouteDistinguisher,
                                                    RtType):
        obj =  { 
                'RtValue' : RtValue
                'VxlanId' : VxlanId
                'RouteDistinguisher' : RouteDistinguisher
                'RtType' : RtType
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceVxlanEvpnVpnTargets(self,
                                                    RtValue,
                                                    VxlanId,
                                                    RouteDistinguisher = None,
                                                    RtType = None):
        obj =  { 
                'RtValue' : RtValue
                'VxlanId' : VxlanId
                'RouteDistinguisher' : RouteDistinguisher
                'RtType' : RtType
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceVxlanEvpnVpnTargetsById(self,
                                                         objectId,
                                                         RouteDistinguisher = None,
                                                         RtType = None):
        obj =  { 
                'objectId': objectId
                'RouteDistinguisher' : RouteDistinguisher
                'RtType' : RtType
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceVxlanEvpnVpnTargets(self,
                                                    RtValue,
                                                    VxlanId):
        obj =  { 
                'RtValue' : RtValue
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceVxlanEvpnVpnTargetsById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVxlanVxlanInstanceVxlanEvpnVpnTargets(self,
                                                 RtValue,
                                                 VxlanId):
        obj =  { 
                'RtValue' : RtValue
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceVxlanEvpnVpnTargetsById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceVxlanEvpnVpnTargets'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanVxlanInstanceVxlanEvpnVpnTargetss(self):
        return self.getObjects( 'VxlanVxlanInstanceVxlanEvpnVpnTargets') 


    def getOspfAreaLsaCountEntryState(self,
                                      AreaLsaCountAreaId,
                                      AreaLsaCountLsaType):
        obj =  { 
                'AreaLsaCountAreaId' : AreaLsaCountAreaId
                'AreaLsaCountLsaType' : AreaLsaCountLsaType
                }
        reqUrl =  self.urlBase+'OspfAreaLsaCountEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaLsaCountEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaLsaCountEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfAreaLsaCountEntryStates(self):
        return self.getObjects( 'OspfAreaLsaCountEntryState') 


    def createBGPPolicyStmt(self,
                            Name,
                            MatchConditions,
                            Conditions,
                            Actions):
        obj =  { 
                'Name' : Name
                'MatchConditions' : MatchConditions
                'Conditions' : Conditions
                'Actions' : Actions
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyStmt(self,
                            Name,
                            MatchConditions = None,
                            Conditions = None,
                            Actions = None):
        obj =  { 
                'Name' : Name
                'MatchConditions' : MatchConditions
                'Conditions' : Conditions
                'Actions' : Actions
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyStmtById(self,
                                 objectId,
                                 MatchConditions = None,
                                 Conditions = None,
                                 Actions = None):
        obj =  { 
                'objectId': objectId
                'MatchConditions' : MatchConditions
                'Conditions' : Conditions
                'Actions' : Actions
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyStmt(self,
                            Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPPolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyStmts(self):
        return self.getObjects( 'BGPPolicyStmt') 


    def createOspfStubAreaEntryConfig(self,
                                      StubTOS,
                                      StubAreaId,
                                      StubMetric,
                                      StubMetricType):
        obj =  { 
                'StubTOS' : StubTOS
                'StubAreaId' : StubAreaId
                'StubMetric' : StubMetric
                'StubMetricType' : StubMetricType
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfStubAreaEntryConfig(self,
                                      StubTOS,
                                      StubAreaId,
                                      StubMetric = None,
                                      StubMetricType = None):
        obj =  { 
                'StubTOS' : StubTOS
                'StubAreaId' : StubAreaId
                'StubMetric' : StubMetric
                'StubMetricType' : StubMetricType
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfStubAreaEntryConfigById(self,
                                           objectId,
                                           StubMetric = None,
                                           StubMetricType = None):
        obj =  { 
                'objectId': objectId
                'StubMetric' : StubMetric
                'StubMetricType' : StubMetricType
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfStubAreaEntryConfig(self,
                                      StubTOS,
                                      StubAreaId):
        obj =  { 
                'StubTOS' : StubTOS
                'StubAreaId' : StubAreaId
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfStubAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfStubAreaEntryConfig(self,
                                   StubTOS,
                                   StubAreaId):
        obj =  { 
                'StubTOS' : StubTOS
                'StubAreaId' : StubAreaId
                }
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfStubAreaEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfStubAreaEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfStubAreaEntryConfigs(self):
        return self.getObjects( 'OspfStubAreaEntryConfig') 


    def getVxlanStateVxlanInstanceAccessVlan(self,
                                             VlanId):
        obj =  { 
                'VlanId' : VlanId
                }
        reqUrl =  self.urlBase+'VxlanStateVxlanInstanceAccessVlan'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanStateVxlanInstanceAccessVlanById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanStateVxlanInstanceAccessVlan'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanStateVxlanInstanceAccessVlans(self):
        return self.getObjects( 'VxlanStateVxlanInstanceAccessVlan') 


    def getIPv4RouteState(self,
                          DestinationNw,
                          NextHopIp):
        obj =  { 
                'DestinationNw' : DestinationNw
                'NextHopIp' : NextHopIp
                }
        reqUrl =  self.urlBase+'IPv4RouteState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4RouteStateById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4RouteState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllIPv4RouteStates(self):
        return self.getObjects( 'IPv4RouteState') 


    def getBfdGlobalState(self,
                          Bfd):
        obj =  { 
                'Bfd' : Bfd
                }
        reqUrl =  self.urlBase+'BfdGlobalState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdGlobalStateById(self, objectId ):
        reqUrl =  self.urlBase+'BfdGlobalState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBfdGlobalStates(self):
        return self.getObjects( 'BfdGlobalState') 


    def getOspfVirtLocalLsdbEntryState(self,
                                       VirtLocalLsdbType,
                                       VirtLocalLsdbNeighbor,
                                       VirtLocalLsdbLsid,
                                       VirtLocalLsdbTransitArea,
                                       VirtLocalLsdbRouterId):
        obj =  { 
                'VirtLocalLsdbType' : VirtLocalLsdbType
                'VirtLocalLsdbNeighbor' : VirtLocalLsdbNeighbor
                'VirtLocalLsdbLsid' : VirtLocalLsdbLsid
                'VirtLocalLsdbTransitArea' : VirtLocalLsdbTransitArea
                'VirtLocalLsdbRouterId' : VirtLocalLsdbRouterId
                }
        reqUrl =  self.urlBase+'OspfVirtLocalLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfVirtLocalLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtLocalLsdbEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfVirtLocalLsdbEntryStates(self):
        return self.getObjects( 'OspfVirtLocalLsdbEntryState') 


    def getVxlanStateVxlanInstanceVxlanEvpnVpnTargets(self,
                                                      RtValue):
        obj =  { 
                'RtValue' : RtValue
                }
        reqUrl =  self.urlBase+'VxlanStateVxlanInstanceVxlanEvpnVpnTargets'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanStateVxlanInstanceVxlanEvpnVpnTargetsById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanStateVxlanInstanceVxlanEvpnVpnTargets'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanStateVxlanInstanceVxlanEvpnVpnTargetss(self):
        return self.getObjects( 'VxlanStateVxlanInstanceVxlanEvpnVpnTargets') 


    def getBGPGlobalState(self,
                          RouterId):
        obj =  { 
                'RouterId' : RouterId
                }
        reqUrl =  self.urlBase+'BGPGlobalState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPGlobalStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPGlobalState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPGlobalStates(self):
        return self.getObjects( 'BGPGlobalState') 


    def getBfdSessionState(self,
                           SessionId):
        obj =  { 
                'SessionId' : SessionId
                }
        reqUrl =  self.urlBase+'BfdSessionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdSessionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BfdSessionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBfdSessionStates(self):
        return self.getObjects( 'BfdSessionState') 


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
                'VirtIfNeighbor' : VirtIfNeighbor
                'VirtIfAreaId' : VirtIfAreaId
                'VirtIfTransitDelay' : VirtIfTransitDelay
                'VirtIfRetransInterval' : VirtIfRetransInterval
                'VirtIfHelloInterval' : VirtIfHelloInterval
                'VirtIfRtrDeadInterval' : VirtIfRtrDeadInterval
                'VirtIfAuthKey' : VirtIfAuthKey
                'VirtIfAuthType' : VirtIfAuthType
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfVirtIfEntryConfig(self,
                                    VirtIfNeighbor,
                                    VirtIfAreaId,
                                    VirtIfTransitDelay = None,
                                    VirtIfRetransInterval = None,
                                    VirtIfHelloInterval = None,
                                    VirtIfRtrDeadInterval = None,
                                    VirtIfAuthKey = None,
                                    VirtIfAuthType = None):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor
                'VirtIfAreaId' : VirtIfAreaId
                'VirtIfTransitDelay' : VirtIfTransitDelay
                'VirtIfRetransInterval' : VirtIfRetransInterval
                'VirtIfHelloInterval' : VirtIfHelloInterval
                'VirtIfRtrDeadInterval' : VirtIfRtrDeadInterval
                'VirtIfAuthKey' : VirtIfAuthKey
                'VirtIfAuthType' : VirtIfAuthType
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfVirtIfEntryConfigById(self,
                                         objectId,
                                         VirtIfTransitDelay = None,
                                         VirtIfRetransInterval = None,
                                         VirtIfHelloInterval = None,
                                         VirtIfRtrDeadInterval = None,
                                         VirtIfAuthKey = None,
                                         VirtIfAuthType = None):
        obj =  { 
                'objectId': objectId
                'VirtIfTransitDelay' : VirtIfTransitDelay
                'VirtIfRetransInterval' : VirtIfRetransInterval
                'VirtIfHelloInterval' : VirtIfHelloInterval
                'VirtIfRtrDeadInterval' : VirtIfRtrDeadInterval
                'VirtIfAuthKey' : VirtIfAuthKey
                'VirtIfAuthType' : VirtIfAuthType
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfVirtIfEntryConfig(self,
                                    VirtIfNeighbor,
                                    VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor
                'VirtIfAreaId' : VirtIfAreaId
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfVirtIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfVirtIfEntryConfig(self,
                                 VirtIfNeighbor,
                                 VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor
                'VirtIfAreaId' : VirtIfAreaId
                }
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfVirtIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfVirtIfEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfVirtIfEntryConfigs(self):
        return self.getObjects( 'OspfVirtIfEntryConfig') 


    def createIPv4Intf(self,
                       IpAddr,
                       IfIndex):
        obj =  { 
                'IpAddr' : IpAddr
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateIPv4Intf(self,
                       IpAddr,
                       IfIndex = None):
        obj =  { 
                'IpAddr' : IpAddr
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateIPv4IntfById(self,
                            objectId,
                            IfIndex = None):
        obj =  { 
                'objectId': objectId
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4Intf(self,
                       IpAddr):
        obj =  { 
                'IpAddr' : IpAddr
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4IntfById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getIPv4Intf(self,
                    IpAddr):
        obj =  { 
                'IpAddr' : IpAddr
                }
        reqUrl =  self.urlBase+'IPv4Intf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4IntfById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllIPv4Intfs(self):
        return self.getObjects( 'IPv4Intf') 


    def getPolicyStmtState(self,
                           Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyStmtState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyStmtStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyStmtState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyStmtStates(self):
        return self.getObjects( 'PolicyStmtState') 


    def getStpBridgeState(self,
                          Vlan):
        obj =  { 
                'Vlan' : Vlan
                }
        reqUrl =  self.urlBase+'StpBridgeState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpBridgeStateById(self, objectId ):
        reqUrl =  self.urlBase+'StpBridgeState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllStpBridgeStates(self):
        return self.getObjects( 'StpBridgeState') 


    def getVrrpIntfState(self,
                         IfIndex,
                         VRID):
        obj =  { 
                'IfIndex' : IfIndex
                'VRID' : VRID
                }
        reqUrl =  self.urlBase+'VrrpIntfState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVrrpIntfStateById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpIntfState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVrrpIntfStates(self):
        return self.getObjects( 'VrrpIntfState') 


    def createVxlanInterfacesInterfaceVtepInstancesBindVxlanId(self,
                                                               VtepId,
                                                               InnerVlanHandlingMode,
                                                               SourceInterface,
                                                               VxlanId,
                                                               MulticastIp,
                                                               VtepName,
                                                               Name):
        obj =  { 
                'VtepId' : VtepId
                'InnerVlanHandlingMode' : InnerVlanHandlingMode
                'SourceInterface' : SourceInterface
                'VxlanId' : VxlanId
                'MulticastIp' : MulticastIp
                'VtepName' : VtepName
                'Name' : Name
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanInterfacesInterfaceVtepInstancesBindVxlanId(self,
                                                               VtepId,
                                                               InnerVlanHandlingMode = None,
                                                               SourceInterface = None,
                                                               VxlanId,
                                                               MulticastIp = None,
                                                               VtepName = None,
                                                               Name):
        obj =  { 
                'VtepId' : VtepId
                'InnerVlanHandlingMode' : InnerVlanHandlingMode
                'SourceInterface' : SourceInterface
                'VxlanId' : VxlanId
                'MulticastIp' : MulticastIp
                'VtepName' : VtepName
                'Name' : Name
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanInterfacesInterfaceVtepInstancesBindVxlanIdById(self,
                                                                    objectId,
                                                                    InnerVlanHandlingMode = None,
                                                                    SourceInterface = None,
                                                                    MulticastIp = None,
                                                                    VtepName = None):
        obj =  { 
                'objectId': objectId
                'InnerVlanHandlingMode' : InnerVlanHandlingMode
                'SourceInterface' : SourceInterface
                'MulticastIp' : MulticastIp
                'VtepName' : VtepName
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanInterfacesInterfaceVtepInstancesBindVxlanId(self,
                                                               VtepId,
                                                               VxlanId,
                                                               Name):
        obj =  { 
                'VtepId' : VtepId
                'VxlanId' : VxlanId
                'Name' : Name
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanInterfacesInterfaceVtepInstancesBindVxlanIdById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVxlanInterfacesInterfaceVtepInstancesBindVxlanId(self,
                                                            VtepId,
                                                            VxlanId,
                                                            Name):
        obj =  { 
                'VtepId' : VtepId
                'VxlanId' : VxlanId
                'Name' : Name
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanInterfacesInterfaceVtepInstancesBindVxlanIdById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceVtepInstancesBindVxlanId'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanInterfacesInterfaceVtepInstancesBindVxlanIds(self):
        return self.getObjects( 'VxlanInterfacesInterfaceVtepInstancesBindVxlanId') 


    def getVxlanStateStaticVxlanTunnelAddressFamilyBindVxlanId(self,
                                                               VxlanTunnelId,
                                                               Af,
                                                               VxlanId):
        obj =  { 
                'VxlanTunnelId' : VxlanTunnelId
                'Af' : Af
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanStateStaticVxlanTunnelAddressFamilyBindVxlanId'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanStateStaticVxlanTunnelAddressFamilyBindVxlanIdById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanStateStaticVxlanTunnelAddressFamilyBindVxlanId'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanStateStaticVxlanTunnelAddressFamilyBindVxlanIds(self):
        return self.getObjects( 'VxlanStateStaticVxlanTunnelAddressFamilyBindVxlanId') 


    def createBGPGlobal(self,
                        ASNum,
                        RouterId,
                        UseMultiplePaths='false',
                        EBGPMaxPaths= 0,
                        EBGPAllowMultipleAS='false',
                        IBGPMaxPaths= 0):
        obj =  { 
                'ASNum' : ASNum
                'RouterId' : RouterId
                'UseMultiplePaths' : UseMultiplePaths
                'EBGPMaxPaths' : EBGPMaxPaths
                'EBGPAllowMultipleAS' : EBGPAllowMultipleAS
                'IBGPMaxPaths' : IBGPMaxPaths
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPGlobal(self,
                        ASNum = None,
                        RouterId,
                        UseMultiplePaths = None,
                        EBGPMaxPaths = None,
                        EBGPAllowMultipleAS = None,
                        IBGPMaxPaths = None):
        obj =  { 
                'ASNum' : ASNum
                'RouterId' : RouterId
                'UseMultiplePaths' : UseMultiplePaths
                'EBGPMaxPaths' : EBGPMaxPaths
                'EBGPAllowMultipleAS' : EBGPAllowMultipleAS
                'IBGPMaxPaths' : IBGPMaxPaths
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPGlobalById(self,
                             objectId,
                             ASNum = None,
                             UseMultiplePaths = None,
                             EBGPMaxPaths = None,
                             EBGPAllowMultipleAS = None,
                             IBGPMaxPaths = None):
        obj =  { 
                'objectId': objectId
                'ASNum' : ASNum
                'UseMultiplePaths' : UseMultiplePaths
                'EBGPMaxPaths' : EBGPMaxPaths
                'EBGPAllowMultipleAS' : EBGPAllowMultipleAS
                'IBGPMaxPaths' : IBGPMaxPaths
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPGlobal(self,
                        RouterId):
        obj =  { 
                'RouterId' : RouterId
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPGlobal(self,
                     RouterId):
        obj =  { 
                'RouterId' : RouterId
                }
        reqUrl =  self.urlBase+'BGPGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPGlobalById(self, objectId ):
        reqUrl =  self.urlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPGlobals(self):
        return self.getObjects( 'BGPGlobal') 


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
                'IfIpAddress' : IfIpAddress
                'AddressLessIf' : AddressLessIf
                'IfAreaId' : IfAreaId
                'IfType' : IfType
                'IfAdminStat' : IfAdminStat
                'IfRtrPriority' : IfRtrPriority
                'IfTransitDelay' : IfTransitDelay
                'IfRetransInterval' : IfRetransInterval
                'IfHelloInterval' : IfHelloInterval
                'IfRtrDeadInterval' : IfRtrDeadInterval
                'IfPollInterval' : IfPollInterval
                'IfAuthKey' : IfAuthKey
                'IfMulticastForwarding' : IfMulticastForwarding
                'IfDemand' : IfDemand
                'IfAuthType' : IfAuthType
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


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
        obj =  { 
                'IfIpAddress' : IfIpAddress
                'AddressLessIf' : AddressLessIf
                'IfAreaId' : IfAreaId
                'IfType' : IfType
                'IfAdminStat' : IfAdminStat
                'IfRtrPriority' : IfRtrPriority
                'IfTransitDelay' : IfTransitDelay
                'IfRetransInterval' : IfRetransInterval
                'IfHelloInterval' : IfHelloInterval
                'IfRtrDeadInterval' : IfRtrDeadInterval
                'IfPollInterval' : IfPollInterval
                'IfAuthKey' : IfAuthKey
                'IfMulticastForwarding' : IfMulticastForwarding
                'IfDemand' : IfDemand
                'IfAuthType' : IfAuthType
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


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
        obj =  { 
                'objectId': objectId
                'IfAreaId' : IfAreaId
                'IfType' : IfType
                'IfAdminStat' : IfAdminStat
                'IfRtrPriority' : IfRtrPriority
                'IfTransitDelay' : IfTransitDelay
                'IfRetransInterval' : IfRetransInterval
                'IfHelloInterval' : IfHelloInterval
                'IfRtrDeadInterval' : IfRtrDeadInterval
                'IfPollInterval' : IfPollInterval
                'IfAuthKey' : IfAuthKey
                'IfMulticastForwarding' : IfMulticastForwarding
                'IfDemand' : IfDemand
                'IfAuthType' : IfAuthType
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfEntryConfig(self,
                                IfIpAddress,
                                AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress
                'AddressLessIf' : AddressLessIf
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfIfEntryConfig(self,
                             IfIpAddress,
                             AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress
                'AddressLessIf' : AddressLessIf
                }
        reqUrl =  self.urlBase+'OspfIfEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfIfEntryConfigs(self):
        return self.getObjects( 'OspfIfEntryConfig') 


    def getOspfAreaEntryState(self,
                              AreaId):
        obj =  { 
                'AreaId' : AreaId
                }
        reqUrl =  self.urlBase+'OspfAreaEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfAreaEntryStates(self):
        return self.getObjects( 'OspfAreaEntryState') 


    def createOspfAreaAggregateEntryConfig(self,
                                           AreaAggregateLsdbType,
                                           AreaAggregateAreaID,
                                           AreaAggregateNet,
                                           AreaAggregateMask,
                                           AreaAggregateEffect,
                                           AreaAggregateExtRouteTag):
        obj =  { 
                'AreaAggregateLsdbType' : AreaAggregateLsdbType
                'AreaAggregateAreaID' : AreaAggregateAreaID
                'AreaAggregateNet' : AreaAggregateNet
                'AreaAggregateMask' : AreaAggregateMask
                'AreaAggregateEffect' : AreaAggregateEffect
                'AreaAggregateExtRouteTag' : AreaAggregateExtRouteTag
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfAreaAggregateEntryConfig(self,
                                           AreaAggregateLsdbType,
                                           AreaAggregateAreaID,
                                           AreaAggregateNet,
                                           AreaAggregateMask,
                                           AreaAggregateEffect = None,
                                           AreaAggregateExtRouteTag = None):
        obj =  { 
                'AreaAggregateLsdbType' : AreaAggregateLsdbType
                'AreaAggregateAreaID' : AreaAggregateAreaID
                'AreaAggregateNet' : AreaAggregateNet
                'AreaAggregateMask' : AreaAggregateMask
                'AreaAggregateEffect' : AreaAggregateEffect
                'AreaAggregateExtRouteTag' : AreaAggregateExtRouteTag
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfAreaAggregateEntryConfigById(self,
                                                objectId,
                                                AreaAggregateEffect = None,
                                                AreaAggregateExtRouteTag = None):
        obj =  { 
                'objectId': objectId
                'AreaAggregateEffect' : AreaAggregateEffect
                'AreaAggregateExtRouteTag' : AreaAggregateExtRouteTag
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaAggregateEntryConfig(self,
                                           AreaAggregateLsdbType,
                                           AreaAggregateAreaID,
                                           AreaAggregateNet,
                                           AreaAggregateMask):
        obj =  { 
                'AreaAggregateLsdbType' : AreaAggregateLsdbType
                'AreaAggregateAreaID' : AreaAggregateAreaID
                'AreaAggregateNet' : AreaAggregateNet
                'AreaAggregateMask' : AreaAggregateMask
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaAggregateEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfAreaAggregateEntryConfig(self,
                                        AreaAggregateLsdbType,
                                        AreaAggregateAreaID,
                                        AreaAggregateNet,
                                        AreaAggregateMask):
        obj =  { 
                'AreaAggregateLsdbType' : AreaAggregateLsdbType
                'AreaAggregateAreaID' : AreaAggregateAreaID
                'AreaAggregateNet' : AreaAggregateNet
                'AreaAggregateMask' : AreaAggregateMask
                }
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaAggregateEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaAggregateEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfAreaAggregateEntryConfigs(self):
        return self.getObjects( 'OspfAreaAggregateEntryConfig') 


    def createVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId(self,
                                                                                TunnelSourceIp,
                                                                                VxlanTunnelId,
                                                                                Name,
                                                                                Af,
                                                                                TunnelDestinationIp,
                                                                                VxlanId,
                                                                                VxlanTunnelName):
        obj =  { 
                'TunnelSourceIp' : TunnelSourceIp
                'VxlanTunnelId' : VxlanTunnelId
                'Name' : Name
                'Af' : Af
                'TunnelDestinationIp' : TunnelDestinationIp
                'VxlanId' : VxlanId
                'VxlanTunnelName' : VxlanTunnelName
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId(self,
                                                                                TunnelSourceIp = None,
                                                                                VxlanTunnelId,
                                                                                Name,
                                                                                Af,
                                                                                TunnelDestinationIp = None,
                                                                                VxlanId,
                                                                                VxlanTunnelName = None):
        obj =  { 
                'TunnelSourceIp' : TunnelSourceIp
                'VxlanTunnelId' : VxlanTunnelId
                'Name' : Name
                'Af' : Af
                'TunnelDestinationIp' : TunnelDestinationIp
                'VxlanId' : VxlanId
                'VxlanTunnelName' : VxlanTunnelName
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanIdById(self,
                                                                                     objectId,
                                                                                     TunnelSourceIp = None,
                                                                                     TunnelDestinationIp = None,
                                                                                     VxlanTunnelName = None):
        obj =  { 
                'objectId': objectId
                'TunnelSourceIp' : TunnelSourceIp
                'TunnelDestinationIp' : TunnelDestinationIp
                'VxlanTunnelName' : VxlanTunnelName
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId(self,
                                                                                VxlanTunnelId,
                                                                                Name,
                                                                                Af,
                                                                                VxlanId):
        obj =  { 
                'VxlanTunnelId' : VxlanTunnelId
                'Name' : Name
                'Af' : Af
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanIdById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId(self,
                                                                             VxlanTunnelId,
                                                                             Name,
                                                                             Af,
                                                                             VxlanId):
        obj =  { 
                'VxlanTunnelId' : VxlanTunnelId
                'Name' : Name
                'Af' : Af
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanIdById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanIds(self):
        return self.getObjects( 'VxlanInterfacesInterfaceStaticVxlanTunnelAddressFamilyBindVxlanId') 


    def createBfdSession(self,
                         IpAddr,
                         PerLink='false',
                         Owner='user'):
        obj =  { 
                'IpAddr' : IpAddr
                'PerLink' : PerLink
                'Owner' : Owner
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBfdSession(self,
                         IpAddr,
                         PerLink = None,
                         Owner = None):
        obj =  { 
                'IpAddr' : IpAddr
                'PerLink' : PerLink
                'Owner' : Owner
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBfdSessionById(self,
                              objectId,
                              PerLink = None,
                              Owner = None):
        obj =  { 
                'objectId': objectId
                'PerLink' : PerLink
                'Owner' : Owner
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdSession(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdSessionById(self, objectId ):
        reqUrl =  self.urlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBfdSession(self,
                      IpAddr):
        obj =  { 
                'IpAddr' : IpAddr
                }
        reqUrl =  self.urlBase+'BfdSession'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdSessionById(self, objectId ):
        reqUrl =  self.urlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBfdSessions(self):
        return self.getObjects( 'BfdSession') 


    def getPolicyConditionState(self,
                                Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyConditionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyConditionStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyConditionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyConditionStates(self):
        return self.getObjects( 'PolicyConditionState') 


    def createVrrpIntf(self,
                       IfIndex,
                       VRID,
                       Priority= 100,
                       VirtualIPv4Addr,
                       AdvertisementInterval=1,
                       PreemptMode='true',
                       AcceptMode='false'):
        obj =  { 
                'IfIndex' : IfIndex
                'VRID' : VRID
                'Priority' : Priority
                'VirtualIPv4Addr' : VirtualIPv4Addr
                'AdvertisementInterval' : AdvertisementInterval
                'PreemptMode' : PreemptMode
                'AcceptMode' : AcceptMode
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVrrpIntf(self,
                       IfIndex,
                       VRID,
                       Priority = None,
                       VirtualIPv4Addr = None,
                       AdvertisementInterval = None,
                       PreemptMode = None,
                       AcceptMode = None):
        obj =  { 
                'IfIndex' : IfIndex
                'VRID' : VRID
                'Priority' : Priority
                'VirtualIPv4Addr' : VirtualIPv4Addr
                'AdvertisementInterval' : AdvertisementInterval
                'PreemptMode' : PreemptMode
                'AcceptMode' : AcceptMode
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVrrpIntfById(self,
                            objectId,
                            Priority = None,
                            VirtualIPv4Addr = None,
                            AdvertisementInterval = None,
                            PreemptMode = None,
                            AcceptMode = None):
        obj =  { 
                'objectId': objectId
                'Priority' : Priority
                'VirtualIPv4Addr' : VirtualIPv4Addr
                'AdvertisementInterval' : AdvertisementInterval
                'PreemptMode' : PreemptMode
                'AcceptMode' : AcceptMode
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVrrpIntf(self,
                       IfIndex,
                       VRID):
        obj =  { 
                'IfIndex' : IfIndex
                'VRID' : VRID
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVrrpIntfById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVrrpIntf(self,
                    IfIndex,
                    VRID):
        obj =  { 
                'IfIndex' : IfIndex
                'VRID' : VRID
                }
        reqUrl =  self.urlBase+'VrrpIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVrrpIntfById(self, objectId ):
        reqUrl =  self.urlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVrrpIntfs(self):
        return self.getObjects( 'VrrpIntf') 


    def getPolicyDefinitionState(self,
                                 Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyDefinitionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyDefinitionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyDefinitionStates(self):
        return self.getObjects( 'PolicyDefinitionState') 


    def createOspfIfMetricEntryConfig(self,
                                      IfMetricAddressLessIf,
                                      IfMetricTOS,
                                      IfMetricIpAddress,
                                      IfMetricValue):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf
                'IfMetricTOS' : IfMetricTOS
                'IfMetricIpAddress' : IfMetricIpAddress
                'IfMetricValue' : IfMetricValue
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfIfMetricEntryConfig(self,
                                      IfMetricAddressLessIf,
                                      IfMetricTOS,
                                      IfMetricIpAddress,
                                      IfMetricValue = None):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf
                'IfMetricTOS' : IfMetricTOS
                'IfMetricIpAddress' : IfMetricIpAddress
                'IfMetricValue' : IfMetricValue
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfIfMetricEntryConfigById(self,
                                           objectId,
                                           IfMetricValue = None):
        obj =  { 
                'objectId': objectId
                'IfMetricValue' : IfMetricValue
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfMetricEntryConfig(self,
                                      IfMetricAddressLessIf,
                                      IfMetricTOS,
                                      IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf
                'IfMetricTOS' : IfMetricTOS
                'IfMetricIpAddress' : IfMetricIpAddress
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfMetricEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfIfMetricEntryConfig(self,
                                   IfMetricAddressLessIf,
                                   IfMetricTOS,
                                   IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf
                'IfMetricTOS' : IfMetricTOS
                'IfMetricIpAddress' : IfMetricIpAddress
                }
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfMetricEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfMetricEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfIfMetricEntryConfigs(self):
        return self.getObjects( 'OspfIfMetricEntryConfig') 


    def getLogicalIntfState(self,
                            Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'LogicalIntfState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteLogicalIntfStateById(self, objectId ):
        reqUrl =  self.urlBase+'LogicalIntfState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllLogicalIntfStates(self):
        return self.getObjects( 'LogicalIntfState') 


    def createVxlanVxlanInstanceAccessTypeMac(self,
                                              VxlanId,
                                              Mac,
                                              L2interface,
                                              VlanId,
                                              InterfaceName):
        obj =  { 
                'VxlanId' : VxlanId
                'Mac' : Mac
                'L2interface' : L2interface
                'VlanId' : VlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceAccessTypeMac(self,
                                              VxlanId,
                                              Mac = None,
                                              L2interface = None,
                                              VlanId = None,
                                              InterfaceName = None):
        obj =  { 
                'VxlanId' : VxlanId
                'Mac' : Mac
                'L2interface' : L2interface
                'VlanId' : VlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceAccessTypeMacById(self,
                                                   objectId,
                                                   Mac = None,
                                                   L2interface = None,
                                                   VlanId = None,
                                                   InterfaceName = None):
        obj =  { 
                'objectId': objectId
                'Mac' : Mac
                'L2interface' : L2interface
                'VlanId' : VlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeMac(self,
                                              VxlanId):
        obj =  { 
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeMacById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVxlanVxlanInstanceAccessTypeMac(self,
                                           VxlanId):
        obj =  { 
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeMacById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeMac'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanVxlanInstanceAccessTypeMacs(self):
        return self.getObjects( 'VxlanVxlanInstanceAccessTypeMac') 


    def createBGPNeighbor(self,
                          PeerAS,
                          LocalAS= 0,
                          AuthPassword='',
                          Description='',
                          NeighborAddress,
                          IfIndex,
                          RouteReflectorClusterId= 0,
                          RouteReflectorClient='false',
                          MultiHopEnable='false',
                          MultiHopTTL='0',
                          ConnectRetryTime= 60,
                          HoldTime= 180,
                          KeepaliveTime= 60,
                          AddPathsRx='false',
                          AddPathsMaxTx='0',
                          PeerGroup='',
                          BfdEnable='false'):
        obj =  { 
                'PeerAS' : PeerAS
                'LocalAS' : LocalAS
                'AuthPassword' : AuthPassword
                'Description' : Description
                'NeighborAddress' : NeighborAddress
                'IfIndex' : IfIndex
                'RouteReflectorClusterId' : RouteReflectorClusterId
                'RouteReflectorClient' : RouteReflectorClient
                'MultiHopEnable' : MultiHopEnable
                'MultiHopTTL' : MultiHopTTL
                'ConnectRetryTime' : ConnectRetryTime
                'HoldTime' : HoldTime
                'KeepaliveTime' : KeepaliveTime
                'AddPathsRx' : AddPathsRx
                'AddPathsMaxTx' : AddPathsMaxTx
                'PeerGroup' : PeerGroup
                'BfdEnable' : BfdEnable
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPNeighbor(self,
                          PeerAS = None,
                          LocalAS = None,
                          AuthPassword = None,
                          Description = None,
                          NeighborAddress,
                          IfIndex,
                          RouteReflectorClusterId = None,
                          RouteReflectorClient = None,
                          MultiHopEnable = None,
                          MultiHopTTL = None,
                          ConnectRetryTime = None,
                          HoldTime = None,
                          KeepaliveTime = None,
                          AddPathsRx = None,
                          AddPathsMaxTx = None,
                          PeerGroup = None,
                          BfdEnable = None):
        obj =  { 
                'PeerAS' : PeerAS
                'LocalAS' : LocalAS
                'AuthPassword' : AuthPassword
                'Description' : Description
                'NeighborAddress' : NeighborAddress
                'IfIndex' : IfIndex
                'RouteReflectorClusterId' : RouteReflectorClusterId
                'RouteReflectorClient' : RouteReflectorClient
                'MultiHopEnable' : MultiHopEnable
                'MultiHopTTL' : MultiHopTTL
                'ConnectRetryTime' : ConnectRetryTime
                'HoldTime' : HoldTime
                'KeepaliveTime' : KeepaliveTime
                'AddPathsRx' : AddPathsRx
                'AddPathsMaxTx' : AddPathsMaxTx
                'PeerGroup' : PeerGroup
                'BfdEnable' : BfdEnable
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPNeighborById(self,
                               objectId,
                               PeerAS = None,
                               LocalAS = None,
                               AuthPassword = None,
                               Description = None,
                               RouteReflectorClusterId = None,
                               RouteReflectorClient = None,
                               MultiHopEnable = None,
                               MultiHopTTL = None,
                               ConnectRetryTime = None,
                               HoldTime = None,
                               KeepaliveTime = None,
                               AddPathsRx = None,
                               AddPathsMaxTx = None,
                               PeerGroup = None,
                               BfdEnable = None):
        obj =  { 
                'objectId': objectId
                'PeerAS' : PeerAS
                'LocalAS' : LocalAS
                'AuthPassword' : AuthPassword
                'Description' : Description
                'RouteReflectorClusterId' : RouteReflectorClusterId
                'RouteReflectorClient' : RouteReflectorClient
                'MultiHopEnable' : MultiHopEnable
                'MultiHopTTL' : MultiHopTTL
                'ConnectRetryTime' : ConnectRetryTime
                'HoldTime' : HoldTime
                'KeepaliveTime' : KeepaliveTime
                'AddPathsRx' : AddPathsRx
                'AddPathsMaxTx' : AddPathsMaxTx
                'PeerGroup' : PeerGroup
                'BfdEnable' : BfdEnable
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPNeighbor(self,
                          NeighborAddress,
                          IfIndex):
        obj =  { 
                'NeighborAddress' : NeighborAddress
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPNeighborById(self, objectId ):
        reqUrl =  self.urlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPNeighbor(self,
                       NeighborAddress,
                       IfIndex):
        obj =  { 
                'NeighborAddress' : NeighborAddress
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'BGPNeighbor'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPNeighborById(self, objectId ):
        reqUrl =  self.urlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPNeighbors(self):
        return self.getObjects( 'BGPNeighbor') 


    def createVxlanVxlanInstanceAccessTypeL3interfaceL3interface(self,
                                                                 VxlanId,
                                                                 InterfaceName):
        obj =  { 
                'VxlanId' : VxlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceAccessTypeL3interfaceL3interface(self,
                                                                 VxlanId,
                                                                 InterfaceName):
        obj =  { 
                'VxlanId' : VxlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateVxlanVxlanInstanceAccessTypeL3interfaceL3interfaceById(self,
                                                                      objectId):
        obj =  { 
                'objectId': objectId
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeL3interfaceL3interface(self,
                                                                 VxlanId,
                                                                 InterfaceName):
        obj =  { 
                'VxlanId' : VxlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeL3interfaceL3interfaceById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getVxlanVxlanInstanceAccessTypeL3interfaceL3interface(self,
                                                              VxlanId,
                                                              InterfaceName):
        obj =  { 
                'VxlanId' : VxlanId
                'InterfaceName' : InterfaceName
                }
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanVxlanInstanceAccessTypeL3interfaceL3interfaceById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanVxlanInstanceAccessTypeL3interfaceL3interface'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanVxlanInstanceAccessTypeL3interfaceL3interfaces(self):
        return self.getObjects( 'VxlanVxlanInstanceAccessTypeL3interfaceL3interface') 


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
                'Vlan' : Vlan
                'Address' : Address
                'Priority' : Priority
                'MaxAge' : MaxAge
                'HelloTime' : HelloTime
                'ForwardDelay' : ForwardDelay
                'ForceVersion' : ForceVersion
                'TxHoldCount' : TxHoldCount
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateStpBridgeInstance(self,
                                Vlan,
                                Address = None,
                                Priority = None,
                                MaxAge = None,
                                HelloTime = None,
                                ForwardDelay = None,
                                ForceVersion = None,
                                TxHoldCount = None):
        obj =  { 
                'Vlan' : Vlan
                'Address' : Address
                'Priority' : Priority
                'MaxAge' : MaxAge
                'HelloTime' : HelloTime
                'ForwardDelay' : ForwardDelay
                'ForceVersion' : ForceVersion
                'TxHoldCount' : TxHoldCount
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateStpBridgeInstanceById(self,
                                     objectId,
                                     Address = None,
                                     Priority = None,
                                     MaxAge = None,
                                     HelloTime = None,
                                     ForwardDelay = None,
                                     ForceVersion = None,
                                     TxHoldCount = None):
        obj =  { 
                'objectId': objectId
                'Address' : Address
                'Priority' : Priority
                'MaxAge' : MaxAge
                'HelloTime' : HelloTime
                'ForwardDelay' : ForwardDelay
                'ForceVersion' : ForceVersion
                'TxHoldCount' : TxHoldCount
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpBridgeInstance(self,
                                Vlan):
        obj =  { 
                'Vlan' : Vlan
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.urlBase+'StpBridgeInstance'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getStpBridgeInstance(self,
                             Vlan):
        obj =  { 
                'Vlan' : Vlan
                }
        reqUrl =  self.urlBase+'StpBridgeInstance'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.urlBase+'StpBridgeInstance'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllStpBridgeInstances(self):
        return self.getObjects( 'StpBridgeInstance') 


    def getOspfExtLsdbEntryState(self,
                                 ExtLsdbType,
                                 ExtLsdbLsid,
                                 ExtLsdbRouterId):
        obj =  { 
                'ExtLsdbType' : ExtLsdbType
                'ExtLsdbLsid' : ExtLsdbLsid
                'ExtLsdbRouterId' : ExtLsdbRouterId
                }
        reqUrl =  self.urlBase+'OspfExtLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfExtLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfExtLsdbEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfExtLsdbEntryStates(self):
        return self.getObjects( 'OspfExtLsdbEntryState') 


    def createBfdInterface(self,
                           IfIndex,
                           LocalMultiplier= 3,
                           DesiredMinTxInterval= 1000,
                           RequiredMinRxInterval= 1000,
                           RequiredMinEchoRxInterval= 0,
                           DemandEnabled='false',
                           AuthenticationEnabled='false',
                           AuthType='simple',
                           AuthKeyId= 1,
                           AuthData='snaproute'):
        obj =  { 
                'IfIndex' : IfIndex
                'LocalMultiplier' : LocalMultiplier
                'DesiredMinTxInterval' : DesiredMinTxInterval
                'RequiredMinRxInterval' : RequiredMinRxInterval
                'RequiredMinEchoRxInterval' : RequiredMinEchoRxInterval
                'DemandEnabled' : DemandEnabled
                'AuthenticationEnabled' : AuthenticationEnabled
                'AuthType' : AuthType
                'AuthKeyId' : AuthKeyId
                'AuthData' : AuthData
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBfdInterface(self,
                           IfIndex,
                           LocalMultiplier = None,
                           DesiredMinTxInterval = None,
                           RequiredMinRxInterval = None,
                           RequiredMinEchoRxInterval = None,
                           DemandEnabled = None,
                           AuthenticationEnabled = None,
                           AuthType = None,
                           AuthKeyId = None,
                           AuthData = None):
        obj =  { 
                'IfIndex' : IfIndex
                'LocalMultiplier' : LocalMultiplier
                'DesiredMinTxInterval' : DesiredMinTxInterval
                'RequiredMinRxInterval' : RequiredMinRxInterval
                'RequiredMinEchoRxInterval' : RequiredMinEchoRxInterval
                'DemandEnabled' : DemandEnabled
                'AuthenticationEnabled' : AuthenticationEnabled
                'AuthType' : AuthType
                'AuthKeyId' : AuthKeyId
                'AuthData' : AuthData
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBfdInterfaceById(self,
                                objectId,
                                LocalMultiplier = None,
                                DesiredMinTxInterval = None,
                                RequiredMinRxInterval = None,
                                RequiredMinEchoRxInterval = None,
                                DemandEnabled = None,
                                AuthenticationEnabled = None,
                                AuthType = None,
                                AuthKeyId = None,
                                AuthData = None):
        obj =  { 
                'objectId': objectId
                'LocalMultiplier' : LocalMultiplier
                'DesiredMinTxInterval' : DesiredMinTxInterval
                'RequiredMinRxInterval' : RequiredMinRxInterval
                'RequiredMinEchoRxInterval' : RequiredMinEchoRxInterval
                'DemandEnabled' : DemandEnabled
                'AuthenticationEnabled' : AuthenticationEnabled
                'AuthType' : AuthType
                'AuthKeyId' : AuthKeyId
                'AuthData' : AuthData
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdInterface(self,
                           IfIndex):
        obj =  { 
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdInterfaceById(self, objectId ):
        reqUrl =  self.urlBase+'BfdInterface'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBfdInterface(self,
                        IfIndex):
        obj =  { 
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'BfdInterface'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBfdInterfaceById(self, objectId ):
        reqUrl =  self.urlBase+'BfdInterface'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBfdInterfaces(self):
        return self.getObjects( 'BfdInterface') 


    def createSystemLogging(self,
                            SRLogger,
                            SystemLogging='on'):
        obj =  { 
                'SRLogger' : SRLogger
                'SystemLogging' : SystemLogging
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateSystemLogging(self,
                            SRLogger,
                            SystemLogging = None):
        obj =  { 
                'SRLogger' : SRLogger
                'SystemLogging' : SystemLogging
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateSystemLoggingById(self,
                                 objectId,
                                 SystemLogging = None):
        obj =  { 
                'objectId': objectId
                'SystemLogging' : SystemLogging
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteSystemLogging(self,
                            SRLogger):
        obj =  { 
                'SRLogger' : SRLogger
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteSystemLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'SystemLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getSystemLogging(self,
                         SRLogger):
        obj =  { 
                'SRLogger' : SRLogger
                }
        reqUrl =  self.urlBase+'SystemLogging'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteSystemLoggingById(self, objectId ):
        reqUrl =  self.urlBase+'SystemLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllSystemLoggings(self):
        return self.getObjects( 'SystemLogging') 


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
                'RouterId' : RouterId
                'AdminStat' : AdminStat
                'ASBdrRtrStatus' : ASBdrRtrStatus
                'TOSSupport' : TOSSupport
                'ExtLsdbLimit' : ExtLsdbLimit
                'MulticastExtensions' : MulticastExtensions
                'ExitOverflowInterval' : ExitOverflowInterval
                'DemandExtensions' : DemandExtensions
                'RFC1583Compatibility' : RFC1583Compatibility
                'ReferenceBandwidth' : ReferenceBandwidth
                'RestartSupport' : RestartSupport
                'RestartInterval' : RestartInterval
                'RestartStrictLsaChecking' : RestartStrictLsaChecking
                'StubRouterAdvertisement' : StubRouterAdvertisement
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


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
        obj =  { 
                'RouterId' : RouterId
                'AdminStat' : AdminStat
                'ASBdrRtrStatus' : ASBdrRtrStatus
                'TOSSupport' : TOSSupport
                'ExtLsdbLimit' : ExtLsdbLimit
                'MulticastExtensions' : MulticastExtensions
                'ExitOverflowInterval' : ExitOverflowInterval
                'DemandExtensions' : DemandExtensions
                'RFC1583Compatibility' : RFC1583Compatibility
                'ReferenceBandwidth' : ReferenceBandwidth
                'RestartSupport' : RestartSupport
                'RestartInterval' : RestartInterval
                'RestartStrictLsaChecking' : RestartStrictLsaChecking
                'StubRouterAdvertisement' : StubRouterAdvertisement
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


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
        obj =  { 
                'objectId': objectId
                'AdminStat' : AdminStat
                'ASBdrRtrStatus' : ASBdrRtrStatus
                'TOSSupport' : TOSSupport
                'ExtLsdbLimit' : ExtLsdbLimit
                'MulticastExtensions' : MulticastExtensions
                'ExitOverflowInterval' : ExitOverflowInterval
                'DemandExtensions' : DemandExtensions
                'RFC1583Compatibility' : RFC1583Compatibility
                'ReferenceBandwidth' : ReferenceBandwidth
                'RestartSupport' : RestartSupport
                'RestartInterval' : RestartInterval
                'RestartStrictLsaChecking' : RestartStrictLsaChecking
                'StubRouterAdvertisement' : StubRouterAdvertisement
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfGlobalConfig(self,
                               RouterId):
        obj =  { 
                'RouterId' : RouterId
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfGlobalConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfGlobalConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfGlobalConfig(self,
                            RouterId):
        obj =  { 
                'RouterId' : RouterId
                }
        reqUrl =  self.urlBase+'OspfGlobalConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfGlobalConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfGlobalConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfGlobalConfigs(self):
        return self.getObjects( 'OspfGlobalConfig') 


    def getBGPPolicyActionState(self,
                                Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyActionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyActionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyActionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyActionStates(self):
        return self.getObjects( 'BGPPolicyActionState') 


    def getOspfAsLsdbEntryState(self,
                                AsLsdbType,
                                AsLsdbRouterId,
                                AsLsdbLsid):
        obj =  { 
                'AsLsdbType' : AsLsdbType
                'AsLsdbRouterId' : AsLsdbRouterId
                'AsLsdbLsid' : AsLsdbLsid
                }
        reqUrl =  self.urlBase+'OspfAsLsdbEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAsLsdbEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAsLsdbEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfAsLsdbEntryStates(self):
        return self.getObjects( 'OspfAsLsdbEntryState') 


    def getBGPPolicyDefinitionState(self,
                                    Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinitionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyDefinitionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyDefinitionStates(self):
        return self.getObjects( 'BGPPolicyDefinitionState') 


    def getPortState(self,
                     PortNum):
        obj =  { 
                'PortNum' : PortNum
                }
        reqUrl =  self.urlBase+'PortState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePortStateById(self, objectId ):
        reqUrl =  self.urlBase+'PortState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPortStates(self):
        return self.getObjects( 'PortState') 


    def createBGPPolicyAction(self,
                              Name,
                              ActionType,
                              GenerateASSet,
                              SendSummaryOnly):
        obj =  { 
                'Name' : Name
                'ActionType' : ActionType
                'GenerateASSet' : GenerateASSet
                'SendSummaryOnly' : SendSummaryOnly
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyAction(self,
                              Name,
                              ActionType = None,
                              GenerateASSet = None,
                              SendSummaryOnly = None):
        obj =  { 
                'Name' : Name
                'ActionType' : ActionType
                'GenerateASSet' : GenerateASSet
                'SendSummaryOnly' : SendSummaryOnly
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyActionById(self,
                                   objectId,
                                   ActionType = None,
                                   GenerateASSet = None,
                                   SendSummaryOnly = None):
        obj =  { 
                'objectId': objectId
                'ActionType' : ActionType
                'GenerateASSet' : GenerateASSet
                'SendSummaryOnly' : SendSummaryOnly
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyAction(self,
                              Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPPolicyAction(self,
                           Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyAction'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyActionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyActions(self):
        return self.getObjects( 'BGPPolicyAction') 


    def getBGPPolicyStmtState(self,
                              Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyStmtState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyStmtStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyStmtState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyStmtStates(self):
        return self.getObjects( 'BGPPolicyStmtState') 


    def createOspfHostEntryConfig(self,
                                  HostTOS,
                                  HostIpAddress,
                                  HostMetric,
                                  HostCfgAreaID):
        obj =  { 
                'HostTOS' : HostTOS
                'HostIpAddress' : HostIpAddress
                'HostMetric' : HostMetric
                'HostCfgAreaID' : HostCfgAreaID
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfHostEntryConfig(self,
                                  HostTOS,
                                  HostIpAddress,
                                  HostMetric = None,
                                  HostCfgAreaID = None):
        obj =  { 
                'HostTOS' : HostTOS
                'HostIpAddress' : HostIpAddress
                'HostMetric' : HostMetric
                'HostCfgAreaID' : HostCfgAreaID
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfHostEntryConfigById(self,
                                       objectId,
                                       HostMetric = None,
                                       HostCfgAreaID = None):
        obj =  { 
                'objectId': objectId
                'HostMetric' : HostMetric
                'HostCfgAreaID' : HostCfgAreaID
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfHostEntryConfig(self,
                                  HostTOS,
                                  HostIpAddress):
        obj =  { 
                'HostTOS' : HostTOS
                'HostIpAddress' : HostIpAddress
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfHostEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfHostEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfHostEntryConfig(self,
                               HostTOS,
                               HostIpAddress):
        obj =  { 
                'HostTOS' : HostTOS
                'HostIpAddress' : HostIpAddress
                }
        reqUrl =  self.urlBase+'OspfHostEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfHostEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfHostEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfHostEntryConfigs(self):
        return self.getObjects( 'OspfHostEntryConfig') 


    def createIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp,
                        Cost,
                        OutgoingIntfType,
                        OutgoingInterface,
                        Protocol):
        obj =  { 
                'DestinationNw' : DestinationNw
                'NetworkMask' : NetworkMask
                'NextHopIp' : NextHopIp
                'Cost' : Cost
                'OutgoingIntfType' : OutgoingIntfType
                'OutgoingInterface' : OutgoingInterface
                'Protocol' : Protocol
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp,
                        Cost = None,
                        OutgoingIntfType = None,
                        OutgoingInterface = None,
                        Protocol = None):
        obj =  { 
                'DestinationNw' : DestinationNw
                'NetworkMask' : NetworkMask
                'NextHopIp' : NextHopIp
                'Cost' : Cost
                'OutgoingIntfType' : OutgoingIntfType
                'OutgoingInterface' : OutgoingInterface
                'Protocol' : Protocol
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateIPv4RouteById(self,
                             objectId,
                             Cost = None,
                             OutgoingIntfType = None,
                             OutgoingInterface = None,
                             Protocol = None):
        obj =  { 
                'objectId': objectId
                'Cost' : Cost
                'OutgoingIntfType' : OutgoingIntfType
                'OutgoingInterface' : OutgoingInterface
                'Protocol' : Protocol
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp):
        obj =  { 
                'DestinationNw' : DestinationNw
                'NetworkMask' : NetworkMask
                'NextHopIp' : NextHopIp
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4RouteById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getIPv4Route(self,
                     DestinationNw,
                     NetworkMask,
                     NextHopIp):
        obj =  { 
                'DestinationNw' : DestinationNw
                'NetworkMask' : NetworkMask
                'NextHopIp' : NextHopIp
                }
        reqUrl =  self.urlBase+'IPv4Route'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteIPv4RouteById(self, objectId ):
        reqUrl =  self.urlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllIPv4Routes(self):
        return self.getObjects( 'IPv4Route') 


    def getVxlanStateVtepInstanceBindVxlanId(self,
                                             VxlanId):
        obj =  { 
                'VxlanId' : VxlanId
                }
        reqUrl =  self.urlBase+'VxlanStateVtepInstanceBindVxlanId'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteVxlanStateVtepInstanceBindVxlanIdById(self, objectId ):
        reqUrl =  self.urlBase+'VxlanStateVtepInstanceBindVxlanId'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllVxlanStateVtepInstanceBindVxlanIds(self):
        return self.getObjects( 'VxlanStateVtepInstanceBindVxlanId') 


    def getPolicyActionState(self,
                             Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyActionState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyActionStateById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyActionState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyActionStates(self):
        return self.getObjects( 'PolicyActionState') 


    def getOspfGlobalState(self,
                           RouterId):
        obj =  { 
                'RouterId' : RouterId
                }
        reqUrl =  self.urlBase+'OspfGlobalState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfGlobalStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfGlobalState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfGlobalStates(self):
        return self.getObjects( 'OspfGlobalState') 


    def getBGPNeighborState(self,
                            NeighborAddress,
                            IfIndex):
        obj =  { 
                'NeighborAddress' : NeighborAddress
                'IfIndex' : IfIndex
                }
        reqUrl =  self.urlBase+'BGPNeighborState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPNeighborStateById(self, objectId ):
        reqUrl =  self.urlBase+'BGPNeighborState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPNeighborStates(self):
        return self.getObjects( 'BGPNeighborState') 


    def getBGPRoute(self,
                    Network,
                    CIDRLen,
                    NextHop):
        obj =  { 
                'Network' : Network
                'CIDRLen' : CIDRLen
                'NextHop' : NextHop
                }
        reqUrl =  self.urlBase+'BGPRoute'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPRouteById(self, objectId ):
        reqUrl =  self.urlBase+'BGPRoute'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPRoutes(self):
        return self.getObjects( 'BGPRoute') 


    def createOspfAreaRangeEntryConfig(self,
                                       AreaRangeAreaId,
                                       AreaRangeNet,
                                       AreaRangeMask,
                                       AreaRangeEffect):
        obj =  { 
                'AreaRangeAreaId' : AreaRangeAreaId
                'AreaRangeNet' : AreaRangeNet
                'AreaRangeMask' : AreaRangeMask
                'AreaRangeEffect' : AreaRangeEffect
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfAreaRangeEntryConfig(self,
                                       AreaRangeAreaId,
                                       AreaRangeNet,
                                       AreaRangeMask = None,
                                       AreaRangeEffect = None):
        obj =  { 
                'AreaRangeAreaId' : AreaRangeAreaId
                'AreaRangeNet' : AreaRangeNet
                'AreaRangeMask' : AreaRangeMask
                'AreaRangeEffect' : AreaRangeEffect
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateOspfAreaRangeEntryConfigById(self,
                                            objectId,
                                            AreaRangeMask = None,
                                            AreaRangeEffect = None):
        obj =  { 
                'objectId': objectId
                'AreaRangeMask' : AreaRangeMask
                'AreaRangeEffect' : AreaRangeEffect
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaRangeEntryConfig(self,
                                       AreaRangeAreaId,
                                       AreaRangeNet):
        obj =  { 
                'AreaRangeAreaId' : AreaRangeAreaId
                'AreaRangeNet' : AreaRangeNet
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaRangeEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getOspfAreaRangeEntryConfig(self,
                                    AreaRangeAreaId,
                                    AreaRangeNet):
        obj =  { 
                'AreaRangeAreaId' : AreaRangeAreaId
                'AreaRangeNet' : AreaRangeNet
                }
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfAreaRangeEntryConfigById(self, objectId ):
        reqUrl =  self.urlBase+'OspfAreaRangeEntryConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfAreaRangeEntryConfigs(self):
        return self.getObjects( 'OspfAreaRangeEntryConfig') 


    def createBGPPolicyDefinition(self,
                                  Name,
                                  Precedence,
                                  MatchType,
                                  StatementList):
        obj =  { 
                'Name' : Name
                'Precedence' : Precedence
                'MatchType' : MatchType
                'StatementList' : StatementList
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyDefinition(self,
                                  Name,
                                  Precedence = None,
                                  MatchType = None,
                                  StatementList = None):
        obj =  { 
                'Name' : Name
                'Precedence' : Precedence
                'MatchType' : MatchType
                'StatementList' : StatementList
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updateBGPPolicyDefinitionById(self,
                                       objectId,
                                       Precedence = None,
                                       MatchType = None,
                                       StatementList = None):
        obj =  { 
                'objectId': objectId
                'Precedence' : Precedence
                'MatchType' : MatchType
                'StatementList' : StatementList
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyDefinition(self,
                                  Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getBGPPolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'BGPPolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.urlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllBGPPolicyDefinitions(self):
        return self.getObjects( 'BGPPolicyDefinition') 


    def createPolicyCondition(self,
                              Name,
                              ConditionType,
                              MatchProtocol,
                              IpPrefix,
                              MaskLengthRange):
        obj =  { 
                'Name' : Name
                'ConditionType' : ConditionType
                'MatchProtocol' : MatchProtocol
                'IpPrefix' : IpPrefix
                'MaskLengthRange' : MaskLengthRange
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyCondition(self,
                              Name,
                              ConditionType = None,
                              MatchProtocol = None,
                              IpPrefix = None,
                              MaskLengthRange = None):
        obj =  { 
                'Name' : Name
                'ConditionType' : ConditionType
                'MatchProtocol' : MatchProtocol
                'IpPrefix' : IpPrefix
                'MaskLengthRange' : MaskLengthRange
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePolicyConditionById(self,
                                   objectId,
                                   ConditionType = None,
                                   MatchProtocol = None,
                                   IpPrefix = None,
                                   MaskLengthRange = None):
        obj =  { 
                'objectId': objectId
                'ConditionType' : ConditionType
                'MatchProtocol' : MatchProtocol
                'IpPrefix' : IpPrefix
                'MaskLengthRange' : MaskLengthRange
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getPolicyCondition(self,
                           Name):
        obj =  { 
                'Name' : Name
                }
        reqUrl =  self.urlBase+'PolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePolicyConditionById(self, objectId ):
        reqUrl =  self.urlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPolicyConditions(self):
        return self.getObjects( 'PolicyCondition') 


    def createPort(self,
                   PortNum,
                   Description,
                   PhyIntfType,
                   AdminState,
                   MacAddr,
                   Speed,
                   Duplex,
                   Autoneg,
                   MediaType,
                   Mtu):
        obj =  { 
                'PortNum' : PortNum
                'Description' : Description
                'PhyIntfType' : PhyIntfType
                'AdminState' : AdminState
                'MacAddr' : MacAddr
                'Speed' : Speed
                'Duplex' : Duplex
                'Autoneg' : Autoneg
                'MediaType' : MediaType
                'Mtu' : Mtu
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePort(self,
                   PortNum,
                   Description = None,
                   PhyIntfType = None,
                   AdminState = None,
                   MacAddr = None,
                   Speed = None,
                   Duplex = None,
                   Autoneg = None,
                   MediaType = None,
                   Mtu = None):
        obj =  { 
                'PortNum' : PortNum
                'Description' : Description
                'PhyIntfType' : PhyIntfType
                'AdminState' : AdminState
                'MacAddr' : MacAddr
                'Speed' : Speed
                'Duplex' : Duplex
                'Autoneg' : Autoneg
                'MediaType' : MediaType
                'Mtu' : Mtu
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def updatePortById(self,
                        objectId,
                        Description = None,
                        PhyIntfType = None,
                        AdminState = None,
                        MacAddr = None,
                        Speed = None,
                        Duplex = None,
                        Autoneg = None,
                        MediaType = None,
                        Mtu = None):
        obj =  { 
                'objectId': objectId
                'Description' : Description
                'PhyIntfType' : PhyIntfType
                'AdminState' : AdminState
                'MacAddr' : MacAddr
                'Speed' : Speed
                'Duplex' : Duplex
                'Autoneg' : Autoneg
                'MediaType' : MediaType
                'Mtu' : Mtu
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePort(self,
                   PortNum):
        obj =  { 
                'PortNum' : PortNum
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePortById(self, objectId ):
        reqUrl =  self.urlBase+'Port'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getPort(self,
                PortNum):
        obj =  { 
                'PortNum' : PortNum
                }
        reqUrl =  self.urlBase+'Port'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deletePortById(self, objectId ):
        reqUrl =  self.urlBase+'Port'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllPorts(self):
        return self.getObjects( 'Port') 


    def getOspfIfEntryState(self,
                            IfIpAddress,
                            AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress
                'AddressLessIf' : AddressLessIf
                }
        reqUrl =  self.urlBase+'OspfIfEntryState'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r.json() 


    def deleteOspfIfEntryStateById(self, objectId ):
        reqUrl =  self.urlBase+'OspfIfEntryState'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r.json() 


    def getAllOspfIfEntryStates(self):
        return self.getObjects( 'OspfIfEntryState') 

