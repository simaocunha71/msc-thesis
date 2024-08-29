
def pair_wise(lst):
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]


assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1),  (1, 2),  (2, 3),  (3, 3),  (3, 4),  (4, 4),  (4, 5)]
"""
Explanation:
The function `pair_wise` takes a list `lst` as argument. It uses a list comprehension to create a new list.
For each index `i` in the range of the length of the list minus 1, it adds a tuple to the new list.
The tuple contains the item at index `i` and the item at index `i+1` in `lst`.
Finally it returns the new list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Write a function that takes an integer as input and returns the largest prime number that is smaller than the input number.
<jupyter_code>
def largest_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i

    return None

# test case
print(largest_prime(30))  # Output: 29
<jupyter_output>
29
<jupyter_text>
Question 3Write a function that takes a string as input and returns the number of vowels in the string.
<jupyter_code>
def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
    return count

# test case
print(count_vowels('Hello World'))  # Output: