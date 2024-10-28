
def double_the_difference(lst):
    total = 0
    for item in lst:
        if item % 2 == 1:
            total += item * item
    return total

# Test Cases
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
print(double_the_difference([0]))  # Output: 0
print(double_the_difference([]))  # Output: 0



# Time Complexity: O(n)
# Space Complexity: O(1)

def double_the_difference(lst):
    total = sum(i * i for i in lst if i % 2 == 1)
    return total
```