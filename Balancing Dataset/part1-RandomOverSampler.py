from imblearn.over_sampling import RandomOverSampler
sm1 = RandomOverSampler() 
### t - dataset, t1 - predictions
t,t1 = sm1.fit_resample(t,t1)
 
