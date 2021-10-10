from pyjstat import pyjstat
import requests
ssburl = 'https://data.ssb.no/api/v0/no/table/06913/'
query = {
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "vs:Landet",
        "values": [
          "0"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Folkemengde"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}
resultat = requests.post(ssburl, json = query)
print(resultat)
dataset = pyjstat.Dataset.read(resultat.text)
type(dataset)
df = dataset.write('dataframe')
df.info
df.to_csv('befolkning.csv', index=False)
