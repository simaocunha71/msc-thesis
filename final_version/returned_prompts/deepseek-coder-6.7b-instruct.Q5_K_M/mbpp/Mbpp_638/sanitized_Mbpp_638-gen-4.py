def wind_chill(velocity, temperature):
    # Formula to calculate wind chill index
    wct = 13.12 + 0.6215 * temperature - 11.37 * velocity**0.16 + 0.3965 * temperature * velocity**0.16
    return round(wct + 0.5)  # Round to next integer