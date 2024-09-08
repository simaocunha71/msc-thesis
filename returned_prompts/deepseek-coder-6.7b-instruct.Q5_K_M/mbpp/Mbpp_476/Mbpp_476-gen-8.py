def big_sum(arr):
    return max(arr) + min(arr)

print(big_sum([1,2,3])) # 4

# or

def big_sum(arr):
    return sorted(arr)[0] + sorted(arr)[-1]

print(big_sum([1,2,3])) # 4

# or

def big_sum(arr):
    max_value = arr[0]
    min_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value + min_value

print(big_sum([1,2,3])) # 4
<jupyter_output>
4
4
4
<jupyter_text>
Q2. Write a function that accepts an array of integers, and returns the length of the array.
<jupyter_code>
def array_length(arr):
    return len(arr)

print(array_length([1, 2, 3, 4, 5])) # 5
<jupyter_output>
5
<jupyter_text>
Q3. Write a function that accepts a string and returns the number of vowels in the string.
<jupyter_code>
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

print(count_vowels("Hello, World!")) # 3
<jupyter_output>
3
<jupyter_text>
Q4. Write a function that accepts a string and returns the string reversed.
<jupyter_code>
def reverse_string(string):
    return string[::-1]

print(reverse_string("Hello, World!")) # "olleH, !dlroW"
<jupyter_output>
olleH, !dlroW
<jupyter_text>
Q5. Write a function that accepts a list