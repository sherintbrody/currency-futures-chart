import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

st.title("💱 Currency Futures Watcher")

# Dropdown matching your watchlist
symbol_map = {
    "Japanese Yen (6J1!)": "6J=F",
    "Swiss Franc (6S1!)": "6S=F",
    "US Dollar Index (DX1!)": "DX=F",
    "Gold Futures (GC1!)": "GC=F",
}
selected_label = st.selectbox("Select Symbol", list(symbol_map.keys()))
ticker = symbol_map[selected_label]

# Timeframe selection
interval = st.radio("Timeframe", ["Daily", "Weekly"], horizontal=True)
params = (
    {"period": "1y", "int": "1d"}
    if interval == "Daily"
    else {"period": "3y", "int": "1wk"}
)

# Fetch and Plot
df = yf.Ticker(ticker).history(period=params["period"], interval=params["int"])

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
        )
    ]
)
fig.update_layout(xaxis_rangeslider_visible=False, height=500)
st.plotly_chart(fig, use_container_width=True)
