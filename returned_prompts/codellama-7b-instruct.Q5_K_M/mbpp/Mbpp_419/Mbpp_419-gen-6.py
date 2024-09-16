
def round_and_sum(numbers):
    rounded_numbers = [round(number) for number in numbers]
    total_sum = sum(rounded_numbers)
    return total_sum * len(rounded_numbers)

# Explanation
# You need to round every number in the given list using the round() function and then find the total sum of the rounded numbers and multiply it by the length of the list.
# Finally you have to return the total_sum * length of the list.
