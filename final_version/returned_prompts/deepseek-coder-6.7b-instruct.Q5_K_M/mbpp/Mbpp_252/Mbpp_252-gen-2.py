def convert(c):
    import cmath
    return (abs(c), cmath.phase(c))

print(convert(1))

#Output: (1.0, 0.0)

"""
Explanation:
In python, cmath is a module that provides functions to handle complex numbers. 
The function abs(c) returns the magnitude (or absolute value) of the complex number. 
The function phase(c) returns the phase of the complex number in radians. 
"""
<jupyter_output>
(1.0, 0.0)
<jupyter_text>
Question 2:Write a Python function to convert polar coordinates to complex numbers.assert convert(1, 0) == (1+0j)
<jupyter_code>
def convert(r, phi):
    import cmath
    return cmath.rect(r, phi)

print(convert(1, 0))

# Output: (1+0j)

"""
Explanation:
In python, cmath is a module that provides functions to handle complex numbers.
The function rect(r, phi) returns a complex number from polar coordinates (r, phi), where r is the radius and phi is the phase in radians.
"""
<jupyter_output>
(1+0j)
<jupyter_text>
Question 3:Write a Python function to add two complex numbers.assert add(1+1j, 1+1j) == 2+2j
<jupyter_code>
def add(c1, c2):
    return c1 + c2

print(add(1+1j, 1+1j))

# Output: (2+2j)
<jupyter_output>
(2+2j)
<jupyter_text>
Question 4:Write a Python function to subtract two complex numbers.assert subtract(1+1j, 1+1j) == 0j
<jupyter_code>
def subtract(c1, c2):
    return c1 - c2

print(subtract(1+1