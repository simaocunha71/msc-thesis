def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                count += 1
    return count


print(find_even_pair([5, 4, 7, 2, 1]))  # 4


"""
Explanation:
The function find_even_pair takes a list of integers as input. It initializes a count variable to 0. 
It then iterates over all pairs of numbers in the list. For each pair, it calculates the xor of the two numbers. 
If the result is even, it increments the count. Finally, it returns the count.
"""
<jupyter_output>
4
<jupyter_text>
Question 2
<jupyter_code>
