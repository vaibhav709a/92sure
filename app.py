streamlit_app.py

import streamlit as st import datetime from quotex_signal_generator import get_sample_candles  # Use your real-time or sample data from smc_analyzer import detect_smc_signal

st.set_page_config(page_title="Quotex SMC Signal Bot", layout="centered") st.title("📈 Quotex SMC/ICT Signal Bot")

st.markdown(""" This bot uses Smart Money Concepts (SMC) and ICT principles to detect high-probability BUY/SELL signals on 1-minute Quotex data. """)

Live or sample candle data (replace with real WebSocket later)

candles = get_sample_candles()

st.subheader("📊 Last 5 Candles") for c in candles[-5:]: st.write(f"Time: {c['time']}, Open: {c['open']}, High: {c['high']}, Low: {c['low']}, Close: {c['close']}")

Signal detection

signal = detect_smc_signal(candles)

st.subheader("📍 Signal") if signal: st.success(f"Signal Detected: {signal}") else: st.warning("No signal at the moment.")

Footer

st.caption("Bot running on SMC/ICT strategy — 1m timeframe | Powered by Streamlit")

