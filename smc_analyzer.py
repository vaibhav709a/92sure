# smc_analyzer.py

def detect_smc_signal(candles):
    """
    Detect potential SMC/ICT trade signal.
    candles: List of dicts with keys 'open', 'high', 'low', 'close'
    """

    if len(candles) < 5:
        return None

    c1 = candles[-5]
    c2 = candles[-4]
    c3 = candles[-3]
    c4 = candles[-2]
    c5 = candles[-1]

    # --- Example: Bullish structure
    if (c3['low'] < c2['low'] < c1['low']) and \
       (c3['high'] > c2['high'] > c1['high']) and \
       (c5['close'] > c4['high'] and c5['close'] > c5['open']):
        return "BUY"

    # --- Example: Bearish structure
    if (c3['high'] > c2['high'] > c1['high']) and \
       (c3['low'] < c2['low'] < c1['low']) and \
       (c5['close'] < c4['low'] and c5['close'] < c5['open']):
        return "SELL"

    return None
