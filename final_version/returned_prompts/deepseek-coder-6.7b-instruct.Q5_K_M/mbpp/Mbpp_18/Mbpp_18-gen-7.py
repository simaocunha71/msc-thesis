def remove_dirty_chars(s1, s2):
    return ''.join([c for c in s1 if c not in s2])

print(remove_dirty_chars("probasscurve", "pros"))
<jupyter_output>
bacuve
<jupyter_text>
Q2. Write a function that returns the sum of all multiples of 3 and 5 that are less than 100.
<jupyter_code>
def sum_multiples(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

print(sum_multiples(100))
<jupyter_output>
2318
<jupyter_text>
Q3. Write a Python function to check whether a number is a perfect number or not.
<jupyter_code>
def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

print(is_perfect(6))  # True
print(is_perfect(28))  # True
print(is_perfect(5))  # False
<jupyter_output>
True
True
False
<jupyter_text>
Q4. Write a function that returns the number of vowels in a string.
<jupyter_code>
def count_vowels(s):
    return sum([1 for c in s if c in 'aeiouAEIOU'])

print(count_vowels('Hello World'))
<jupyter_output>
3
<jupyter_text>
Q5. Write a function that returns the number of words in a string.
<jupyter_code>
def count_words(s):
    return len(s.split())

print(count_words('Hello World'))
<jupyter_output>
2
<jupyter_text>
Q6. Write a function that returns the longest word in a string.
<jupyter_code>
def longest_word(s):