
    def exchange(lst1, lst2):
        odd_in_lst1 = sum(x % 2 != 0 for x in lst1)
        even_in_lst2 = sum(x % 2 == 0 for x in lst2)
        return "YES" if odd_in_lst1 <= even_in_lst2 else "NO"

    print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # => "YES"
    print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # => "NO"

Explanation:

This function works by counting the number of odd numbers in lst1 and even numbers in lst2.
If there are more odd numbers in lst1 than even numbers in lst2, it is not possible to make all numbers in lst1 even by exchanging elements between lst1 and lst2.
Therefore, the function returns "NO". Otherwise, it returns "YES".
The logic is that exchanging odd numbers from lst1 with even numbers from lst2 will result in even numbers in lst1.
"""

def exchange(lst1, lst2):
    odd_in_lst1 = sum(x % 2 != 0 for x in lst1)
    even_in_lst2 = sum(x % 2 == 0 for x in lst2)
    return "YES" if odd_in_lst1 <= even_in_lst2 else "NO"

print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # => "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # => "NO"
<jupyter_output>
YES
NO
<jupyter_text>
Problem 6
<jupyter_code>
"""
