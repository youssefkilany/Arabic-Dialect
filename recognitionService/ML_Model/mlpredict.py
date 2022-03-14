# from ArabicDialect.ArabicDialect.settings import STATIC_ROOT

from cProfile import label
from csv import Dialect
from operator import inv
from django.conf import settings

import os
import json
import joblib
import pandas as pd
from sklearn import pipeline

from sklearn.pipeline import Pipeline
# from sklearn.linear_model import SGDClassifier
# from sklearn.ensemble import RandomForestClassifier, VotingClassifier

from .preprocessing import clean

STATIC_URL = 'static'

DialectsJsonURI = f'{STATIC_URL}/dialects.json'

datasetIds = pd.read_csv(f'{STATIC_URL}/dialect_dataset.csv', usecols=['dialect'])

try:
    with open(DialectsJsonURI, 'r') as dialectsJson:
        dialectsMap = json.load(dialectsJson)
except Exception:
    # This is a csv link that lists all countries with their 2 digit code
    # Not sure if PL code belongs to Poland, but I'm gussing PL here actually means
    # Palestine, according to `Figure 1` in `arXiv:2005.06557` linked in the pdf.
    # 'https://pkgstore.datahub.io/core/country-list/data_csv/data/d7c9d7cfb42cb69f4422dec222dbbaa8/data_csv.csv'
    country_iso = f'{STATIC_URL}/data_csv.csv'
    country_iso = pd.read_csv(country_iso, index_col='Code')
    country_iso.loc['PL'] = 'Palestine'

    countries = country_iso.loc[datasetIds,'Name'].values
    dialectsMap = dict(sorted(zip(datasetIds, countries)))

    with open(DialectsJsonURI, 'w+') as dialectsJson:
        json.dump(dialectsMap, dialectsJson)


dialects = sorted(datasetIds.dialect.unique())
label_map = dict(zip(dialects, range(len(dialects))))
inv_label_map = dict(enumerate(dialects))

# this model from pkl, already contains the pipeline for
# transforming inputs then predicting
sgd = joblib.load(f'{STATIC_URL}/SGDClassifier_0.pkl')

eclf = joblib.load(f'{STATIC_URL}/VotingClassifier.pkl')

def mlpredict(text):
    input = clean(text)
    pred = sgd.predict([input])[0]
    # pred = eclf.predict([input])[0]
    pred = inv_label_map[pred]
    dialect = dialectsMap.get(pred, f'{pred} -- dialect not found')
    return dialect
