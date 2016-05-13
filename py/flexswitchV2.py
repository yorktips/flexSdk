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
            ret = {}
            try:
                ret = r.json()
            except:
                print 'Did not receive Json. HTTP Status %s: Code %s ' %(r.reason, r.status_code) 
                return ret, r.reason
            print 'Error from server. Error code %s, Error Message: %s' %(r.status_code, r.json()['Error']) 
            return (r.json(), "Error")
    return returnDetails

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

    """
    .. automethod :: createIPv4Route(self,
        :param string DestinationNw :  IP address of the route  IP address of the route
        :param string NetworkMask :  mask of the route  mask of the route
        :param string NextHopIp :  next hop ip of the route  next hop ip of the route
        :param string OutgoingIntfType : Interface type of the next hop interface Interface type of the next hop interface
        :param string OutgoingInterface : Interface ID of the next hop interface Interface ID of the next hop interface
        :param string Protocol : Protocol type of the route Protocol type of the route
        :param int32 Weight :  Weight of the next hop  Weight of the next hop
        :param uint32 Cost : Cost of this route Cost of this route

	"""
    @processReturnCode
    def createIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHopIp,
                        OutgoingIntfType,
                        OutgoingInterface,
                        Protocol='STATIC',
                        Weight=0,
                        Cost=0):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHopIp' : NextHopIp,
                'OutgoingIntfType' : OutgoingIntfType,
                'OutgoingInterface' : OutgoingInterface,
                'Protocol' : Protocol,
                'Weight' : int(Weight),
                'Cost' : int(Cost),
                }
        reqUrl =  self.cfgUrlBase+'IPv4Route'
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
                        Weight = None,
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

        if Weight != None :
            obj['Weight'] = int(Weight)

        if Cost != None :
            obj['Cost'] = int(Cost)

        reqUrl =  self.cfgUrlBase+'IPv4Route'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateIPv4RouteById(self,
                             objectId,
                             OutgoingIntfType = None,
                             OutgoingInterface = None,
                             Protocol = None,
                             Weight = None,
                             Cost = None):
        obj =  {'objectId': objectId }
        if OutgoingIntfType !=  None:
            obj['OutgoingIntfType'] = OutgoingIntfType

        if OutgoingInterface !=  None:
            obj['OutgoingInterface'] = OutgoingInterface

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if Weight !=  None:
            obj['Weight'] = Weight

        if Cost !=  None:
            obj['Cost'] = Cost

        reqUrl =  self.cfgUrlBase+'IPv4Route'
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
        reqUrl =  self.cfgUrlBase+'IPv4Route'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteIPv4RouteById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv4Route'+"/%s"%(objectId)
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
        reqUrl =  self.stateUrlBase+'IPv4Route'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getIPv4RouteById(self, objectId ):
        reqUrl =  self.stateUrlBase+'IPv4Route'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllIPv4Routes(self):
        return self.getObjects( 'IPv4Route', self.cfgUrlBase)

