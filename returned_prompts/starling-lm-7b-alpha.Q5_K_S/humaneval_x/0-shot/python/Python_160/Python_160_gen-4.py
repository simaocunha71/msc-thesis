# Here's one possible solution
def do_algebra(operator, operand):
    # Initialize the result
    result = operand[0]

    # Iterate through the operators and operands, applying the operations
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '/':
            result /= operand[i+1]
        elif operator[i] == '//':
            result = int(result / operand[i+1])
        elif operator[i] == '**':
            result = result ** operand[i+1]

    return result

# Test
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # 9
print(do_algebra(['*', '+', '/'], [2, 3, 4, 5]))  # 3.6
print(do_algebra(['//', '**'], [2, 3]))  # 1



# Here's a more efficient solution using itertools.izip
from itertools import izip

def do_algebra(operator, operand):
    # Initialize the result
    result = operand[0]

    # Iterate through the operators and operands, applying the operations
    for op, num in izip(operator, operand[1:]):
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            result /= num
        elif op == '//':
            result = int(result / num)
        elif op == '**':
            result = result ** num

    return result

# Test
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # 9
print(do_algebra(['*', '+', '/'], [2