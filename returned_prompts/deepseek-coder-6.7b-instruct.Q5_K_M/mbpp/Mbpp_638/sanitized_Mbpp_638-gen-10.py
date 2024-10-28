def wind_chill(velocity, temp):
    # Formula to calculate wind chill index
    wci = 13.12 + 0.6215*temp - 11.37*(velocity**0.16) + 0.3965*temp*(velocity**0.16)
    # Round the result to the next integer
    return round(wci + 0.5)