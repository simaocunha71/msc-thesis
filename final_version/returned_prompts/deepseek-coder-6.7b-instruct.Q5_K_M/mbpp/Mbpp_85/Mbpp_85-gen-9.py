def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)

print(surfacearea_sphere(10))

# If the result is close to 1256.6370614359173, it means the function is correct.
<jupyter_output>
1256.6370614359173
<jupyter_text>
Q2: Write a function to solve the quadratic equation: ax² + bx + c = 0  (a ≠ 0). The function should return the two solutions in a list.
<jupyter_code>
def solve_quadratic(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return [sol1, sol2]

print(solve_quadratic(1, -3, 2))
<jupyter_output>
[1.0, 2.0]
<jupyter_text>
Q3: Write a function that takes a list of integers and returns the difference between the largest and smallest values.
<jupyter_code>
def diff_max_min(lst):
    return max(lst) - min(lst)

print(diff_max_min([1, 2, 3, 4, 5]))
<jupyter_output>
4
<jupyter_text>
Q4: Write a function that takes a list of integers and returns the median of the list.
<jupyter_code>
def find_median(lst):
    n = len(lst)
    lst.sort()
    
    if n % 2 == 0:
        median1 = lst[n//2]
        median2 = lst[n//2 - 1]
        median = (median1