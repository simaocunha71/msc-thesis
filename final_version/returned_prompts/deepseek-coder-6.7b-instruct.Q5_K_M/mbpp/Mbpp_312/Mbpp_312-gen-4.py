def volume_cone(radius, height):
    return 1/3 * math.pi * radius**2 * height

print(math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001))

# 3. Write a Python function that takes a list of strings, and returns a list with the strings 
# sorted by last letter.
# Example: ['hello', 'world', 'python', 'is', 'awesome'] => ['is', 'awesome', 'hello', 'python', 'world']

