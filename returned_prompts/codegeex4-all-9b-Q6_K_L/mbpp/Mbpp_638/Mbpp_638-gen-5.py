def wind_chill(wind_vel:float, temp:float) -> int:
    wind_chill_index = 13.12 + 0.6215 * temp - 11.37 * (wind_vel ** 0.16) + 0.3965 * temp * (wind_vel ** 0.16)
    return round(wind_chill_index)