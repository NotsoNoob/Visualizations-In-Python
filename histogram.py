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
