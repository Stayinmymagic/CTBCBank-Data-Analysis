import pandas as pd
import numpy as np
df=pd.read_hdf('D:\Data\data_all_5.h5')
#%%
print(df.columns)
#%%
x=df[['deplist', 'Education_Code', 'house', 'age', 'Gender_Code',
       'Marital_Status_Code', 'monthly_income']]
#%%
y=df[['asset20list']]
#%%
set(x['Marital_Status_Code'])
#%%
x=x.copy()
x.loc[:,'Education_Code_1']=(x.Education_Code==1).astype('int')
x.loc[:,'Education_Code_2']=(x.Education_Code==2).astype('int')
x.loc[:,'Education_Code_3']=(x.Education_Code==3).astype('int')
x.loc[:,'Education_Code_7']=(x.Education_Code==7).astype('int')
x.loc[:,'Education_Code_8']=(x.Education_Code==8).astype('int')
x.loc[:,'Education_Code_9']=(x.Education_Code==9).astype('int')
del x['Education_Code']
#%%
x.loc[:,'house_0']=(x.house==0).astype('int')
x.loc[:,'house_1']=(x.house==1).astype('int')
x.loc[:,'house_2']=(x.house==2).astype('int')
del x['house']
#%%
x.loc[:,'Gender_Code_1']=(x.Gender_Code==1).astype('int')
x.loc[:,'Gender_Code_2']=(x.Gender_Code==2).astype('int')
del x['Gender_Code']
#%%
x.loc[:,'Marital_Status_Code_1']=(x.Marital_Status_Code==1).astype('int')
x.loc[:,'Marital_Status_Code_2']=(x.Marital_Status_Code==2).astype('int')
x.loc[:,'Marital_Status_Code_3']=(x.Marital_Status_Code==3).astype('int')
del x['Marital_Status_Code']
#%%
print(x.columns)
#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
        x,y,test_size=0.3, random_state=0)
#%%
from sklearn.tree import DecisionTreeClassifier
tree=DecisionTreeClassifier(criterion='entropy',random_state=0)
#%%
tree.fit(x_train,y_train)
tree.score(x_test,y_test)
#%%
y_pred=tree.predict(x_test)
#%%
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
cm=confusion_matrix(y_test,y_pred)
print(cm)
print('Accuracy: '+str(accuracy_score(y_test,y_pred)))

#%%
cm=confusion_matrix(y_test,y_pred)
pd.options.display.float_format='{:,.5f}'.format
cm=pd.DataFrame(cm)
ratio=[]

for j in range(len(cm[[]])):
    su=0
    for k in range(len(cm[[]])):
        su=su+cm[cm.columns[k]][cm.index[j]]
    ratio.append('%.4f'%(cm[cm.columns[j]][cm.index[j]]/su))
cm.insert(len(cm[[]]),'ratio',ratio)
print(cm)

print('Accuracy: '+str(accuracy_score(y_test,y_pred)))
#%%
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(max_depth=100,random_state=0)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
#%%
cm=confusion_matrix(y_test,y_pred)
pd.options.display.float_format='{:,.5f}'.format
cm=pd.DataFrame(cm)
ratio=[]

for j in range(len(cm[[]])):
    su=0
    for k in range(len(cm[[]])):
        su=su+cm[cm.columns[k]][cm.index[j]]
    ratio.append('%.4f'%(cm[cm.columns[j]][cm.index[j]]/su))
cm.insert(len(cm[[]]),'ratio',ratio)
print(cm)

print('Accuracy: '+str(accuracy_score(y_test,y_pred)))






