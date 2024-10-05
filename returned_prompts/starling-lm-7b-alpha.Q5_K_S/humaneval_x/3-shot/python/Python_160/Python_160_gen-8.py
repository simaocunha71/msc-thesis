    def compute(operator, operand):
        if len(operator) == 0:
            return operand[0]
        elif len(operator) == 1:
            return operand[0] * operand[1]
        elif len(operator) == 2:
            if operator[0] == '+':
                return operand[0] + operand[1]
            elif operator[0] == '-':
                return operand[0] - operand[1]
            elif operator[0] == '*':
                return operand[0] * operand[1]
            elif operator[0] == '//':
                return operand[0] // operand[1]
            elif operator[0] == '**':
                return operand[0] ** operand[1]
        else:
            return compute(operator[:-1], operand[:-1]) * compute(operator[-1:], operand[-1:])

    return compute(operator, operand)


# Run the tests
if __name__ == '__main__':
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
    print(separate_paren_groups('( ) (( )) (( )( ))'))
    print(truncate_number(3.5))
    print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
    print(do_algebra(['*', '//'], [2, 3, 4, 5]))
    print(do_algebra(['+', '-', '*', '//', '**'], [2, 3, 4, 5]))










































































































