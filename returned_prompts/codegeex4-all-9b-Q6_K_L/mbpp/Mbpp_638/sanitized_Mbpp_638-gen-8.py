def wind_chill(v, t):
    if v > 4 and t < 10:
        return round(13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16)
    else:
        return t