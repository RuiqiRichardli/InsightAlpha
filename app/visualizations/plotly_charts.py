
import plotly.graph_objs as go
import plotly.express as px

def plot_price_with_ma(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['close'], name='Close Price'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA_20'], name='MA 20'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA_50'], name='MA 50'))

    fig.update_layout(
        title='TSLA Price with MA20 & MA50',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        template='plotly_dark',
        hovermode='x unified'
    )
    fig.show()


def plot_rsi(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], name='RSI'))
    fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought")
    fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold")

    fig.update_layout(
        title='Relative Strength Index (RSI)',
        xaxis_title='Date',
        yaxis_title='RSI',
        template='plotly_dark',
        hovermode='x unified'
    )
    fig.show()


def plot_macd(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], name='MACD'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD_signal'], name='Signal Line'))

    fig.update_layout(
        title='MACD & Signal Line',
        xaxis_title='Date',
        yaxis_title='MACD',
        template='plotly_dark',
        hovermode='x unified'
    )
    fig.show()
