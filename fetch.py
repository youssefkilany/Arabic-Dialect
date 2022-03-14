import pandas as pd
import requests
import json

try:
    rawDataFile = open('arabicDialects.json', 'r', encoding='utf-8')
except Exception:
    datasetIds = pd.read_csv('dialect_dataset.csv').set_index('id')

    lnk = 'https://recruitment.aimtechnologies.co/ai-tasks'

    rawData = {}
    for i in range(0, len(data)+1, 1000):
        chunk = datasetIds.iloc[i:i+1000]
        body = list(map(str, chunk.index))
        body = json.dumps(body)
    #     print(i); assert len(body.split(',')) == 1000, 'not exactly 1000'
        res = requests.post(lnk, body)
        res = json.loads(res.text)
        rawData.update(res)

    with open(f'arabicDialects.json', 'w+', encoding='utf-8') as rawDataFile:
        json.dump(rawData, rawDataFile)
