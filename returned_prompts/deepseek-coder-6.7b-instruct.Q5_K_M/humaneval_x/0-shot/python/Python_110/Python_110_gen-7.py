
def exchange(lst1, lst2):
    odd_lst1 = sum(x % 2 != 0 for x in lst1)
    even_lst2 = sum(x % 2 == 0 for x in lst2)
    return "YES" if odd_lst1 <= even_lst2 else "NO"

print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # "NO"

This Python solution works by first counting the number of odd numbers in lst1 and even numbers in lst2. Then it checks if the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2. If so, it returns "YES", otherwise "NO".

It's important to note that this solution assumes that lst1 and lst2 are non-empty lists of integers. If the input is not guaranteed to be in this format, additional error checking would be necessary.

The time complexity of this solution is O(n), where n is the length of the longer list. This is because it iterates over each element in both lists once. The space complexity is O(1), since it only uses a constant amount of additional space to store the counts of odd numbers in lst1 and even numbers in lst2.
"""

def exchange(lst1: list, lst2: list) -> str:
    odd_lst1 = sum(x % 2 != 0 for x in lst1)
    even_lst2 = sum(x % 2 == 0 for x in lst2)
    return "YES" if odd_lst1 <= even_lst2 else "NO"

print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # "NO"
<jupyter_output