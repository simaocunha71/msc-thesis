
def wind_chill(wind_vel: float, temp: float) -> float:
    wind_chill_index = 35.74 + 0.6215*wind_vel - 35.75*temp**0.16 + 0.4275*temp**0.16*wind_vel**0.1
    return int(wind_chill_index)


