from openbb import obb

def get_stock_price(ticker: str, start_date: str = "2020-01-01"):
    output = obb.equity.price.historical(
        symbol=ticker,
        start_date=start_date,
        provider="yfinance"
    )
    return output.to_dataframe()
