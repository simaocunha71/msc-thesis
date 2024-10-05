
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0)

print(solution([5, 8, 7, 1])) #==> 12
print(solution([3, 3, 3, 3, 3])) #==> 9
print(solution([30, 13, 24, 321])) #==>0

# In this code, the function solution is defined to take a list lst as an argument. The sum function is used to add up all the odd numbers in the list that are in even positions. For every pair of index and value in the list, the if condition checks whether the index is even (i % 2 == 0) and the value is odd (x % 2 != 0). If both conditions are met, the value is added to the total sum.
<jupyter_output>
12
9
0
<jupyter_text>
2. Write a Python function that takes a string and returns a dictionary with the frequency count of each word in the string.
<jupyter_code>
