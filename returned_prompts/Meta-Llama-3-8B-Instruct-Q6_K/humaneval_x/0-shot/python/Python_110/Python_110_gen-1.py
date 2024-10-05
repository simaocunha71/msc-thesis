def exchange(lst1, lst2):
    even_numbers = [num for num in lst1 if num % 2 == 0]
    odd_numbers = [num for num in lst1 if num % 2 != 0]
    
    for num in odd_numbers:
        if num in lst2:
            even_numbers.append(num)
            lst2.remove(num)
        else:
            return "NO"
    
    if len(even_numbers) == len(lst1):
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4])) # "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4])) # "NO"
print(exchange([1, 2, 3, 4], [2, 4, 6, 8])) # "YES"
print(exchange([1, 2, 3, 4], [1, 1, 1, 1])) # "NO"
print(exchange([1, 2, 3, 4], [1, 2, 3, 5])) # "NO"  # test case with 5
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5])) # "NO"  # test case with 5
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6])) # "YES"  # test case with 5 and 6
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7])) # "NO"  # test case with 5, 6, 7
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8])) # "YES"  # test case with 5, 6, 7, 8
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6