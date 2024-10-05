
    def will_it_fly(q,w):
        if q == q[::-1] and sum(q) <= w:
            return True
        else:
            return False


# Test cases
print(will_it_fly([1, 2], 5)) # ➞ False
print(will_it_fly([3, 2, 3], 1)) # ➞ False
print(will_it_fly([3, 2, 3], 9)) # ➞ True
print(will_it_fly([3], 5)) # ➞ True

The function works by first checking if the list is a palindrome (i.e., the list reads the same forwards and backwards) and then checking if the sum of its elements is less than or equal to the maximum weight. If both conditions are met, the function returns True. Otherwise, it returns False.

This solution uses the Python built-in function sum() to calculate the sum of the elements in the list and the list slicing syntax [::-1] to reverse the list and check if it is a palindrome.

The time complexity of this solution is O(n) because it traverses the list twice (once to check if it is a palindrome and once to calculate the sum). The space complexity is O(1) because it uses a fixed amount of space to store the sum and the reversed list.

'''

'''

def will_it_fly(q,w):
    return q == q[::-1] and sum(q) <= w

print(will_it_fly([1, 2], 5)) # ➞ False
print(will_it_fly([3, 2, 3], 1)) # ➞ False
print(will_it_fly([3, 2, 3], 9)) # ➞ True
print(will_it_fly([3], 5)) # ➞ True
'''

# One liner solution
def will_it_fly(q,w):
    return q == q[::-1] and sum(q) <= w

print(will_it_fly([1,