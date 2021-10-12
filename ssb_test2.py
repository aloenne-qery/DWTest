from pyjstat import pyjstat
import requests
ssburl = 'https://data.ssb.no/api/v0/no/table/07221/'
query = {
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "item",
        "values": [
          "TOTAL"
        ]
      }
    },
    {
      "code": "Boligtype",
      "selection": {
        "filter": "item",
        "values": [
          "00",
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Boligindeks"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "top",
        "values": [
          17
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}
resultat = requests.post(ssburl, json = query)
dataset = pyjstat.Dataset.read(resultat.text)
type(dataset)
df = dataset.write('dataframe')
df.to_csv('bruktbolig1.csv', index=False)
