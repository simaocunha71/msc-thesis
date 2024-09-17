
def wind_chill(v: float, t: float) -> int:
    """
    Calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.

    Parameters:
    v (float): Wind velocity in km/h
    t (float): Temperature in Celsius

    Returns:
    int: Wind chill index
    """

    # Wind chill formula
    w = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)

    # Round to nearest integer
    return round(w)


