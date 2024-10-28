def wind_chill(wind_velocity, temp):
    wc = 35.74 + 0.6215*temp - 35.75*((10**0.16 + 0.4275*temp)**0.16) + 0.4275*temp*(10**0.16)
    if wc<0:
        wc = 0
    else:
        wc = int(wc + 0.5)
    return wc