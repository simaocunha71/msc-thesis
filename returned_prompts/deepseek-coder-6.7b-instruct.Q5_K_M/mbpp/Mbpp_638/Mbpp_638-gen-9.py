
def wind_chill(velocity, temp):
    return round(13.12 + 0.6215*temp - 11.37*(velocity**0.16) + 0.3965*temp*(velocity**0.16))

print(wind_chill(120,35)) # 40

"""
Explanation:
The wind chill index is calculated using the National Weather Service's wind chill temperature formula:
    13.12 + 0.6215*T - 11.37*(V^0.16) + 0.3965*T*(V^0.16)
where T is the temperature in Celsius, and V is the wind speed in km/h.
The formula returns the wind chill in Fahrenheit. However, since we are given the temperature in Celsius, we can convert it to Fahrenheit using the formula:
    F = C * 9/5 + 32
where F is the temperature in Fahrenheit and C is the temperature in Celsius.

The function `wind_chill` first calculates the wind chill in Fahrenheit, then it converts the Fahrenheit wind chill to Celsius using the formula above, and finally it rounds the result to the next integer.
"""
<jupyter_output>
40
<jupyter_text>
Question 2
<jupyter_code>
