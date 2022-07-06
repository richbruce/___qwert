from pathlib import Path

syms = ["AMD", "QCOM", "ATVI", "DOCU", "MAR", "NTES", "MRNA", "CTSH", "INCY", "CDNS"]

strat_params = {
    # # ## mute for first run
    "risk_unit_mltp": 1.0,  # for tradelog
    "reward_ratio": 3.0,  # for tradelog
    # "weak_risk_unit_mltp": 2.0,
    # "weak_reward_ratio": 0.5,
    # # ## mute for first run
    #
    #
    #
    "data_dir": Path.home() / "__DATA/polygon/stocks/raw/min_1/2018_2021",
    # ## minute time frame
    "resample_int": 5,
    # ## 'forex', 'stock', etc...
    "asset_class": "stock",
    "min_risk_unit": 0.20,
    "min_rwrd_unit": 0.20,
    "price_decimal": 2,
    "side": "long",  # long, short
    "max_duration": "eod",  # end of day or till stop
    "risk_type": "aon",  # aon:all or nothing -- be:breakeven
    "date_range_start": "2020-01-01",
    "date_range_stop": "2021-01-01",
    "base_risk_source": "sig_bar_range",
    "entry_point": "sig_bar_close",
    "min_win_rate": 0.25,
    "min_price": 10.00,
    "max_price": 100.00,
    "indicators": ["macd"],  # for charting
}


__all__ = ["syms", "strat_params"]
