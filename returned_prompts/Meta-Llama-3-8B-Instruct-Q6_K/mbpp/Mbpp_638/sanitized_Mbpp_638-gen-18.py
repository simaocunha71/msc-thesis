def wind_chill(wind_velocity, temperature):
    if wind_velocity < 5:
        return int(13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16))
    else:
        return int(13.12 + 0.6215*temperature - 35.75*(wind_velocity**0.16) + 0.4275*temperature*(wind_velocity**0.16))