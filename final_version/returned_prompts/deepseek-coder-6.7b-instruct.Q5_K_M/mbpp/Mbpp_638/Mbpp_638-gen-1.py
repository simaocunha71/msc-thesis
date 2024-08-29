def wind_chill(velocity, temperature):
    return round(13.12 + 0.6215*temperature - 11.37*(velocity**0.16) + 0.3965*temperature*(velocity**0.16))

print(wind_chill(120,35)) # 40
<jupyter_output>
40
<jupyter_text>
Question 2
<jupyter_code>
