for index, row in df.iterrows():
    # print(row)
    row1=list(row)
    dt=row1[0].split('/')
    d1=date(int(dt[2]),int(dt[1]),int(dt[0]))
    delta=(d1-d0).days
    if delta in d:
      #row1[col_size-2] contains the sentiment
      #row1[4] contains the number of retweets for the particular tweet
      # d dict contains the mean sentiment for the particular day
      #count dict contains the number of tweets on that particular day
    
      d[delta]+=(row1[4]+1)*(row1[col_size-2])
      count[delta]+=1
    else:
      
      d[delta]=(row1[4]+1)*(row1[col_size-2])
      count[delta]=1


for key in d:
  d[key]/=(count[key])

x=[]
y=[]
set = d.keys()
for key in sorted(d.keys()):
  y.append(d[key])
  ar=[]
  ar.append(key)
  x.append(ar)

import matplotlib.pyplot as plt
plt.scatter(x,y)

### Outlier Removal

lower_bound = 0.05
upper_bound = 0.95
data_points = pd.DataFrame(y)
end_points = data_points[0].quantile([lower_bound,upper_bound])
indexes = (end_points.loc[lower_bound]<data_points[0].values) & (data_points[0].values<end_points.loc[upper_bound])
### indexes store the index of days where it is an outlier or not

x1 = []
y1 = []
for i in range(len(indexes)):
    if(indexes[i]==True):
        x1.append(x[i])
        y1.append(y[i])

### x1 contains the days which we are considering for training which are not outlier
### y1 contains the prediction for corresponding days. 
plt.scatter(x1,y1)
