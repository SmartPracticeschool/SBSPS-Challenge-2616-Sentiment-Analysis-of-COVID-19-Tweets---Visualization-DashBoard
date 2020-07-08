# statewise extraction of dataset from main datacollected

dict_state=[]
count_state=[]
for i in range(23):
  dict_state.append({})
  count_state.append({})

for index, row in df.iterrows():
    # print(row)
    row1=list(row)
    state=row1[len(row1)-1]

      # print(state)
    dt=row1[0].split('/')
    d1=date(int(dt[2]),int(dt[1]),int(dt[0]))
    delta=(d1-d0).days
    # print(dict_state,count_state)
    if delta in dict_state[state]:
      print(row1[col_size-2])
      dict_state[state][delta]+=(row1[4]+1)*(row1[col_size-2])
      count_state[state][delta]+=(row1[4]+1)
    else:
      print(row1[col_size-2])
      dict_state[state][delta]=(row1[4]+1)*(row1[col_size-2])
      count_state[state][delta]=(row1[4]+1)

for i in range(0,23):
  d1=dict_state[i]
  d2=count_state[i]
  for key in d1:
    d1[key]/=d2[key]

x_states=[]
y_states=[]

for i in range(0,23):
  lower_bound = 0.05
  upper_bound = 0.95
  
  y=y_states[i]
  x=x_states[i]
  if len(x)!=0:
    data_points = pd.DataFrame(y)
    end_points = data_points[0].quantile([lower_bound,upper_bound])
    indexes = (end_points.loc[lower_bound]<data_points[0].values) & (data_points[0].values<end_points.loc[upper_bound])
    # print(i)
    x1 = []
    y1 = []
    # print(i)
    for j in range(len(indexes)):
        if(indexes[j]==True):
            x1.append(x[j])
            y1.append(y[j])
    x_states[i]=x1
    y_states[i]=y1



x_state_fin=[]
y_state_fin=[]
for i in range(0,23):
  for j in range(0,len(x_states[i])):
    r=x_states[i][j]
    r.append(i)
    x_state_fin.append(r)
    y_state_fin.append(y_states[i][j])

    