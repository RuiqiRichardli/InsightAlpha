
from openbb import obb
import pandas as pd
import numpy as np 

# 获取指定股票的财务数据
def get_financial_metrics(ticker: str = "TSLA", provider: str = "yfinance", period: str = "annual", limit: int = 1) -> pd.DataFrame:
    """
    使用 OpenBB 获取公司估值和财务指标数据（默认为 yfinance 提供商）
    """
    result = obb.equity.fundamental.metrics(
        symbol=ticker,
        provider=provider,
        period=period,
        limit=limit
    )
    df = result.to_dataframe()
    return df

#计算 Value Score（越高表示估值越便宜、盈利能力越好）
def calculate_value_score(df: pd.DataFrame, normalize: bool = False) -> pd.DataFrame:
    """
    计算 Value Score，用于评估公司估值吸引力
    - normalize=False：适合单家公司分析（不标准化）
    - normalize=True：适合多家公司横向比较（0~100标准化）
    """

    selected_columns = [
        "pe_ratio",             # 越低越好
        "price_to_book",        # 越低越好
        "return_on_equity",     # 越高越好
        "enterprise_value",     # 越低越好（适合 log 处理）
        "market_cap"            # 越高越好（适合 log 处理）
    ]

    # 只保留可用字段
    available = [col for col in selected_columns if col in df.columns]
    df = df[available].copy()

    # ➤ 指标处理
    for col in available:
        if col in ["pe_ratio", "price_to_book"]:  # 直接反转
            df[col + "_score"] = 1 / (df[col] + 1e-6)

        elif col in ["enterprise_value"]:  # log 反转
            df[col + "_score"] = 1 / (np.log(df[col] + 1e-6))

        elif col in ["market_cap"]:  # log 保留
            df[col + "_score"] = np.log(df[col] + 1e-6)

        elif col in ["return_on_equity"]:  # 保留原值
            df[col + "_score"] = df[col]

    # ➤ 标准化处理（适用于多家公司）
    score_cols = [c for c in df.columns if c.endswith("_score")]
    if normalize and len(df) > 1:
        for col in score_cols:
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-6) * 100

    # ➤ 计算平均 Value Score
    df["value_score"] = df[score_cols].mean(axis=1).round(2)

    return df