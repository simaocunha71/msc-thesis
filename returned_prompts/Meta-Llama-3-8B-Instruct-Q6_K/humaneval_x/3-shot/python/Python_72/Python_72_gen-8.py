    def will_it_fly(q, w):
        if q == q[::-1]:
            return sum(q) <= w
        return False

# Test cases
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
print(will_it_fly([1, 2, 3, 4], 10))  # True
print(will_it_fly([1, 2, 3, 4], 5))  # False

# Example explanation
# The list [3, 2, 3] is a palindrome, because it's the same when reversed.
# The sum of the elements is 8, which is less than or equal to the maximum possible weight 9, so the function returns True.