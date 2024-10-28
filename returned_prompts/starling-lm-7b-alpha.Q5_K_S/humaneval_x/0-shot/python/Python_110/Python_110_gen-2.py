
def exchange(lst1, lst2):
    odd_count = 0
    for num in lst1:
        if num % 2 != 0:
            odd_count += 1
    if odd_count > len(lst2) - odd_count:
        return "NO"
    else:
        for num in lst1:
            if num % 2 != 0:
                for i in range(len(lst2)):
                    if lst2[i] % 2 == 0:
                        lst2[i] = num
                        lst1[lst1.index(num)] = lst2[i]
                        break
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"


# Test cases:
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Expected output: "YES"
print(exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]))  # Expected output: "NO"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Expected output: "NO"
print(exchange([1, 2, 3, 4, 5], [1, 3, 5, 4]))  # Expected output: "NO"
print(exchange([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]))  # Expected output: "YES"
print(exchange([], []))  # Expected output: "YES"
print(exchange([1, 2, 3, 4, 5], []))  # Expected output: "NO"






















































