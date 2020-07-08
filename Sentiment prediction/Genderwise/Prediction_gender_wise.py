

"""Now no outlier is present in the graph.

# Training and testing on various ML models

The models used are:
1) Linear
2) Lasso
3) Ridge
4) Elastic Net
5) Bayesian Ridge
6) SVR
7) Decision Tree
8) Random Forest
"""

from sklearn.model_selection import train_test_split

X_train,X_valid,y_train,y_valid = train_test_split(x_gender_fin,y_gender_fin,test_size=0.2)

from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet,BayesianRidge
alphas = [0.01,0.1,1,5]
max1 = 0
best = 0.1
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



y_pred=reg.predict(x_test)
y_pred1=las.predict(x_test)
y_pred2 = rid.predict(x_test)
y_pred3 = ela.predict(x_test)
y_pred4 = br.predict(x_test)
y_pred5 = clf.predict(x_test)
y_pred6 = dt.predict(x_test)
y_pred7 = rf.predict(x_test)
#y_pred8 = xgb_reg.predict(x_test)
# for k in range(3):
#     xx=[]
#     yy=[]
#     for j in range(0,10): 
#       xx.append(x_test[j][k])
#       yy.append(y_pred[j])
#     plt.plot(xx,yy)
# # plt.legend()
# plt.show()
pred0 = reg.predict(X_valid)
xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred0[j+t])
            elif t==1:
                yy2.append(pred0[j+t])
            else:
                yy3.append(pred0[j+t])
        j+=3

plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',reg.score(X_train,y_train))
print('R2 score of Linar regreesion is: ',reg.score(X_valid,y_valid))
print('MSE of validation set for lin Reg: ',mean_squared_error(pred0,y_valid))



pred1 = las.predict(X_valid)
xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred1[j+t])
            elif t==1:
                yy2.append(pred1[j+t])
            else:
                yy3.append(pred1[j+t])
        j+=3
plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',las.score(X_train,y_train))
print('R2 score of lasso is: ',las.score(X_valid,y_valid))
print('MSE of validation set for lasso: ',mean_squared_error(pred1,y_valid))


pred2 = rid.predict(X_valid)

xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred2[j+t])
            elif t==1:
                yy2.append(pred2[j+t])
            else:
                yy3.append(pred2[j+t])
        j+=3
plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',rid.score(X_train,y_train))
print('R2 score of ridge is: ',rid.score(X_valid,y_valid))
print('MSE of validation set for Ridge: ',mean_squared_error(pred2,y_valid))

pred3 = ela.predict(X_valid)

xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred3[j+t])
            elif t==1:
                yy2.append(pred3[j+t])
            else:
                yy3.append(pred3[j+t])
        j+=3
plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',ela.score(X_train,y_train))
print('R2 score for Elastic is: ',ela.score(X_valid,y_valid))
print('MSE of validation set for Elastic Reg is: ',mean_squared_error(pred3,y_valid))


pred4 = br.predict(X_valid)

xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred4[j+t])
            elif t==1:
                yy2.append(pred4[j+t])
            else:
                yy3.append(pred4[j+t])
        j+=3
plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',br.score(X_train,y_train))
print('R2 score for bayesian ridge is: ',br.score(X_valid,y_valid))
print('MSE For validation set for bayesian ridge is: ',mean_squared_error(pred4,y_valid))

pred5 = clf.predict(X_valid)

xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred5[j+t])
            elif t==1:
                yy2.append(pred5[j+t])
            else:
                yy3.append(pred5[j+t])
        j+=3


plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',clf.score(X_train,y_train))
print('R2 score for SVR is :',clf.score(X_valid,y_valid))
print('MSE for validation set for SVM is: ',mean_squared_error(pred5,y_valid))

pred6 = dt.predict(X_valid)

xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred6[j+t])
            elif t==1:
                yy2.append(pred6[j+t])
            else:
                yy3.append(pred6[j+t])
        j+=3
plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',dt.score(X_train,y_train))
print('R2 score for decision tree is: ',dt.score(X_valid,y_valid))
print('MSE for validation set for Decision Tree is: ',mean_squared_error(pred6,y_valid))

pred7 = rf.predict(X_valid)

xx1 = []
yy1 = []
yy2 = []
yy3 = []

j = 0 
while(j<len(X_valid)-2):
        xx1.append(j)
        for t in range(3):
            if t==0:
                yy1.append(pred7[j+t])
            elif t==1:
                yy2.append(pred7[j+t])
            else:
                yy3.append(pred7[j+t])
        j+=3
        
plt.plot(xx1,yy1)
plt.plot(xx1,yy2)
plt.plot(xx1,yy3)
plt.show()

print('Model score is: ',rf.score(X_train,y_train))
print('R2 score for Random Forest is: ',rf.score(X_valid,y_valid))
print('MSE for validation set for Random Forest is: ',mean_squared_error(pred7,y_valid))

"""# We will use SVR (clf) as it is not very well fitted to the validation set and neither too badly fitted So it will be a good estimator for new Data Points"""



"""The models used are:
1) Linear
2) Lasso
3) Ridge
4) Elastic Net
5) Bayesian Ridge
6) SVR
7) Decision Tree
8) Random Forest
"""

