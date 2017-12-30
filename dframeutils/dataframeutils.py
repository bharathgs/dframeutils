import pandas as pd
import warnings
warnings.simplefilter("ignore", RuntimeWarning)


__all__ = ["dtype_converter", "print_all"]


def dtype_converter(features, df, data_type):
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


def remove_special():
    pass


def print_all(df, max_rows=999, max_colwidth=200):
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
