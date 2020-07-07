from imblearn.over_sampling import RandomOverSampler
sm1 = RandomOverSampler() 
t,t1 = sm1.fit_resample(t,t1)
