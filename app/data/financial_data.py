# app/data/financial_data.py

from openbb import obb
import pandas as pd

def get_financial_metrics(ticker: str = "TSLA", provider: str = "yfinance", period: str = "annual", limit: int = 1) -> pd.DataFrame:
    """
    获取公司财务估值指标（使用OpenBB SDK）
    """
    result = obb.equity.fundamental.metrics(
        symbol=ticker,
        provider=provider,
        period=period,
        limit=limit
    )
    df = result.to_dataframe()
    return df

def calculate_value_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    对选定财务指标进行归一化处理，计算 Value Score（越高越好）
    """
    # 选取常用财务指标（已确认字段）
    selected_columns = [
        "pe_ratio",             # 越低越好
        "price_to_book",        # 越低越好
        "return_on_equity",     # 越高越好
        "enterprise_value",     # 越低越好
        "market_cap"            # 越高越好（辅助参考）
    ]

    # 只保留选定指标
    available = [col for col in selected_columns if col in df.columns]
    df = df[available].copy()

    # 反转分数方向（低 = 高分）以统一方向
    for col in ["pe_ratio", "price_to_book", "enterprise_value"]:
        if col in df.columns:
            df[col + "_score"] = 1 / (df[col] + 1e-6)  # 防止除以0

    # 对ROE和market_cap等“高越好”直接保留原值作为得分
    for col in ["return_on_equity", "market_cap"]:
        if col in df.columns:
            df[col + "_score"] = df[col]

    # 标准化所有 *_score 字段
    score_cols = [c for c in df.columns if c.endswith("_score")]
    for col in score_cols:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-6) * 100

    # 计算 Value Score 平均值
    df["value_score"] = df[score_cols].mean(axis=1).round(2)
    return df
