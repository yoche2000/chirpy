import requests
import pandas as pd

def getdevprofid(token="", api="http://localhost:8080/api/"):

    print("[SYS] Fetching device profile list from api: " + api)

    r = requests.get(
            url = api+"device-profiles",
            headers={
                "Grpc-Metadata-Authorization": token ,
                "verify": "False"
                },
            params = {"limit":"100"}
            )

    data = r.json()

    return data["result"]

