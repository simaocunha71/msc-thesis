
def wind_chill(velocity, temperature):
    # Formula to calculate wind chill index
    wct = 13.12 + 0.6215 * temperature - 11.37 * velocity**0.16 + 0.3965 * temperature * velocity**0.16
    return round(wct + 0.5)  # Round to next integer

print(wind_chill(120,35))  # Test case
assert wind_chill(120,35)==40
"""

def wind_chill(velocity, temperature):
    # Formula to calculate wind chill index
    wct = 13.12 + 0.6215 * temperature - 11.37 * velocity**0.16 + 0.3965 * temperature * velocity**0.16
    return round(wct + 0.5)  # Round to next integer

print(wind_chill(120,35))  # Test case
assert wind_chill(120,35)==40
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
