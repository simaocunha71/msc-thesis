
    for i in l:
        if i >= t:
            return False
    return True

print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))

# Output:
# True
# False

Explanation:

The function below_threshold checks if all numbers in the list l are below the threshold t. If it finds a number in l that is greater than or equal to t, it returns False. If it doesn't find any such number in l, it returns True after the loop finishes.
"""

# ----------------------------------
# 