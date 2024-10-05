
def do_algebra(operator, operand):
    result = 0
    for i in range(len(operand)):
        if i == 0:
            result = operand[i]
        else:
            result = operator[i-1](result, operand[i])
    return result


def test_do_algebra():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['-', '*', '+'], [2, 3, 4, 5]) == 6
    assert do_algebra(['-', '-', '*'], [2, 3, 4, 5]) == 10
    assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 12
    assert do_algebra(['+', '-', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '-', '*', '-'], [2, 3, 4, 5]) == 10
    assert do_algebra(['-', '-', '*', '-'], [2, 3, 4, 5]) == 10
    assert do_algebra(['*', '*', '*', '*'], [2, 3, 4, 5]) == 64
    assert do_algebra(['-', '-', '*', '-'], [2, 3, 4, 5]) == 10
    assert do_algebra(['-', '-', '*', '-'], [2, 3, 4, 5]) == 10
    assert do_algebra(['-', '-', '*', '-'], [2, 3, 4, 5]) == 10
    assert do_algebra(['-', '-', '*', '-'], [2, 3, 4, 5]) == 10

test_do_algebra()