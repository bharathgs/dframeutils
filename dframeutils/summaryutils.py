import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats.mstats import mode
import warnings
warnings.simplefilter("ignore", RuntimeWarning)


__all__ = ["na_count",
           "na_plot", "extreme_observations",
           "df_numerical_summary"]


# pdf per col
# cdf per col
# kde per col

def extreme_observations(df, feature, n=3, n_largest=True, n_smallest=True):
    """
    Returns the n-largest or/and n-smallest observations in a dataframe
    based on a particular feature passed along.

    Parameters:
    ___________

    df:
        DataFrame

    feature:
        the feature (str)

    n:
        number of smallest/largest (int)

    n_largest:
        if set to false, returns only n-smallest rows based on feature (bool), default: true

    n_smallest:
        if set to false, returns only n-largest rows based on feature (bool), default: true

    returns:
    ________

        DataFrame

    """

    li = [i for i in df[feature].nlargest(n).reset_index()["index"]]
    si = [i for i in df[feature].nsmallest(n).reset_index()["index"]]

    if n_largest is False:
        return df.iloc[si, :]

    if n_smallest is False:
        return df.iloc[li, :]

    return pd.concat([df.iloc[si, :], df.iloc[li, :]])


def na_count(df):
    """
    Returns the information about the percentage of missing values in a dataframe

    Parameters:
    ___________

    df:
        DataFrame

    returns:
    ________

        DataFrame

    """
    counts = df.isnull().sum()
    percentage = counts / len(df)

    NaDf = DataFrame({"miss": counts, "miss_percent": percentage})
    NaDf['miss_percent'] = NaDf['miss_percent'].map('{:,.2%}'.format)

    return NaDf


def df_numerical_summary(df):
    """
    automatically selects all the numeric columns in a dataframe and provides their summary statistics

    Parameters: 
    ___________

        df: 
            Dataframe

    Returns:
    ________

        Dataframe

    """
    ndf = df.select_dtypes(include=[np.number])
    dft = ndf.describe().T
    nunique = [n for n in ndf.apply(pd.Series.nunique)]
    nzeros = [((ndf[col] == 0).sum()) for col in ndf]
    kurt = [x for x in ndf.kurtosis()]
    skewness = [x for x in ndf.skew()]
    modes = [x for x in ndf.apply(lambda x: mode(x, axis=None)[0]).iloc[0]]
    ranges = DataFrame({"1%": ndf.quantile(0.01), "5%": ndf.quantile(
        0.05), "95%": ndf.quantile(0.95), "99%": ndf.quantile(0.99)})
    infodf = dft.assign(nunique=nunique, mode=modes, median=ndf.apply(
        np.median), nzeros=nzeros, kurtosis=kurt, skewness=skewness,
        iqr=dft['75%'] - dft['25%']).join(na_count(ndf)).join(ranges)

    def Round(x): return np.round(x, 2)

    rnd = ['count', 'mean', 'mode', 'median', 'std', 'min',
           'max', 'nunique', 'nzeros', 'miss', 'kurtosis', 'skewness',
           '25%', '50%', '75%', '1%', '95%', '99%', '5%', 'iqr']

    infodf[rnd] = infodf[rnd].apply(Round)

    infodf = infodf[['count', 'mean', 'mode', 'median', 'std', 'min', 'max',
                     'nunique', 'nzeros', 'kurtosis', 'skewness', 'miss',
                     'miss_percent', 'iqr', '1%', '5%', '25%', '50%', '75%', '95%',
                     '99%']]
    return infodf


def na_plot(df, font_scale=3, figsize=(24, 16)):
    """
    Plots a bargraph of the NaNs in a given dataset

    Parameters:
    ___________

    df: 
        dataframe

    font_scale:
        the scale of the plot's font(int)

    figsize:
        tuple, to control the figure size

    Returns:
    _______

        plot

    """
    sns.set(font_scale=font_scale)
    NaDf = (df.isnull().sum() / len(df)) * 100
    NaDf = NaDf.drop(NaDf[NaDf == 0].index).sort_values(ascending=False)

    sns.set_style("whitegrid")
    f, ax = plt.subplots(figsize=figsize)
    plt.xticks(rotation='90')
    sns.barplot(x=NaDf.index, y=NaDf)
    ax.set(title='Percentage NaN by Feature', ylabel='Percentage of Missing')
    plt.subplots_adjust(top=0.95, bottom=0.3)
    plt.show()


def df_categorical_summary():
    pass


def correlation_matrix():
    pass


def cdf_plot():
    pass


def histogram():
    pass


def pairwise_density_plot():
    pass


def cross_tab():
    pass


def distribution_plot():
    pass


def pair_info():
    #correlation, pair_detail
    pass
