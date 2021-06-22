#!/usr/bin/env python
import requests

token = (
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjQzNzIwNjAsIm5iZiI6MTYyNDM3MjA2MCwianRpIjoiN2IzM2VjN2UtYTEzYy00Yjc3LTk1NWEtZjQ4YWY0MWJkOGVjIiwiZXhwIjoxNjI0NDU4NDYwLCJpZGVudGl0eSI6InBoMTdiMDExQHNtYWlsLmlpdG0uYWMuaW4iLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.bD3JmLaZp7Uy2GOdQaIJgUP-gNIaKRyzFPj_IOEFNDQ'
)
hostname = 'materiae.iphy.ac.cn'
#url = "http://%s/api/materials" % hostname
url = "http://%s/api/materials?spacegroup.number[in]=194" % hostname
#params = {'nsoc_topo_class': 'GM_SM'}
headers = {'Authorization': 'Bearer %s' % token}

response = requests.get(url=url, headers=headers)

count = response.json()['count']
mats = response.json()['materials']

for mat in mats:
    url = "http://%s/api/materials/%s" % (hostname, mat['id'])
    #params = {'fields': 'mp_id'}
    headers = {'Authorization': 'Bearer %s' % token}
    response = requests.get(url=url, headers=headers)
    print(response.json()) 
