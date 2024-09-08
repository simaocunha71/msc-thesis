
def wind_chill(velocity, temp):
    # wind chill formula
    wct = 13.12 + 0.6215*temp - 11.37*(velocity**0.16) + 0.3965*temp*(velocity**0.16)
    return round(wct)

print(wind_chill(120,35))

# Output: 40

# It means the wind chill index is 40 when the wind velocity is 120 km/h and the temperature is 35°C.
<jupyter_output>
40
<jupyter_text>
