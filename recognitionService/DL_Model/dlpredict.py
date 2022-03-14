from transformers import *

from arabert.preprocess import ArabertPreprocessor

from recognitionService.ML_Model.mlpredict import dialectsMap

STATIC_URL = 'static'

# A dummy tiny model for testing ~ 30mb
dlModel = f'{STATIC_URL}/bert-tiny-mnli'

# AraBERT trained on QADI Arabic Dialect dataset - 1 epoch ~ 600mb
# dlModel = f'{STATIC_URL}/ArabiceDialect_BERT'

pipe = pipeline('sentiment-analysis', model=dlModel,
                max_length=90, truncation=True,
                # uncomment this line to return all classes with probs
                # return_all_scores=True, 
                )

def dlpredict(text):
    s = pipe([text])

    # incase return all class with probs
    # topK = 3
    # preds = sorted([(x['score'], x['label']) for x in s[0]], reverse=True)
    # pred = preds[:topK]
    # dialect = [(dialectsMap.get(x,f'{x[1]} -- dialect not found'), x[0]) for x in pred]

    pred = s[0]['label']
    dialect = dialectsMap.get(pred, f'{pred} -- dialect not found')
    return dialect
