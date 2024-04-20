"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
class Solution:
    def dog_years(self, year):
        if int(type(year)) == 3 and year is not None:
            return ((int(year)/365)+1)*((1-int(year)/365))
        else:
            return float("inf")