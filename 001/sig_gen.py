##

import datetime as dt
import pandas_ta as ta
import pandas as pd


def _add_indi(df_list: list) -> pd.DataFrame:
    df = pd.concat(df_list, axis=1)
    return df


# ## PASTE sig_gen BELOW ############################################################################

def sig_gen(df: pd.DataFrame) -> pd.DataFrame:

    # ## create default FALSE signal colum ##
    df["signal"] = False

    # ## Create Boolean for conditions ##
    con_1 = df.index.time == dt.time(9, 30)
    con_2 = df["close"] > df["open"]

    # ## create signals ##
    df.loc[con_1 & con_2, "signal"] = True

    return df
