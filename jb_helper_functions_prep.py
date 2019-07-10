import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

def create_enc(df, columns):
    for col in columns:
        df[col+'_enc'] = df[col]
        encoder = LabelEncoder()
        encoder.fit(df[col])
        df[col+'_enc'] = encoder.transform(df[col])
    return df