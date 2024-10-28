
def add(lst):
    return sum(lst[i] for i in range(1, len(lst), 2))


# test cases to validate the solution

print(add([4, 2, 6, 7])) # 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 22
print(add([-4, 2, 6, 7, 9, 10])) # -1
print(add([1])) # 0
print(add([4, 5, 6])) # 6
<jupyter_output>
2
22
-1
0
6
<jupyter_text>
Problem 2Write a function called "count_vowels" that takes a string as its parameter and returns the number of vowels in the string. The function should be case-insensitive.
<jupyter_code>
