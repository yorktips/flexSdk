#!/usr/bin/python                                                                                                       
import requests                                                                                                         
import json                                                                                                             
import urllib2                                                                                                          
                                                                                                                        
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}                                          
#def processReturnCode (method) :
#    def returnDetails (self, *args, **kwargs) :
#        r = method(self, *args, **kwargs)
#        if r.status_code in self.httpSuccessCodes:
#            return (r.json(), None)
#        else:
#            ret = {}
#            try:
#                ret = r.json()
#            except:
#                print 'Did not receive Json. HTTP Status %s: Code %s ' %(r.reason, r.status_code) 
#                return ret, r.reason
#            print 'Error from server. Error code %s, Error Message: %s' %(r.status_code, r.json()['Error']) 
#            return (r.json(), "Error")
#    return returnDetails
class FlexSwitch( object):                                                                                              
    httpSuccessCodes = [200, 201, 202, 204]
    def  __init__ (self, ip, port):                                                                                     
        self.ip    = ip                                                                                                 
        self.port  = port                                                                                               
        self.cfgUrlBase = 'http://%s:%s/public/v1/config/'%(ip,str(port))                                                         
        self.stateUrlBase = 'http://%s:%s/public/v1/state/'%(ip,str(port))                                                         

    def getObjects(self, objName, urlPath):
        currentMarker = 0                                                                                                  
        nextMarker = 0                                                                                                     
        count = 10
        more = True                                                                                                        
        entries = []                                                                                                       
        while more == True:                                                                                                
            more = False
            qry = '%s/%ss?CurrentMarker=%d&NextMarker=%d&Count=%d' %(urlPath, objName, currentMarker, nextMarker, count)
            response = requests.get(qry)                                                                                   
            if response.status_code in self.httpSuccessCodes:
                data = response.json()                                                                                         
                more =  data['MoreExist']                                                                                      
                currentMarker =  data['NextMarker']                                                                            
                NextMarker    =  data['NextMarker']                                                                            
                if data['Objects'] != None:                                                                               
                    entries.extend(data['Objects'])                                                                       
            else:
                print 'Server returned Error for %s' %(qry)
        return entries

    def getArpEntryState(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'ArpEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getArpEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ArpEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpEntryStates(self):
        return self.getObjects( 'ArpEntry', self.stateUrlBase)


    """
    .. automethod :: createPolicyStmt(self,
        :param string Name : Policy Statement Name Policy Statement Name
        :param string Conditions : List of conditions added to this policy statement List of conditions added to this policy statement
        :param string Action : Action for this policy statement Action for this policy statement
        :param string MatchConditions : Specifies whether to match all/any of the conditions of this policy statement Specifies whether to match all/any of the conditions of this policy statement

	"""
    def createPolicyStmt(self,
                         Name,
                         Conditions,
                         Action='deny',
                         MatchConditions='all'):
        obj =  { 
                'Name' : Name,
                'Conditions' : Conditions,
                'Action' : Action,
                'MatchConditions' : MatchConditions,
                }
        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePolicyStmt(self,
                         Name,
                         Conditions = None,
                         Action = None,
                         MatchConditions = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Conditions != None :
            obj['Conditions'] = Conditions

        if Action != None :
            obj['Action'] = Action

        if MatchConditions != None :
            obj['MatchConditions'] = MatchConditions

        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePolicyStmtById(self,
                              objectId,
                              Conditions = None,
                              Action = None,
                              MatchConditions = None):
        obj =  {'objectId': objectId }
        if Conditions !=  None:
            obj['Conditions'] = Conditions

        if Action !=  None:
            obj['Action'] = Action

        if MatchConditions !=  None:
            obj['MatchConditions'] = MatchConditions

        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePolicyStmtById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getPolicyStmt(self,
                      Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPolicyStmtById(self, objectId ):
        reqUrl =  self.stateUrlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyStmts(self):
        return self.getObjects( 'PolicyStmt', self.cfgUrlBase)


    """
    .. automethod :: createVlan(self,
        :param int32 VlanId : 802.1Q tag/Vlan ID for vlan being provisioned 802.1Q tag/Vlan ID for vlan being provisioned
        :param string IntfList : List of interface names or ifindex values to  be added as tagged members of the vlan List of interface names or ifindex values to  be added as tagged members of the vlan
        :param string UntagIntfList : List of interface names or ifindex values to  be added as untagged members of the vlan List of interface names or ifindex values to  be added as untagged members of the vlan

	"""
    def createVlan(self,
                   VlanId,
                   IntfList,
                   UntagIntfList):
        obj =  { 
                'VlanId' : int(VlanId),
                'IntfList' : IntfList,
                'UntagIntfList' : UntagIntfList,
                }
        reqUrl =  self.cfgUrlBase+'Vlan'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateVlan(self,
                   VlanId,
                   IntfList = None,
                   UntagIntfList = None):
        obj =  {}
        if VlanId != None :
            obj['VlanId'] = int(VlanId)

        if IntfList != None :
            obj['IntfList'] = IntfList

        if UntagIntfList != None :
            obj['UntagIntfList'] = UntagIntfList

        reqUrl =  self.cfgUrlBase+'Vlan'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateVlanById(self,
                        objectId,
                        IntfList = None,
                        UntagIntfList = None):
        obj =  {'objectId': objectId }
        if IntfList !=  None:
            obj['IntfList'] = IntfList

        if UntagIntfList !=  None:
            obj['UntagIntfList'] = UntagIntfList

        reqUrl =  self.cfgUrlBase+'Vlan'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVlan(self,
                   VlanId):
        obj =  { 
                'VlanId' : VlanId,
                }
        reqUrl =  self.cfgUrlBase+'Vlan'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVlanById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'Vlan'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getVlan(self,
                VlanId):
        obj =  { 
                'VlanId' : int(VlanId),
                }
        reqUrl =  self.cfgUrlBase + 'Vlan'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVlanById(self, objectId ):
        reqUrl =  self.stateUrlBase+'Vlan'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVlans(self):
        return self.getObjects( 'Vlan', self.cfgUrlBase)


    """
    .. automethod :: createComponentLogging(self,
        :param string Module : Module name to set logging level Module name to set logging level
        :param string Level : Logging level Logging level

	"""
    def createComponentLogging(self,
                               Module,
                               Level='info'):
        obj =  { 
                'Module' : Module,
                'Level' : Level,
                }
        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateComponentLogging(self,
                               Module,
                               Level = None):
        obj =  {}
        if Module != None :
            obj['Module'] = Module

        if Level != None :
            obj['Level'] = Level

        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateComponentLoggingById(self,
                                    objectId,
                                    Level = None):
        obj =  {'objectId': objectId }
        if Level !=  None:
            obj['Level'] = Level

        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteComponentLogging(self,
                               Module):
        obj =  { 
                'Module' : Module,
                }
        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteComponentLoggingById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'ComponentLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getComponentLogging(self,
                            Module):
        obj =  { 
                'Module' : Module,
                }
        reqUrl =  self.cfgUrlBase + 'ComponentLogging'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getComponentLoggingById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ComponentLogging'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllComponentLoggings(self):
        return self.getObjects( 'ComponentLogging', self.cfgUrlBase)


    def getIPv4EventState(self,
                          Index):
        obj =  { 
                'Index' : int(Index),
                }
        reqUrl =  self.stateUrlBase + 'IPv4Event'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIPv4EventStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4Event'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4EventStates(self):
        return self.getObjects( 'IPv4Event', self.stateUrlBase)


    """
    .. automethod :: createOspfAreaEntry(self,
        :param string AreaId : A 32-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone. A 32-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone.
        :param int32 AuthType : The authentication type specified for an area. The authentication type specified for an area.
        :param int32 ImportAsExtern : Indicates if an area is a stub area Indicates if an area is a stub area
        :param int32 AreaSummary : The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary
        :param int32 AreaNssaTranslatorRole : Indicates an NSSA border router's ability to perform NSSA translation of type-7 LSAs into type-5 LSAs. Indicates an NSSA border router's ability to perform NSSA translation of type-7 LSAs into type-5 LSAs.
        :param int32 StubDefaultCost : For ABR this cost indicates default cost for summary LSA. For ABR this cost indicates default cost for summary LSA.

	"""
    def createOspfAreaEntry(self,
                            AreaId,
                            AuthType,
                            ImportAsExtern,
                            AreaSummary,
                            AreaNssaTranslatorRole,
                            StubDefaultCost=10):
        obj =  { 
                'AreaId' : AreaId,
                'AuthType' : int(AuthType),
                'ImportAsExtern' : int(ImportAsExtern),
                'AreaSummary' : int(AreaSummary),
                'AreaNssaTranslatorRole' : int(AreaNssaTranslatorRole),
                'StubDefaultCost' : int(StubDefaultCost),
                }
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfAreaEntry(self,
                            AreaId,
                            AuthType = None,
                            ImportAsExtern = None,
                            AreaSummary = None,
                            AreaNssaTranslatorRole = None,
                            StubDefaultCost = None):
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

        if StubDefaultCost != None :
            obj['StubDefaultCost'] = int(StubDefaultCost)

        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfAreaEntryById(self,
                                 objectId,
                                 AuthType = None,
                                 ImportAsExtern = None,
                                 AreaSummary = None,
                                 AreaNssaTranslatorRole = None,
                                 StubDefaultCost = None):
        obj =  {'objectId': objectId }
        if AuthType !=  None:
            obj['AuthType'] = AuthType

        if ImportAsExtern !=  None:
            obj['ImportAsExtern'] = ImportAsExtern

        if AreaSummary !=  None:
            obj['AreaSummary'] = AreaSummary

        if AreaNssaTranslatorRole !=  None:
            obj['AreaNssaTranslatorRole'] = AreaNssaTranslatorRole

        if StubDefaultCost !=  None:
            obj['StubDefaultCost'] = StubDefaultCost

        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfAreaEntry(self,
                            AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfAreaEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getOspfAreaEntry(self,
                         AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.cfgUrlBase + 'OspfAreaEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfAreaEntryById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfAreaEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaEntrys(self):
        return self.getObjects( 'OspfAreaEntry', self.cfgUrlBase)


    def getLaPortChannelState(self,
                              LagId):
        obj =  { 
                'LagId' : int(LagId),
                }
        reqUrl =  self.stateUrlBase + 'LaPortChannel'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLaPortChannelStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LaPortChannel'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLaPortChannelStates(self):
        return self.getObjects( 'LaPortChannel', self.stateUrlBase)


    """
    .. automethod :: createDhcpRelayIntf(self,
        :param int32 IfIndex : Interface index for which Relay Agent Config needs to be done Interface index for which Relay Agent Config needs to be done
        :param bool Enable : Enabling/Disabling relay agent per interface Enabling/Disabling relay agent per interface
        :param string ServerIp : Dhcp Server(s) where relay agent can relay client dhcp requests Dhcp Server(s) where relay agent can relay client dhcp requests

	"""
    def createDhcpRelayIntf(self,
                            IfIndex,
                            Enable,
                            ServerIp):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'Enable' : True if Enable else False,
                'ServerIp' : ServerIp,
                }
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpRelayIntfById(self,
                                 objectId,
                                 Enable = None,
                                 ServerIp = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        if ServerIp !=  None:
            obj['ServerIp'] = ServerIp

        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpRelayIntf(self,
                            IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getDhcpRelayIntf(self,
                         IfIndex):
        obj =  { 
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'DhcpRelayIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayIntfs(self):
        return self.getObjects( 'DhcpRelayIntf', self.cfgUrlBase)


    def getStpPortState(self,
                        BrgIfIndex,
                        IfIndex):
        obj =  { 
                'BrgIfIndex' : int(BrgIfIndex),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'StpPort'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getStpPortStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'StpPort'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpPortStates(self):
        return self.getObjects( 'StpPort', self.stateUrlBase)


    """
    .. automethod :: createFMgrGlobal(self,
        :param string Vrf : System Vrf System Vrf
        :param bool Enable : Enable Fault Manager Enable Fault Manager

	"""
    def createFMgrGlobal(self,
                         Enable):
        obj =  { 
                'Vrf' : 'default',
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateFMgrGlobal(self,
                         Vrf,
                         Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateFMgrGlobalById(self,
                              objectId,
                              Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteFMgrGlobal(self,
                         Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteFMgrGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getFMgrGlobal(self,
                      Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'FMgrGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getFMgrGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'FMgrGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllFMgrGlobals(self):
        return self.getObjects( 'FMgrGlobal', self.cfgUrlBase)


    """
    .. automethod :: createLaPortChannel(self,
        :param int32 LagId : Id of the lag group Id of the lag group
        :param int32 LagType : Sets the type of LAG Sets the type of LAG
        :param uint16 MinLinks : Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available
        :param string SystemIdMac : The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8-octet system-id The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8-octet system-id
        :param uint16 SystemPriority : Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system. Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system.
        :param string AdminState : Convenient way to disable/enable a lag group.  The behaviour should be such that all traffic should stop.  LACP frames should continue to be processed Convenient way to disable/enable a lag group.  The behaviour should be such that all traffic should stop.  LACP frames should continue to be processed
        :param int32 Members : List of current member interfaces for the aggregate List of current member interfaces for the aggregate
        :param int32 Interval : Set the period between LACP messages -- uses the lacp-period-type enumeration. Set the period between LACP messages -- uses the lacp-period-type enumeration.
        :param int32 LagHash : The tx hashing algorithm used by the lag group The tx hashing algorithm used by the lag group
        :param int32 LacpMode : ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets. ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets.

	"""
    def createLaPortChannel(self,
                            LagId,
                            LagType,
                            MinLinks,
                            SystemIdMac,
                            SystemPriority,
                            AdminState,
                            Members,
                            Interval=1,
                            LagHash=0,
                            LacpMode=0):
        obj =  { 
                'LagId' : int(LagId),
                'LagType' : int(LagType),
                'MinLinks' : int(MinLinks),
                'SystemIdMac' : SystemIdMac,
                'SystemPriority' : int(SystemPriority),
                'AdminState' : AdminState,
                'Members' : Members,
                'Interval' : int(Interval),
                'LagHash' : int(LagHash),
                'LacpMode' : int(LacpMode),
                }
        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLaPortChannel(self,
                            LagId,
                            LagType = None,
                            MinLinks = None,
                            SystemIdMac = None,
                            SystemPriority = None,
                            AdminState = None,
                            Members = None,
                            Interval = None,
                            LagHash = None,
                            LacpMode = None):
        obj =  {}
        if LagId != None :
            obj['LagId'] = int(LagId)

        if LagType != None :
            obj['LagType'] = int(LagType)

        if MinLinks != None :
            obj['MinLinks'] = int(MinLinks)

        if SystemIdMac != None :
            obj['SystemIdMac'] = SystemIdMac

        if SystemPriority != None :
            obj['SystemPriority'] = int(SystemPriority)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if Members != None :
            obj['Members'] = Members

        if Interval != None :
            obj['Interval'] = int(Interval)

        if LagHash != None :
            obj['LagHash'] = int(LagHash)

        if LacpMode != None :
            obj['LacpMode'] = int(LacpMode)

        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLaPortChannelById(self,
                                 objectId,
                                 LagType = None,
                                 MinLinks = None,
                                 SystemIdMac = None,
                                 SystemPriority = None,
                                 AdminState = None,
                                 Members = None,
                                 Interval = None,
                                 LagHash = None,
                                 LacpMode = None):
        obj =  {'objectId': objectId }
        if LagType !=  None:
            obj['LagType'] = LagType

        if MinLinks !=  None:
            obj['MinLinks'] = MinLinks

        if SystemIdMac !=  None:
            obj['SystemIdMac'] = SystemIdMac

        if SystemPriority !=  None:
            obj['SystemPriority'] = SystemPriority

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if Members !=  None:
            obj['Members'] = Members

        if Interval !=  None:
            obj['Interval'] = Interval

        if LagHash !=  None:
            obj['LagHash'] = LagHash

        if LacpMode !=  None:
            obj['LacpMode'] = LacpMode

        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLaPortChannel(self,
                            LagId):
        obj =  { 
                'LagId' : LagId,
                }
        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLaPortChannelById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'LaPortChannel'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getLaPortChannel(self,
                         LagId):
        obj =  { 
                'LagId' : int(LagId),
                }
        reqUrl =  self.cfgUrlBase + 'LaPortChannel'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLaPortChannelById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LaPortChannel'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLaPortChannels(self):
        return self.getObjects( 'LaPortChannel', self.cfgUrlBase)


    def getBGPPolicyConditionState(self,
                                   Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyConditionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyConditionStates(self):
        return self.getObjects( 'BGPPolicyCondition', self.stateUrlBase)


    def getOspfIPv4Routes(self,
                          DestId,
                          DestType,
                          AddrMask):
        obj =  { 
                'DestId' : DestId,
                'DestType' : DestType,
                'AddrMask' : AddrMask,
                }
        reqUrl =  self.stateUrlBase + 'OspfIPv4Routes'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfIPv4RoutesById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfIPv4Routes'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIPv4Routess(self):
        return self.getObjects( 'OspfIPv4Routes', self.stateUrlBase)


    def getIPv4RouteHwState(self,
                            DestinationNw):
        obj =  { 
                'DestinationNw' : DestinationNw,
                }
        reqUrl =  self.stateUrlBase + 'IPv4RouteHw'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIPv4RouteHwStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4RouteHw'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4RouteHwStates(self):
        return self.getObjects( 'IPv4RouteHw', self.stateUrlBase)


    """
    .. automethod :: createBfdSessionParam(self,
        :param string Name : Session parameters Session parameters
        :param uint32 RequiredMinRxInterval : Required minimum rx interval in ms Required minimum rx interval in ms
        :param string AuthData : Authentication password Authentication password
        :param bool DemandEnabled : Enable or disable demand mode Enable or disable demand mode
        :param uint32 AuthKeyId : Authentication key id Authentication key id
        :param string AuthType : Authentication type Authentication type
        :param uint32 DesiredMinTxInterval : Desired minimum tx interval in ms Desired minimum tx interval in ms
        :param bool AuthenticationEnabled : Enable or disable authentication Enable or disable authentication
        :param uint32 RequiredMinEchoRxInterval : Required minimum echo rx interval in ms Required minimum echo rx interval in ms
        :param uint32 LocalMultiplier : Detection multiplier Detection multiplier

	"""
    def createBfdSessionParam(self,
                              Name,
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
                'Name' : Name,
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
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBfdSessionParam(self,
                              Name,
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
        if Name != None :
            obj['Name'] = Name

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

        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBfdSessionParamById(self,
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

        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBfdSessionParam(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBfdSessionParamById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBfdSessionParam(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BfdSessionParam'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBfdSessionParamById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BfdSessionParam'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdSessionParams(self):
        return self.getObjects( 'BfdSessionParam', self.cfgUrlBase)


    def getOspfNbrEntryState(self,
                             NbrIpAddr,
                             NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr,
                'NbrAddressLessIndex' : int(NbrAddressLessIndex),
                }
        reqUrl =  self.stateUrlBase + 'OspfNbrEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfNbrEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfNbrEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfNbrEntryStates(self):
        return self.getObjects( 'OspfNbrEntry', self.stateUrlBase)


    def getDhcpRelayIntfState(self,
                              IntfId):
        obj =  { 
                'IntfId' : int(IntfId),
                }
        reqUrl =  self.stateUrlBase + 'DhcpRelayIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpRelayIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayIntfStates(self):
        return self.getObjects( 'DhcpRelayIntf', self.stateUrlBase)


    """
    .. automethod :: createDhcpRelayGlobal(self,
        :param string DhcpRelay : Global Dhcp Relay Agent Information Global Dhcp Relay Agent Information
        :param bool Enable : Global Config stating whether DHCP Relay Agent is enabled on the box or not Global Config stating whether DHCP Relay Agent is enabled on the box or not

	"""
    def createDhcpRelayGlobal(self,
                              DhcpRelay,
                              Enable=False):
        obj =  { 
                'DhcpRelay' : DhcpRelay,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpRelayGlobal(self,
                              DhcpRelay,
                              Enable = None):
        obj =  {}
        if DhcpRelay != None :
            obj['DhcpRelay'] = DhcpRelay

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpRelayGlobalById(self,
                                   objectId,
                                   Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpRelayGlobal(self,
                              DhcpRelay):
        obj =  { 
                'DhcpRelay' : DhcpRelay,
                }
        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getDhcpRelayGlobal(self,
                           DhcpRelay):
        obj =  { 
                'DhcpRelay' : DhcpRelay,
                }
        reqUrl =  self.cfgUrlBase + 'DhcpRelayGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayGlobals(self):
        return self.getObjects( 'DhcpRelayGlobal', self.cfgUrlBase)


    def getBfdSessionParamState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BfdSessionParam'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBfdSessionParamStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BfdSessionParam'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdSessionParamStates(self):
        return self.getObjects( 'BfdSessionParam', self.stateUrlBase)


    def getOspfLsdbEntryState(self,
                              LsdbType,
                              LsdbAreaId,
                              LsdbLsid,
                              LsdbRouterId):
        obj =  { 
                'LsdbType' : int(LsdbType),
                'LsdbAreaId' : LsdbAreaId,
                'LsdbLsid' : LsdbLsid,
                'LsdbRouterId' : LsdbRouterId,
                }
        reqUrl =  self.stateUrlBase + 'OspfLsdbEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfLsdbEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfLsdbEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfLsdbEntryStates(self):
        return self.getObjects( 'OspfLsdbEntry', self.stateUrlBase)


    def getArpLinuxEntryState(self,
                              IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'ArpLinuxEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getArpLinuxEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ArpLinuxEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpLinuxEntryStates(self):
        return self.getObjects( 'ArpLinuxEntry', self.stateUrlBase)


    """
    .. automethod :: createBGPPolicyCondition(self,
        :param string Name : Name of the BGP policy condition Name of the BGP policy condition
        :param string ConditionType : Type of the BGP policy condition. Type of the BGP policy condition.
        :param string IpPrefix : IP adddress to match in CIDR format IP adddress to match in CIDR format
        :param string MaskLengthRange : IP address mask lenght range to match IP address mask lenght range to match

	"""
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
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyCondition(self,
                                 Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPPolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyConditions(self):
        return self.getObjects( 'BGPPolicyCondition', self.cfgUrlBase)


    """
    .. automethod :: createOspfGlobal(self,
        :param string RouterId : A 32-bit integer uniquely identifying the router in the Autonomous System. By convention A 32-bit integer uniquely identifying the router in the Autonomous System. By convention
        :param int32 AdminStat : Indicates if OSPF is enabled globally Indicates if OSPF is enabled globally
        :param bool ASBdrRtrStatus : A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non-volatile storage. A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non-volatile storage.
        :param int32 RestartSupport : *** This element is added for future use. *** The router's support for OSPF graceful restart. Options include *** This element is added for future use. *** The router's support for OSPF graceful restart. Options include
        :param int32 RestartInterval : *** This element is added for future use. *** Configured OSPF graceful restart timeout interval. This object is persistent and when written the entity SHOULD save the change to non-volatile storage. *** This element is added for future use. *** Configured OSPF graceful restart timeout interval. This object is persistent and when written the entity SHOULD save the change to non-volatile storage.
        :param bool TOSSupport : *** This element is added for future use. *** The router's support for type-of-service routing. This object is persistent and when written the entity SHOULD save the change to non-volatile storage. *** This element is added for future use. *** The router's support for type-of-service routing. This object is persistent and when written the entity SHOULD save the change to non-volatile storage.
        :param uint32 ReferenceBandwidth : Reference bandwidth in kilobits/second for calculating default interface metrics. Unit Reference bandwidth in kilobits/second for calculating default interface metrics. Unit

	"""
    def createOspfGlobal(self,
                         RouterId,
                         AdminStat,
                         ASBdrRtrStatus,
                         RestartSupport,
                         RestartInterval,
                         TOSSupport=False,
                         ReferenceBandwidth=100):
        obj =  { 
                'RouterId' : RouterId,
                'AdminStat' : int(AdminStat),
                'ASBdrRtrStatus' : True if ASBdrRtrStatus else False,
                'RestartSupport' : int(RestartSupport),
                'RestartInterval' : int(RestartInterval),
                'TOSSupport' : True if TOSSupport else False,
                'ReferenceBandwidth' : int(ReferenceBandwidth),
                }
        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfGlobal(self,
                         RouterId,
                         AdminStat = None,
                         ASBdrRtrStatus = None,
                         RestartSupport = None,
                         RestartInterval = None,
                         TOSSupport = None,
                         ReferenceBandwidth = None):
        obj =  {}
        if RouterId != None :
            obj['RouterId'] = RouterId

        if AdminStat != None :
            obj['AdminStat'] = int(AdminStat)

        if ASBdrRtrStatus != None :
            obj['ASBdrRtrStatus'] = True if ASBdrRtrStatus else False

        if RestartSupport != None :
            obj['RestartSupport'] = int(RestartSupport)

        if RestartInterval != None :
            obj['RestartInterval'] = int(RestartInterval)

        if TOSSupport != None :
            obj['TOSSupport'] = True if TOSSupport else False

        if ReferenceBandwidth != None :
            obj['ReferenceBandwidth'] = int(ReferenceBandwidth)

        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfGlobalById(self,
                              objectId,
                              AdminStat = None,
                              ASBdrRtrStatus = None,
                              RestartSupport = None,
                              RestartInterval = None,
                              TOSSupport = None,
                              ReferenceBandwidth = None):
        obj =  {'objectId': objectId }
        if AdminStat !=  None:
            obj['AdminStat'] = AdminStat

        if ASBdrRtrStatus !=  None:
            obj['ASBdrRtrStatus'] = ASBdrRtrStatus

        if RestartSupport !=  None:
            obj['RestartSupport'] = RestartSupport

        if RestartInterval !=  None:
            obj['RestartInterval'] = RestartInterval

        if TOSSupport !=  None:
            obj['TOSSupport'] = TOSSupport

        if ReferenceBandwidth !=  None:
            obj['ReferenceBandwidth'] = ReferenceBandwidth

        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfGlobal(self,
                         RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getOspfGlobal(self,
                      RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.cfgUrlBase + 'OspfGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfGlobals(self):
        return self.getObjects( 'OspfGlobal', self.cfgUrlBase)


    def getDhcpRelayHostDhcpState(self,
                                  MacAddr):
        obj =  { 
                'MacAddr' : MacAddr,
                }
        reqUrl =  self.stateUrlBase + 'DhcpRelayHostDhcp'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpRelayHostDhcpStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpRelayHostDhcp'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayHostDhcpStates(self):
        return self.getObjects( 'DhcpRelayHostDhcp', self.stateUrlBase)


    def getDhcpRelayIntfServerState(self,
                                    IntfId):
        obj =  { 
                'IntfId' : int(IntfId),
                }
        reqUrl =  self.stateUrlBase + 'DhcpRelayIntfServer'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpRelayIntfServerStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpRelayIntfServer'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpRelayIntfServerStates(self):
        return self.getObjects( 'DhcpRelayIntfServer', self.stateUrlBase)


    def getLLDPIntfState(self,
                         IfIndex):
        obj =  { 
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'LLDPIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLLDPIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LLDPIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLLDPIntfStates(self):
        return self.getObjects( 'LLDPIntf', self.stateUrlBase)


    """
    .. automethod :: createPolicyDefinition(self,
        :param string Name : Policy Name Policy Name
        :param int32 Priority : Priority of the policy w.r.t other policies configured Priority of the policy w.r.t other policies configured
        :param PolicyDefinitionStmtPriority StatementList : Specifies list of statements along with their precedence order. Specifies list of statements along with their precedence order.
        :param string MatchType : Specifies whether to match all/any of the statements within this policy Specifies whether to match all/any of the statements within this policy
        :param string PolicyType : Specifies the intended protocol application for the policy Specifies the intended protocol application for the policy

	"""
    def createPolicyDefinition(self,
                               Name,
                               Priority,
                               StatementList,
                               MatchType='all',
                               PolicyType='ALL'):
        obj =  { 
                'Name' : Name,
                'Priority' : int(Priority),
                'StatementList' : StatementList,
                'MatchType' : MatchType,
                'PolicyType' : PolicyType,
                }
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePolicyDefinition(self,
                               Name,
                               Priority = None,
                               StatementList = None,
                               MatchType = None,
                               PolicyType = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Priority != None :
            obj['Priority'] = int(Priority)

        if StatementList != None :
            obj['StatementList'] = StatementList

        if MatchType != None :
            obj['MatchType'] = MatchType

        if PolicyType != None :
            obj['PolicyType'] = PolicyType

        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePolicyDefinitionById(self,
                                    objectId,
                                    Priority = None,
                                    StatementList = None,
                                    MatchType = None,
                                    PolicyType = None):
        obj =  {'objectId': objectId }
        if Priority !=  None:
            obj['Priority'] = Priority

        if StatementList !=  None:
            obj['StatementList'] = StatementList

        if MatchType !=  None:
            obj['MatchType'] = MatchType

        if PolicyType !=  None:
            obj['PolicyType'] = PolicyType

        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePolicyDefinitionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getPolicyDefinition(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPolicyDefinitionById(self, objectId ):
        reqUrl =  self.stateUrlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyDefinitions(self):
        return self.getObjects( 'PolicyDefinition', self.cfgUrlBase)


    def getOspfVirtNbrEntryState(self,
                                 VirtNbrRtrId,
                                 VirtNbrArea):
        obj =  { 
                'VirtNbrRtrId' : VirtNbrRtrId,
                'VirtNbrArea' : VirtNbrArea,
                }
        reqUrl =  self.stateUrlBase + 'OspfVirtNbrEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfVirtNbrEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfVirtNbrEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfVirtNbrEntryStates(self):
        return self.getObjects( 'OspfVirtNbrEntry', self.stateUrlBase)


    """
    .. automethod :: createStpPort(self,
        :param int32 BrgIfIndex : The value of the instance of the ifIndex object The value of the instance of the ifIndex object
        :param int32 IfIndex : The port number of the port for which this entry contains Spanning Tree Protocol management information. The port number of the port for which this entry contains Spanning Tree Protocol management information.
        :param int32 BpduGuardInterval : The interval time to which a port will try to recover from BPDU Guard err-disable state.  If no BPDU frames are detected after this timeout plus 3 Times Hello Time then the port will transition back to Up state.  If condition is cleared manually then this operation is ignored.  If set to zero then timer is inactive and recovery is based on manual intervention. The interval time to which a port will try to recover from BPDU Guard err-disable state.  If no BPDU frames are detected after this timeout plus 3 Times Hello Time then the port will transition back to Up state.  If condition is cleared manually then this operation is ignored.  If set to zero then timer is inactive and recovery is based on manual intervention.
        :param int32 PathCost : The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  New implementations should support PathCost32. If the port path costs exceeds the maximum value of this object then this object should report the maximum value The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  New implementations should support PathCost32. If the port path costs exceeds the maximum value of this object then this object should report the maximum value
        :param int32 Priority : The value of the priority field that is contained in the first (in network byte order) octet of the (2 octet long) Port ID.  The other octet of the Port ID is given by the value of StpPort. On bridges supporting IEEE 802.1t or IEEE 802.1w The value of the priority field that is contained in the first (in network byte order) octet of the (2 octet long) Port ID.  The other octet of the Port ID is given by the value of StpPort. On bridges supporting IEEE 802.1t or IEEE 802.1w
        :param int32 AdminEdgePort : The administrative value of the Edge Port parameter.  A value of true(1) indicates that this port should be assumed as an edge-port The administrative value of the Edge Port parameter.  A value of true(1) indicates that this port should be assumed as an edge-port
        :param int32 Enable : The enabled/disabled status of the port. The enabled/disabled status of the port.
        :param int32 ProtocolMigration : When operating in RSTP (version 2) mode When operating in RSTP (version 2) mode
        :param int32 BridgeAssurance : When enabled BPDUs will be transmitted out of all stp ports regardless of state.  When an stp port fails to receive a BPDU the port should  transition to a Blocked state.  Upon reception of BDPU after shutdown  should transition port into the bridge. When enabled BPDUs will be transmitted out of all stp ports regardless of state.  When an stp port fails to receive a BPDU the port should  transition to a Blocked state.  Upon reception of BDPU after shutdown  should transition port into the bridge.
        :param int32 BpduGuard : A Port as OperEdge which receives BPDU with BpduGuard enabled will shut the port down. A Port as OperEdge which receives BPDU with BpduGuard enabled will shut the port down.
        :param int32 AdminPointToPoint : The administrative point-to-point status of the LAN segment attached to this port The administrative point-to-point status of the LAN segment attached to this port
        :param int32 AdminPathCost : The administratively assigned value for the contribution of this port to the path cost of paths toward the spanning tree root.  Writing a value of '0' assigns the automatically calculated default Path Cost value to the port.  If the default Path Cost is being used The administratively assigned value for the contribution of this port to the path cost of paths toward the spanning tree root.  Writing a value of '0' assigns the automatically calculated default Path Cost value to the port.  If the default Path Cost is being used
        :param int32 PathCost32 : The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  This object replaces PathCost to support IEEE 802.1t. Value of 1 will force node to auto discover the value        based on the ports capabilities. The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  This object replaces PathCost to support IEEE 802.1t. Value of 1 will force node to auto discover the value        based on the ports capabilities.

	"""
    def createStpPort(self,
                      BrgIfIndex,
                      IfIndex,
                      BpduGuardInterval,
                      PathCost=1,
                      Priority=128,
                      AdminEdgePort=2,
                      Enable=2,
                      ProtocolMigration=1,
                      BridgeAssurance=2,
                      BpduGuard=2,
                      AdminPointToPoint=2,
                      AdminPathCost=200000,
                      PathCost32=1):
        obj =  { 
                'BrgIfIndex' : int(BrgIfIndex),
                'IfIndex' : int(IfIndex),
                'BpduGuardInterval' : int(BpduGuardInterval),
                'PathCost' : int(PathCost),
                'Priority' : int(Priority),
                'AdminEdgePort' : int(AdminEdgePort),
                'Enable' : int(Enable),
                'ProtocolMigration' : int(ProtocolMigration),
                'BridgeAssurance' : int(BridgeAssurance),
                'BpduGuard' : int(BpduGuard),
                'AdminPointToPoint' : int(AdminPointToPoint),
                'AdminPathCost' : int(AdminPathCost),
                'PathCost32' : int(PathCost32),
                }
        reqUrl =  self.cfgUrlBase+'StpPort'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateStpPort(self,
                      BrgIfIndex,
                      IfIndex,
                      BpduGuardInterval = None,
                      PathCost = None,
                      Priority = None,
                      AdminEdgePort = None,
                      Enable = None,
                      ProtocolMigration = None,
                      BridgeAssurance = None,
                      BpduGuard = None,
                      AdminPointToPoint = None,
                      AdminPathCost = None,
                      PathCost32 = None):
        obj =  {}
        if BrgIfIndex != None :
            obj['BrgIfIndex'] = int(BrgIfIndex)

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if BpduGuardInterval != None :
            obj['BpduGuardInterval'] = int(BpduGuardInterval)

        if PathCost != None :
            obj['PathCost'] = int(PathCost)

        if Priority != None :
            obj['Priority'] = int(Priority)

        if AdminEdgePort != None :
            obj['AdminEdgePort'] = int(AdminEdgePort)

        if Enable != None :
            obj['Enable'] = int(Enable)

        if ProtocolMigration != None :
            obj['ProtocolMigration'] = int(ProtocolMigration)

        if BridgeAssurance != None :
            obj['BridgeAssurance'] = int(BridgeAssurance)

        if BpduGuard != None :
            obj['BpduGuard'] = int(BpduGuard)

        if AdminPointToPoint != None :
            obj['AdminPointToPoint'] = int(AdminPointToPoint)

        if AdminPathCost != None :
            obj['AdminPathCost'] = int(AdminPathCost)

        if PathCost32 != None :
            obj['PathCost32'] = int(PathCost32)

        reqUrl =  self.cfgUrlBase+'StpPort'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateStpPortById(self,
                           objectId,
                           BpduGuardInterval = None,
                           PathCost = None,
                           Priority = None,
                           AdminEdgePort = None,
                           Enable = None,
                           ProtocolMigration = None,
                           BridgeAssurance = None,
                           BpduGuard = None,
                           AdminPointToPoint = None,
                           AdminPathCost = None,
                           PathCost32 = None):
        obj =  {'objectId': objectId }
        if BpduGuardInterval !=  None:
            obj['BpduGuardInterval'] = BpduGuardInterval

        if PathCost !=  None:
            obj['PathCost'] = PathCost

        if Priority !=  None:
            obj['Priority'] = Priority

        if AdminEdgePort !=  None:
            obj['AdminEdgePort'] = AdminEdgePort

        if Enable !=  None:
            obj['Enable'] = Enable

        if ProtocolMigration !=  None:
            obj['ProtocolMigration'] = ProtocolMigration

        if BridgeAssurance !=  None:
            obj['BridgeAssurance'] = BridgeAssurance

        if BpduGuard !=  None:
            obj['BpduGuard'] = BpduGuard

        if AdminPointToPoint !=  None:
            obj['AdminPointToPoint'] = AdminPointToPoint

        if AdminPathCost !=  None:
            obj['AdminPathCost'] = AdminPathCost

        if PathCost32 !=  None:
            obj['PathCost32'] = PathCost32

        reqUrl =  self.cfgUrlBase+'StpPort'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteStpPort(self,
                      BrgIfIndex,
                      IfIndex):
        obj =  { 
                'BrgIfIndex' : BrgIfIndex,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'StpPort'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteStpPortById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'StpPort'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getStpPort(self,
                   BrgIfIndex,
                   IfIndex):
        obj =  { 
                'BrgIfIndex' : int(BrgIfIndex),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'StpPort'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getStpPortById(self, objectId ):
        reqUrl =  self.stateUrlBase+'StpPort'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpPorts(self):
        return self.getObjects( 'StpPort', self.cfgUrlBase)


    def getRouteDistanceState(self,
                              Protocol):
        obj =  { 
                'Protocol' : Protocol,
                }
        reqUrl =  self.stateUrlBase + 'RouteDistance'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getRouteDistanceStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'RouteDistance'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllRouteDistanceStates(self):
        return self.getObjects( 'RouteDistance', self.stateUrlBase)


    """
    .. automethod :: createLogicalIntf(self,
        :param string Name : Name of logical interface Name of logical interface
        :param string Type : Type of logical interface (e.x. loopback) Type of logical interface (e.x. loopback)

	"""
    def createLogicalIntf(self,
                          Name,
                          Type='Loopback'):
        obj =  { 
                'Name' : Name,
                'Type' : Type,
                }
        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLogicalIntf(self,
                          Name,
                          Type = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Type != None :
            obj['Type'] = Type

        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLogicalIntfById(self,
                               objectId,
                               Type = None):
        obj =  {'objectId': objectId }
        if Type !=  None:
            obj['Type'] = Type

        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLogicalIntf(self,
                          Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLogicalIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getLogicalIntf(self,
                       Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'LogicalIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLogicalIntfById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLogicalIntfs(self):
        return self.getObjects( 'LogicalIntf', self.cfgUrlBase)


    def getMacTableEntryState(self,
                              MacAddr):
        obj =  { 
                'MacAddr' : MacAddr,
                }
        reqUrl =  self.stateUrlBase + 'MacTableEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getMacTableEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'MacTableEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllMacTableEntryStates(self):
        return self.getObjects( 'MacTableEntry', self.stateUrlBase)


    """
    .. automethod :: createBGPPeerGroup(self,
        :param string Name : Name of the BGP peer group Name of the BGP peer group
        :param string UpdateSource : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
        :param string AuthPassword : Password to connect to the BGP neighbor Password to connect to the BGP neighbor
        :param string Description : Description of the BGP neighbor Description of the BGP neighbor
        :param uint8 MaxPrefixesRestartTimer : Time to wait before we start BGP peer session when we receive max prefixes Time to wait before we start BGP peer session when we receive max prefixes
        :param bool RouteReflectorClient : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
        :param uint8 MultiHopTTL : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
        :param bool MaxPrefixesDisconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
        :param uint32 LocalAS : Local AS of the BGP neighbor Local AS of the BGP neighbor
        :param uint32 KeepaliveTime : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
        :param uint32 RouteReflectorClusterId : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
        :param uint32 MaxPrefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
        :param uint8 AddPathsMaxTx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
        :param bool MultiHopEnable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
        :param bool AddPathsRx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
        :param uint8 MaxPrefixesThresholdPct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
        :param uint32 HoldTime : Hold time for the BGP neighbor Hold time for the BGP neighbor
        :param uint32 PeerAS : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
        :param uint32 ConnectRetryTime : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

	"""
    def createBGPPeerGroup(self,
                           Name,
                           UpdateSource='',
                           AuthPassword='',
                           Description='',
                           MaxPrefixesRestartTimer=0,
                           RouteReflectorClient=False,
                           MultiHopTTL=0,
                           MaxPrefixesDisconnect=False,
                           LocalAS=0,
                           KeepaliveTime=60,
                           RouteReflectorClusterId=0,
                           MaxPrefixes=0,
                           AddPathsMaxTx=0,
                           MultiHopEnable=False,
                           AddPathsRx=False,
                           MaxPrefixesThresholdPct=0,
                           HoldTime=180,
                           PeerAS=0,
                           ConnectRetryTime=60):
        obj =  { 
                'Name' : Name,
                'UpdateSource' : UpdateSource,
                'AuthPassword' : AuthPassword,
                'Description' : Description,
                'MaxPrefixesRestartTimer' : int(MaxPrefixesRestartTimer),
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'MultiHopTTL' : int(MultiHopTTL),
                'MaxPrefixesDisconnect' : True if MaxPrefixesDisconnect else False,
                'LocalAS' : int(LocalAS),
                'KeepaliveTime' : int(KeepaliveTime),
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'MaxPrefixes' : int(MaxPrefixes),
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'AddPathsRx' : True if AddPathsRx else False,
                'MaxPrefixesThresholdPct' : int(MaxPrefixesThresholdPct),
                'HoldTime' : int(HoldTime),
                'PeerAS' : int(PeerAS),
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.cfgUrlBase+'BGPPeerGroup'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBGPPeerGroup(self,
                           Name,
                           UpdateSource = None,
                           AuthPassword = None,
                           Description = None,
                           MaxPrefixesRestartTimer = None,
                           RouteReflectorClient = None,
                           MultiHopTTL = None,
                           MaxPrefixesDisconnect = None,
                           LocalAS = None,
                           KeepaliveTime = None,
                           RouteReflectorClusterId = None,
                           MaxPrefixes = None,
                           AddPathsMaxTx = None,
                           MultiHopEnable = None,
                           AddPathsRx = None,
                           MaxPrefixesThresholdPct = None,
                           HoldTime = None,
                           PeerAS = None,
                           ConnectRetryTime = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if UpdateSource != None :
            obj['UpdateSource'] = UpdateSource

        if AuthPassword != None :
            obj['AuthPassword'] = AuthPassword

        if Description != None :
            obj['Description'] = Description

        if MaxPrefixesRestartTimer != None :
            obj['MaxPrefixesRestartTimer'] = int(MaxPrefixesRestartTimer)

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if MaxPrefixesDisconnect != None :
            obj['MaxPrefixesDisconnect'] = True if MaxPrefixesDisconnect else False

        if LocalAS != None :
            obj['LocalAS'] = int(LocalAS)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if MaxPrefixes != None :
            obj['MaxPrefixes'] = int(MaxPrefixes)

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if MaxPrefixesThresholdPct != None :
            obj['MaxPrefixesThresholdPct'] = int(MaxPrefixesThresholdPct)

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if PeerAS != None :
            obj['PeerAS'] = int(PeerAS)

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.cfgUrlBase+'BGPPeerGroup'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBGPPeerGroupById(self,
                                objectId,
                                UpdateSource = None,
                                AuthPassword = None,
                                Description = None,
                                MaxPrefixesRestartTimer = None,
                                RouteReflectorClient = None,
                                MultiHopTTL = None,
                                MaxPrefixesDisconnect = None,
                                LocalAS = None,
                                KeepaliveTime = None,
                                RouteReflectorClusterId = None,
                                MaxPrefixes = None,
                                AddPathsMaxTx = None,
                                MultiHopEnable = None,
                                AddPathsRx = None,
                                MaxPrefixesThresholdPct = None,
                                HoldTime = None,
                                PeerAS = None,
                                ConnectRetryTime = None):
        obj =  {'objectId': objectId }
        if UpdateSource !=  None:
            obj['UpdateSource'] = UpdateSource

        if AuthPassword !=  None:
            obj['AuthPassword'] = AuthPassword

        if Description !=  None:
            obj['Description'] = Description

        if MaxPrefixesRestartTimer !=  None:
            obj['MaxPrefixesRestartTimer'] = MaxPrefixesRestartTimer

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if MaxPrefixesDisconnect !=  None:
            obj['MaxPrefixesDisconnect'] = MaxPrefixesDisconnect

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if MaxPrefixes !=  None:
            obj['MaxPrefixes'] = MaxPrefixes

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if MaxPrefixesThresholdPct !=  None:
            obj['MaxPrefixesThresholdPct'] = MaxPrefixesThresholdPct

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.cfgUrlBase+'BGPPeerGroup'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPeerGroup(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPeerGroup'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPeerGroupById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPeerGroup'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPPeerGroup(self,
                        Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPeerGroup'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPeerGroupById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPeerGroup'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPeerGroups(self):
        return self.getObjects( 'BGPPeerGroup', self.cfgUrlBase)


    """
    .. automethod :: createSystemParam(self,
        :param string Vrf : System Vrf System Vrf
        :param string MgmtIp : Management Ip of System Management Ip of System
        :param string Hostname : System Host Name System Host Name
        :param string Version : System Version Information System Version Information
        :param string SwitchMac : Switch Mac Address Switch Mac Address
        :param string Description : System Description System Description

	"""
    def createSystemParam(self,
                          MgmtIp,
                          Hostname,
                          Version,
                          SwitchMac,
                          Description):
        obj =  { 
                'Vrf' : 'default',
                'MgmtIp' : MgmtIp,
                'Hostname' : Hostname,
                'Version' : Version,
                'SwitchMac' : SwitchMac,
                'Description' : Description,
                }
        reqUrl =  self.cfgUrlBase+'SystemParam'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateSystemParam(self,
                          Vrf,
                          MgmtIp = None,
                          Hostname = None,
                          Version = None,
                          SwitchMac = None,
                          Description = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if MgmtIp != None :
            obj['MgmtIp'] = MgmtIp

        if Hostname != None :
            obj['Hostname'] = Hostname

        if Version != None :
            obj['Version'] = Version

        if SwitchMac != None :
            obj['SwitchMac'] = SwitchMac

        if Description != None :
            obj['Description'] = Description

        reqUrl =  self.cfgUrlBase+'SystemParam'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateSystemParamById(self,
                               objectId,
                               MgmtIp = None,
                               Hostname = None,
                               Version = None,
                               SwitchMac = None,
                               Description = None):
        obj =  {'objectId': objectId }
        if MgmtIp !=  None:
            obj['MgmtIp'] = MgmtIp

        if Hostname !=  None:
            obj['Hostname'] = Hostname

        if Version !=  None:
            obj['Version'] = Version

        if SwitchMac !=  None:
            obj['SwitchMac'] = SwitchMac

        if Description !=  None:
            obj['Description'] = Description

        reqUrl =  self.cfgUrlBase+'SystemParam'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteSystemParam(self,
                          Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'SystemParam'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteSystemParamById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'SystemParam'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getSystemParam(self,
                       Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'SystemParam'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSystemParamById(self, objectId ):
        reqUrl =  self.stateUrlBase+'SystemParam'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSystemParams(self):
        return self.getObjects( 'SystemParam', self.cfgUrlBase)


    """
    .. automethod :: createBfdGlobal(self,
        :param string Vrf : VRF id where BFD is globally enabled or disabled VRF id where BFD is globally enabled or disabled
        :param bool Enable : Global BFD state in this VRF Global BFD state in this VRF

	"""
    def createBfdGlobal(self,
                        Enable=True):
        obj =  { 
                'Vrf' : 'default',
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'BfdGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBfdGlobal(self,
                        Vrf,
                        Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'BfdGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBfdGlobalById(self,
                             objectId,
                             Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'BfdGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBfdGlobal(self,
                        Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'BfdGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBfdGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBfdGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'BfdGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBfdGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdGlobals(self):
        return self.getObjects( 'BfdGlobal', self.cfgUrlBase)


    """
    .. automethod :: createBGPPolicyStmt(self,
        :param string Name : Name of the BGP policy statement Name of the BGP policy statement
        :param string MatchConditions : Match conditions all/any Match conditions all/any
        :param string Conditions : List of conditions List of conditions
        :param string Actions : List of actions List of actions

	"""
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
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyStmt(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPPolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyStmts(self):
        return self.getObjects( 'BGPPolicyStmt', self.cfgUrlBase)


    """
    .. automethod :: createArpGlobal(self,
        :param string Vrf : System Vrf System Vrf
        :param int32 Timeout : Global Arp entry timeout value. Default value Global Arp entry timeout value. Default value

	"""
    def createArpGlobal(self,
                        Timeout=600):
        obj =  { 
                'Vrf' : 'default',
                'Timeout' : int(Timeout),
                }
        reqUrl =  self.cfgUrlBase+'ArpGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateArpGlobal(self,
                        Vrf,
                        Timeout = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Timeout != None :
            obj['Timeout'] = int(Timeout)

        reqUrl =  self.cfgUrlBase+'ArpGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateArpGlobalById(self,
                             objectId,
                             Timeout = None):
        obj =  {'objectId': objectId }
        if Timeout !=  None:
            obj['Timeout'] = Timeout

        reqUrl =  self.cfgUrlBase+'ArpGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteArpGlobal(self,
                        Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'ArpGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteArpGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'ArpGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getArpGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'ArpGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getArpGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ArpGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpGlobals(self):
        return self.getObjects( 'ArpGlobal', self.cfgUrlBase)


    def getBGPPolicyStmtState(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyStmtStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyStmtStates(self):
        return self.getObjects( 'BGPPolicyStmt', self.stateUrlBase)


    def getIPv4RouteState(self,
                          DestinationNw):
        obj =  { 
                'DestinationNw' : DestinationNw,
                }
        reqUrl =  self.stateUrlBase + 'IPv4Route'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIPv4RouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4RouteStates(self):
        return self.getObjects( 'IPv4Route', self.stateUrlBase)


    def getBfdGlobalState(self,
                          Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'BfdGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBfdGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BfdGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdGlobalStates(self):
        return self.getObjects( 'BfdGlobal', self.stateUrlBase)


    def getBGPGlobalState(self,
                          RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.stateUrlBase + 'BGPGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPGlobalStates(self):
        return self.getObjects( 'BGPGlobal', self.stateUrlBase)


    def getBfdSessionState(self,
                           IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'BfdSession'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBfdSessionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdSessionStates(self):
        return self.getObjects( 'BfdSession', self.stateUrlBase)


    """
    .. automethod :: createLLDPIntf(self,
        :param int32 IfIndex : IfIndex where lldp needs is enabled/disabled IfIndex where lldp needs is enabled/disabled
        :param bool Enable : Enable/Disable lldp config Per Port Enable/Disable lldp config Per Port

	"""
    def createLLDPIntf(self,
                       IfIndex,
                       Enable=True):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'LLDPIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLLDPIntf(self,
                       IfIndex,
                       Enable = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'LLDPIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLLDPIntfById(self,
                            objectId,
                            Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'LLDPIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLLDPIntf(self,
                       IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'LLDPIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLLDPIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'LLDPIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getLLDPIntf(self,
                    IfIndex):
        obj =  { 
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'LLDPIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLLDPIntfById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LLDPIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLLDPIntfs(self):
        return self.getObjects( 'LLDPIntf', self.cfgUrlBase)


    """
    .. automethod :: createDhcpGlobalConfig(self,
        :param string DhcpConfigKey : DHCP global config DHCP global config
        :param bool Enable : DHCP Server enable/disable control DEFAULT DHCP Server enable/disable control DEFAULT
        :param uint32 DefaultLeaseTime : Default Lease Time in seconds DEFAULT Default Lease Time in seconds DEFAULT
        :param uint32 MaxLeaseTime : Max Lease Time in seconds DEFAULT Max Lease Time in seconds DEFAULT

	"""
    def createDhcpGlobalConfig(self,
                               DhcpConfigKey,
                               Enable,
                               DefaultLeaseTime,
                               MaxLeaseTime):
        obj =  { 
                'DhcpConfigKey' : DhcpConfigKey,
                'Enable' : True if Enable else False,
                'DefaultLeaseTime' : int(DefaultLeaseTime),
                'MaxLeaseTime' : int(MaxLeaseTime),
                }
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpGlobalConfig(self,
                               DhcpConfigKey,
                               Enable = None,
                               DefaultLeaseTime = None,
                               MaxLeaseTime = None):
        obj =  {}
        if DhcpConfigKey != None :
            obj['DhcpConfigKey'] = DhcpConfigKey

        if Enable != None :
            obj['Enable'] = True if Enable else False

        if DefaultLeaseTime != None :
            obj['DefaultLeaseTime'] = int(DefaultLeaseTime)

        if MaxLeaseTime != None :
            obj['MaxLeaseTime'] = int(MaxLeaseTime)

        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpGlobalConfigById(self,
                                    objectId,
                                    Enable = None,
                                    DefaultLeaseTime = None,
                                    MaxLeaseTime = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        if DefaultLeaseTime !=  None:
            obj['DefaultLeaseTime'] = DefaultLeaseTime

        if MaxLeaseTime !=  None:
            obj['MaxLeaseTime'] = MaxLeaseTime

        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpGlobalConfig(self,
                               DhcpConfigKey):
        obj =  { 
                'DhcpConfigKey' : DhcpConfigKey,
                }
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpGlobalConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getDhcpGlobalConfig(self,
                            DhcpConfigKey):
        obj =  { 
                'DhcpConfigKey' : DhcpConfigKey,
                }
        reqUrl =  self.cfgUrlBase + 'DhcpGlobalConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpGlobalConfigById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpGlobalConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpGlobalConfigs(self):
        return self.getObjects( 'DhcpGlobalConfig', self.cfgUrlBase)


    """
    .. automethod :: createIPv4Intf(self,
        :param string IntfRef : Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured
        :param string IpAddr : Interface IP/Net mask in CIDR format to provision on switch interface Interface IP/Net mask in CIDR format to provision on switch interface

	"""
    def createIPv4Intf(self,
                       IntfRef,
                       IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateIPv4Intf(self,
                       IntfRef,
                       IpAddr = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateIPv4IntfById(self,
                            objectId,
                            IpAddr = None):
        obj =  {'objectId': objectId }
        if IpAddr !=  None:
            obj['IpAddr'] = IpAddr

        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteIPv4Intf(self,
                       IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteIPv4IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getIPv4Intf(self,
                    IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'IPv4Intf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIPv4IntfById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4Intfs(self):
        return self.getObjects( 'IPv4Intf', self.cfgUrlBase)


    def getPolicyStmtState(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyStmt'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPolicyStmtStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'PolicyStmt'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyStmtStates(self):
        return self.getObjects( 'PolicyStmt', self.stateUrlBase)


    def getStpBridgeState(self,
                          Vlan):
        obj =  { 
                'Vlan' : int(Vlan),
                }
        reqUrl =  self.stateUrlBase + 'StpBridge'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getStpBridgeStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'StpBridge'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpBridgeStates(self):
        return self.getObjects( 'StpBridge', self.stateUrlBase)


    """
    .. automethod :: createDhcpIntfConfig(self,
        :param string IntfRef : Interface name or ifindex of L3 interface object on which Dhcp Server need to be configured Interface name or ifindex of L3 interface object on which Dhcp Server need to be configured
        :param string Subnet : Subnet Subnet
        :param string SubnetMask : Subnet Mask Subnet Mask
        :param string IPAddrRange : Range of IP Addresses DEFAULT Range of IP Addresses DEFAULT
        :param string BroadcastAddr : Broadcast Address DEFAULT Broadcast Address DEFAULT
        :param string RouterAddr : Router Address DEFAULT Router Address DEFAULT
        :param string DNSServerAddr : Comma seperated List of DNS Server Address DEFAULT Comma seperated List of DNS Server Address DEFAULT
        :param string DomainName : Domain Name Address DEFAULT Domain Name Address DEFAULT
        :param bool Enable : Enable and Disable Control DEFAULT Enable and Disable Control DEFAULT

	"""
    def createDhcpIntfConfig(self,
                             IntfRef,
                             Subnet,
                             SubnetMask,
                             IPAddrRange,
                             BroadcastAddr,
                             RouterAddr,
                             DNSServerAddr,
                             DomainName,
                             Enable):
        obj =  { 
                'IntfRef' : IntfRef,
                'Subnet' : Subnet,
                'SubnetMask' : SubnetMask,
                'IPAddrRange' : IPAddrRange,
                'BroadcastAddr' : BroadcastAddr,
                'RouterAddr' : RouterAddr,
                'DNSServerAddr' : DNSServerAddr,
                'DomainName' : DomainName,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpIntfConfig(self,
                             IntfRef,
                             Subnet = None,
                             SubnetMask = None,
                             IPAddrRange = None,
                             BroadcastAddr = None,
                             RouterAddr = None,
                             DNSServerAddr = None,
                             DomainName = None,
                             Enable = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if Subnet != None :
            obj['Subnet'] = Subnet

        if SubnetMask != None :
            obj['SubnetMask'] = SubnetMask

        if IPAddrRange != None :
            obj['IPAddrRange'] = IPAddrRange

        if BroadcastAddr != None :
            obj['BroadcastAddr'] = BroadcastAddr

        if RouterAddr != None :
            obj['RouterAddr'] = RouterAddr

        if DNSServerAddr != None :
            obj['DNSServerAddr'] = DNSServerAddr

        if DomainName != None :
            obj['DomainName'] = DomainName

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateDhcpIntfConfigById(self,
                                  objectId,
                                  Subnet = None,
                                  SubnetMask = None,
                                  IPAddrRange = None,
                                  BroadcastAddr = None,
                                  RouterAddr = None,
                                  DNSServerAddr = None,
                                  DomainName = None,
                                  Enable = None):
        obj =  {'objectId': objectId }
        if Subnet !=  None:
            obj['Subnet'] = Subnet

        if SubnetMask !=  None:
            obj['SubnetMask'] = SubnetMask

        if IPAddrRange !=  None:
            obj['IPAddrRange'] = IPAddrRange

        if BroadcastAddr !=  None:
            obj['BroadcastAddr'] = BroadcastAddr

        if RouterAddr !=  None:
            obj['RouterAddr'] = RouterAddr

        if DNSServerAddr !=  None:
            obj['DNSServerAddr'] = DNSServerAddr

        if DomainName !=  None:
            obj['DomainName'] = DomainName

        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpIntfConfig(self,
                             IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteDhcpIntfConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getDhcpIntfConfig(self,
                          IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'DhcpIntfConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDhcpIntfConfigById(self, objectId ):
        reqUrl =  self.stateUrlBase+'DhcpIntfConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDhcpIntfConfigs(self):
        return self.getObjects( 'DhcpIntfConfig', self.cfgUrlBase)


    def getVrrpIntfState(self,
                         VRID,
                         IfIndex):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'VrrpIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVrrpIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVrrpIntfStates(self):
        return self.getObjects( 'VrrpIntf', self.stateUrlBase)


    def getSystemStatusState(self,
                             Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'SystemStatus'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSystemStatusStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'SystemStatus'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSystemStatusStates(self):
        return self.getObjects( 'SystemStatus', self.stateUrlBase)


    """
    .. automethod :: createIpTableAcl(self,
        :param string Name : Ip Table ACL rule name Ip Table ACL rule name
        :param string Action : ACCEPT or DROP ACCEPT or DROP
        :param string IpAddr : ip address of subnet or host ip address of subnet or host
        :param string Protocol :  
        :param string Port :  
        :param string PhysicalPort : IfIndex where the acl rule is to be applied IfIndex where the acl rule is to be applied

	"""
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
        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteIpTableAcl(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteIpTableAclById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IpTableAcl'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getIpTableAcl(self,
                      Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'IpTableAcl'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIpTableAclById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IpTableAcl'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIpTableAcls(self):
        return self.getObjects( 'IpTableAcl', self.cfgUrlBase)


    """
    .. automethod :: createOspfIfEntry(self,
        :param string IfIpAddress : The IP address of this OSPF interface. The IP address of this OSPF interface.
        :param int32 AddressLessIf : For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address. For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address.
        :param int32 IfAdminStat : Indiacates if OSPF is enabled on this interface Indiacates if OSPF is enabled on this interface
        :param string IfAreaId : A 32-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone. A 32-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone.
        :param string IfType : The OSPF interface type. By way of a default The OSPF interface type. By way of a default
        :param int32 IfRtrPriority : The priority of this interface.  Used in multi-access networks The priority of this interface.  Used in multi-access networks
        :param int32 IfTransitDelay : The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second. The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second.
        :param int32 IfRetransInterval : The number of seconds between link state advertisement retransmissions The number of seconds between link state advertisement retransmissions
        :param int32 IfPollInterval : The larger time interval The larger time interval
        :param string IfAuthKey : *** This element is added for future use. *** The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g. *** This element is added for future use. *** The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g.
        :param int32 IfAuthType : The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router. The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router.
        :param int32 IfHelloInterval : The length of time The length of time
        :param int32 IfRtrDeadInterval : The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network. The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network.

	"""
    def createOspfIfEntry(self,
                          IfIpAddress,
                          AddressLessIf,
                          IfAdminStat,
                          IfAreaId,
                          IfType,
                          IfRtrPriority,
                          IfTransitDelay,
                          IfRetransInterval,
                          IfPollInterval,
                          IfAuthKey,
                          IfAuthType,
                          IfHelloInterval=10,
                          IfRtrDeadInterval=40):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                'IfAdminStat' : int(IfAdminStat),
                'IfAreaId' : IfAreaId,
                'IfType' : IfType,
                'IfRtrPriority' : int(IfRtrPriority),
                'IfTransitDelay' : int(IfTransitDelay),
                'IfRetransInterval' : int(IfRetransInterval),
                'IfPollInterval' : int(IfPollInterval),
                'IfAuthKey' : IfAuthKey,
                'IfAuthType' : int(IfAuthType),
                'IfHelloInterval' : int(IfHelloInterval),
                'IfRtrDeadInterval' : int(IfRtrDeadInterval),
                }
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfIfEntry(self,
                          IfIpAddress,
                          AddressLessIf,
                          IfAdminStat = None,
                          IfAreaId = None,
                          IfType = None,
                          IfRtrPriority = None,
                          IfTransitDelay = None,
                          IfRetransInterval = None,
                          IfPollInterval = None,
                          IfAuthKey = None,
                          IfAuthType = None,
                          IfHelloInterval = None,
                          IfRtrDeadInterval = None):
        obj =  {}
        if IfIpAddress != None :
            obj['IfIpAddress'] = IfIpAddress

        if AddressLessIf != None :
            obj['AddressLessIf'] = int(AddressLessIf)

        if IfAdminStat != None :
            obj['IfAdminStat'] = int(IfAdminStat)

        if IfAreaId != None :
            obj['IfAreaId'] = IfAreaId

        if IfType != None :
            obj['IfType'] = IfType

        if IfRtrPriority != None :
            obj['IfRtrPriority'] = int(IfRtrPriority)

        if IfTransitDelay != None :
            obj['IfTransitDelay'] = int(IfTransitDelay)

        if IfRetransInterval != None :
            obj['IfRetransInterval'] = int(IfRetransInterval)

        if IfPollInterval != None :
            obj['IfPollInterval'] = int(IfPollInterval)

        if IfAuthKey != None :
            obj['IfAuthKey'] = IfAuthKey

        if IfAuthType != None :
            obj['IfAuthType'] = int(IfAuthType)

        if IfHelloInterval != None :
            obj['IfHelloInterval'] = int(IfHelloInterval)

        if IfRtrDeadInterval != None :
            obj['IfRtrDeadInterval'] = int(IfRtrDeadInterval)

        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfIfEntryById(self,
                               objectId,
                               IfAdminStat = None,
                               IfAreaId = None,
                               IfType = None,
                               IfRtrPriority = None,
                               IfTransitDelay = None,
                               IfRetransInterval = None,
                               IfPollInterval = None,
                               IfAuthKey = None,
                               IfAuthType = None,
                               IfHelloInterval = None,
                               IfRtrDeadInterval = None):
        obj =  {'objectId': objectId }
        if IfAdminStat !=  None:
            obj['IfAdminStat'] = IfAdminStat

        if IfAreaId !=  None:
            obj['IfAreaId'] = IfAreaId

        if IfType !=  None:
            obj['IfType'] = IfType

        if IfRtrPriority !=  None:
            obj['IfRtrPriority'] = IfRtrPriority

        if IfTransitDelay !=  None:
            obj['IfTransitDelay'] = IfTransitDelay

        if IfRetransInterval !=  None:
            obj['IfRetransInterval'] = IfRetransInterval

        if IfPollInterval !=  None:
            obj['IfPollInterval'] = IfPollInterval

        if IfAuthKey !=  None:
            obj['IfAuthKey'] = IfAuthKey

        if IfAuthType !=  None:
            obj['IfAuthType'] = IfAuthType

        if IfHelloInterval !=  None:
            obj['IfHelloInterval'] = IfHelloInterval

        if IfRtrDeadInterval !=  None:
            obj['IfRtrDeadInterval'] = IfRtrDeadInterval

        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfIfEntry(self,
                          IfIpAddress,
                          AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : AddressLessIf,
                }
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfIfEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getOspfIfEntry(self,
                       IfIpAddress,
                       AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                }
        reqUrl =  self.cfgUrlBase + 'OspfIfEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfIfEntryById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfIfEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIfEntrys(self):
        return self.getObjects( 'OspfIfEntry', self.cfgUrlBase)


    """
    .. automethod :: createBGPGlobal(self,
        :param string RouterId : Router id for BGP global config Router id for BGP global config
        :param uint32 ASNum : Local AS for BGP global config Local AS for BGP global config
        :param bool UseMultiplePaths : Enable/disable ECMP for BGP Enable/disable ECMP for BGP
        :param uint32 EBGPMaxPaths : Max ECMP paths from External BGP neighbors Max ECMP paths from External BGP neighbors
        :param bool EBGPAllowMultipleAS : Enable/diable ECMP paths from multiple ASes Enable/diable ECMP paths from multiple ASes
        :param uint32 IBGPMaxPaths : Max ECMP paths from Internal BGP neighbors Max ECMP paths from Internal BGP neighbors
        :param SourcePolicyList Redistribution : Provide redistribution policies for BGP from different sources Provide redistribution policies for BGP from different sources

	"""
    def createBGPGlobal(self,
                        RouterId,
                        ASNum,
                        UseMultiplePaths=False,
                        EBGPMaxPaths=0,
                        EBGPAllowMultipleAS=False,
                        IBGPMaxPaths=0,
                        Redistribution=[]):
        obj =  { 
                'RouterId' : RouterId,
                'ASNum' : int(ASNum),
                'UseMultiplePaths' : True if UseMultiplePaths else False,
                'EBGPMaxPaths' : int(EBGPMaxPaths),
                'EBGPAllowMultipleAS' : True if EBGPAllowMultipleAS else False,
                'IBGPMaxPaths' : int(IBGPMaxPaths),
                'Redistribution' : Redistribution,
                }
        reqUrl =  self.cfgUrlBase+'BGPGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBGPGlobal(self,
                        RouterId,
                        ASNum = None,
                        UseMultiplePaths = None,
                        EBGPMaxPaths = None,
                        EBGPAllowMultipleAS = None,
                        IBGPMaxPaths = None,
                        Redistribution = None):
        obj =  {}
        if RouterId != None :
            obj['RouterId'] = RouterId

        if ASNum != None :
            obj['ASNum'] = int(ASNum)

        if UseMultiplePaths != None :
            obj['UseMultiplePaths'] = True if UseMultiplePaths else False

        if EBGPMaxPaths != None :
            obj['EBGPMaxPaths'] = int(EBGPMaxPaths)

        if EBGPAllowMultipleAS != None :
            obj['EBGPAllowMultipleAS'] = True if EBGPAllowMultipleAS else False

        if IBGPMaxPaths != None :
            obj['IBGPMaxPaths'] = int(IBGPMaxPaths)

        if Redistribution != None :
            obj['Redistribution'] = Redistribution

        reqUrl =  self.cfgUrlBase+'BGPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBGPGlobalById(self,
                             objectId,
                             ASNum = None,
                             UseMultiplePaths = None,
                             EBGPMaxPaths = None,
                             EBGPAllowMultipleAS = None,
                             IBGPMaxPaths = None,
                             Redistribution = None):
        obj =  {'objectId': objectId }
        if ASNum !=  None:
            obj['ASNum'] = ASNum

        if UseMultiplePaths !=  None:
            obj['UseMultiplePaths'] = UseMultiplePaths

        if EBGPMaxPaths !=  None:
            obj['EBGPMaxPaths'] = EBGPMaxPaths

        if EBGPAllowMultipleAS !=  None:
            obj['EBGPAllowMultipleAS'] = EBGPAllowMultipleAS

        if IBGPMaxPaths !=  None:
            obj['IBGPMaxPaths'] = IBGPMaxPaths

        if Redistribution !=  None:
            obj['Redistribution'] = Redistribution

        reqUrl =  self.cfgUrlBase+'BGPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPGlobal(self,
                        RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.cfgUrlBase+'BGPGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPGlobal(self,
                     RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.cfgUrlBase + 'BGPGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPGlobals(self):
        return self.getObjects( 'BGPGlobal', self.cfgUrlBase)


    def getOspfAreaEntryState(self,
                              AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.stateUrlBase + 'OspfAreaEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfAreaEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfAreaEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfAreaEntryStates(self):
        return self.getObjects( 'OspfAreaEntry', self.stateUrlBase)


    """
    .. automethod :: createBfdSession(self,
        :param string IpAddr : BFD neighbor IP address BFD neighbor IP address
        :param string Interface : Name of the interface this session has to be established on Name of the interface this session has to be established on
        :param string Owner : Module requesting BFD session configuration Module requesting BFD session configuration
        :param bool PerLink : Run BFD sessions on individual link of a LAG if the neighbor is reachable through LAG Run BFD sessions on individual link of a LAG if the neighbor is reachable through LAG
        :param string ParamName : Name of the session parameters object to be applied on this session Name of the session parameters object to be applied on this session

	"""
    def createBfdSession(self,
                         IpAddr,
                         Interface='None',
                         Owner='user',
                         PerLink=False,
                         ParamName='default'):
        obj =  { 
                'IpAddr' : IpAddr,
                'Interface' : Interface,
                'Owner' : Owner,
                'PerLink' : True if PerLink else False,
                'ParamName' : ParamName,
                }
        reqUrl =  self.cfgUrlBase+'BfdSession'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBfdSession(self,
                         IpAddr,
                         Interface = None,
                         Owner = None,
                         PerLink = None,
                         ParamName = None):
        obj =  {}
        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Interface != None :
            obj['Interface'] = Interface

        if Owner != None :
            obj['Owner'] = Owner

        if PerLink != None :
            obj['PerLink'] = True if PerLink else False

        if ParamName != None :
            obj['ParamName'] = ParamName

        reqUrl =  self.cfgUrlBase+'BfdSession'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBfdSessionById(self,
                              objectId,
                              Interface = None,
                              Owner = None,
                              PerLink = None,
                              ParamName = None):
        obj =  {'objectId': objectId }
        if Interface !=  None:
            obj['Interface'] = Interface

        if Owner !=  None:
            obj['Owner'] = Owner

        if PerLink !=  None:
            obj['PerLink'] = PerLink

        if ParamName !=  None:
            obj['ParamName'] = ParamName

        reqUrl =  self.cfgUrlBase+'BfdSession'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBfdSession(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase+'BfdSession'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBfdSessionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBfdSession(self,
                      IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase + 'BfdSession'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBfdSessionById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BfdSession'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBfdSessions(self):
        return self.getObjects( 'BfdSession', self.cfgUrlBase)


    def getPolicyConditionState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPolicyConditionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyConditionStates(self):
        return self.getObjects( 'PolicyCondition', self.stateUrlBase)


    """
    .. automethod :: createVrrpIntf(self,
        :param int32 VRID : Virtual Router's Unique Identifier Virtual Router's Unique Identifier
        :param int32 IfIndex : Interface index for which VRRP Config needs to be done Interface index for which VRRP Config needs to be done
        :param string VirtualIPv4Addr : Virtual Router Identifier Virtual Router Identifier
        :param bool PreemptMode : Controls whether a (starting or restarting) higher-priority Backup router preempts a lower-priority Master router Controls whether a (starting or restarting) higher-priority Backup router preempts a lower-priority Master router
        :param int32 Priority : Sending VRRP router's priority for the virtual router Sending VRRP router's priority for the virtual router
        :param int32 AdvertisementInterval : Time interval between ADVERTISEMENTS Time interval between ADVERTISEMENTS
        :param bool AcceptMode : Controls whether a virtual router in Master state will accept packets addressed to the address owner's IPvX address as its own if it is not the IPvX address owner. Controls whether a virtual router in Master state will accept packets addressed to the address owner's IPvX address as its own if it is not the IPvX address owner.

	"""
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
        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVrrpIntf(self,
                       VRID,
                       IfIndex):
        obj =  { 
                'VRID' : VRID,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVrrpIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getVrrpIntf(self,
                    VRID,
                    IfIndex):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'VrrpIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVrrpIntfById(self, objectId ):
        reqUrl =  self.stateUrlBase+'VrrpIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVrrpIntfs(self):
        return self.getObjects( 'VrrpIntf', self.cfgUrlBase)


    """
    .. automethod :: createLLDPGlobal(self,
        :param string Vrf : LLDP Global Config For Default VRF LLDP Global Config For Default VRF
        :param bool Enable : Enable/Disable LLDP Globally Enable/Disable LLDP Globally

	"""
    def createLLDPGlobal(self,
                         Enable=False):
        obj =  { 
                'Vrf' : 'default',
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'LLDPGlobal'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLLDPGlobal(self,
                         Vrf,
                         Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'LLDPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateLLDPGlobalById(self,
                              objectId,
                              Enable = None):
        obj =  {'objectId': objectId }
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'LLDPGlobal'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLLDPGlobal(self,
                         Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'LLDPGlobal'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteLLDPGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'LLDPGlobal'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getLLDPGlobal(self,
                      Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'LLDPGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLLDPGlobalById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LLDPGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLLDPGlobals(self):
        return self.getObjects( 'LLDPGlobal', self.cfgUrlBase)


    """
    .. automethod :: createSubIPv4Intf(self,
        :param string IntfRef : Intf name of system generated id (ifindex) of the ipv4Intf where sub interface is to be configured Intf name of system generated id (ifindex) of the ipv4Intf where sub interface is to be configured
        :param string IpAddr : Ip Address for the interface Ip Address for the interface
        :param string Type : Type of interface Type of interface
        :param string MacAddr : Mac address to be used for the sub interface. If none specified IPv4Intf mac address will be used Mac address to be used for the sub interface. If none specified IPv4Intf mac address will be used
        :param bool Enable : Enable or disable this interface Enable or disable this interface

	"""
    def createSubIPv4Intf(self,
                          IntfRef,
                          IpAddr,
                          Type,
                          MacAddr,
                          Enable=False):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                'Type' : Type,
                'MacAddr' : MacAddr,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateSubIPv4Intf(self,
                          IntfRef,
                          IpAddr,
                          Type = None,
                          MacAddr = None,
                          Enable = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Type != None :
            obj['Type'] = Type

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteSubIPv4Intf(self,
                          IntfRef,
                          IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteSubIPv4IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getSubIPv4Intf(self,
                       IntfRef,
                       IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase + 'SubIPv4Intf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSubIPv4IntfById(self, objectId ):
        reqUrl =  self.stateUrlBase+'SubIPv4Intf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSubIPv4Intfs(self):
        return self.getObjects( 'SubIPv4Intf', self.cfgUrlBase)


    def getPolicyDefinitionState(self,
                                 Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'PolicyDefinition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyDefinitionStates(self):
        return self.getObjects( 'PolicyDefinition', self.stateUrlBase)


    def getVlanState(self,
                     VlanId):
        obj =  { 
                'VlanId' : int(VlanId),
                }
        reqUrl =  self.stateUrlBase + 'Vlan'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVlanStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'Vlan'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVlanStates(self):
        return self.getObjects( 'Vlan', self.stateUrlBase)


    def getLogicalIntfState(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'LogicalIntf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLogicalIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LogicalIntf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLogicalIntfStates(self):
        return self.getObjects( 'LogicalIntf', self.stateUrlBase)


    """
    .. automethod :: createBGPNeighbor(self,
        :param string NeighborAddress : Address of the BGP neighbor Address of the BGP neighbor
        :param int32 IfIndex : Interface of the BGP neighbor Interface of the BGP neighbor
        :param string UpdateSource : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
        :param string AuthPassword : Password to connect to the BGP neighbor Password to connect to the BGP neighbor
        :param string Description : Description of the BGP neighbor Description of the BGP neighbor
        :param string PeerGroup : Peer group of the BGP neighbor Peer group of the BGP neighbor
        :param bool BfdEnable : Enable/Disable BFD for the BGP neighbor Enable/Disable BFD for the BGP neighbor
        :param uint8 MultiHopTTL : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
        :param uint32 LocalAS : Local AS of the BGP neighbor Local AS of the BGP neighbor
        :param uint32 KeepaliveTime : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
        :param bool AddPathsRx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
        :param bool RouteReflectorClient : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
        :param uint8 MaxPrefixesRestartTimer : Time in seconds to wait before we start BGP peer session when we receive max prefixes Time in seconds to wait before we start BGP peer session when we receive max prefixes
        :param bool MultiHopEnable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
        :param uint32 RouteReflectorClusterId : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
        :param bool MaxPrefixesDisconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
        :param uint32 PeerAS : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
        :param uint8 AddPathsMaxTx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
        :param uint32 MaxPrefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
        :param uint8 MaxPrefixesThresholdPct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
        :param string BfdSessionParam : Bfd session param name to be applied Bfd session param name to be applied
        :param uint32 HoldTime : Hold time for the BGP neighbor Hold time for the BGP neighbor
        :param uint32 ConnectRetryTime : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

	"""
    def createBGPNeighbor(self,
                          NeighborAddress,
                          IfIndex,
                          UpdateSource='',
                          AuthPassword='',
                          Description='',
                          PeerGroup='',
                          BfdEnable=False,
                          MultiHopTTL=0,
                          LocalAS=0,
                          KeepaliveTime=60,
                          AddPathsRx=False,
                          RouteReflectorClient=False,
                          MaxPrefixesRestartTimer=0,
                          MultiHopEnable=False,
                          RouteReflectorClusterId=0,
                          MaxPrefixesDisconnect=False,
                          PeerAS=0,
                          AddPathsMaxTx=0,
                          MaxPrefixes=0,
                          MaxPrefixesThresholdPct=80,
                          BfdSessionParam='default',
                          HoldTime=180,
                          ConnectRetryTime=60):
        obj =  { 
                'NeighborAddress' : NeighborAddress,
                'IfIndex' : int(IfIndex),
                'UpdateSource' : UpdateSource,
                'AuthPassword' : AuthPassword,
                'Description' : Description,
                'PeerGroup' : PeerGroup,
                'BfdEnable' : True if BfdEnable else False,
                'MultiHopTTL' : int(MultiHopTTL),
                'LocalAS' : int(LocalAS),
                'KeepaliveTime' : int(KeepaliveTime),
                'AddPathsRx' : True if AddPathsRx else False,
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'MaxPrefixesRestartTimer' : int(MaxPrefixesRestartTimer),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'MaxPrefixesDisconnect' : True if MaxPrefixesDisconnect else False,
                'PeerAS' : int(PeerAS),
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'MaxPrefixes' : int(MaxPrefixes),
                'MaxPrefixesThresholdPct' : int(MaxPrefixesThresholdPct),
                'BfdSessionParam' : BfdSessionParam,
                'HoldTime' : int(HoldTime),
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.cfgUrlBase+'BGPNeighbor'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBGPNeighbor(self,
                          NeighborAddress,
                          IfIndex,
                          UpdateSource = None,
                          AuthPassword = None,
                          Description = None,
                          PeerGroup = None,
                          BfdEnable = None,
                          MultiHopTTL = None,
                          LocalAS = None,
                          KeepaliveTime = None,
                          AddPathsRx = None,
                          RouteReflectorClient = None,
                          MaxPrefixesRestartTimer = None,
                          MultiHopEnable = None,
                          RouteReflectorClusterId = None,
                          MaxPrefixesDisconnect = None,
                          PeerAS = None,
                          AddPathsMaxTx = None,
                          MaxPrefixes = None,
                          MaxPrefixesThresholdPct = None,
                          BfdSessionParam = None,
                          HoldTime = None,
                          ConnectRetryTime = None):
        obj =  {}
        if NeighborAddress != None :
            obj['NeighborAddress'] = NeighborAddress

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if UpdateSource != None :
            obj['UpdateSource'] = UpdateSource

        if AuthPassword != None :
            obj['AuthPassword'] = AuthPassword

        if Description != None :
            obj['Description'] = Description

        if PeerGroup != None :
            obj['PeerGroup'] = PeerGroup

        if BfdEnable != None :
            obj['BfdEnable'] = True if BfdEnable else False

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if LocalAS != None :
            obj['LocalAS'] = int(LocalAS)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if MaxPrefixesRestartTimer != None :
            obj['MaxPrefixesRestartTimer'] = int(MaxPrefixesRestartTimer)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if MaxPrefixesDisconnect != None :
            obj['MaxPrefixesDisconnect'] = True if MaxPrefixesDisconnect else False

        if PeerAS != None :
            obj['PeerAS'] = int(PeerAS)

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if MaxPrefixes != None :
            obj['MaxPrefixes'] = int(MaxPrefixes)

        if MaxPrefixesThresholdPct != None :
            obj['MaxPrefixesThresholdPct'] = int(MaxPrefixesThresholdPct)

        if BfdSessionParam != None :
            obj['BfdSessionParam'] = BfdSessionParam

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.cfgUrlBase+'BGPNeighbor'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateBGPNeighborById(self,
                               objectId,
                               UpdateSource = None,
                               AuthPassword = None,
                               Description = None,
                               PeerGroup = None,
                               BfdEnable = None,
                               MultiHopTTL = None,
                               LocalAS = None,
                               KeepaliveTime = None,
                               AddPathsRx = None,
                               RouteReflectorClient = None,
                               MaxPrefixesRestartTimer = None,
                               MultiHopEnable = None,
                               RouteReflectorClusterId = None,
                               MaxPrefixesDisconnect = None,
                               PeerAS = None,
                               AddPathsMaxTx = None,
                               MaxPrefixes = None,
                               MaxPrefixesThresholdPct = None,
                               BfdSessionParam = None,
                               HoldTime = None,
                               ConnectRetryTime = None):
        obj =  {'objectId': objectId }
        if UpdateSource !=  None:
            obj['UpdateSource'] = UpdateSource

        if AuthPassword !=  None:
            obj['AuthPassword'] = AuthPassword

        if Description !=  None:
            obj['Description'] = Description

        if PeerGroup !=  None:
            obj['PeerGroup'] = PeerGroup

        if BfdEnable !=  None:
            obj['BfdEnable'] = BfdEnable

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if MaxPrefixesRestartTimer !=  None:
            obj['MaxPrefixesRestartTimer'] = MaxPrefixesRestartTimer

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if MaxPrefixesDisconnect !=  None:
            obj['MaxPrefixesDisconnect'] = MaxPrefixesDisconnect

        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if MaxPrefixes !=  None:
            obj['MaxPrefixes'] = MaxPrefixes

        if MaxPrefixesThresholdPct !=  None:
            obj['MaxPrefixesThresholdPct'] = MaxPrefixesThresholdPct

        if BfdSessionParam !=  None:
            obj['BfdSessionParam'] = BfdSessionParam

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.cfgUrlBase+'BGPNeighbor'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPNeighbor(self,
                          NeighborAddress,
                          IfIndex):
        obj =  { 
                'NeighborAddress' : NeighborAddress,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'BGPNeighbor'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPNeighborById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPNeighbor(self,
                       NeighborAddress,
                       IfIndex):
        obj =  { 
                'NeighborAddress' : NeighborAddress,
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'BGPNeighbor'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPNeighborById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPNeighbors(self):
        return self.getObjects( 'BGPNeighbor', self.cfgUrlBase)


    """
    .. automethod :: createStpBridgeInstance(self,
        :param uint16 Vlan : Each bridge is associated with a domain.  Typically this domain is represented as the vlan; The default domain is typically 1 Each bridge is associated with a domain.  Typically this domain is represented as the vlan; The default domain is typically 1
        :param int32 HelloTime : The value that all bridges use for HelloTime when this bridge is acting as the root.  The granularity of this timer is specified by 802.1D-1998 to be 1 second.  An agent may return a badValue error if a set is attempted    to a value that is not a whole number of seconds. The value that all bridges use for HelloTime when this bridge is acting as the root.  The granularity of this timer is specified by 802.1D-1998 to be 1 second.  An agent may return a badValue error if a set is attempted    to a value that is not a whole number of seconds.
        :param int32 ForwardDelay : The value that all bridges use for ForwardDelay when this bridge is acting as the root.  Note that 802.1D-1998 specifies that the range for this parameter is related to the value of MaxAge.  The granularity of this timer is specified by 802.1D-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds. The value that all bridges use for ForwardDelay when this bridge is acting as the root.  Note that 802.1D-1998 specifies that the range for this parameter is related to the value of MaxAge.  The granularity of this timer is specified by 802.1D-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds.
        :param int32 MaxAge : The value that all bridges use for MaxAge when this bridge is acting as the root.  Note that 802.1D-1998 specifies that the range for this parameter is related to the value of HelloTime.  The granularity of this timer is specified by 802.1D-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds. The value that all bridges use for MaxAge when this bridge is acting as the root.  Note that 802.1D-1998 specifies that the range for this parameter is related to the value of HelloTime.  The granularity of this timer is specified by 802.1D-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds.
        :param int32 TxHoldCount : Configures the number of BPDUs that can be sent before pausing for 1 second. Configures the number of BPDUs that can be sent before pausing for 1 second.
        :param int32 Priority : The value of the write-able portion of the Bridge ID (i.e. The value of the write-able portion of the Bridge ID (i.e.
        :param int32 ForceVersion : Stp Version Stp Version
        :param string Address : The bridge identifier of the root of the spanning tree The bridge identifier of the root of the spanning tree

	"""
    def createStpBridgeInstance(self,
                                Vlan,
                                HelloTime=200,
                                ForwardDelay=1500,
                                MaxAge=2000,
                                TxHoldCount=6,
                                Priority=4096,
                                ForceVersion=2,
                                Address='00'):
        obj =  { 
                'Vlan' : int(Vlan),
                'HelloTime' : int(HelloTime),
                'ForwardDelay' : int(ForwardDelay),
                'MaxAge' : int(MaxAge),
                'TxHoldCount' : int(TxHoldCount),
                'Priority' : int(Priority),
                'ForceVersion' : int(ForceVersion),
                'Address' : Address,
                }
        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateStpBridgeInstance(self,
                                Vlan,
                                HelloTime = None,
                                ForwardDelay = None,
                                MaxAge = None,
                                TxHoldCount = None,
                                Priority = None,
                                ForceVersion = None,
                                Address = None):
        obj =  {}
        if Vlan != None :
            obj['Vlan'] = int(Vlan)

        if HelloTime != None :
            obj['HelloTime'] = int(HelloTime)

        if ForwardDelay != None :
            obj['ForwardDelay'] = int(ForwardDelay)

        if MaxAge != None :
            obj['MaxAge'] = int(MaxAge)

        if TxHoldCount != None :
            obj['TxHoldCount'] = int(TxHoldCount)

        if Priority != None :
            obj['Priority'] = int(Priority)

        if ForceVersion != None :
            obj['ForceVersion'] = int(ForceVersion)

        if Address != None :
            obj['Address'] = Address

        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateStpBridgeInstanceById(self,
                                     objectId,
                                     HelloTime = None,
                                     ForwardDelay = None,
                                     MaxAge = None,
                                     TxHoldCount = None,
                                     Priority = None,
                                     ForceVersion = None,
                                     Address = None):
        obj =  {'objectId': objectId }
        if HelloTime !=  None:
            obj['HelloTime'] = HelloTime

        if ForwardDelay !=  None:
            obj['ForwardDelay'] = ForwardDelay

        if MaxAge !=  None:
            obj['MaxAge'] = MaxAge

        if TxHoldCount !=  None:
            obj['TxHoldCount'] = TxHoldCount

        if Priority !=  None:
            obj['Priority'] = Priority

        if ForceVersion !=  None:
            obj['ForceVersion'] = ForceVersion

        if Address !=  None:
            obj['Address'] = Address

        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteStpBridgeInstance(self,
                                Vlan):
        obj =  { 
                'Vlan' : Vlan,
                }
        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getStpBridgeInstance(self,
                             Vlan):
        obj =  { 
                'Vlan' : int(Vlan),
                }
        reqUrl =  self.cfgUrlBase + 'StpBridgeInstance'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.stateUrlBase+'StpBridgeInstance'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllStpBridgeInstances(self):
        return self.getObjects( 'StpBridgeInstance', self.cfgUrlBase)


    def getLaPortChannelMemberState(self,
                                    IfIndex):
        obj =  { 
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'LaPortChannelMember'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLaPortChannelMemberStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'LaPortChannelMember'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllLaPortChannelMemberStates(self):
        return self.getObjects( 'LaPortChannelMember', self.stateUrlBase)


    """
    .. automethod :: createOspfVirtIfEntry(self,
        :param string VirtIfNeighbor : The Router ID of the virtual neighbor. The Router ID of the virtual neighbor.
        :param string VirtIfAreaId : The transit area that the virtual link traverses.  By definition The transit area that the virtual link traverses.  By definition
        :param int32 VirtIfTransitDelay : The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second. The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second.
        :param int32 VirtIfRetransInterval : The number of seconds between link state avertisement retransmissions The number of seconds between link state avertisement retransmissions
        :param int32 VirtIfHelloInterval : The length of time The length of time
        :param int32 VirtIfRtrDeadInterval : The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor. The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor.
        :param string VirtIfAuthKey : The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g. The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g.
        :param int32 VirtIfAuthType : The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router. The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router.

	"""
    def createOspfVirtIfEntry(self,
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
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfVirtIfEntry(self,
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

        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfVirtIfEntryById(self,
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

        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfVirtIfEntry(self,
                              VirtIfNeighbor,
                              VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                }
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfVirtIfEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getOspfVirtIfEntry(self,
                           VirtIfNeighbor,
                           VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                }
        reqUrl =  self.cfgUrlBase + 'OspfVirtIfEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfVirtIfEntryById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfVirtIfEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfVirtIfEntrys(self):
        return self.getObjects( 'OspfVirtIfEntry', self.cfgUrlBase)


    """
    .. automethod :: createSystemLogging(self,
        :param string Vrf : Vrf name Vrf name
        :param string Logging : Global logging Global logging

	"""
    def createSystemLogging(self,
                            Logging='on'):
        obj =  { 
                'Vrf' : 'default',
                'Logging' : Logging,
                }
        reqUrl =  self.cfgUrlBase+'SystemLogging'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateSystemLogging(self,
                            Vrf,
                            Logging = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Logging != None :
            obj['Logging'] = Logging

        reqUrl =  self.cfgUrlBase+'SystemLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateSystemLoggingById(self,
                                 objectId,
                                 Logging = None):
        obj =  {'objectId': objectId }
        if Logging !=  None:
            obj['Logging'] = Logging

        reqUrl =  self.cfgUrlBase+'SystemLogging'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteSystemLogging(self,
                            Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'SystemLogging'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteSystemLoggingById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'SystemLogging'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getSystemLogging(self,
                         Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'SystemLogging'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSystemLoggingById(self, objectId ):
        reqUrl =  self.stateUrlBase+'SystemLogging'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSystemLoggings(self):
        return self.getObjects( 'SystemLogging', self.cfgUrlBase)


    def getBGPPolicyActionState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyAction'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyActionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyActionStates(self):
        return self.getObjects( 'BGPPolicyAction', self.stateUrlBase)


    """
    .. automethod :: createVxlanInstance(self,
        :param uint32 VxlanId : VxLAN ID or VNI VxLAN ID or VNI
        :param string McDestIp : VxLAN multicast IP address used when destination is uknown VxLAN multicast IP address used when destination is uknown
        :param uint16 VlanId : Vlan associated with the Access targets.  Used in conjunction with a given VTEP inner-vlan-handling-mode Vlan associated with the Access targets.  Used in conjunction with a given VTEP inner-vlan-handling-mode
        :param uint32 Mtu : Set the MTU to be applied to all VTEP within this VxLAN Set the MTU to be applied to all VTEP within this VxLAN

	"""
    def createVxlanInstance(self,
                            VxlanId,
                            McDestIp,
                            VlanId,
                            Mtu=1500):
        obj =  { 
                'VxlanId' : int(VxlanId),
                'McDestIp' : McDestIp,
                'VlanId' : int(VlanId),
                'Mtu' : int(Mtu),
                }
        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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
            obj['VlanId'] = int(VlanId)

        if Mtu != None :
            obj['Mtu'] = int(Mtu)

        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVxlanInstance(self,
                            VxlanId):
        obj =  { 
                'VxlanId' : VxlanId,
                }
        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVxlanInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'VxlanInstance'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getVxlanInstance(self,
                         VxlanId):
        obj =  { 
                'VxlanId' : int(VxlanId),
                }
        reqUrl =  self.cfgUrlBase + 'VxlanInstance'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVxlanInstanceById(self, objectId ):
        reqUrl =  self.stateUrlBase+'VxlanInstance'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVxlanInstances(self):
        return self.getObjects( 'VxlanInstance', self.cfgUrlBase)


    def getBGPPolicyDefinitionState(self,
                                    Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyDefinitionStates(self):
        return self.getObjects( 'BGPPolicyDefinition', self.stateUrlBase)


    def getIPv4IntfState(self,
                         IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'IPv4Intf'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIPv4IntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4Intf'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4IntfStates(self):
        return self.getObjects( 'IPv4Intf', self.stateUrlBase)


    def getPortState(self,
                     IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'Port'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPortStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'Port'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPortStates(self):
        return self.getObjects( 'Port', self.stateUrlBase)


    """
    .. automethod :: createOspfIfMetricEntry(self,
        :param int32 IfMetricAddressLessIf : For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation
        :param int32 IfMetricTOS : The Type of Service metric being referenced. On row creation The Type of Service metric being referenced. On row creation
        :param string IfMetricIpAddress : The IP address of this OSPF interface.  On row creation The IP address of this OSPF interface.  On row creation
        :param int32 IfMetricValue : The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed. The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed.

	"""
    def createOspfIfMetricEntry(self,
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
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfIfMetricEntry(self,
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

        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateOspfIfMetricEntryById(self,
                                     objectId,
                                     IfMetricValue = None):
        obj =  {'objectId': objectId }
        if IfMetricValue !=  None:
            obj['IfMetricValue'] = IfMetricValue

        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfIfMetricEntry(self,
                                IfMetricAddressLessIf,
                                IfMetricTOS,
                                IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf,
                'IfMetricTOS' : IfMetricTOS,
                'IfMetricIpAddress' : IfMetricIpAddress,
                }
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteOspfIfMetricEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getOspfIfMetricEntry(self,
                             IfMetricAddressLessIf,
                             IfMetricTOS,
                             IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : int(IfMetricAddressLessIf),
                'IfMetricTOS' : int(IfMetricTOS),
                'IfMetricIpAddress' : IfMetricIpAddress,
                }
        reqUrl =  self.cfgUrlBase + 'OspfIfMetricEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfIfMetricEntryById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfIfMetricEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIfMetricEntrys(self):
        return self.getObjects( 'OspfIfMetricEntry', self.cfgUrlBase)


    """
    .. automethod :: createVxlanVtepInstances(self,
        :param uint32 VtepId : VTEP ID. VTEP ID.
        :param uint32 VxlanId : VxLAN ID. VxLAN ID.
        :param string VtepName : VTEP instance name. VTEP instance name.
        :param int32 SrcIfIndex : Source physical interface ifIndex. Source physical interface ifIndex.
        :param uint16 TTL : TTL of the Vxlan tunnel TTL of the Vxlan tunnel
        :param uint16 TOS : Type of Service Type of Service
        :param int32 Learning : specifies if unknown source link layer  addresses and IP addresses are entered into the VXLAN  device forwarding database. specifies if unknown source link layer  addresses and IP addresses are entered into the VXLAN  device forwarding database.
        :param int32 Rsc : specifies if route short circuit is turned on. specifies if route short circuit is turned on.
        :param int32 L2miss : specifies if netlink LLADDR miss notifications are generated. specifies if netlink LLADDR miss notifications are generated.
        :param int32 L3miss : specifies if netlink IP ADDR miss notifications are generated. specifies if netlink IP ADDR miss notifications are generated.
        :param string DstIp : Destination IP address for the static VxLAN tunnel Destination IP address for the static VxLAN tunnel
        :param string DstMac : Destination MAC address for the static VxLAN tunnel Destination MAC address for the static VxLAN tunnel
        :param uint16 VlanId : Vlan Id to encapsulate with the vtep tunnel ethernet header Vlan Id to encapsulate with the vtep tunnel ethernet header
        :param uint16 UDP : vxlan udp port.  Deafult is the iana default udp port vxlan udp port.  Deafult is the iana default udp port
        :param int32 InnerVlanHandlingMode : The inner vlan tag handling mode. The inner vlan tag handling mode.

	"""
    def createVxlanVtepInstances(self,
                                 VtepId,
                                 VxlanId,
                                 VtepName,
                                 SrcIfIndex,
                                 TTL,
                                 TOS,
                                 Learning,
                                 Rsc,
                                 L2miss,
                                 L3miss,
                                 DstIp,
                                 DstMac,
                                 VlanId,
                                 UDP=4789,
                                 InnerVlanHandlingMode=0):
        obj =  { 
                'VtepId' : int(VtepId),
                'VxlanId' : int(VxlanId),
                'VtepName' : VtepName,
                'SrcIfIndex' : int(SrcIfIndex),
                'TTL' : int(TTL),
                'TOS' : int(TOS),
                'Learning' : int(Learning),
                'Rsc' : int(Rsc),
                'L2miss' : int(L2miss),
                'L3miss' : int(L3miss),
                'DstIp' : DstIp,
                'DstMac' : DstMac,
                'VlanId' : int(VlanId),
                'UDP' : int(UDP),
                'InnerVlanHandlingMode' : int(InnerVlanHandlingMode),
                }
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstances'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateVxlanVtepInstances(self,
                                 VtepId,
                                 VxlanId,
                                 VtepName = None,
                                 SrcIfIndex = None,
                                 TTL = None,
                                 TOS = None,
                                 Learning = None,
                                 Rsc = None,
                                 L2miss = None,
                                 L3miss = None,
                                 DstIp = None,
                                 DstMac = None,
                                 VlanId = None,
                                 UDP = None,
                                 InnerVlanHandlingMode = None):
        obj =  {}
        if VtepId != None :
            obj['VtepId'] = int(VtepId)

        if VxlanId != None :
            obj['VxlanId'] = int(VxlanId)

        if VtepName != None :
            obj['VtepName'] = VtepName

        if SrcIfIndex != None :
            obj['SrcIfIndex'] = int(SrcIfIndex)

        if TTL != None :
            obj['TTL'] = int(TTL)

        if TOS != None :
            obj['TOS'] = int(TOS)

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
            obj['VlanId'] = int(VlanId)

        if UDP != None :
            obj['UDP'] = int(UDP)

        if InnerVlanHandlingMode != None :
            obj['InnerVlanHandlingMode'] = int(InnerVlanHandlingMode)

        reqUrl =  self.cfgUrlBase+'VxlanVtepInstances'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateVxlanVtepInstancesById(self,
                                      objectId,
                                      VtepName = None,
                                      SrcIfIndex = None,
                                      TTL = None,
                                      TOS = None,
                                      Learning = None,
                                      Rsc = None,
                                      L2miss = None,
                                      L3miss = None,
                                      DstIp = None,
                                      DstMac = None,
                                      VlanId = None,
                                      UDP = None,
                                      InnerVlanHandlingMode = None):
        obj =  {'objectId': objectId }
        if VtepName !=  None:
            obj['VtepName'] = VtepName

        if SrcIfIndex !=  None:
            obj['SrcIfIndex'] = SrcIfIndex

        if TTL !=  None:
            obj['TTL'] = TTL

        if TOS !=  None:
            obj['TOS'] = TOS

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

        if UDP !=  None:
            obj['UDP'] = UDP

        if InnerVlanHandlingMode !=  None:
            obj['InnerVlanHandlingMode'] = InnerVlanHandlingMode

        reqUrl =  self.cfgUrlBase+'VxlanVtepInstances'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVxlanVtepInstances(self,
                                 VtepId,
                                 VxlanId):
        obj =  { 
                'VtepId' : VtepId,
                'VxlanId' : VxlanId,
                }
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstances'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteVxlanVtepInstancesById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstances'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getVxlanVtepInstances(self,
                              VtepId,
                              VxlanId):
        obj =  { 
                'VtepId' : int(VtepId),
                'VxlanId' : int(VxlanId),
                }
        reqUrl =  self.cfgUrlBase + 'VxlanVtepInstances'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVxlanVtepInstancesById(self, objectId ):
        reqUrl =  self.stateUrlBase+'VxlanVtepInstances'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVxlanVtepInstancess(self):
        return self.getObjects( 'VxlanVtepInstances', self.cfgUrlBase)


    """
    .. automethod :: createBGPPolicyAction(self,
        :param string Name : Name of the BGP policy action Name of the BGP policy action
        :param string ActionType : Type of the BGP policy action Type of the BGP policy action
        :param bool GenerateASSet : Enable/Disable generating AS set for BGP aggregate action Enable/Disable generating AS set for BGP aggregate action
        :param bool SendSummaryOnly : Enable/Disable sending summary only for BGP aggregate action Enable/Disable sending summary only for BGP aggregate action

	"""
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
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyAction(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyActionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPPolicyAction(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyAction'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyActionById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyAction'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyActions(self):
        return self.getObjects( 'BGPPolicyAction', self.cfgUrlBase)


    def getSystemSwVersionState(self,
                                FlexswitchVersion):
        obj =  { 
                'FlexswitchVersion' : FlexswitchVersion,
                }
        reqUrl =  self.stateUrlBase + 'SystemSwVersion'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSystemSwVersionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'SystemSwVersion'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSystemSwVersionStates(self):
        return self.getObjects( 'SystemSwVersion', self.stateUrlBase)


    def getDaemonState(self,
                       Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'Daemon'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDaemonStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'Daemon'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllDaemonStates(self):
        return self.getObjects( 'Daemon', self.stateUrlBase)


    def getSystemParamState(self,
                            Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'SystemParam'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSystemParamStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'SystemParam'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllSystemParamStates(self):
        return self.getObjects( 'SystemParam', self.stateUrlBase)


    def getBGPRouteState(self,
                         Network,
                         NextHop,
                         CIDRLen):
        obj =  { 
                'Network' : Network,
                'NextHop' : NextHop,
                'CIDRLen' : int(CIDRLen),
                }
        reqUrl =  self.stateUrlBase + 'BGPRoute'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPRouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPRoute'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPRouteStates(self):
        return self.getObjects( 'BGPRoute', self.stateUrlBase)


    """
    .. automethod :: createIPv4Route(self,
        :param string DestinationNw : IP address of the route IP address of the route
        :param string NetworkMask : mask of the route mask of the route
        :param NextHopInfo NextHop :  
        :param string Protocol : Protocol type of the route Protocol type of the route
        :param bool NullRoute : Specify if this is a null route Specify if this is a null route
        :param uint32 Cost : Cost of this route Cost of this route

	"""
    def createIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHop,
                        Protocol='STATIC',
                        NullRoute=False,
                        Cost=0):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHop' : NextHop,
                'Protocol' : Protocol,
                'NullRoute' : True if NullRoute else False,
                'Cost' : int(Cost),
                }
        reqUrl =  self.cfgUrlBase+'IPv4Route'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHop = None,
                        Protocol = None,
                        NullRoute = None,
                        Cost = None):
        obj =  {}
        if DestinationNw != None :
            obj['DestinationNw'] = DestinationNw

        if NetworkMask != None :
            obj['NetworkMask'] = NetworkMask

        if NextHop != None :
            obj['NextHop'] = NextHop

        if Protocol != None :
            obj['Protocol'] = Protocol

        if NullRoute != None :
            obj['NullRoute'] = True if NullRoute else False

        if Cost != None :
            obj['Cost'] = int(Cost)

        reqUrl =  self.cfgUrlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateIPv4RouteById(self,
                             objectId,
                             NextHop = None,
                             Protocol = None,
                             NullRoute = None,
                             Cost = None):
        obj =  {'objectId': objectId }
        if NextHop !=  None:
            obj['NextHop'] = NextHop

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if NullRoute !=  None:
            obj['NullRoute'] = NullRoute

        if Cost !=  None:
            obj['Cost'] = Cost

        reqUrl =  self.cfgUrlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteIPv4Route(self,
                        DestinationNw,
                        NetworkMask):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                }
        reqUrl =  self.cfgUrlBase+'IPv4Route'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteIPv4RouteById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getIPv4Route(self,
                     DestinationNw,
                     NetworkMask):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                }
        reqUrl =  self.cfgUrlBase + 'IPv4Route'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getIPv4RouteById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4Routes(self):
        return self.getObjects( 'IPv4Route', self.cfgUrlBase)


    def getArpEntryHwState(self,
                           IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'ArpEntryHw'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getArpEntryHwStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ArpEntryHw'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpEntryHwStates(self):
        return self.getObjects( 'ArpEntryHw', self.stateUrlBase)


    def getOspfGlobalState(self,
                           RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.stateUrlBase + 'OspfGlobal'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfGlobal'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfGlobalStates(self):
        return self.getObjects( 'OspfGlobal', self.stateUrlBase)


    def getBGPNeighborState(self,
                            NeighborAddress,
                            IfIndex):
        obj =  { 
                'NeighborAddress' : NeighborAddress,
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'BGPNeighbor'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPNeighborStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPNeighbor'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPNeighborStates(self):
        return self.getObjects( 'BGPNeighbor', self.stateUrlBase)


    def getVrrpVridState(self,
                         VRID,
                         IfIndex):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'VrrpVrid'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVrrpVridStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'VrrpVrid'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllVrrpVridStates(self):
        return self.getObjects( 'VrrpVrid', self.stateUrlBase)


    """
    .. automethod :: createBGPPolicyDefinition(self,
        :param string Name : Name of the BGP policy definition Name of the BGP policy definition
        :param int32 Precedence : Precedence of the policy definition Precedence of the policy definition
        :param string MatchType : Match type for policy definition Match type for policy definition
        :param BGPPolicyDefinitionStmtPrecedence StatementList : Precedence of statements in the policy Precedence of statements in the policy

	"""
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
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

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

        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyDefinition(self,
                                  Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deleteBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getBGPPolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyDefinition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.stateUrlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllBGPPolicyDefinitions(self):
        return self.getObjects( 'BGPPolicyDefinition', self.cfgUrlBase)


    """
    .. automethod :: createPolicyCondition(self,
        :param string Name : PolicyConditionName PolicyConditionName
        :param string ConditionType : Specifies the match criterion this condition defines Specifies the match criterion this condition defines
        :param string Protocol : Protocol to match on if the ConditionType is set to MatchProtocol Protocol to match on if the ConditionType is set to MatchProtocol
        :param string IpPrefix : Used in conjunction with MaskLengthRange to specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix. Used in conjunction with MaskLengthRange to specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix.
        :param string MaskLengthRange : Used in conjuction with IpPrefix to specify specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix. Used in conjuction with IpPrefix to specify specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix.

	"""
    def createPolicyCondition(self,
                              Name,
                              ConditionType,
                              Protocol,
                              IpPrefix,
                              MaskLengthRange):
        obj =  { 
                'Name' : Name,
                'ConditionType' : ConditionType,
                'Protocol' : Protocol,
                'IpPrefix' : IpPrefix,
                'MaskLengthRange' : MaskLengthRange,
                }
        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePolicyCondition(self,
                              Name,
                              ConditionType = None,
                              Protocol = None,
                              IpPrefix = None,
                              MaskLengthRange = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ConditionType != None :
            obj['ConditionType'] = ConditionType

        if Protocol != None :
            obj['Protocol'] = Protocol

        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange != None :
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePolicyConditionById(self,
                                   objectId,
                                   ConditionType = None,
                                   Protocol = None,
                                   IpPrefix = None,
                                   MaskLengthRange = None):
        obj =  {'objectId': objectId }
        if ConditionType !=  None:
            obj['ConditionType'] = ConditionType

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if IpPrefix !=  None:
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange !=  None:
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePolicyConditionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getPolicyCondition(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyCondition'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPolicyConditionById(self, objectId ):
        reqUrl =  self.stateUrlBase+'PolicyCondition'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPolicyConditions(self):
        return self.getObjects( 'PolicyCondition', self.cfgUrlBase)


    """
    .. automethod :: createPort(self,
        :param string IntfRef : Front panel port name or system assigned interface id Front panel port name or system assigned interface id
        :param int32 IfIndex : System assigned interface id for this port. Read only attribute System assigned interface id for this port. Read only attribute
        :param string PhyIntfType : Type of internal phy interface Type of internal phy interface
        :param string MacAddr : Mac address associated with this port Mac address associated with this port
        :param int32 Speed : Port speed in Mbps Port speed in Mbps
        :param string Duplex : Duplex setting for this port Duplex setting for this port
        :param string MediaType : Type of media inserted into this port Type of media inserted into this port
        :param int32 Mtu : Maximum transmission unit size for this port Maximum transmission unit size for this port
        :param string BreakOutMode : Break out mode for the port. Only applicable on ports that support breakout. Valid modes - 1x40 Break out mode for the port. Only applicable on ports that support breakout. Valid modes - 1x40
        :param string Description : User provided string description User provided string description
        :param string AdminState : Administrative state of this port Administrative state of this port
        :param string Autoneg : Autonegotiation setting for this port Autonegotiation setting for this port

	"""
    def createPort(self,
                   IntfRef,
                   IfIndex,
                   PhyIntfType,
                   MacAddr,
                   Speed,
                   Duplex,
                   MediaType,
                   Mtu,
                   BreakOutMode,
                   Description='FP Port',
                   AdminState='DOWN',
                   Autoneg='OFF'):
        obj =  { 
                'IntfRef' : IntfRef,
                'IfIndex' : int(IfIndex),
                'PhyIntfType' : PhyIntfType,
                'MacAddr' : MacAddr,
                'Speed' : int(Speed),
                'Duplex' : Duplex,
                'MediaType' : MediaType,
                'Mtu' : int(Mtu),
                'BreakOutMode' : BreakOutMode,
                'Description' : Description,
                'AdminState' : AdminState,
                'Autoneg' : Autoneg,
                }
        reqUrl =  self.cfgUrlBase+'Port'
        r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePort(self,
                   IntfRef,
                   IfIndex = None,
                   PhyIntfType = None,
                   MacAddr = None,
                   Speed = None,
                   Duplex = None,
                   MediaType = None,
                   Mtu = None,
                   BreakOutMode = None,
                   Description = None,
                   AdminState = None,
                   Autoneg = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if PhyIntfType != None :
            obj['PhyIntfType'] = PhyIntfType

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Speed != None :
            obj['Speed'] = int(Speed)

        if Duplex != None :
            obj['Duplex'] = Duplex

        if MediaType != None :
            obj['MediaType'] = MediaType

        if Mtu != None :
            obj['Mtu'] = int(Mtu)

        if BreakOutMode != None :
            obj['BreakOutMode'] = BreakOutMode

        if Description != None :
            obj['Description'] = Description

        if AdminState != None :
            obj['AdminState'] = AdminState

        if Autoneg != None :
            obj['Autoneg'] = Autoneg

        reqUrl =  self.cfgUrlBase+'Port'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updatePortById(self,
                        objectId,
                        IfIndex = None,
                        PhyIntfType = None,
                        MacAddr = None,
                        Speed = None,
                        Duplex = None,
                        MediaType = None,
                        Mtu = None,
                        BreakOutMode = None,
                        Description = None,
                        AdminState = None,
                        Autoneg = None):
        obj =  {'objectId': objectId }
        if IfIndex !=  None:
            obj['IfIndex'] = IfIndex

        if PhyIntfType !=  None:
            obj['PhyIntfType'] = PhyIntfType

        if MacAddr !=  None:
            obj['MacAddr'] = MacAddr

        if Speed !=  None:
            obj['Speed'] = Speed

        if Duplex !=  None:
            obj['Duplex'] = Duplex

        if MediaType !=  None:
            obj['MediaType'] = MediaType

        if Mtu !=  None:
            obj['Mtu'] = Mtu

        if BreakOutMode !=  None:
            obj['BreakOutMode'] = BreakOutMode

        if Description !=  None:
            obj['Description'] = Description

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if Autoneg !=  None:
            obj['Autoneg'] = Autoneg

        reqUrl =  self.cfgUrlBase+'Port'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePort(self,
                   IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'Port'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def deletePortById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'Port'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    def getPort(self,
                IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'Port'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getPortById(self, objectId ):
        reqUrl =  self.stateUrlBase+'Port'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllPorts(self):
        return self.getObjects( 'Port', self.cfgUrlBase)


    def getOspfIfEntryState(self,
                            IfIpAddress,
                            AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                }
        reqUrl =  self.stateUrlBase + 'OspfIfEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getOspfIfEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'OspfIfEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllOspfIfEntryStates(self):
        return self.getObjects( 'OspfIfEntry', self.stateUrlBase)

