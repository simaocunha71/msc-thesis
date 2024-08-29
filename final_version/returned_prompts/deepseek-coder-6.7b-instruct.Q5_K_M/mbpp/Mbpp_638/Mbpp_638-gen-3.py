
def wind_chill(velocity, temp):
    return round(13.12 + 0.6215*temp - 11.37*(velocity**0.16) + 0.3965*temp*(velocity**0.16))

print(wind_chill(120,35))
<jupyter_output>
40
<jupyter_text>
Question 3
<jupyter_code>
