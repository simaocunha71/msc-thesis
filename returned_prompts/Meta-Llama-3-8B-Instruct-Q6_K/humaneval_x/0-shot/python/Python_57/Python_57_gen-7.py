def monotonic(l: list):
    return (all(l[i] <= l[i+1] for i in range(len(l)-1)) or
            all(l[i] >= l[i+1] for i in range(len(l)-1)))
    
# Testing
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 3, 4]))  # True
print(monotonic([4, 3, 2, 1]))  # True
print(monotonic([1, 1, 1, 1]))  # True
print(monotonic([1, 2, 1, 4]))  # False
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([1, 1, 1, 1]))  # True
print(monotonic([5, 4, 3, 2]))  # True
print(monotonic([1, 2, 3, 5]))  # True
print(monotonic([5, 3, 2, 1]))  # True
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([1, 2, 3, 5]))  # True
print(monotonic([5, 3, 2, 1]))  # True
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([1, 2, 3, 5]))  # True
print(monotonic([5, 3, 2, 1]))  # True
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([1, 2, 3, 4]))  # True
print(monotonic([4, 3, 2, 1]))  # True
print(monotonic([1, 1, 1, 1]))  # True
print(monotonic([1, 2, 1, 4])) 