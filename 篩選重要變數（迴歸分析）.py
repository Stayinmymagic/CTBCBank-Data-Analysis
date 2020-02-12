import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#匯入資料
df=pd.read_hdf('D:\Data\data_all_1.h5')

#%%
asset2list=[]
li20=list(df['asset20list'])
for i in li20:
    if 0<i<15:
        asset2list.append(1)
    elif 14<i<21:
        asset2list.append(2)
df.insert(2,"asset2list",asset2list)  
#%%
df_c1=df[df['asset2list']==1]
df_c2=df[df['asset2list']==2]
#%%
df_c1=df_c1.sample(100000)
df_c2=df_c2.sample(100000,replace=True)
df_sam=pd.concat([df_c1,df_c2],axis=0)

#%%model1
X=df_sam[['deplist','Education_Code','Gender_Code','Marital_Status_Code','monthly_income']]
y=df_sam[['asset2list']]


X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=0)



sc=StandardScaler()
sc.fit(X_train)

X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)


classifier=LogisticRegression()
classifier.fit(X_train_std,y_train)
y_pro=pd.DataFrame(classifier.predict_proba(X_test_std))

#%%model2
df_c1=df[df['asset4list']==1]
df_c2=df[df['asset4list']==2]
df_c1=df_c1.sample(100000,replace=True)
df_c2=df_c2.sample(100000,replace=True)
df_sam=pd.concat([df_c1,df_c2],axis=0)
#%%
X=df_sam[['deplist','Education_Code','Gender_Code','Marital_Status_Code','monthly_income']]
y=df_sam[['asset2list']]

X_train2, X_test2, y_train2, y_test2= train_test_split(X,y,test_size=0.3,random_state=0)

sc=StandardScaler()
sc.fit(X_train)

X_train_std2=sc.transform(X_train)
X_test_std2=sc.transform(X_test)

classifier2=LogisticRegression()
classifier2.fit(X_train_std2,y_train)
y_pro2=pd.DataFrame(classifier2.predict_proba(X_test_std2))
#%%
y_pred2=[]
for i in range(len(y_pro[[]])):
    if y_pro2[0][i]>0.2:
        y_pred2.append(1)
    else:
        y_pred2.append(2)
cm=confusion_matrix(y_test2,y_pred2)
print(cm)
print('Accuracy: '+str(accuracy_score(y_test2,y_pred2)))
#%%
y_pred=[]
for i in range(len(y_pro[[]])):
    if y_pro[0][i]>0.563:
        y_pro2[0]
    else:
        y_pred.append(2)
          
from sklearn.metrics import confusion_matrix, accuracy_score
cm=confusion_matrix(y_test,y_pred)
print(cm)
print('Accuracy: '+str(accuracy_score(y_test,y_pred)))
#%%

