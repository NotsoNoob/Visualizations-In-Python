import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##change the file path
df = pd.read_csv("file path")

##checking column names ##
df.info()

## Checking for null values ##

df.isna().sum()


## Histogram ##

help(sns.histplot)

sns.histplot(data = df['SepalLengthCm'], kde = True, bins = 5 , color = 'brown', stat='density')
plt.title('Customized Histogram with Seaborn')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

f.info()

## Checking for null values ##

df.isna().sum()


## Histogram 1 ##

help(sns.histplot)

bin_edges=list(range(2011, 2026))

sns.histplot(data = df, x='Model Year' ,bins = bin_edges ,color = 'green', hue = 'Electric Vehicle Type', legend = True)
plt.title('Year wise electrical vehicle data')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.show()

df=pd_read_csv('file path')
##histogram 2##

##counting the occurunces 
df['Make'].value_counts()

#labeling tesla vs others
categories_to_keep = ['TESLA','CHEVROLET','NISSAN','FORD','KIA']
df['Make_grouped'] = df['Make'].apply(lambda x: x if x in categories_to_keep else 'Others')
hue_order = ['TESLA','CHEVROLET','NISSAN','FORD','KIA','Others']
sns.histplot(data=df,x = 'Model Year',bins=bin_edges[7:],color='red',hue = 'Make_grouped',hue_order=hue_order, stat='count')
