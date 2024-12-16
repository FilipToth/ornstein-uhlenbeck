# Normalize equity prices to an initial value;
# this is standard practice in stat-arb and will
# make directional effects stronger because we
# omit magnitudes.

# Read from `nasdaq_original` and write
# normalized to `nasdaq`

import os
import pandas as pd

data_path = "../data/nasdaq_original/"
export_path = "../data/nasdaq/"

for filename in os.listdir(data_path):
    file = os.path.join(data_path, filename)
    df = pd.read_pickle(file)

    prices = df[0]
    initial = prices[0]
    normalized = prices / initial

    export_file = os.path.join(export_path, filename)
    normalized.to_pickle(export_file)
