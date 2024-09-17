import math
def wind_chill(v, T):
    # Check if the wind velocity and temperature are valid
    if v < 0 or T < -50:
        raise ValueError("Invalid input")

    # Calculate the wind chill index
    wind_chill = -10.3 * v + 0.6 * T + 3.5 * v * T

    # Round the wind chill index to the next integer
    return math.ceil(wind_chill)