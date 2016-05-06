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
	
	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"ArpConfigKey":"VRF Name", "Timeout":<*Timeout Value in seconds*>}' 'http://<*your-switchip*>:8080/public/v1/config/ArpConfig'
	

OPTIONS:

+------------+------------+-------------------------------------------+----------+----------+
| Variables  | Type       |  Description                              | Required |  Default |   
+============+============+===========================================+==========+==========+ 
|ArpConfigKey| string     | VRF name where configuration is applied.  |    No    | "default"|
+------------+------------+-------------------------------------------+----------+----------+
| Timeout    | int32      | Length of ARP timeout in seconds.         |    Yes   |    600s  |   
+------------+------------+-------------------------------------------+----------+----------+ 


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

Setting the ARP Timeout to 1000 seconds via FlexSwitch's Python SDK, utilizing method *createArpConfig()*. 

COMMAND:
::

	>>> FlexSwitch("*Switch IP*", *TCP port*).createArpConfig("<*VRF*>",<"*Timeout*">)
	
OPTIONS:

::
	
  createArpConfig(self, param string ArpConfigKey :  Arp config VRF ID,
                        param int32 Timeout :  Global Arp entry timeout value. Default value:600 seconds)

+------------------+------------+------------+-------------------------------------------+----------+----------+
| Python Method    | Variables  | Type       |  Description                              | Required |  Default |   
+==================+============+============+===========================================+==========+==========+ 
| createArpConfig  |ArpConfigKey| string     | VRF name where configuration is applied.  |    No    | "default"|
+                  +------------+------------+-------------------------------------------+----------+----------+
|                  | Timeout    | int32      | Length of ARP timeout in seconds.         |    Yes   |    600s  |   
+------------------+------------+------------+-------------------------------------------+----------+----------+   


EXAMPLE:

Below are examples for utilizing this method via the Python CLI, python script and Displaying the results 

1. Python CLI:


::  

	>>>from flexswitchV2 import FlexSwitch
	>>> FlexSwitch("10.1.10.243", 8080).createArpConfig("1", 1000)
	({u'ObjectId': u'45dff5a0-7dc1-441d-723d-ccf731186ece', u'Error': u''}, None)      

	>>> FlexSwitch("10.1.10.243", 8080).getAllArpConfigs()
	[{u'Object': {u'ConfigObj': None, u'ArpConfigKey': u'1', u'Timeout': 1000}, u'ObjectId': u'45dff5a0-7dc1-441d-723d-ccf731186ece'},	

.. Note:: the ObjectID and UUID are the same.

2. Utilizing a Python Script to set ARP timeout

::

	#!/usr/bin/python
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		switch_ip = "10.1.10.243"
		Timeout=1000
		restIf = FlexSwitch(switch_ip, 8080)
		restIf.createArpConfig("1",Timeout)


3. Display results of this change:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		switch_ip = "10.1.10.243"
		restIf = FlexSwitch(switch_ip, 8080)
		print json.dumps(restIf.getAllArpConfigs(), indent=4)	

Output:

::

	acasella@snaproute-lab-r710-1:~$ python getarpconfig.py 
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

-----------------

Configuring Static Entries
^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring with Rest API 
""""""""""""""""""""""""""""""""

FlexSwitch has a REST based API, and below is an example utilzing Linux cURL:

COMMAND:
::

        curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"IP":"<*IPv4 Address*>", "MAC":"<*MAC address*>"}' 'http://<*your-switchip*>:8080/public/v1/config/ArpConfig'


OPTIONS:

+------------+------------+---------------------------------------------------+----------+----------+
| Variables  | Type       |  Description                                      | Required |  Default |    
+============+============+===================================================+==========+==========+  
| IP         | String     | IPv4 address to have a static entry applied       |    Yes   |   None   |
+------------+------------+---------------------------------------------------+----------+----------+
| MAC        | String     | Layer 2 MAC address associated with IPv4 address. |    Yes   |   None   |   
+------------+------------+---------------------------------------------------+----------+----------+  

	
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
Setting a static arp entry via FlexSwitch's Python SDK, utilizing method *createArpStatic()*. 


COMMAND:
::

	>>> FlexSwitch("<*Switch IP*>", <*TCP port*>).createArpStatic(<*IPv4Address*>, <*MAC*>)

OPTIONS:
::

   createArpStatic(self, param string IPv4Address :  IPv4 address for ARP,
        				 param string MAC  :   MAC address associated with IPv4 address)


+------------------+------------+------------+---------------------------------------------------+----------+----------+
| Python Method    | Variables  | Type       |  Description                                      | Required |  Default |    
+==================+============+============+===================================================+==========+==========+  
| createArpStatic  | IP         | String     | IPv4 address to have a static entry applied       |    Yes   |   None   |
+                  +------------+------------+---------------------------------------------------+----------+----------+
|                  | MAC        | String     | Layer 2 MAC address associated with IPv4 address. |    Yes   |   None   |   
+------------------+------------+------------+---------------------------------------------------+----------+----------+  

EXAMPLE:

Below are examples for utilizing this method via the Python CLI, python script and displaying the results:

1. Python CLI:

::

	>>>from flexswitchV2 import FlexSwitch
	>>> FlexSwitch("10.1.10.243", 8080).createArpStatic("50.1.1.10","01:23:34:56:78")
	({u'ObjectId': u'9e81f7d4-f9f0-4c86-556b-6398e47897bc', u'Error': u''}, None)
	
2. Utilizing a Python Script to set Static ARP:

::

	#!/usr/bin/python
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		switch_ip = "10.1.10.243"
		Timeout=1000
		restIf = FlexSwitch(switch_ip, 8080)
		arp_ip="192.168.0.1"
		mac="01:23:34:56:78"
		restIf.createArpStatic(arp_ip,mac)


3. Display results of this change:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		switch_ip = "10.1.10.243"
		restIf = FlexSwitch(switch_ip, 8080)
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

----------------------

Display ARP Entry
^^^^^^^^^^^^^^^^^

Display All ARP Entries
"""""""""""""""""""""""

Display via Rest API 
********************
 
Utilizing the GetBulk API for ARP, "*ArpEntrys*", we can display all ARP entries learned on the device.  

COMMAND:
::

        curl -X GET --header 'Content-Type: application/json' 'http://<*your-switchip*>:8080/public/v1/state/ArpEntrys'


OPTIONS

::

	None

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


Displaying via Python SDK
*************************

Displaying all ARP entries utilizing FlexSwitch's Python SDK, utilizing method *getAllArpEntryStates()*

COMMAND:

::

	>>> FlexSwitch("<*Switch IP*>", <*TCP Port*>).getAllArpEntryStates()


OPTIONS:

::

   getAllArpEntryStates(self)
	

EXAMPLE:

Below are examples for utilizing this method via the Python CLI, python script and displaying the results:

1. Python CLI 
::

	>>>from flexswitchV2 import FlexSwitch
	>>>FlexSwitch("10.1.10.243", 8080).getAllArpEntryStates()
	[{u'Object': {u'ConfigObj': None, u'Intf': u'fpPort47', u'Vlan': u'Internal Vlan', u'IpAddr': u'172.16.0.14', u'ExpiryTimeLeft': u'9m24.869691096s', u'MacAddr': u'a8:9d:21:aa:8e:01'}, u'ObjectId': u''}, {u'Object': {u'ConfigObj': None, u'Intf': u'fpPort49', u'Vlan': u'Internal Vlan', u'IpAddr': u'172.16.0.20', u'ExpiryTimeLeft': u'9m43.991376701s', u'MacAddr': u'00:02:03:04:05:00'}, u'ObjectId': u''}]



2. Utilizing a Python Script pretty print Arp Entries

You can display the results of this change with the following Python Script:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		switch_ip = "10.1.10.243"
		restIf = FlexSwitch(switch_ip, 8080)
		print json.dumps(restIf.getAllArpEntryStates(), indent=4)	

Output:

::

	acasella@snaproute-lab-r710-1:~$ python getAllArpEntry.py
	[
		{
			"Object": {
				"ConfigObj": null, 
				"Intf": "fpPort47", 
				"Vlan": "Internal Vlan", 
				"IpAddr": "172.16.0.14", 
				"ExpiryTimeLeft": "16m38.415016779s", 
				"MacAddr": "a8:9d:21:aa:8e:01"
			}, 
			"ObjectId": ""
		}, 
		{
			"Object": {
				"ConfigObj": null, 
				"Intf": "fpPort49", 
				"Vlan": "Internal Vlan", 
				"IpAddr": "172.16.0.20", 
				"ExpiryTimeLeft": "16m29.520461011s", 
				"MacAddr": "00:02:03:04:05:00"
			}, 
			"ObjectId": ""
		}
	]


-----------------------

Display a specific ARP entry
""""""""""""""""""""""""""""

Display via Rest API 
********************

You can return the value of an object based on any of the variables within that object.  For example you can query an ARP entry via an IPv4 Address. 

The example below will show how to grab a specific ARP entry based on IP address. 

COMMAND:

::

	curl -X GET --header 'Content-Type: application/json' -d '{"IpAddr":"<*IPv4 Address*>"}' 'http://<*your-switchip*>:8080/public/v1/state/ArpEntry'


OPTIONS:

+------------+------------+---------------------------------------+----------+----------+
| Variables  | Type       |  Description                          | Required |  Default |     
+============+============+=======================================+==========+==========+   
| IpAddr     | String     | IPv4 Address ArpEntry to be queried   |    Yes   |   None   |
+------------+------------+---------------------------------------+----------+----------+

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



Displaying via Python SDK
*************************

Displaying all ARP entries utilizing FlexSwitch's Python SDK, utilizing method *getAllArpEntryStates()*

COMMAND:

::

	>>> FlexSwitch("<*Switch IP*>", <*TCP Port*>).getArpEntryState("<*IPv4Address*>")

OPTIONS:

::

	getArpEntryState(self, param string IPv4Address :  IPv4 address to return from ARP Table)

+------------------+------------+-------+--------------------------------------+----------+----------+
| Python Method    | Variables  | Type  | Description                          | Required |  Default |  
+==================+============+=======+======================================+==========+==========+
| getArpEntryState | IPv4Address| String|  IPv4 Address ArpEntry to be queried |    Yes   |   None   |
+------------------+------------+-------+--------------------------------------+----------+----------+

	
EXAMPLE:

::

	>>>from flexswitchV2 import FlexSwitch
	>>> FlexSwitch("10.1.10.243", 8080).getArpEntryState("172.16.0.20")
	({u'Object': {u'ConfigObj': None, u'Intf': u'fpPort49', u'Vlan': u'Internal Vlan', u'IpAddr': u'172.16.0.20', u'ExpiryTimeLeft': u'16m38.505153914s', u'MacAddr': u'00:02:03:04:05:00'}, u'ObjectId': u''}, None)


.. Hint:: You can pretty print the results with the following python script:

::

	#!/usr/bin/python
	import json
	from flexswitchV2 import FlexSwitch


	if __name__ =='__main__':
		switch_ip = "10.1.10.243"
		restIf = FlexSwitch(switch_ip, 8080)
		print json.dumps(restIf.getArpEntryState("172.16.0.20"), indent=4)

Output:

::

	acasella@snaproute-lab-r710-1:~$  python ~/getArpState.py
	[
		{
			"Object": {
				"ConfigObj": null, 
				"Intf": "fpPort49", 
				"Vlan": "Internal Vlan", 
				"IpAddr": "172.16.0.20", 
				"ExpiryTimeLeft": "16m19.337528389s", 
				"MacAddr": "00:02:03:04:05:00"
			}, 
			"ObjectId": ""
		}, 
		null
	]



-------------------------

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

---------------------

---------------------

Configuring BFD
---------------
BFD provides an independent method to validate the operation of the forwarding plane between two routers.  
This can be utilized to ensure subsecond detection of a failure and be utilized to trigger an action in a routing protocol (severing a session or adjacency).

BFD Support
^^^^^^^^^^^

BFD supports the following options:

 - Asynchronous mode
 - Demand mode
 - Authentication  
 - BGP peer failure detection 

-------------

BFD Operation
^^^^^^^^^^^^^^

Flexswitch's BFD implementation was designed to allow for single or multi-hop sessions. This is done by either having an IP based BFD session, where there could be one of many layer 3 hops between the two devices
or interface based sessions, where the BFD peer, much be directly attached.  This allows for BFD sessions to be tied an interface based protocol, such as OSPF vs a peer-based protocol, such as BGP. 

------------------

Session Establishment 
"""""""""""""""""""""

BFD session establishments begins by implementing a slow timer, by setting the *Desired min Tx Interval* to 2000 ms with a multiplier of 3, resulting in a 6000ms timeout for hello packets that are sent.  
This is done to ensure proper interoperability between 3rd-party peers by ensuring the appropriate BFD parameters are correctly negotiated; I.E. RemoteDiscriminator, SessionState and failure detection timers. 
Once this information is negotiated, we begin to send BFD hello packets at the configured rate. 

If a BFD session does not see hello packets within the configured *Required min Rx Interval*, three things occur:

	1. BFD session state is set to down 
	2. Any associated protocol sessions are torn down
	3. BFD will flush the learned Remote Discriminator  
	
If BFD is associated to a particular protocol, BFD will hold down that protocols session state, until the associated routing-protocol or user-created session is reset by an administrator.   If BFD is brought administratively-down (either locally or remotely), the BFD session is cleared without any impact 
to the associated protocol and only the BFD session is self is torn down. 

For details surrounding specific routing protocol implementations, check out the "BGP with BFD" or "OSPF with BFD" sections. 

Demand Mode
""""""""""""

In demand mode, no Hello packets are exchanged after the session is established; it is assumed that the endpoints have another way to verify connectivity to each other, perhaps on the underlying physical layer.

Per-link
""""""""

Since traditional Asynchronous BFD is an IP point-to-point protocol, it has no concept of layer 2 links that may exist between two devices.  This is especially true for layer 2 port-channels with multiple member-links.   
If these one of these links happen to fail, while BFD is running across them, it may result in a false-positive detection of a connectivity failure.  This could have unintended impact, by bringing down an associated routing-protocol session incorrectly, 
thus taking our an entire port-channel, rather than a single-link.  

BFD over LAG or BFD per-link was created as an enhancement to limit the impact of single port-channel member-link failure.  When BFD per-link is enabled on a port-channel interface, an asynchronous mode BFD sessions is run on every port-channel member link.  This allows for failure detection of a single port-channel member-link, 
limiting the impact and traffic-transitions to only links that failed.  When all BFD sessions fail on a particular port-channel interface, only then are the associated protocol sessions torn down, allowing for accurate fault detection. 


Protocol Specific failure detection
""""""""""""""""""""""""""""""""""""

For more details on how BFD integrates with other protocols, please see that protocols specific section:

    - BGP with BFD 
    - OSPF with BFD 
    
-------------------

Enabling BFD
^^^^^^^^^^^^

BFD is enabled in the following order:

 1. Enable globally (Default when daemon is started)
 2. Creation of BFD session parameter profile
 3. Attach to User created BFD session or a routing protocol 
 4. Review configuration and state 

The above assumes that the BFD daemon is already running and has registered with the system. 

-----------------

Configuring with Rest API 
"""""""""""""""""""""""""

Enable BFD Globally
*******************

You need to set the "*Enable*" parameter to "*true*".  You can also see the "*Bfd*" parameter is set to the name "*default*".  This value is the 
VRF name where BFD will be Globally enabled. By default this is the "*default*" VRF and should not need to be set by the user. 

.. Note::BFD is enabled by default when the Daemon is started. 

COMMAND:
::

	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Bfd":"default","Enable":"true"}' 'http://<*your-switchip*>:8080/public/v1/config/BfdGlobal'
	

OPTIONS:

+------------+------------+--------------------------------------------------------+----------+----------+
| Variables  | Type       |  Description                                           | Required |  Default |     
+============+============+========================================================+==========+==========+   
| Bfd        | string     | VRF where BFD will be enabled.                         |    Yes   |   None   |
+------------+------------+--------------------------------------------------------+----------+----------+
| Enable     | boolean    | IPv4 Address ArpEntry to be queried; I.E. true/false.  |    Yes   |   None   |
+------------+------------+--------------------------------------------------------+----------+----------+


EXAMPLE:
::
	
	acasella@snaproute-lab-r710-1:~$ curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Bfd":"default","Enable":true}' 'http://10.1.10.43:8080/public/v1/config/BfdGlobal'
	{"ObjectId":"0880b0cb-d0da-461e-7826-9b2eef1b800e","Error":""}

Creating BFD session parameters 
*******************************

COMMAND:
::

	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Name":"<*Param Profile Name*>","LocalMultiplier":3,"DesiredMinTxInterval":250,"RequiredMinRxInterval":250,"RequiredMinEchoRxInterval":0,"DemandEnabled":false,"AuthenticationEnabled":false,"AuthKeyId":1,"AuthData":"snaproute"}' 'http://<*your-switchip*>:8080/public/v1/config/BfdSessionParam'
	

OPTIONS:


+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| Variables                 | Type       |  Description                                                                     | Required |  Default  |     
+===========================+============+==================================================================================+==========+===========+   
| Name                      | string     | Name of the BFD session                                                          |    Yes   |   None    |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| LocalMultiplier           | int32      | Multiplier of BFD hello RX interval to wait before tearing down session          |    no    |   3       |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| DesiredMinTxInterval      | int32      | Time in milliseconds between interval TX of BFD hello packets                    |    no    |   1000    |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| RequiredMinRxInterval     | int32      | Expected interval in milliseconds between RX of BFD  packets                     |    no    |   1000    |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| RequiredMinRxEchoInterval | int32      | Expected interval in milliseconds between RX of BFD echo packets                 |    no    |   0       |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| DemandEnabled             | boolean    | Boolean value to specify the global state for BFD demand mode; I.E. true/false   |    no    |   false   |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| AuthenticationEnabled     | boolean    | Boolean value to specify the global state for BFD authentication; I.E. true/false|    no    |   false   |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| AuthType                  | string     | Authentication type; I.E. keyed MD5, simple, keyed Sha1                          |    no    |   None    |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| AuthKeyId                 | int32      | Authentication key ID                                                            |    no    |   1       |
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| AuthData                  | string     | Authentication string                                                            |    no    |"snaproute"|
+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+



EXAMPLE:

::

	acasella@snaproute-lab-r710-1:~$ curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"Name":"BFD_session","LocalMultiplier":3,"DesiredMinTxInterval":250,"RequiredMinRxInterval":250,"RequiredMinEchoRxInterval":0,"DemandEnabled":false,"AuthenticationEnabled":false,"AuthKeyId":1,"AuthData":"snaproute"}' 'http://10.1.10.43:8080/public/v1/config/BfdSessionParam'
	{"ObjectId":"40ebf60d-1230-4c7b-4c91-bc4a076693d4","Error":""}
	
	
Attaching BFD params to a BFD session  
*************************************

	Attaching to user create BFD session:

		1. Create User session with BFD session parameter profile specified
		
			COMMAND:
			::
				
				curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"IpAddr":"<*IPv4 Address*>","ParamName":"<*Param Profile Name*>","Interface":"None","Owner":"user"}' 'http://<*your-switchip*>:8080/public/v1/config/BfdSession'

				
			OPTIONS:
				+-----------+------------+---------------------------------------------------------------------------------------+----------+-----------+
				| Variables | Type       |  Description                                                                          | Required |  Default  |     
				+===========+============+=======================================================================================+==========+===========+   
				| IpAddr    | string     | BFD neighbor IP address                                                               |    Yes   |   None    |
				+-----------+------------+---------------------------------------------------------------------------------------+----------+-----------+
				| ParaName  | string     | Name of the session parameters object to be applied on this session                   |    no    | "default" |
				+-----------+------------+---------------------------------------------------------------------------------------+----------+-----------+
				| Interface | boolean    | Name of the interface this session has to be established on                           |    no    |   None    |
				+-----------+------------+---------------------------------------------------------------------------------------+----------+-----------+
				| PerLink   | string     | Run BFD sessions on individual link of a LAG if the neighbor is reachable through LAG |    no    |   false   |
				+-----------+------------+---------------------------------------------------------------------------------------+----------+-----------+
				| Owner     | string     | Module requesting BFD session configuration                                           |    no    |   user    |
				+-----------+------------+---------------------------------------------------------------------------------------+----------+-----------+
						
			
			
			EXAMPLE:
			::
				
				curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"IpAddr":"1.1.1.1","ParamName":"BFD_session","Interface":"None","Owner":"user"}' 'http://10.1.10.43:8080/public/v1/config/BfdSession'

	Attaching to protocol created BFD session:

		For more details on how BFD integrates with other protocols, please goto that protocols specific section:

		    - BGP with BFD 
   		    - OSPF with BFD 
    
							

Configuring BFD demand mode
***************************

Configuring BFD Authentication
******************************


Displaying Configuration and State
**********************************


Display BFD session parameter profile configuration:

COMMAND:
::
	
	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.43:8080/public/v1/config/BfdSessionParams'

OPTIONS:
::
	
	None
	
EXAMPLE:
	
We can start by looking at the BFD configuration of was setup in the example sections above.  We can view the session parameters:

::

	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.43:8080/public/v1/config/BfdSessionParams' | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
									 Dload  Upload   Total   Spent    Left  Speed
	100   386  100   386    0     0  51411      0 --:--:-- --:--:-- --:--:-- 55142
	{
		"CurrentMarker": 0,
		"MoreExist": false,
		"NextMarker": 0,
		"ObjCount": 1,
		"Objects": [
			{
				"Object": {
					"AuthData": "snaproute",
					"AuthKeyId": 1,
					"AuthType": "",
					"AuthenticationEnabled": false,
					"ConfigObj": null,
					"DemandEnabled": false,
					"DesiredMinTxInterval": 250,
					"LocalMultiplier": 3,
					"Name": "BFD_session",
					"RequiredMinEchoRxInterval": 0,
					"RequiredMinRxInterval": 250
				},
				"ObjectId": "4c46080c-f4c1-477b-6ce3-873aee89ab9c"
			}
		]
	}


Display BFD Session configuration:


COMMAND:
::
	
	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.43:8080/public/v1/config/BfdSessions'

OPTIONS:
::
	
	None
	
EXAMPLE:

Below we can see the BFD Session Parameter profile "BFD_Session": parameter profile as well:

::

	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.43:8080/public/v1/config/BfdSessions' | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
									 Dload  Upload   Total   Spent    Left  Speed
	100   431  100   431    0     0  64987      0 --:--:-- --:--:-- --:--:-- 71833
	{
		"CurrentMarker": 0,
		"MoreExist": false,
		"NextMarker": 0,
		"ObjCount": 1,
		"Objects": [
			{
				"Object": {
					"ConfigObj": null,
					"Interface": "None",
					"IpAddr": "1.1.1.1",
					"Owner": "user",
					"ParamName": "BFD_session",
					"PerLink": false
				},
				"ObjectId": "b825914b-5b6c-4c5f-6a65-a80fc958d38d"
			},



Display BFD Session Parameter State:


COMMAND:

::

	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.245:8080/public/v1/state/BfdSessionParams'

OPTIONS:
::
	
	None
	
EXAMPLE:

When we look at the BfdSessionParams status, we see very similar data to that of the configuration, but there are a few very important differences:

1. This indicated that BFDd has ingested the configuration and is ready to begin utilizing it.
2. State related items to show us how this configuration is being utilized. 

   
If we look at the "NumSessions" variable, we can see this BFD session parameter profile is being utilized by 1 BFD session. We can also see that the 
millisecond variables we utilized in the configuration have been changed to microseconds.  This is done for RFC compliance and interoperability with 3rd-party
BFD implementations. 


::

	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.43:8080/public/v1/state/BfdSessionParams' | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
									 Dload  Upload   Total   Spent    Left  Speed
	100   789  100   789    0     0  55657      0 --:--:-- --:--:-- --:--:-- 60692
	{
		"CurrentMarker": 0,
		"MoreExist": false,
		"NextMarker": 0,
		"ObjCount": 1,
		"Objects": [
			{
				"Object": {
					"AuthenticationData": "snaproute",
					"AuthenticationEnabled": false,
					"AuthenticationKeyId": 1,
					"AuthenticationType": "",
					"ConfigObj": null,
					"DemandEnabled": false,
					"DesiredMinTxInterval": "250000(us)",
					"LocalMultiplier": 3,
					"Name": "BFD_session",
					"NumSessions": 0,
					"RequiredMinEchoRxInterval": "0(us)",
					"RequiredMinRxInterval": "250000(us)"
				},
				"ObjectId": "4c46080c-f4c1-477b-6ce3-873aee89ab9c"
			}
		]
	}

Display BFD Session State:


COMMAND:

::

	curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.245:8080/public/v1/state/BfdSessions'

OPTIONS:
::
	
	None
	
EXAMPLE:

The BfdSessions state API responds with the relevant state of all BFD sessions.  We can see the current BFD timers being utilized, the BFD Parameter Profile this information was
inherited via the *ParamName* variable, BFD_Sessions in this case. As well aa BFD session status via *SessionState* variable, which is up and working. 

::

	curl -H "Content-Type: application/json" 'http://10.1.10.245:8080/public/v1/state/BfdSessions' | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
									 Dload  Upload   Total   Spent    Left  Speed
	100  1391  100  1391    0     0  95371      0 --:--:-- --:--:-- --:--:-- 99357
	{
		"CurrentMarker": 0,
		"MoreExist": false,
		"NextMarker": 0,
		"ObjCount": 2,
		"Objects": [
			{
				"Object": {
					"AuthSeqKnown": false,
					"AuthType": "",
					"ConfigObj": null,
					"DemandMode": false,
					"DesiredMinTxInterval": "250000(us)",
					"DetectionMultiplier": 3,
					"IfIndex": 30,
					"IfName": "",
					"InterfaceSpecific": false,
					"IpAddr": "1.1.1.1",
					"LocalDiagType": "None",
					"LocalDiscriminator": 979,
					"LocalMacAddr": "",
					"NumRxPackets": 217275,
					"NumTxPackets": 199389,
					"ParamName": "BFD_Sessions",
					"PerLinkSession": false,
					"ReceivedAuthSeq": 0,
					"RegisteredProtocols": "user, ",
					"RemoteDemandMode": false,
					"RemoteDiscriminator": 533,
					"RemoteMacAddr": "",
					"RemoteMinRxInterval": "250000(us)",
					"RemoteSessionState": "up",
					"RequiredMinRxInterval": "250000(us)",
					"SentAuthSeq": 0,
					"SessionId": 979,
					"SessionState": "up"
				},
				"ObjectId": ""
			},

-------------------

Configuring with Python SDK
"""""""""""""""""""""""""""

COMMAND:

	>>> FlexSwitch("<*Switch IP*>", <*TCP port*>).createBfdSessionParam(<*Name*>, <*LocalMultiplier*>, <*DesiredMinTxInterval*>, <*RequiredMinRxInterval*>,<*RequiredMinRxEchoInterval*>,<*DemandEnabled*>,<*AuthenticationEnabled*>, <*AuthKeyId*>,<*AuthData*> )

OPTIONS:

+------------------------+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
| Python Method          | Variables                 | Type       |  Description                                                                     | Required |  Default  |     
+========================+===========================+============+==================================================================================+==========+===========+   
| createBfdSessionParam  | Name                      | string     | Name of the BFD session                                                          |    Yes   |   None    |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | LocalMultiplier           | int32      | Multiplier of BFD hello RX interval to wait before tearing down session          |    no    |   3       |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | DesiredMinTxInterval      | int32      | Time in milliseconds between interval TX of BFD hello packets                    |    no    |   1000    |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | RequiredMinRxInterval     | int32      | Expected interval in milliseconds between RX of BFD  packets                     |    no    |   1000    |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | RequiredMinRxEchoInterval | int32      | Expected interval in milliseconds between RX of BFD echo packets                 |    no    |   0       |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | DemandEnabled             | boolean    | Boolean value to specify the global state for BFD demand mode; I.E. true/false   |    no    |   false   |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | AuthenticationEnabled     | boolean    | Boolean value to specify the global state for BFD authentication; I.E. true/false|    no    |   false   |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | AuthKeyId                 | int32      | Authentication key ID                                                            |    no    |   1       |
|                        +---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+
|                        | AuthData                  | string     | Authentication string                                                            |    no    |"snaproute"|
+------------------------+---------------------------+------------+----------------------------------------------------------------------------------+----------+-----------+

::

	createBfdSessionParam(self,
       					 param string Name :  Session parameters  Session parameters
       					 param uint32 RequiredMinRxInterval :  Required minimum rx interval in ms  Required minimum rx interval in ms
       					 param string AuthData :  Authentication password  Authentication password
       					 param bool DemandEnabled :  Enable or disable demand mode  Enable or disable demand mode
       					 param uint32 AuthKeyId :  Authentication key id  Authentication key id
       					 param string AuthType :  Authentication type  Authentication type
       					 param uint32 DesiredMinTxInterval :  Desired minimum tx interval in ms  Desired minimum tx interval in ms
       					 param bool AuthenticationEnabled :  Enable or disable authentication  Enable or disable authentication
       					 param uint32 RequiredMinEchoRxInterval :  Required minimum echo rx interval in ms  Required minimum echo rx interval in ms
       					 param uint32 LocalMultiplier :  Detection multiplier  Detection multiplier



EXAMPLE:




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
