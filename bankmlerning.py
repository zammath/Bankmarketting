import pandas as pd
import numpy as np
from sklearn.ensemble import  RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings
import pickle
import streamlit as st
warnings.filterwarnings("ignore")

df=pd.read_csv("bank.csv")


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['job']= le.fit_transform(df['job'])

le1=LabelEncoder()
df['marital']= le1.fit_transform(df['marital'])

le1=LabelEncoder()
df['education']= le1.fit_transform(df['education'])

le2=LabelEncoder()
df['default']= le2.fit_transform(df['default'])

le3=LabelEncoder()
df['housing']= le3.fit_transform(df['housing'])

le4=LabelEncoder()
df['loan']= le4.fit_transform(df['loan'])

le5=LabelEncoder()
df['contact']= le5.fit_transform(df['contact'])

le6=LabelEncoder()
df['month']= le6.fit_transform(df['month'])

le7=LabelEncoder()
df['poutcome']= le7.fit_transform(df['poutcome'])

le8=LabelEncoder()
df['deposit']= le8.fit_transform(df['deposit'])

df.drop(["default"],axis=1)
df=np.array(df)


X = df[1:, 1:-1]
y = df[1:, -1]
y = y.astype('int')
X = X.astype('int')

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.75,random_state=0)




from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(X_train)
x_test=sc.fit_transform(X_test)


from sklearn.linear_model import LogisticRegression
lg_model=LogisticRegression()
lg_model.fit(X_train,y_train)
pred=lg_model.predict(X_test)

from sklearn.metrics import  accuracy_score
acc=accuracy_score(y_test,pred)

rf_model=RandomForestClassifier()
rf_model.fit(X_train,y_train)

y_pred=rf_model.predict(X_test)

from sklearn.metrics import  accuracy_score
acc1=accuracy_score(y_test,y_pred)


from sklearn.svm import SVC
sv_model=SVC()
sv_model.fit(X_train,y_train)
y_pred1=rf_model.predict(X_test)

from sklearn.metrics import  accuracy_score
acc2=accuracy_score(y_test,y_pred1)



pickle.dump(rf_model,open('rf_model.pkl','wb'))
pickle.dump(lg_model,open('lg_model.pkl','wb'))
pickle.dump(sv_model,open('sv_model.pkl','wb'))