import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns


__all__ = ["DataTypeConverter", "NaCount",
           "NaPlot", "ExtremeObservations", "PrintAll"]


def DataTypeConverter(features, df, data_type):
    """
    converts multiple columns from one dtype to other in a pandas dataframe

    Parameters:
    ___________

    features : 
        a list or a str of features/feature who's dtype is to be converted.

    df: 
        DataFrame

    data_type : 
        the target data type passed on as string


    returns: 
    ________

        DataFrame 

    """

    if type(features) == str:
        df[features] = df[features].astype(data_type)

    else:
        df[features] = df[features].apply(lambda x: x.astype(data_type))

    return df


def ExtremeObservations(df, feature, n=3, n_largest=True, n_smallest=True):
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


def NaCount(df):
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

    NaDf = DataFrame({"Na_Count": counts, "Na_Percentage": percentage})
    NaDf['Na_Percentage'] = NaDf['Na_Percentage'].map('{:,.2%}'.format)

    return NaDf


def Information():
    # ad_ _ _ _ _wans functionality
    # charinfo
    # numinfo
    # frequency info
    pass


def SummaryInfo():
    pass


def RemoveSpecial():
    pass


def NaPlot(df, font_scale=3, figsize=(24, 16)):
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


def PrintAll(df, max_rows=999, max_colwidth=200):
    """prints the entire dataframe (up to max_rows) and returns to original context

    Parameters:
    ___________

    df:
        Dataframe
    max_rows:
        maximum number of rows to be printed (default: 999)(int)
    max_colwidth:
        maximum number of columns to be printed (default: 200)(int)

    Returns:
    _______

        Dataframe

    """
    with pd.option_context('display.max_rows', max_rows, 'display.max_colwidth', max_colwidth):
        print(df)
