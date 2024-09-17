
def wind_chill(wind_velocity, temperature):
    w = 0.0000000125 * wind_velocity ** 0.16 + 0.00000033 * temperature + 0.0237
    wind_chill = -273.15 + 0.6515 * temperature + 1.0908 * w + 1.1312 * temperature * w
    return int(round(wind_chill))


