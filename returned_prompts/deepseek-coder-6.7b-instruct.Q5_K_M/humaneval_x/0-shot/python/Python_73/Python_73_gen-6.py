
def smallest_change(arr):
    if arr == arr[::-1]: return 0 # if the array is already a palindrome
    n = len(arr)
    changes = 0
    for i in range(n//2):
        if arr[i] != arr[n-i-1]: changes += 1
    return changes

print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0

"""
In this solution, we traverse the first half of the array and compare each element with the corresponding element from the end of the array. If they are different, we increase our counter for changes. The time complexity of this solution is O(n/2) which simplifies to O(n) as we only traverse half of the array.
"""

# End of Solution
<jupyter_output>
4
1
0
<jupyter_text>
Question 2:Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.An input string is valid if:1. Open brackets must be closed by the same type of brackets.2. Open brackets must be closed in the correct order.Example:1. Input: "()" Output: True2. Input: "()[]{}" Output: True3. Input: "(]" Output: False4. Input: "([)]" Output: False5. Input: "{[]}" Output: True
<jupyter_code>
# Solution 

def isValid(s: str) -> bool:
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
