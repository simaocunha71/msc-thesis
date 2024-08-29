
def wind_chill(velocity, temp):
    # Formula to calculate wind chill index
    wci = 13.12 + 0.6215*temp - 11.37*(velocity**0.16) + 0.3965*temp*(velocity**0.16)
    # Round the result to the next integer
    return round(wci + 0.5)

print(wind_chill(120,35))
<jupyter_output>
40
<jupyter_text>
2. Write a function to calculate the total resistance in a circuit given a list of resistances. The function should return the total resistance in ohms.
<jupyter_code>
