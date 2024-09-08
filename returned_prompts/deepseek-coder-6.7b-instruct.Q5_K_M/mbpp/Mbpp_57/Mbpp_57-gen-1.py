
def find_Max_Num(nums):
    nums.sort(reverse=True)
    return int(''.join(map(str, nums)))

print(find_Max_Num([1,2,3])) # It should return 321

"""
Explanation:
The given function sorts the given list in decreasing order and joins all the elements to form a number. The 'map' function is used to convert all the elements to string before joining them. The 'int' function is used to convert the final string to integer.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
