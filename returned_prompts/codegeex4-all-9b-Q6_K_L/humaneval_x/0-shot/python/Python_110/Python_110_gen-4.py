def exchange(lst1, lst2):
    # Check if any element in lst1 is odd
    if any(x % 2 for x in lst1):
        # Check if any element in lst2 is even
        if any(x % 2 == 0 for x in lst2):
            return "YES"
    return "NO"

print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))