
def common_in_nested_lists(nested_list):
    # Find the common elements in the first list
    common = set(nested_list[0])
    # Iterate over the rest of the lists
    for lst in nested_list[1:]:
        # Update the set of common elements
        common = common & set(lst)
    # Return the set of common elements
    return list(common)


print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))

# Output: {18, 12}

# Answer:
{18, 12}
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Given a string, count the number of words in it.For example, for the string "Hello World", the output should be 2.
<jupyter_code>
# Answer:
def count_words(s):
    return len(s.split())

print(count_words("Hello World"))

# Output: 2
<jupyter_output>
2
<jupyter_text>
Question 3:Given a list of integers, write a function to return the sum of all the prime numbers in the list.
<jupyter_code>
# Answer:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    return sum(n for n in numbers if is_prime(n))

print(sum_of_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Output: 1