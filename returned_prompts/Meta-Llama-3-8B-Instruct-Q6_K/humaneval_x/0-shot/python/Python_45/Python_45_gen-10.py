    return (a*h)/2

# Testing
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 4))  # Output: 20.0
print(triangle_area(3, 2))   # Output: 3.0
print(triangle_area(2, 1))   # Output: 1.0
print(triangle_area(10, 0))  # Output: 0.0
print(triangle_area(0, 10))  # Output: 0.0
print(triangle_area(-10, 5)) # Output: 0.0
print(triangle_area(10, -5)) # Output: 0.0
print(triangle_area(-5, 10)) # Output: 0.0
print(triangle_area(5, -10)) # Output: 0.0
print(triangle_area(-5, -10)) # Output: 0.0
print(triangle_area(0, 0))   # Output: 0.0

# Testing with non-numeric inputs
print(triangle_area("5", 3))  # Output: TypeError
print(triangle_area(5, "3"))  # Output: TypeError
print(triangle_area("five", 3))  # Output: TypeError
print(triangle_area(5, "three"))  # Output: TypeError
print(triangle_area(5, 3.5))    # Output: TypeError
print(triangle_area(5, 3.5, 4)) # Output: TypeError
print(triangle_area("a", 3, 4)) # Output: TypeError
print(triangle_area(5, "a", 4)) # Output: TypeError
print(triangle_area(5, 3, "a")) # Output: TypeError
print(triangle_area(5, 3, 4, "b")) # Output: TypeError
print(triangle_area(5, 3, "b", 4)) # Output: TypeError
print(triangle_area(5, 3, 4, "c")) # Output: TypeError
print(triangle_area(5, "b", 4, "c")) # Output: TypeError
print(triangle_area(5, 3, "c", 4)) # Output: TypeError
print(triangle_area(5, "c