
def convert_list_dictionary(keys, names, scores):
    return [{keys[i]: {names[i]: scores[i]}} for i in range(len(keys))]

keys = ["S001", "S002", "S003", "S004"]
names = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
scores = [85, 98, 89, 92]

print(convert_list_dictionary(keys, names, scores))

Output:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

This function uses list comprehension to create a new list. For each index 'i', it creates a dictionary where the key is the 'i'-th element of 'keys' and the value is another dictionary where the key is the 'i'-th element of 'names' and the value is the 'i'-th element of 'scores'.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python program to solve the quadratic equation. The user should be able to enter the coefficients a, b and c.
<jupyter_code>
import cmath

def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return sol1, sol2

a = int(input('Enter coefficient a: '))
b = int(input('Enter coefficient b: '))
c = int(input('Enter coefficient c: '))

sol = solve_quadratic(a, b, c)
print("The solutions are {0} and {1}".format(sol[0], sol[1]))
<j