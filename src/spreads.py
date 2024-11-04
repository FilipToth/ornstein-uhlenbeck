import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# PEP, KO
pep = pd.read_pickle('../data/pep.pkl')[0]
ko = pd.read_pickle('../data/ko.pkl')[0]

spreads = pep - ko
spreads.to_pickle('../data/spreads.pkl')

sns.lineplot(data=spreads)
plt.show()
