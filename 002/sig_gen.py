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

    # ## add indicators ##
    macd = ta.macd(df["close"])  # -> returns MACD df
    df = _add_indi([df, macd])

    # ## create condition columns ##
    df["range"] = df["high"] - df["low"]
    df["range_limit"] = df["high"] - (df["range"] * 0.40)

    # ## Create Boolean for conditions ##
    con_s = df.index.time >= dt.time(9, 30)
    con_e = df.index.time <= dt.time(12, 00)
    con_1 = df["open"] > df["range_limit"]
    con_2 = df["close"] > df["range_limit"]
    con_2a = df["close"] > df["open"]

    con_3 = df["MACDh_12_26_9"] > 0
    con_4 = df["MACD_12_26_9"] < 0
    con_5 = df["MACDs_12_26_9"] < 0
    con_6 = df["MACD_12_26_9"] > df["MACDs_12_26_9"]

    # ## create signals ##
    df.loc[
        con_s & con_e & con_1 & con_2 & con_3 & con_4 & con_5 & con_6 & con_2a, "signal"
    ] = True

    return df
