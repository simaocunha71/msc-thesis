def angle_complex(z):
    if z.real > 0:
        return np.arctan(z.imag/z.real)
    elif z.real < 0 and z.imag >= 0:
        return np.arctan(z.imag/z.real) + np.pi
    elif z.real < 0 and z.imag < 0:
        return np.arctan(z.imag/z.real) - np.pi
    elif z.real == 0 and z.imag > 0:
        return np.pi/2
    elif z.real == 0 and z.imag < 0:
        return -np.pi/2
    else:
        return 0

print(angle_complex(0+1j))

# Output: 1.5707963267948966
# The output is close to the expected value, hence the function is correct
<jupyter_output>
1.5707963267948966
<jupyter_text>
3. Write a function to calculate the roots of a quadratic equation in the form `ax**2 + bx + c = 0`. Your function should take three arguments `a, b, c` and return a tuple containing the roots. If the roots are complex numbers, they should be returned as complex numbers.
<jupyter_code>
