import requests
import pandas as pd

def get_applications(token="", api="http://localhost:8080/api/"):

    print("[SYS] Fetching application list from api: " + api)

    r = requests.get(
            url = api,
            headers={
                "Grpc-Metadata-Authorization": token ,
                "verify": "False"
                },
            params = {"limit":"100"}
            )

    data = r.json()

    return data["result"]


