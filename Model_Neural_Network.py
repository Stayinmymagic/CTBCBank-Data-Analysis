from tensorflow.python.keras.layers.core import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.models import Sequential
#%%
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
model=Sequential()
#%%
model.add(Dense(units=1, input_dim=17,activation='sigmoid'))
#model.add(Dense(units=200, input_dim=17,activation='relu'))
#model.add(Dense(units=20, input_dim=17,activation='softmax'))
#%%
model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['acc'])
#%%
his=model.fit(x,y,epochs=10,verbose=0)
#%%
import matplotlib.pyplot as plt
plt.plot(range(10),his.history.get('acc'))
#%%
predictions=model.predict(x)
#%%














