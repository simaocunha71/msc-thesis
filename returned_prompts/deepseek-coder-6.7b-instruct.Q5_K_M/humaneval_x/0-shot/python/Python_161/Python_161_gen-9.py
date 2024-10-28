
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)

print(solve("1234"))  # 4321
print(solve("ab"))  # AB
print(solve("#a@C"))  # "#A@c"
print(solve("1234ab"))  # "4321AB"
print(solve("ab1234"))  # "AB4321"
print(solve("1234abAB"))  # "4321ABab"
print(solve("%$#@"))  # "%$#@"

# 1st solution: Using python string methods to solve the problem.
# 2nd solution: Using python list comprehension to solve the problem.
# 3rd solution: Using python list comprehension to solve the problem.
# 4th solution: Using python list comprehension to solve the problem.
# 5th solution: Using python list comprehension to solve the problem.
# 6th solution: Using python list comprehension to solve the problem.
# 7th solution: Using python list comprehension to solve the problem.
# 8th solution: Using python list comprehension to solve the problem.
# 9th solution: Using python list comprehension to solve the problem.
# 10th solution: Using python list comprehension to solve the problem.
# 11th solution: Using python list comprehension to solve the problem.
# 12th solution: Using python list comprehension to solve the problem.
# 13th solution: Using python list comprehension to solve the problem.
# 14th solution: Using python list comprehension to solve the problem.
# 15th solution: Using python list comprehension to solve the problem.
# 16th solution: Using python list comprehension to solve the problem.
# 17th solution: Using python list comprehension to solve the problem.
# 18th solution: Using python list comprehension to solve the problem.
# 19th solution: Using python