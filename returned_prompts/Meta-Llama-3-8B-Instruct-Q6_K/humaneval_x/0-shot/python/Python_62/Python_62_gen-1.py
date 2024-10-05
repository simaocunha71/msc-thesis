def derivative(xs: list):
    return [i * x for i, x in enumerate(xs[1:], 1)]

# test the function
print(derivative([3, 1, 2, 4, 5])) # [1, 4, 12, 20]
print(derivative([1, 2, 3])) # [2, 6]  # test the function
print(derivative([1])) # [0]
print(derivative([])) # []
print(derivative([1, 2])) # [2]
print(derivative([1, 2, 3, 4])) # [2, 6, 8]  # test the function
print(derivative([1, 2, 3, 4, 5, 6])) # [2, 6, 12, 20]
print(derivative([1, 2, 3, 4, 5, 6, 7])) # [2, 6, 12, 20, 30]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8])) # [2, 6, 12, 20, 30, 40]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [2, 6, 12, 20, 30, 42]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [2, 6, 12, 20, 30, 42, 50]  # test the function
print(derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # [2, 6, 12, 20, 30, 42, 54]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # [2, 6, 12, 20, 30, 42, 54, 66]
