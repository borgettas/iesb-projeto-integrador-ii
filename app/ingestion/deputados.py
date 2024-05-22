import json
import pandas as pd
import requests

response=requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome").json()
df = pd.DataFrame.from_dict(response["dados"], orient='columns')

with open("response.json", "w") as fp:
    json.dump(response , fp)   


print(df)