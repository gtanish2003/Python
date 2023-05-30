import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

file=pd.read_csv('excel1.csv')
sns.scatterplot(x='Name',y='Matches',data=file)
plt.show()
