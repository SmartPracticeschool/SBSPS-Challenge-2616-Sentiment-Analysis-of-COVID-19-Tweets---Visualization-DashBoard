import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
# Stop words considered are coronavirus,covid19,lockdown,and,the,corona,at,is,you,your,#
# Also words with min freq <=3 are removed
vectorizer = TfidfVectorizer(min_df=3,stop_words={'coronavirus','covid19','lockdown','and','the','corona','at','is','you','your',"#"})
train_text = vectorizer.fit_transform(X_t)
