def wind_chill(wind_kmph, temp_c):
    wind_chill_index = 13.12 + 0.63 * temp_c - 11.37 * wind_kmph**0.16 + 0.39 * temp_c * wind_kmph**0.16
    return round(wind_chill_index)