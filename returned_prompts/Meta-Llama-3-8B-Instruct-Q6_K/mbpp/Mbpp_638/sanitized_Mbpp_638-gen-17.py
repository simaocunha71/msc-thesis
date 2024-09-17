def wind_chill(wind_velocity, temperature):
    if wind_velocity < 0 or temperature < -40:
        return None
    w = 0.216
    t = 0.5
    v = wind_velocity * 1.852
    wci = 13.12 + 0.6215 * temperature - 11.37 * v + 0.3965 * temperature * v
    wci -= w * v ** t
    return round(wci)