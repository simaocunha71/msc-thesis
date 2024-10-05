
def exchange(lst1, lst2):
    odd_lst1 = [x for x in lst1 if x % 2 != 0]
    even_lst2 = [x for x in lst2 if x % 2 == 0]
    if len(odd_lst1) <= len(even_lst2):
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # => "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # => "NO"

In this solution, we first create two lists: odd_lst1 which contains all odd numbers in lst1, and even_lst2 which contains all even numbers in lst2. 
Then, we check if the amount of odd numbers in lst1 is less or equal to the amount of even numbers in lst2. 
If it is, it means we can exchange some odd numbers in lst1 with even numbers in lst2 to make all numbers in lst1 to be even. 
Therefore, we return "YES". If not, we return "NO".

"""
Time complexity: O(n)
Space complexity: O(n)
"""

"""
Solution 2:
"""

def exchange(lst1, lst2):
    odd_count = sum(x % 2 != 0 for x in lst1)
    even_count = sum(x % 2 == 0 for x in lst2)
    return "YES" if odd_count <= even_count else "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # => "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # => "NO"

"""
Time complexity: O(n)
Space complexity: O(1)
"""

Both solutions have