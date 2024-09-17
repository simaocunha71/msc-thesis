def wind_chill(wind_velocity, temperature):
    if wind_velocity < 40 or temperature < -12.5:
        return round(temperature)
    else:
        return round(13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16))