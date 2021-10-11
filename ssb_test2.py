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
          "01",
          "02",
          "03"
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
        "filter": "item",
        "values": [
          "2016K1",
          "2016K2",
          "2016K3",
          "2016K4",
          "2017K1",
          "2017K2",
          "2017K3",
          "2017K4",
          "2018K1",
          "2018K2",
          "2018K3",
          "2018K4",
          "2019K1",
          "2019K2",
          "2019K3",
          "2019K4",
          "2020K1",
          "2020K2",
          "2020K3",
          "2020K4",
          "2021K1",
          "2021K2"
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
df.to_csv('bruktbolig.csv', index=False)
