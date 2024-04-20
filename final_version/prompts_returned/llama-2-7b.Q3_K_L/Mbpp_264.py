"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
import math
def dog_age(dog_years):
	if 0 < dog_years <= 8:
		return float(math.ceil((float(3.5)/4)*(dog_years+1)))
	elif 9 < dog_years <= 15:
		return float(math.floor((float(5) / 4)*(dog_years+1)))
	else:
		return "N/A"
