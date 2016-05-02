.. FlexSwitchSDK documentation master file, created by
   sphinx-quickstart on Mon Apr  4 12:27:04 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. sectnum::

Configuration Examples 
========================================

Configuring ARP
---------------

The ARP protocol is utilized to be learn the layer 2 MAC address of a directly attached device and associate it with an IP address in which to communicate.  ARPd is the daemon on FlexSwitch that manages, learns, and programs layer 2 adjancency information into the data-plane.   

Timeout Values
^^^^^^^^^^^^^^
FlexSwitch supports the ability to change the ARP timers Globally.  The default timeout value is 10 minutes(600 seconds).  ARP daemon will attempt refresh of the ARP entry at the following intervals, with example times based on default timer and number of attempts:

	- 50% of ARP timeout (300 seconds, 1 ARP request frame sent)
	- 25% of ARP timeout (150 seconds, 1 ARP request frame sent)

With more aggressve attempts in the last minute for timeout:

	- 60 seconds of ARP Timeout (1 ARP request frame sent)
	- 30 seconds remaining in ARP Timeout (1 ARP request frame sent)
	- 10 seconds remaining in ARP timeout (10 ARP request frames sent)

Configuring  with Rest API 
"""""""""""""""""""""""""""""""""""""

FlexSwitch has a REST based API, and below is an example utilzing Linux cURL: 

COMMAND:
::
	
	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Timeout":<*Timeout Value in seconds*>}' 'http://<*your-switchip*>:8080/public/v1/config/ArpConfig'
	

OPTIONS:

::

	Timeout - Length of ARP timeout in seconds. 

EXAMPLE:
::
	
	root@5b5a8d783113:/# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"ArpConfigKey":"1", "Timeout":1000}' http://localhost:8080/public/v1/config/ArpConfig
	{"ObjectId":"a97b920d-8b10-47b1-7ea9-890b07f6e712","Error":""}


	root@5b5a8d783113:/# curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' http://localhost:8080/public/v1/config/ArpConfigs | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
					 Dload  Upload   Total   Spent    Left  Speed
	100   174  100   174    0     0  87087      0 --:--:-- --:--:-- --:--:--  169k
	{
	    "CurrentMarker": 0,
	    "MoreExist": false,
	    "NextMarker": 0,
	    "ObjCount": 1,
	    "Objects": [
		{
		    "Object": {
			"ArpConfigKey": "1",
			"Timeout": 1000
		    },
		    "ObjectId": "a97b920d-8b10-47b1-7ea9-890b07f6e712"
		}
	    ]
	}



Configuring with Python SDK
""""""""""""""""""""""""""""""""""

FlexSwitch has a Python SDK for utiliztion of programtically adjusting a device via a python script/application.  This SDK has full parody with FlexSwitch's RESTful API.

Below is an example to set the ARP Timeout to 1000 seconds via the Python SDK:

::

	#!/usr/bin/python
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		ip = "192.168.0.3"
		Timeout=1000
		restIf = FlexSwitch(ip, 8080)
		restIf.createArpConfig("1",Timeout)


You can display the results of this change with the followin Python Script below:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		ip = "192.168.0.3"
		restIf = FlexSwitch(ip, 8080)
		print json.dumps(restIf.getAllArpConfigs(), indent=4)	

Output:

::

	acasella@snaproute-lab-r710-1:~$ ./getarpconfig.py 
	[
	    {
		"Object": {
		    "ArpConfigKey": "1", 
		    "Timeout": 1000
		}, 
		"ObjectId": "e607400d-71f1-4fd2-4574-e40d313fd3e7"
	    }
	]

Configuring via Configuration file 
""""""""""""""""""""""""""""""""""

Static Entries
^^^^^^^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""

FlexSwitch has a REST based API, and below is an example utilzing Linux cURL:

COMMAND:
::

        curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"IP":"<*IPv4 Address*>", "MAC":"<*MAC address*>"}' 'http://<*your-switchip*>:8080/public/v1/config/ArpConfig'


OPTIONS:

::

        IP - IPv4 address to have a static entry applied 
	MAC - Layer 2 MAC address that will be configured for the associated IPv4 address. 

EXAMPLE:
::

        root@5b5a8d783113:/# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"IP":"192.168.0.1", "MAC":"01:23:34:56:78"}' http://localhost:8080/public/v1/config/ArpConfig
        {"ObjectId":"a97b920d-8b10-47b1-7ea9-890b07f6e712","Error":""}


        root@5b5a8d783113:/# curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' http://localhost:8080/public/v1/config/ArpConfigs | python -m json.tool
          % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                         Dload  Upload   Total   Spent    Left  Speed
        100   174  100   174    0     0  87087      0 --:--:-- --:--:-- --:--:--  169k
        {
            "CurrentMarker": 0,
            "MoreExist": false,
            "NextMarker": 0,
            "ObjCount": 1,
            "Objects": [
                {
                    "Object": {
                        "IP": "192.168.0.1",
                        "MAC":"01:23:34:56:78"
                    },
                    "ObjectId": "a97b920d-8b10-47b1-7ea9-890b07f6e712"
                }
            ]
        }




Configuring with Python SDK
""""""""""""""""""""""""""""""""""
Below is an example to set the ARP Timeout to 1000 seconds via the Python SDK:

::

	#!/usr/bin/python
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		ip = "192.168.0.3"
		Timeout=1000
		restIf = FlexSwitch(ip, 8080)
		arp_ip="192.168.0.1"
		mac="01:23:34:56:78"
		restIf.createArpStatic(arp_ip,mac)


You can display the results of this change with the followin Python Script below:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		ip = "192.168.0.3"
		restIf = FlexSwitch(ip, 8080)
		print json.dumps(restIf.getAllArpStatics(), indent=4)	

Output:

::

	acasella@snaproute-lab-r710-1:~$ ./getarpstatic.py 
	[
	   {
	       "Object": {
	   	   "IP": "192.168.0.1",
	 	   "MAC":"01:23:34:56:78"
	       },
	       "ObjectId": "a97b920d-8b10-47b1-7ea9-890b07f6e712"
	   }
	]



Configuring via Configuration file
""""""""""""""""""""""""""""""""""

Display ARP State
^^^^^^^^^^^^^^^^^


Display via Rest API 
"""""""""""""""""""""


Display All ARP Entries
***********************
 
Utilizing the GetBulk API for ARP, "*ArpEntrys*", we can display all ARP entries learned on the device.  

COMMAND:
::

        curl -X GET --header 'Content-Type: application/json' 'http://<*your-switchip*>:8080/public/v1/state/ArpEntrys'


EXAMPLE:
::

	root@5c3bca6fb77e:/# curl -X GET --header 'Content-Type: application/json' 'http://localhost:8080/public/v1/state/ArpEntrys' | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
					 Dload  Upload   Total   Spent    Left  Speed
	100   213  100   213    0     0  44654      0 --:--:-- --:--:-- --:--:-- 53250
	{
	    "CurrentMarker": 0,
	    "MoreExist": false,
	    "NextMarker": 0,
	    "ObjCount": 1,
	    "Objects": [
		{
		    "Object": {
			"ExpiryTimeLeft": "9m57.74904463s",
			"Intf": "eth1",
			"IpAddr": "51.1.1.5",
			"MacAddr": "4e:8c:3d:c8:d4:09",
			"Vlan": "5"
		    },
		    "ObjectId": ""
		}
	    ]
	}


Display a specific ARP entry
****************************

You can return the value of an object based on any of the variables within that object.  For example you can query an ARP entry on any of the follownig parameters:

- IPv4 Address (*IpAddr* variable)

The example below will show how to grab a specific ARP entry based on IP address. 

COMMAND:

::
	curl -X GET --header 'Content-Type: application/json' -d '{"IpAddr":"<*IPv4 Address*>"}' 'http://<*your-switchip*>:8080/public/v1/state/ArpEntry'


OPTIONS:

::

	IpAddr - IPv4 Address ArpEntry to be queried 

EXAMPLE:
::

	root@5c3bca6fb77e:/# curl -X GET --header 'Content-Type: application/json' -d '{"IpAddr":"51.1.1.5"}' 'http://localhost:8080/public/v1/state/ArpEntry' | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
					 Dload  Upload   Total   Spent    Left  Speed
	100   157  100   136  100    21  25185   3888 --:--:-- --:--:-- --:--:-- 27200
	{
	    "Object": {
		"ExpiryTimeLeft": "9m56.277773536s",
		"Intf": "eth1",
		"IpAddr": "51.1.1.5",
		"MacAddr": "4e:8c:3d:c8:d4:09",
		"Vlan": "5"
	    },
	    "ObjectId": ""
	}

Displaying State with Python SDK
""""""""""""""""""""""""""""""""""
Below is an example to set the ARP Timeout to 1000 seconds via the Python SDK:

::

	#!/usr/bin/python
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		ip = "192.168.0.3"
		restIf = FlexSwitch(ip, 8080)
		restIf.getAllArpEntrys()


You can display the results of this change with the followin Python Script below:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		ip = "192.168.0.3"
		restIf = FlexSwitch(ip, 8080)
		print json.dumps(restIf.getAllArpEntrys(), indent=4)	

Output:

::

	acasella@snaproute-lab-r710-1:~$ python getarpall.py 
	[
	    {
		"Object": {
		    "Intf": "eth1", 
		    "Vlan": "5", 
		    "MacAddr": "1e:b9:5a:e9:52:a1", 
		    "IpAddr": "51.1.1.5", 
		    "ExpiryTimeLeft": "9m48.458947622s"
		}, 
		"ObjectId": ""
	    }
	]




Python SDK ARP Methods
^^^^^^^^^^^^^^^^^^^^^^
State Methods
"""""""""""""

::

    @processReturnCode
    def getArpEntryState(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase+'ArpEntry'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getArpEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ArpEntry'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpEntryStates(self):
        return self.getObjects( 'ArpEntry', self.stateUrlBase)

Config Methods
""""""""""""""

::

    """
    .. automethod :: createArpConfig(self,
        :param string ArpConfigKey :  Arp config  Arp config
        :param int32 Timeout :  Global Arp entry timeout value. Default value  Global Arp entry timeout value. Default value

	"""
    @processReturnCode
    def createArpConfig(self,
                        ArpConfigKey,
                        Timeout):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey,
                'Timeout' : int(Timeout),
                }
        reqUrl =  self.cfgUrlBase+'ArpConfig'
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

        reqUrl =  self.cfgUrlBase+'ArpConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def updateArpConfigById(self,
                             objectId,
                             Timeout = None):
        obj =  {'objectId': objectId }
        if Timeout !=  None:
            obj['Timeout'] = Timeout

        reqUrl =  self.cfgUrlBase+'ArpConfig'
        r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteArpConfig(self,
                        ArpConfigKey):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey,
                }
        reqUrl =  self.cfgUrlBase+'ArpConfig'
        r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def deleteArpConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'ArpConfig'+"/%s"%(objectId)
        r = requests.delete(reqUrl, data=None, headers=headers) 
        return r

    @processReturnCode
    def getArpConfig(self,
                     ArpConfigKey):
        obj =  { 
                'ArpConfigKey' : ArpConfigKey,
                }
        reqUrl =  self.stateUrlBase+'ArpConfig'
        r = requests.get(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    @processReturnCode
    def getArpConfigById(self, objectId ):
        reqUrl =  self.stateUrlBase+'ArpConfig'+"/%s"%(objectId)
        r = requests.get(reqUrl, data=None, headers=headers) 
        return r

    def getAllArpConfigs(self):
        return self.getObjects( 'ArpConfig', self.cfgUrlBase)


Configuring BFD
---------------
BFD provides an independent method to validate the operation of the forwarding plane between two routers.  
This can be utilized to ensure subsecond detection of a failure and be utilized to trigger an action in a routing protocol (severing a session or adjacency).


BFD Operation
^^^^^^^^^^^^^^

BFD in Flexswitch operates in the following manner 


Enabling BFD
^^^^^^^^^^^^

BFD Needs to be enabled in the following order:

 - Enable globally
 - Creation of BFD session parameters
 - Attach session User independent session or Routing protocol 

The above assumes that the BFD daemon is already running and has registered with the system. 


Configuring with Rest API 
"""""""""""""""""""""""""

Step 1. Enable BFD Globally

You need to set the "*Enable*" parameter to "*true*".  You can also see the "*Bfd*" parameter is set to the name "*default*".  This value is the 
VRF name where BFD will be Globally enabled. By default this is the "*default*" VRF and should not need to be set by the user. 

::

	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Bfd":"default","Enable":"true"}' 'http://<*your-switchip*>:8080/public/v1/config/BfdGlobal'
	

Step 2. Create BFD session parameters

Here we need to 

::

	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Name":"BFD_session","LocalMultiplier":"3","DesiredMinTxInterval":"250","RequiredMinRxInterval":"250","RequiredMinEchoRxInterval":"0","DemandEnabled":"false","AuthenticationEnabled":"false","AuthKeyId":"1","AuthData":"snaproute"}' 'http://<*your-switchip*>:8080/public/v1/Config/BfdSessionParam'
	

OPTIONS:

EXAMPLE:



Configuring with Python SDK
""""""""""""""""""""""""""""

Configuring BGP
---------------

Global
^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""
MultiPath
^^^^^^^^^
Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Neighbors 
^^^^^^^^^^
Timers
""""""
BFD 
"""
Local AS
""""""""
Authentication
""""""""""""""

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Peer Groups
^^^^^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Policies
^^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Route Reflectors
^^^^^^^^^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Add Path
^^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Configuring DHCP Relay
-----------------------
Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring LLDP
-----------------
Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Configuring LoopBacks
----------------------
Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring Logging
---------------------
System 
^^^^^^^
Configuring with Rest API 
""""""""""""""""""""""""""""""""""
Configuring with Python SDK
""""""""""""""""""""""""""""""""""

Daemon
^^^^^^^
Configuring with Rest API 
""""""""""""""""""""""""""""""""""
Configuring with Python SDK
""""""""""""""""""""""""""""""""""


Configuring OSPF
------------------

Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring IP Addresses
--------------------------

Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring Routing Policies 
-----------------------------
Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring Routing 
-------------------

Admin Distance
^^^^^^^^^^^^^^^
Static
^^^^^^^
Dynamic Protocols
^^^^^^^^^^^^^^^^^^
Policies 
^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
""""""""""""""""""""""""""""""""""

Configuring STP
----------------

RSTP
^^^^^
RSTP-PVST+
^^^^^^^^^^
Configuring with Rest API 
""""""""""""""""""""""""""""""""
Configuring with Python SDK
"""""""""""""""""""""""""""""""""""

Configuring VLANS
-------------------


Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Configuring VxLAN
--------------------

Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring VRRP
-------------------

Configuring with Rest API 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring with Python SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
