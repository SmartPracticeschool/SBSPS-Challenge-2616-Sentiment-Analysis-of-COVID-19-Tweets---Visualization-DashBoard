# training and testing on statewise data collected

region=['KL', 'MH', 'RJ', 'KA', 'GA', 'MP', 'UP', 'GJ', 'TN', 'JK', 'PY', 'HR', 'AP', 'WB', 'CT', 'OR', 'JH', 'AS', 'HP', 'AR', 'TR', 'UT', 'CH', 'DL']

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet,BayesianRidge

X_train,X_valid,y_train,y_valid = train_test_split(x_state_fin,y_state_fin,test_size=0.2)

alphas = [0.01,0.1,1,5]
max1 = 0
best = 0.1
print(X_train)
for alpha in alphas:
    reg = LinearRegression(alpha).fit(X_train, y_train)
    a = reg.score(X_valid,y_valid)
    if(a>max):
        best = alpha
        max1 = a

reg = LinearRegression(best).fit(X_train,y_train)

max2 = 0
best = 0.1
for alpha in alphas:
    reg = Lasso(alpha).fit(X_train, y_train)
    a = reg.score(X_valid,y_valid)
    if(a>max):
        best = alpha
        max2 = a

las = Lasso(best).fit(X_train,y_train)

max3 = 0
best = 0.1
for alpha in alphas:
    reg = Ridge(alpha).fit(X_train, y_train)
    a = reg.score(X_valid,y_valid)
    if(a>max):
        best = alpha
        max3 = a

rid = Ridge(best).fit(X_train,y_train)

max4 = 0
best = 0.1
for alpha in alphas:
    reg = ElasticNet(alpha).fit(X_train, y_train)
    a = reg.score(X_valid,y_valid)
    if(a>max):
        best = alpha
        max4 = a

ela = ElasticNet(best).fit(X_train,y_train)

max5 = 0
best = 1
for alpha in alphas:
    if alpha>=1:
        reg = BayesianRidge(alpha).fit(X_train, y_train)
        a = reg.score(X_valid,y_valid)
        if(a>max):
            best = alpha
            max5 = a

br = BayesianRidge(best).fit(X_train,y_train)

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
dt = DecisionTreeRegressor(max_depth=5)
rf = RandomForestRegressor(max_depth=5)
dt.fit(X_train,y_train)
rf.fit(X_train,y_train)

# plt.scatter(X_valid,y_valid)
# plt.show()

from sklearn.svm import SVR
clf = SVR()
clf.fit(X_train,y_train)

x_test=[]
for k in range(0,23):

  for j in range(60,200):
    x_test.append([j,k])
    
y_pred=reg.predict(x_test)
y_pred1=las.predict(x_test)
y_pred2 = rid.predict(x_test)
y_pred3 = ela.predict(x_test)
y_pred4 = br.predict(x_test)
y_pred5 = clf.predict(x_test)
y_pred6 = dt.predict(x_test)
y_pred7 = rf.predict(x_test)
#y_pred8 = xgb_reg.predict(x_test)
for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred0 = reg.predict(X_valid)
print('R2 score of Linar regreesion is: ',reg.score(X_valid,y_valid))
print('MSE of validation set for lin Reg: ',mean_squared_error(pred0,y_valid))
print('R2 score of Linar regreesion is: ',reg.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred1[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred1 = las.predict(X_valid)
print('R2 score of lasso is: ',las.score(X_valid,y_valid))
print('MSE of validation set for lasso: ',mean_squared_error(pred1,y_valid))
print('R2 score of lasso is: ',las.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred2[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred2 = rid.predict(X_valid)
print('R2 score of ridge is: ',rid.score(X_valid,y_valid))
print('MSE of validation set for Ridge: ',mean_squared_error(pred2,y_valid))
print('R2 score of ridge is: ',rid.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred3[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred3 = ela.predict(X_valid)
print('R2 score for Elastic is: ',ela.score(X_valid,y_valid))
print('MSE of validation set for Elastic Reg is: ',mean_squared_error(pred3,y_valid))
print('R2 score for Elastic is: ',ela.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred4[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred4 = br.predict(X_valid)
print('R2 score for bayesian ridge is: ',br.score(X_valid,y_valid))
print('MSE For validation set for bayesian ridge is: ',mean_squared_error(pred4,y_valid))
print('R2 score for bayesian ridge is: ',br.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred5[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred5 = clf.predict(X_valid)
print('R2 score for SVR is :',clf.score(X_valid,y_valid))
print('MSE for validation set for SVM is: ',mean_squared_error(pred5,y_valid))
print('R2 score for SVR is :',clf.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred6[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred6 = dt.predict(X_valid)
print('R2 score for decision tree is: ',dt.score(X_valid,y_valid))
print('MSE for validation set for Decision Tree is: ',mean_squared_error(pred6,y_valid))
print('R2 score for decision tree is: ',dt.score(X_train,y_train))

for k in range(0,23):
  
  xx=[]
  yy=[]
  for j in range(k*140,k*140+140): 
    xx.append(x_test[j][0])
    yy.append(y_pred7[j])
  plt.plot(xx,yy,label=region[k])
# plt.legend()
plt.show()
pred7 = rf.predict(X_valid)
print('R2 score for Random Forest is: ',rf.score(X_valid,y_valid))
print('MSE for validation set for Random Forest is: ',mean_squared_error(pred7,y_valid))
print('R2 score for Random Forest is: ',rf.score(X_train,y_train))