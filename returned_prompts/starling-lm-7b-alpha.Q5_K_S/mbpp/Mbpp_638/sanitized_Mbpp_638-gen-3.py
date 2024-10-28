def wind_chill(W, T):
    return round(-10.3 + 0.6 * (T + 10) - 0.4 * (W ** 0.16 + 5) * (T - 10) ** 0.2 + 3.5 * W ** 0.25)