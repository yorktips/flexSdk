.. FlexSwitchSDK documentation master file, created by
   sphinx-quickstart on Mon Apr  4 12:27:04 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Installation of FlexSwitch
==========================


Ubuntu/Debian Installation via Linux
--------------------------------------

1. SCP flexswitch debian package to the whitebox switch:
   *Default username: admin, default password: snaproute*

:: 
	
	Adams-MacBook-Pro:Apps acasella$ scp flexswitch_0.0.80_amd64.deb admin@10.1.10.240:./
	admin@10.1.10.240's password: 
	flexswitch_0.0.80_amd64.deb                                                                                                                                                    100%   59MB   9.9MB/s   00:06 ``

2. Once complete login to the whitebox switch and utilize dpkg to install package on the system:

:: 
	
	admin@localhost:~$ sudo dpkg -i flexswitch_0.0.80_amd64_wedge.deb 
	(Reading database ... 20599 files and directories currently installed.)
	Preparing to unpack flexswitch_0.0.80_amd64_wedge.deb ...
	Getting MAC address
	Stopping Daemon asicd
	Stopping Daemon sysd
	Stopping Daemon ribd
	Stopping Daemon bfdd
	Stopping Daemon arpd
	Stopping Daemon bgpd
	Stopping Daemon ospfd
	Stopping Daemon lacpd
	Stopping Daemon dhcprelayd
	Stopping Daemon stpd
	Stopping Daemon vrrpd
	Stopping Daemon lldpd
	Stopping Daemon vxland
	Stopping Daemon confd
	preinst INSTALL called with argument `upgrade'
	Unpacking flexswitch (0.0.80) over (0.0.80) ...
	Setting up flexswitch (0.0.80) ...
	postinst Configure called with unknown argument `configure'
	Getting MAC address
	Starting Daemon asicd Params: -params=/opt/flexswitch/params
	Starting Daemon sysd Params: -params=/opt/flexswitch/params
	Starting Daemon ribd Params: -params=/opt/flexswitch/params
	Starting Daemon bfdd Params: -params=/opt/flexswitch/params
	Starting Daemon arpd Params: -params=/opt/flexswitch/params
	Starting Daemon bgpd Params: -params=/opt/flexswitch/params
	Starting Daemon ospfd Params: -params=/opt/flexswitch/params
	Starting Daemon lacpd Params: -params=/opt/flexswitch/params
	Starting Daemon dhcprelayd Params: -params=/opt/flexswitch/params
	Starting Daemon stpd Params: -params=/opt/flexswitch/params
	Starting Daemon vrrpd Params: -params=/opt/flexswitch/params
	Starting Daemon lldpd Params: -params=/opt/flexswitch/params
	Starting Daemon vxland Params: -params=/opt/flexswitch/params
	Starting Daemon confd Params: -params=/opt/flexswitch/params
	Total time taken to start all 14 daemons is  0:00:28.025121
	Processing triggers for libc-bin (2.19-18+deb8u4) ...
	admin@localhost:~$`` 

3. Verify FlexSwitch is up and running via RestFul API
::

	curl --user admin:snaproute curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.243:8080/public/v1/state/SystemStatus' | python -m json.tool
	% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
									 Dload  Upload   Total   Spent    Left  Speed
	100  2311    0  2311    0     0   206k      0 --:--:-- --:--:-- --:--:--  225k
	{
		"Object": {
			"ConfigObj": null,
			"FlexDaemons": [
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 2 keepalives",
					"Name": "arpd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 3 keepalives",
					"Name": "stpd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 3 keepalives",
					"Name": "dhcprelayd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 3 keepalives",
					"Name": "ribd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 2 keepalives",
					"Name": "vxland",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 2 keepalives",
					"Name": "bfdd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 2 keepalives",
					"Name": "vrrpd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 3 keepalives",
					"Name": "lacpd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 3 keepalives",
					"Name": "bgpd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 3 keepalives",
					"Name": "lldpd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				},
				{
					"ConfigObj": null,
					"Enable": true,
					"KeepAlive": "Received 2 keepalives",
					"Name": "asicd",
					"Reason": "None",
					"RestartCount": 0,
					"RestartReason": "",
					"RestartTime": "",
					"State": "up",
					"Version": ""
				}
			],
			"Name": "rxp-tor-ru40",
			"NumActionCalls": "Total 0 Success 0",
			"NumCreateCalls": "Total 17 Success 16",
			"NumDeleteCalls": "Total 0 Success 0",
			"NumGetCalls": "Total 12 Success 9",
			"NumUpdateCalls": "Total 3 Success 2",
			"Ready": true,
			"Reason": "None",
			"SwVersion": "",
			"UpTime": "17h17m26.846427945s"
		},
		"ObjectId": ""
	}

4. To change the daemons that start on restart edit the file /opt/flexswitch/params/clients.json and remove or add daemon specific JSON, I.E. *{"Name": "<daemon>", "Port": <port-number>}*

::

	[
		{"Name": "asicd",
		 "Port": 4000},

		{"Name": "bgpd",
		 "Port": 4050},

		{"Name":"ribd",  
		 "Port":5000},
	
		{"Name":"arpd", 
		 "Port":6000},
		
		{"Name":"lacpd",
		 "Port":6050},

		{"Name":"ospfd",
		 "Port":7000},
	
		{"Name":"stpd",
		 "Port":7050},

		{"Name":"dhcprelayd",
		 "Port": 9000},

		{"Name":"bfdd",
		 "Port":9050},

		{"Name":"vrrpd",
		 "Port":10000},

		{"Name":"sysd",
		 "Port":10050},
	
		{"Name":"lldpd",
		 "Port":11000},
	
		{"Name":"vxland",
		 "Port":11059},
	
		{"Name":"local",
		  "Port":0}
	] 
..		
	Ubuntu/Debian Installation via FlexSwitch API
	---------------------------------------------

	1. Utilize HTTP PUT the FlexSwitch debian package to the whitebox switch.  Example below is done utilizing Linux cURL command, 

	::

		curl --user admin:snaproute --upload-file flexswitch_0.0.80_amd64.deb https://10.1.10.244:8080/public/v1/upload/
			% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
							 Dload  Upload   Total   Spent    Left  Speed
			100   254  100   254    0     0  38760      0 --:--:-- --:--:-- --:--:-- 42333
		
	2. Once the file is uploaded, list all files that are available for download

	::

		curl --user admin:snaproute --upload-file flexswitch_0.0.80_amd64.deb https://10.1.10.244:8080/public/v1/upload/
			% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
							 Dload  Upload   Total   Spent    Left  Speed
			100   254  100   254    0     0  38760      0 --:--:-- --:--:-- --:--:-- 42333
			{
			"StateObjects": [
			{
				"ObjectId": "",
				{
				  "Object": {
				  "File":"flexswitch_0.0.80_amd64.deb",
				  "Type":"Debian package",
				  "MD5":"07f67fc21949981007caf7dbee0908b0"
				   }
				},
				"ObjectId": "",
				{
				  "Object": {
				  "File":"flexswitch_0.0.70_amd64.deb",
				  "Type":"Debian package",
				  "MD5":"96d511af7d64a20aeee1d1ebf0ce89ed"
				   }
				},
			  ]
			}
		
	3. Trigger upgrade of device by specifying the file, time, and specifying "Yes" operator to start the upgrade. 

	::

		curl --user admin:snaproute -H "Content-Type: application/json" -d '{"File":"flexswitch_0.0.80_amd64.deb", "Upgrade":"Yes", "StartTime":"Now"}' https://10.1.10.242:8080/public/v1/upgrade/
			% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
							 Dload  Upload   Total   Spent    Left  Speed
			100   254  100   254    0     0  38760      0 --:--:-- --:--:-- --:--:-- 42333
			{
				"StateObjects": [
				{
					"ObjectId": "",
					{
					  "Object": {
					  "UpgradeStarted":"Success",
					  "UpgradeStartTime":"Wed Apr 13 14:22:44 PDT 2016",
					  "UpgradeEndTime":""
					  }
					},
				  ]
				}
			  

	You can also periodically check the status of the upgrade:

	::

		curl --user admin:snaproute -H "Content-Type: application/json"  https://10.1.10.242:8080/public/v1/state/UpgradeStatus/
			% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
							 Dload  Upload   Total   Spent    Left  Speed
			100   254  100   254    0     0  38760      0 --:--:-- --:--:-- --:--:-- 42333
			{
				"StateObjects": [
				{
					"ObjectId": "",
					{
					  "Object": {
					  "UpgradeStarted":"Running",
					  "UpgradeStartTime":"Wed Apr 13 14:22:44 PDT 2016",
					  "UpgradeEndTime":""
					  }
					},
				  ]
				}

		curl --user admin:snaproute -H "Content-Type: application/json"  https://10.1.10.242:8080/public/v1/state/UpgradeStatus/
			% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
							 Dload  Upload   Total   Spent    Left  Speed
			100   254  100   254    0     0  38760      0 --:--:-- --:--:-- --:--:-- 42333
			{
				"StateObjects": [
				{
					"ObjectId": "",
					{
					  "Object": {
					  "UpgradeStarted":"Complete",
					  "UpgradeStartTime":"Wed Apr 13 14:22:44:45 PDT 2016",
					  "UpgradeEndTime":""Wed Apr 13 14:22:45:10 PDT 2016"
					  }
					},
				  ]
				}		
		
	4. Confirm Daemon status by looking at the SystemStatus API and confirm correct version is running 

	::

		curl --user admin:snaproute curl -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://10.1.10.243:8080/public/v1/state/SystemStatus' | python -m json.tool
		% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
										 Dload  Upload   Total   Spent    Left  Speed
		100  2311    0  2311    0     0   206k      0 --:--:-- --:--:-- --:--:--  225k
		{
			"Object": {
				"ConfigObj": null,
				"FlexDaemons": [
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 2 keepalives",
						"Name": "arpd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 3 keepalives",
						"Name": "stpd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 3 keepalives",
						"Name": "dhcprelayd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 3 keepalives",
						"Name": "ribd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 2 keepalives",
						"Name": "vxland",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 2 keepalives",
						"Name": "bfdd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 2 keepalives",
						"Name": "vrrpd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 3 keepalives",
						"Name": "lacpd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 3 keepalives",
						"Name": "bgpd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 3 keepalives",
						"Name": "lldpd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					},
					{
						"ConfigObj": null,
						"Enable": true,
						"KeepAlive": "Received 2 keepalives",
						"Name": "asicd",
						"Reason": "None",
						"RestartCount": 0,
						"RestartReason": "",
						"RestartTime": "",
						"State": "up",
						"Version": ""
					}
				],
				"Name": "rxp-tor-ru40",
				"NumActionCalls": "Total 0 Success 0",
				"NumCreateCalls": "Total 17 Success 16",
				"NumDeleteCalls": "Total 0 Success 0",
				"NumGetCalls": "Total 12 Success 9",
				"NumUpdateCalls": "Total 3 Success 2",
				"Ready": true,
				"Reason": "None",
				"SwVersion": "",
				"UpTime": "17h17m26.846427945s"
			},
			"ObjectId": ""
		}

