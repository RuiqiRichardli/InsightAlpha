from app.data.stock_data import get_stock_price,add_technical_indicators

df = get_stock_price("TSLA", "2015-01-01")
df = add_technical_indicators(df)

print(df.tail())


from app.visualizations.plotly_charts import plot_price_with_ma, plot_rsi, plot_macd
plot_price_with_ma(df)
plot_rsi(df)
plot_macd(df)






from app.data.macro_data import get_macro_data

def main():
    # 第四章 · 宏观经济数据示例
    df_rate = get_macro_data("DGS10")       # 10年期国债收益率
    df_unemp = get_macro_data("UNRATE")     # 失业率
    df_cpi = get_macro_data("CPIAUCSL")     # CPI
    df_vix = get_macro_data("VIXCLS")       # VIX 波动率指数

    # 合并展示
    df_macro = df_rate.join([df_unemp, df_cpi, df_vix], how="outer")
    print("📈 宏观经济数据：")
    print(df_macro.tail())

if __name__ == "__main__":
    main()