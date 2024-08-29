def sum_in_range(l,r):
    return sum([i for i in range(l,r+1) if i%2 != 0])

print(sum_in_range(2,5)) # 8

# Approach:
# We use list comprehension to iterate over the numbers in the range from l to r (inclusive).
# For each number, we check if it is odd by checking if the remainder of the division of the number by 2 is not 0 (i.e., i%2 != 0).
# If it is odd, we include it in the sum.
# Finally, we return the sum of all odd numbers in the range.


