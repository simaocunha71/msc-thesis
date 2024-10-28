
def exchange(lst1, lst2):
    """
    If lst1 is already a list of only even numbers, then we can directly return "YES".
    Otherwise, we can check if there are any even numbers in lst2 that can be exchanged
    with the odd numbers in lst1 to make lst1 a list of only even numbers.
    """
    if all(i % 2 == 0 for i in lst1):
        return "YES"
    for i in lst2:
        if i % 2 == 0:
            if i < lst1[0]:
                return "NO"
            lst1[0] = i
            break
    for i in lst2:
        if i % 2 == 0:
            if i > lst1[len(lst1)-1]:
                return "NO"
            lst1[len(lst1)-1] = i
            break
    for i in range(1, len(lst1)-1):
        if lst1[i] % 2 != 0:
            for j in lst2:
                if j % 2 == 0 and j > lst1[i]:
                    lst1[i] = j
                    break
    if all(i % 2 == 0 for i in lst1):
        return "YES"
    return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # "YES"
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]))  # "NO"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # "NO"

# Time complexity: O(n^2)
# Space complexity: O(1)

# Here's a solution that is more efficient in terms of time complexity:

def exchange(lst1, lst2):
    """
    If lst1 is already a list of only even numbers, then