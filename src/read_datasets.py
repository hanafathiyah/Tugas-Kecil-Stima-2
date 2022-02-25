import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

def read_datasets():
    data = datasets.load(input_datasets);
    #create a DataFrame
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print(df.shape)
    df.head()