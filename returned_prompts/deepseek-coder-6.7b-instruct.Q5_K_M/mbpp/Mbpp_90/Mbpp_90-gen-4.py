def len_log(words):
    return max(len(word) for word in words)

assert len_log(["python","PHP","bigdata"]) == 7

# 2nd method
def len_log(words):
    return max(words, key=len)

assert len_log(["python","PHP","bigdata"]) == "bigdata"

# 3rd method
def len_log(words):
    longest_word = max(words)
    return len(longest_word)

assert len_log(["python","PHP","bigdata"]) == 7

# 4th method
def len_log(words):
    return len(max(words, key=len))

assert len_log(["python","PHP","bigdata"]) == 7
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a python function to find the square of each number in a list.
assert square_nums([2,3,4,5]) == [4,9,16,25]
"""

def square_nums(nums):
    return [num**2 for num in nums]

assert square_nums([2,3,4,5]) == [4,9,16,25]
<jupyter_output>
<empty_output>
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a python function to find the largest and smallest number in a list.
assert find_max_min([2,3,4,5]) == (5,2)
"""

def find_max_min(nums):
    return max(nums), min(nums)

assert find_max_min([2,3,4,5]) == (5,2)
<jupyter_output>
<empty_output>
<jupyter_text>
Q4:
<jupyter_code>
"""
Write a python function to find the sum of all the elements in a list.
assert sum_list([2,