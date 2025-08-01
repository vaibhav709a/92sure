# streamlit_app.py

import streamlit as st
import datetime
from data_feed import get_live_candles
from smc_analyzer import detect_smc_signal

st.set_page_config(page_title="Quotex SMC Signal Bot", layout="centered")
st.title("📈 Quotex SMC/ICT Signal Bot")

st.markdown("""
This bot uses **Smart Money Concepts (SMC)** and **ICT principles** to detect
high-probability BUY/SELL signals on 1-minute Quotex data using **TwelveData API**.
""")

# 🔁 Get live data
symbol = st.selectbox("Select Pair", ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD"], index=0)
candles = get_live_candles(symbol=symbol)

# 🔍 Display recent candles
st.subheader("📊 Last 5 Candles")
for c in candles[-5:]:
    st.write(f"🕒 {c['time']} | O: {c['open']} H: {c['high']} L: {c['low']} C: {c['close']}")

# ⚙️ Signal detection
signal = detect_smc_signal(candles)

st.subheader("📍 Signal")
if signal:
    st.success(f"Signal Detected: {signal}")
else:
    st.warning("No signal at the moment.")

# 🔁 Optional auto-refresh every 10 seconds
import time
time.sleep(10)
st.experimental_rerun()
