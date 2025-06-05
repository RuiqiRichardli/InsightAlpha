from openbb import obb
import pandas as pd

def get_macro_data(series_id: str, start_date: str = "2010-01-01", provider: str = "fred") -> pd.DataFrame:
    """
    使用 OpenBB SDK 获取宏观经济数据
    支持 series_id 示例: 'DGS10', 'UNRATE', 'CPIAUCSL', 'VIXCLS'
    """
    try:
        result = obb.economy.macro(
            series_id=series_id,
            provider=provider
        )
        df = result.to_dataframe()
        df.index = pd.to_datetime(df.index)
        df = df[df.index >= start_date]
        df.columns = [series_id]
        return df
    except Exception as e:
        print(f"❌ 抓取 {series_id} 数据失败: {e}")
        return pd.DataFrame()