import pandas as pd
import numpy as np

ticker = input('ticker? ')
data = pd.read_pickle(f"../data/{ticker}.pkl")
print(data)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
sns.lineplot(data=data[0])
plt.title('Filtered Close Prices Without Linear Segments')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()
