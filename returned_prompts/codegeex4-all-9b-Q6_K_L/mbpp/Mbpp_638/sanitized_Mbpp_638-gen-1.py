def wind_chill(velocity, temperature):
    """
    Calculate wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
    :param velocity: wind velocity in km/h
    :param temperature: temperature in celsius
    :return: wind chill index rounded to the next integer
    """
    if velocity < 4.8 or temperature > 10:
        return round(temperature)
    else:
        return round(13.12 + 0.6215 * temperature - 11.37 * velocity ** 0.16 + 0.3965 * temperature * velocity ** 0.16)