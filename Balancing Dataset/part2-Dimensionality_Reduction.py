from sklearn.decomposition import TruncatedSVD
tr = TruncatedSVD(200)

p = tr.fit_transform(train_text)
print(sum(tr.explained_variance_ratio_))

''' The MinMax Scaling is done as the values after dimensionality reduction are very small'''
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
p = min_max_scaler.fit_transform(p)
