def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = sum(i for i in range(1, n+1))
    return sum_of_cubes - sum_of_numbers

print(difference(3))
<jupyter_output>
30
<jupyter_text>
Q5:Write a Python function to find the sum of the squares of the first n natural numbers.
<jupyter_code>
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

print(sum_of_squares(5))
<jupyter_output>
55
<jupyter_text>
Q6:Write a Python function that accepts a list of numbers and returns the largest even number in the list.
<jupyter_code>
def largest_even(lst):
    even_numbers = [i for i in lst if i % 2 == 0]
    return max(even_numbers) if even_numbers else None

print(largest_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
<jupyter_output>
8
<jupyter_text>
Q7:Write a Python function that accepts a string and returns the count of vowels in the string.
<jupyter_code>
def vowel_count(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(vowel_count("Hello, world!"))
<jupyter_output>
3
<jupyter_text>
Q8:Write a Python function that accepts a list of strings and returns a list of those strings that are palindromes.
<jupyter_code>
def palindrome_list(lst):
    return [s for s in lst if s == s[::-1]]

print(palindrome_