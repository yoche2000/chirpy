import requests
import pandas as pd

def post_devices(appid, dpid, name, desc, deui, token="", api="http://localhost:8080/api/"):

   headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Grpc-Metadata-Authorization': token
        }

    data = '{  "device": { "applicationID": "var_appid",  "description": "var_desc",  "devEUI": "var_deui", "deviceProfileID": "var_dpid", "isDisabled": true, "name": "var_name", "referenceAltitude": 0, "skipFCntCheck": true, "tags": {}, "variables": {} }  }'
    
    data = data.replace("var_appid", appid)
    data = data.replace("var_desc", desc)
    data = data.replace("var_deui", deui)
    data = data.replace("var_name", name)
    data = data.replace("var_dpid", dpid)

    response = requests.post(api, headers=headers, data=data)
    data = response.json()

    if data != {}:
        print("[ERR] Device "+ deui + ": " +str(data['error']))

    #return

