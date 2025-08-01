import streamlit as st
from data_feed import get_live_candles
from smc_analyzer import detect_smc_signal
import time

st.set_page_config(page_title="Quotex SMC Signal Bot", layout="wide")
st.title("🔁 Quotex Auto Signal Scanner (SMC/ICT)")

# ⏱ Auto-refresh every 15 seconds using query_params
refresh_time = str(time.time())
st.query_params.update(refresh=refresh_time)

# 📌 List of currency pairs to scan
currency_pairs = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD",
    "USD/CAD", "USD/CHF", "NZD/USD", "EUR/JPY"
]

interval = "1min"

col1, col2 = st.columns(2)
signal_found = False

for i, pair in enumerate(currency_pairs):
    try:
        candles = get_live_candles(symbol=pair, interval=interval)
        signal = detect_smc_signal(candles)

        chart_data = [c['close'] for c in candles]

        if signal:
            signal_found = True
            with (col1 if i % 2 == 0 else col2):
                st.success(f"📈 Signal for {pair}: **{signal}**")
                st.line_chart(chart_data)
        else:
            with (col1 if i % 2 == 0 else col2):
                st.info(f"No signal for {pair}")
    except Exception as e:
        st.error(f"Error fetching data for {pair}: {e}")

if not signal_found:
    st.warning("🚫 No valid signals at this moment")

# Wait 15 seconds, then rerun
time.sleep(15)
st.rerun()
