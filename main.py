from app.data.stock_data import get_stock_price

df = get_stock_price("TSLA", "2020-01-01")
print(df.head())
