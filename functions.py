#!/usr/bin/env python

import re
def get_banned_ip_address():
        ret_str=""
        try:
          matches=[]
          fp=open("/etc/csf/csf.deny","r")
          for line in fp:
            matches.extend(re.findall("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+",line))
          #Take unquie collections IP
          matches=list(set(matches))
          for item in matches:
                ret_str+=item+";"
        except Exception, err:
          ret_str=str(err)
        return ret_str

import os
def get_load():
        ret_str=""
        try:
           matches=os.getloadavg()
           for item in matches:
             ret_str+=str(item)+";"
        except Exception, err:
          ret_str=str(err)
        return ret_str

def get_total_ram():
        ret_str=""
        try:
          matches=[]
          fp=open("/proc/meminfo","r")
          for line in fp:
            matches.extend(re.findall("^MemTotal:.*",line))
          ram=matches[0].rsplit(':')[1]
          ret_str=ram.lstrip()
        except Exception, err:
          ret_str=str(err)
        return ret_str


from datetime import timedelta
def get_uptime():
    ret_str=""
    try:
        with open('/proc/uptime', 'r') as f:
           uptime_seconds = float(f.readline().split()[0])
           uptime_string = str(timedelta(seconds = uptime_seconds))
           ret_str=uptime_string
    except Exception, err:
        ret_str=str(err)
    return ret_str


import platform
import datetime
from subprocess import Popen, PIPE
import multiprocessing
def get_info_in_json():
        json_str="{\n"
        json_str+=" \"os\":\""+platform.system()+"\",\n"
        json_str+=" \"processor\":\""+platform.processor()+"\",\n"
        json_str+=" \"release\":\""+platform.release()+"\",\n"
        json_str+=" \"uname\":\""
        items=platform.uname()
        for item in items:
                json_str+=item+";"
        json_str+="\",\n"
        items=platform.linux_distribution()
        json_str+=" \"distro\":\""
        for item in items:
                json_str+=item+";"
        json_str+="\",\n"
        items=platform.libc_ver()
        json_str+=" \"libc\":\""
        for item in items:
                json_str+=item+";"
        json_str+="\",\n"
        json_str+=" \"tram\":\""+get_total_ram()+"\",\n"
        json_str+=" \"ncpu\":\""+str(multiprocessing.cpu_count())+"\",\n"
        json_str+=" \"uptime\":\""+get_uptime()+"\",\n"
        json_str+=" \"date\":\""+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\",\n"
        json_str+=" \"badips\":\""+get_banned_ip_address()+"\",\n"
        json_str+=" \"load\":\""+get_load()+"\"\n"
        json_str+="}\n"
        return json_str




import urllib
import httplib
import urllib2
import json
import string
def post_data(json_text):

        params={}
        parsed_json = json.loads(json_text)
        for keys in parsed_json:
          params[keys]=parsed_json[keys]

        data = urllib.urlencode(params)

        h = httplib.HTTPSConnection('apis.secpanel.com');

        headers = {
                        "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"
                  }

        h.request('POST', '/csf/receive.php', data, headers)
        r = h.getresponse()
        return r.read()


