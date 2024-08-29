def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3)) # 2

Explanation:
The function count_Pairs takes a list lst and its length n as input. It initializes count to 0, which will store the number of pairs. 
It then uses two nested loops to traverse all pairs of elements in lst. The outer loop runs from 0 to n-1, and the inner loop starts from i+1 to n. 
For each pair, it checks if the elements are unequal. If they are, it increments count. 
Finally, it returns count.

The assert statement checks if the output of the function count_Pairs([1,2,1],3) is equal to 2. If it is, the program does nothing. If not, an AssertionError is raised.
"""

def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3)) # 2
"""
This program will output 2, which is the number of pairs of unequal elements in the list [1,2,1], where each element is pair with each other.
"""
<jupyter_output>
2
<jupyter_text>
