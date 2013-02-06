#!/usr/bin/env python


#Importing modules for HTTPS Connection
import urllib
import httplib

#Importing modules for parsing JSON 
import json
from pprint import pprint
import os
#Upload  environment information to Secpanel APIs
#Server for analysis.


#Get the JSON Data
import functions
json_response=functions.post_data(functions.get_info_in_json())

#Chomp new white chars to make a Good JSON
json_response=json_response.strip()

#Parse JSON String
parsed_json = json.loads(json_response)

#Create a blank Dictionary to store ip and respective 
#Geolocation attributes
ips=[]
total_records=0


#Read the parsed JSON
for keys in parsed_json:
 if keys=='total':
   total_records=int(parsed_json[keys])
 elif keys=='err':
    import sys
    print "Error : ",parsed_json[keys]
    sys.exit(1)
 elif keys=='ips':
    for ip in parsed_json[keys]:
       #Store the IPs
       ips.append(ip)
 else:
    print "Unknown Parameter : ",parsed_json[keys]

#Process as per application logic
if total_records < 1:
    print "No records returned"
else:
   for ip in ips:
        os.system("/usr/sbin/csf -d "+ip+" \"Blocked by Secpanel\" > /dev/null 2>&1")
        print "Requested CSF Firewall for blocking ",ip

