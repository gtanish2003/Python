import pandas as pd
import seaborn as sns
from matplotlib import  pyplot  as plt

file=pd.read_csv('excel1.csv')
print(file.head())

sns.barplot(x='Name',y='Matches',data=file,hue='Run',palette='rocket')
plt.show()