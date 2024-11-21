import math
import numpy as np
import pandas as pd
import statsmodels.api as sm

def calibrate(xt):
    # get the mean of the spreads
    index = xt.index.to_list()
    index_param = sm.add_constant(index)

    model = sm.OLS(xt, index_param)
    res = model.fit()

    mean_coeff = res.params[1]
    mean_intercept = res.params[0]

    delta_xt = xt.diff().dropna().reset_index()

    # disregard the last value of xt
    xt_mu = pd.Series(xt.index * mean_coeff + mean_intercept)
    xt = xt_mu - xt
    xt = xt[:-1]

    xt_param = sm.add_constant(xt)

    model = sm.OLS(delta_xt[0], xt_param)
    res = model.fit()
    theta = res.params[0]

    # estimate process variance
    resid = res.resid
    sigma = math.sqrt(np.var(resid))

    return mean_coeff, mean_intercept, theta, sigma
