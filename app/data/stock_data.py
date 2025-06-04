from openbb import obb
import pandas as pd
import ta     # Technical Analysis Library

def get_stock_price(ticker: str, start_date: str = "2020-01-01"):
    output = obb.equity.price.historical(
        symbol=ticker,
        start_date=start_date,
        provider="yfinance"
    )
    return output.to_dataframe()

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 计算 MA（移动平均线）
    df["MA_20"] = df["close"].rolling(window=20).mean()
    df["MA_50"] = df["close"].rolling(window=50).mean()

    # 计算 RSI（相对强弱指数）
    df["RSI"] = ta.momentum.RSIIndicator(close=df["close"]).rsi()

    # 计算 MACD
    macd = ta.trend.MACD(close=df["close"])
    df["MACD"] = macd.macd()
    df["MACD_signal"] = macd.macd_signal()

    return df