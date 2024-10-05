    return 0.5 * a * h

# Test
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(3, 4))  # Output: 6.0
print(triangle_area(7, 2))  # Output: 7.0
print(triangle_area(2, 7))  # Output: 14.0
print(triangle_area(1, 1))  # Output: 0.5
print(triangle_area(1, 0))  # Output: 0
print(triangle_area(0, 1))  # Output: 0

# Error handling
try:
    triangle_area("a", 3)
except TypeError:
    print("Error: Argument 'a' should be a number.")
try:
    triangle_area(5, "h")
except TypeError:
    print("Error: Argument 'h' should be a number.")    
try:
    triangle_area("a", "h")
except TypeError:
    print("Error: Both arguments 'a' and 'h' should be numbers.")   



