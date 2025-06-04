
# 📊 InsightAlpha 投资预测系统

一个结合 **价值投资理念**、**宏观经济因子分析**、**历史风险模拟** 的智能投资决策仪表盘。

---

## 🚀 项目功能

- 输入股票组合（支持美股/加股）
- 抓取历史股价、财务指标（OpenBB）
- 构建估值打分 + 回归模型预测收益率
- 模拟危机年份下的风险敞口
- 展示交互式图表（Streamlit）
- 一键导出 PDF 报告
- 可部署到 Streamlit Cloud

---

## 📦 技术栈

- Python, Pandas, NumPy, OpenBB
- Scikit-learn, XGBoost
- Streamlit, Plotly, pdfkit
- Git + GitHub + Streamlit Cloud

---

## ▶️ 如何运行

```bash
# 安装依赖（在虚拟环境中）
pip install -r requirements.txt

# 运行主程序
streamlit run main.py

