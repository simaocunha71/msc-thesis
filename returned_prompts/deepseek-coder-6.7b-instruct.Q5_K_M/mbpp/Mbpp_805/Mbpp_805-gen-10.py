def max_sum_list(l):
    max_sum = 0
    max_list = []
    for sublist in l:
        if sum(sublist) > max_sum:
            max_sum = sum(sublist)
            max_list = sublist
    return max_list

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))

"""
The function works by initializing the maximum sum and the list with the maximum sum to be an empty list. 
It then iterates through each sublist in the input list. 
If the sum of the sublist is greater than the current maximum sum, the maximum sum is updated and the list with the maximum sum is updated to be the sublist.
Finally, the function returns the list with the maximum sum.
"""
<jupyter_output>
[10, 11, 12]
<jupyter_text>
Q5: Write a Python program that takes a list of numbers and returns a list with the running sum of the numbers in the input list. For example, if the input list is [1,2,3,4,5], the output list should be [1,3,6,10,15].
<jupyter_code>
def running_sum(l):
    sum = 0
    running_sum_list = []
    for num in l:
        sum += num
        running_sum_list.append(sum)
    return running_sum_list

print(running_sum([1,2,3,4,5]))
<jupyter_output>
[1, 3, 6, 10, 15]
<jupyter_text>
Q6: Given a string, write a Python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is