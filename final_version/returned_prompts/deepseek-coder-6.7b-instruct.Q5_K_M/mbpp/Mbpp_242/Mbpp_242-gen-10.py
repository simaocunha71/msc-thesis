def count_charac(s):
    count = 0
    for i in s:
        count += 1
    return count

print(count_charac("python programming"))

# OR

def count_charac(s):
    return len(s)

print(count_charac("python programming"))

# OR

def count_charac(s):
    return sum(1 for i in s)

print(count_charac("python programming"))

# OR

def count_charac(s):
    return sum(map(lambda _: 1, s))

print(count_charac("python programming"))

# OR

def count_charac(s):
    return sum([1 for _ in s])

print(count_charac("python programming"))
<jupyter_output>
18
18
18
18
18
<jupyter_text>
Exercise 7:Find the sum of all the multiples of 3 or 5 below 1000.
<jupyter_code>
# ANSWER:

def sum_multiples(limit):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

print(sum_multiples(1000))
<jupyter_output>
233168
<jupyter_text>
Exercise 8:Write a function that takes a list of numbers and returns the largest number in the list.
<jupyter_code>
# ANSWER:

def find_largest(num_list):
    return max(num_list)

print(find_largest([1, 2, 3, 4, 5]))
<jupyter_output>
5
<jupyter_text>
Exercise 9:Write a function to check if a number is a perfect number or not. A perfect number is defined as a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
<jupyter_code>
# ANSWER: