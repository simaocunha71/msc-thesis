def max_product_tuple(lst):
    max_product = 0
    for tup in lst:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))  # Output: 36

"""
Explanation:
The function iterates over each tuple in the list. It calculates the absolute product of the numbers in the tuple and compares it with the current maximum product. If the product is larger, it updates the maximum product. Finally, it returns the maximum product.
"""
<jupyter_output>
36
<jupyter_text>
Q2:Write a Python program that counts the number of occurrences of each character in a string.
<jupyter_code>
# Answer:

def char_count(str):
    count_dict = {}
    for char in str:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

print(char_count("google.com"))
<jupyter_output>
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
<jupyter_text>
Q3:Write a Python program that reverses a string.
<jupyter_code>
# Answer:

def reverse_string(str):
    return str[::-1]

print(reverse_string("Hello, World!"))
<jupyter_output>
<empty_output>
<jupyter_text>
Q4:Write a Python program that checks whether a given key already exists in a dictionary.
<jupyter_code>
# Answer:

def check_key(dict, key):
    if key in dict:
        return True
    else:
        return