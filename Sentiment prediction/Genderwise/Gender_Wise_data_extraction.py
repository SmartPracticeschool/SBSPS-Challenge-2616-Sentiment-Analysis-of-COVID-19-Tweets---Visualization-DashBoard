### We will create a dictionary of dicionary with 3 keys for gender 0 - male,1 - female, 2- third gender
### further for each key there is a dctionary with keys as date
### dict_gender is for storing the mean sentiments for each gender for each day
### count_gender is for storing the number of tweets for each gender for each day

dict_gender={0:{},1:{},2:{}}
count_gender={0:{},1:{},2:{}}

for index, row in df.iterrows():
    
    row1=list(row)
    # The 2nd row contains the gender 0 for male 1 for female 2 for third gender
    gender=row1[2]

    dt=row1[0].split('/')
    # our date is in dd/mm/yyyy format  
    d1=date(int(dt[2]),int(dt[1]),int(dt[0]))
    delta=(d1-d0).days
    
    
    if delta in dict_gender[gender]:
      
      # The 4th row contains the number of retweets for each tweet and 2nd last column contains the sentiment
      dict_gender[gender][delta]+=(row1[4]+1)*(row1[col_size-2])
      count_gender[gender][delta]+=(row1[4]+1)
      for j in range(3):
         if j!=gender:
            if delta not in dict_gender[j]:
                dict_gender[j][delta]=0
                count_gender[j][delta]=0
            else:
                dict_gender[j][delta]+=0
                count_gender[j][delta]+=0
    else:
    
      dict_gender[gender][delta]=(row1[4]+1)*(row1[col_size-2])
      count_gender[gender][delta]=(row1[4]+1)
      for j in range(3):
          if j!=gender:
             if delta not in dict_gender[j]:
               dict_gender[j][delta]=0
               count_gender[j][delta]=0
             else:
                dict_gender[j][delta]+=0
                count_gender[j][delta]+=0
        
for i in range(0,3):
  d1=dict_gender[i]
  d2=count_gender[i]
  for key in d1:
    d1[key]/=(d2[key]+1)
    
x_gender=[]
y_gender=[]

for i in range(0,3):
  d=dict_gender[i]
  set = d.keys()
  x11=[]
  y11=[]
  for key in sorted(d.keys()):
    y11.append(d[key])
    ar=[]
    ar.append(key)
    x11.append(ar)
  x_gender.append(x11)
  y_gender.append(y11)


x_gender_fin=[]
y_gender_fin=[]
for i in range(0,3):
  for j in range(0,len(x_gender[i])):
    r=x_gender[i][j]
    r.append(i)
    x_gender_fin.append(r)
    y_gender_fin.append(y_gender[i][j])

####  Now x_gender_fin and y_gender_fin is prepared for training 
####  x_gender_fin is of the format [[date,gender]]
####  y_gender_fin contains corresponding prediction for the date and gender given

