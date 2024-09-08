def wind_chill(v,t):
    if t > 10:
        return int(13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16)
    else:
        return int(33 - 0.70 * v)