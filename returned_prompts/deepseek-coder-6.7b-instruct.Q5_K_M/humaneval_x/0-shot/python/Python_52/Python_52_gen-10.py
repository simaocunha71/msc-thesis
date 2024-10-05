
    for num in l:
        if num >= t:
            return False
    return True

# Test Cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False

# Additional Test Cases
print(below_threshold([1, 2, 4, 10], 11))  # True
print(below_threshold([1, 20, 4, 10], 21))  # False
print(below_threshold([], 10))  # True
print(below_threshold([10], 10))  # False
print(below_threshold([10, 20], 15))  # False
print(below_threshold([15, 20], 15))  # False
print(below_threshold([15, 20], 25))  # True
<jupyter_output>
True
False
True
False
True
False
False
True
True
True
<jupyter_text>
Problem 2Given a list of integers, return a new list with the sum of each pair of adjacent numbers.For example, given the list [1, 2, 3, 4, 5], the function should return [3, 5, 7, 9] because 1+2=3, 2+3=5, 3+4=7, and 4+5=9. 