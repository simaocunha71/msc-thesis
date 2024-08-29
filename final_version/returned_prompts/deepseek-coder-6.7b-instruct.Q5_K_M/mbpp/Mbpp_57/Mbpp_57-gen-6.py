
def find_Max_Num(nums):
    return int("".join(sorted(map(str, nums), reverse=True)))

print(find_Max_Num([1,2,3]))

# Alternate Solution

def find_Max_Num(nums):
    nums.sort(reverse=True)
    return int("".join(map(str, nums)))

print(find_Max_Num([1,2,3]))

# Both the above solutions work, but the first one is faster because it does not require the use of the sorted function twice.
<jupyter_output>
321
321
<jupyter_text>
6) Given a number n, write a Python function to check if it is a power of two.
<jupyter_code>
