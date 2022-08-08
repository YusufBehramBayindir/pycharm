# Tüm sütunlar gözüksün
pd.set_option('display.max_columns', None)

# Tüm satırlar gözüksün
# pd.set_option('display.max_rows', None)

#Sayısal değerlerin sıfırdan sonra kaç basamağını görmek istediğimizi belirtiriz
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# python -m pip install --upgrade pip
# pip install lifetimes

"""
import pandas as pd
import datetime as dt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from sklearn.preprocessing import MinMaxScaler

# konsolda yazı boyutunu 500 ile sınırlandırır.
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# yan yana olarak gösterir
pd.set_option('display.expand_frame_repr', False) 
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)

    print("##################### Types #####################")
    print(dataframe.dtypes)

    print("##################### Head #####################")
    print(dataframe.head(head))

    print("##################### Tail #####################")
    print(dataframe.tail(head))

    print("##################### NA #####################")
    print(dataframe.isnull().sum())

    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print(dataframe.describe().T)

check_df(df)

"""


# df.isnull().values.any()

"""
def bayesian_average_rating(n, confidence=0.95):
    if sum(n) == 0:
        return 0
    K = len(n)
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    N = sum(n)
    first_part = 0.0
    second_part = 0.0
    for k, n_k in enumerate(n):
        first_part += (k + 1) * (n[k] + 1) / (N + K)
        second_part += (k + 1) * (k + 1) * (n[k] + 1) / (N + K)
    score = first_part - z * math.sqrt((second_part - first_part * first_part) / (N + K + 1))
    return score

"""

"""
excel dosyası okunurken problem olursa bu şekilde çalıştırmak denenmeli

# pip install openpyxl
# df_ = pd.read_excel("datasets/online_retail_II.xlsx",
#                     sheet_name="Year 2010-2011", engine="openpyxl")

"""