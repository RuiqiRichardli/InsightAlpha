from app.data.stock_data import get_stock_price,add_technical_indicators

df = get_stock_price("TSLA", "2015-01-01")
df = add_technical_indicators(df)

print(df.tail())


from app.visualizations.plotly_charts import plot_price_with_ma, plot_rsi, plot_macd
plot_price_with_ma(df)
plot_rsi(df)
plot_macd(df)




# main.py

from app.data.financial_data import get_financial_metrics, calculate_value_score

def main():
    ticker = "TSLA"
    df = get_financial_metrics(ticker)
    print("原始财务数据：")
    print(df.head())

    scored_df = calculate_value_score(df)
    print("\n📊 Value Score 结果：")
    print(scored_df[["value_score"]])

if __name__ == "__main__":
    main()
