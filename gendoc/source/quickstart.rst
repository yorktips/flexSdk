.. FlexSwitchSDK documentation master file, created by
   sphinx-quickstart on Mon Apr  4 12:27:04 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


QuickStart Guide
================
What is FlexSwitch?
^^^^^^^^^^^^^^^^^^^
FlexSwitch is the first fully programmable layer2/3 network stack.  

How to use it?
^^^^^^^^^^^^^^

FlexSwitch comes supplied with a configuration manager which supplies the FrontEnd to our system and acts as a light-weight director of RESTful API calls.  This is the portion of the system, that will direct a configuration item to the appropriate daemon or database call.  In order to simplify how these calls are segmented for the user, the API calls are organized into two categories. *State* and *Config* operations.  Every object in the system has both a State and Config operation that can be performed against it.  

On the Config portion, this means when you supply the data you want in JSON format and sent to the associated API to have the configuration applied. For example, if you wanted to configure the global ARP timeout value, you would create the JSON and send to the ArpConfig REST API:


::

        root@5b5a8d783113:/# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"ArpConfigKey":"1", "Timeout":1000}' http://localhost:8080/public/v1/config/ArpConfig
        {"ObjectId":"a97b920d-8b10-47b1-7ea9-890b07f6e712","Error":""}
  
As you can see This is a 1:1 mapping of config to a specifc Object, in this case Timeout value of 1000 to ARP.


On the State side, this is more invovled, since you can have multiple items, that could potentially have thousand of different states.  Think the prefixes/next-hop entries` in the routing table or multiple IP/MAC mappings with an ARP table.  Due to this variance in data supplied, State operations are broken down into GetBulk, which supplies information from the entire object OR just an indiviual Get, which returns, just the parameters requested from an object.  The way in which these calls are made is based on the pluralization of the object itself.  

Lets use ARP again as an example.  If you wished to grab all entry's from the ARP table, you would query the "*ArpEntry*" state object. However, in order to dictate you wanted all entires, rather than a specific value, you would add a trailing "*s*" to make the operation plural, resulting in a call of "*ArpEntrys*", see below:

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


If you attempted to make such a call to just "*ArpEntry*", you would be returned an error:

::

	root@5c3bca6fb77e:/# curl  -H "Accept: application/json" "http://localhost:8080/public/v1/state/ArpEntry" | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
					 Dload  Upload   Total   Spent    Left  Speed
	100   119  100   119    0     0  21715      0 --:--:-- --:--:-- --:--:-- 23800
	{
	    "Error": "Failed to find entry. Internal error processing GetArpEntryState: Unable to find Arp entry for given IP: \n"
	}

This is due to the fact, that configruation manager expected JSON data to be supplied requesting a specific parameter to search the ARP table on. 


In order to sucessfully, complete the "*ArpEntry*" query, we will supply JSON data requrst for IP address 51.1.1.5:

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

The call now returns sucessfully with the requested data.  Also note, that returned data is no longer wrapped in GetBulk "*Objects*" header; I.E. the following is missing:
::

            "CurrentMarker": 0,
            "MoreExist": false,
            "NextMarker": 0,
            "ObjCount": 1,
            "Objects": [{}]



This is due to the fact, that only a single object of data was returned, rather than a multiple. 



