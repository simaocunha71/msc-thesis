
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    try:
        if x == n:
            return True
        x_str = str(x)
        y_str =  str(n)
        x = eval(x_str)
        n = eval(y_str)
        if isinstance(x, int):
            if x == 0 or not x.is_integer:
                return False
            else:
                return True
        elif isinstance(n, int) and not n.is_integer:
            return False
    except Exception as e:
        print("Exception error while solving the problem")
        print(e)

    return False

input_list = ['1/5', '2/10', '1/4']
for i in input_list:
    if simplify(i, '3'):
        print('True.')