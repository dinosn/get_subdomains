#!/usr/bin/python3
import requests
import traceback
import json
import os
import urllib3
import sys
import socket
urllib3.disable_warnings()


def get_sub_domains(domain):
    url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
    querystring = {"children_only":"true"}
    headers = {
    'accept': "application/json",
    'apikey': "securitytrails_api_key_goes_here"
    }
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    result_json=json.loads(response.text)
    sub_domains=[i+'.'+domain for i in result_json['subdomains']]
    f=open(domain + '_results.txt','a+')
    for i in sub_domains:
        f.write(i+'\n')
    f.close()   
    return sub_domains

def resolve_all(domain):
    with open(domain + '_results.txt','r') as domain_file:
        for hostname in domain_file.readlines():
            hostname = hostname.strip()
            try:
                ip = socket.gethostbyname(hostname)
                print(ip)
                f=open(domain + '_ip.txt','a+')
                f.write(ip + ' ' + hostname + '\n')
            except:
                print('Unable to resolve: ' + hostname)


if __name__ == '__main__' :
    try:
        domain = sys.argv[1]
        get_sub_domains (domain) 
        resolve_all(domain)
    except:
        traceback.print_exc()
        print('Usage: python3 get_sub.py domain')
        pass
