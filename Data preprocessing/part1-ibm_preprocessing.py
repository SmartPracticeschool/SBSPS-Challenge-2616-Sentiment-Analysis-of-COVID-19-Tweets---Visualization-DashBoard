from googletrans import Translator
import csv
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import pandas as pd
import os

java_path = "C:/Java/jre-10.0.1/bin/java.exe"
os.environ['JAVAHOME'] = java_path
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz',
                       'stanford-ner.jar',
                       encoding='utf-8')
df = pd.read_excel('dataset_actual.xlsx',encoding="utf-8")

f=open("dataset_processed.csv","w", encoding='utf-8')
w = csv.writer(f,lineterminator='\n')
for i in range(len(df)):
	try:
		translator=Translator()
		row=[df['Date'][i],df['Name'][i],df['Gender'][i],df['Text'][i],df['Retweets'][i],df['State'][i],df['Corona cases']]
		tokenized=word_tokenize(row[1])
		classified_text = st.tag(tokenized)
		print(classified_text[0][1])
		if classified_text[0][1]=='PERSON':
			row[3]=translator.translate(row[3])
			w.writerow(row)
	except Exception as e:
		print(e)
		continue
