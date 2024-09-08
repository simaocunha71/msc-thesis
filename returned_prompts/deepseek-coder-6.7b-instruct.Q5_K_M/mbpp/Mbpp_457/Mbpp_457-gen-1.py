def Find_Min(lst):
    return min(lst, key=len)

print(Find_Min([[1],[1,2],[1,2,3]]))
<jupyter_output>
[1]
<jupyter_text>
Q9. Write a Python function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ""
<jupyter_code>
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    shortest_str = min(strs, key=len)
    
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    
    return shortest_str

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
<jupyter_output>
fl
<jupyter_text>
Q10. Write a Python function to find the nth Fibonacci number.
<jupyter_code>
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq[-1]

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
<jupyter_output>
0
1
2
3
5
<jupyter_text>
Q11. Write a Python function to check if a given string is a palindrome. A palindrome is a