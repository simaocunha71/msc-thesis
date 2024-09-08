def find_sum(lst):
    non_repeated = set()
    for num in lst:
        if lst.count(num) == 1:
            non_repeated.add(num)
    return sum(non_repeated)

print(find_sum([1,2,3,1,1,4,5,6]))

# Alternative solution using list comprehension
def find_sum(lst):
    return sum([num for num in set(lst) if lst.count(num) == 1])

print(find_sum([1,2,3,1,1,4,5,6]))

"""
Explanation:

1. We first define a function called find_sum that takes a list of integers as an argument.

2. Inside the function, we create an empty set called non_repeated.

3. We then loop through each number in the list. If a number appears only once in the list (i.e., it is not repeated), we add it to the non_repeated set.

4. Finally, we return the sum of all the numbers in the non_repeated set.

5. The function is then tested with the list [1,2,3,1,1,4,5,6].

6. The sum of the non-repeated numbers in this list is 1+2+3+4+5+6 = 21.

7. The function returns this sum.

8. The alternative solution uses list comprehension to achieve the same result.
"""
<jupyter_output>
21
21
<jupyter_text>
Q2.
<jupyter_code>
