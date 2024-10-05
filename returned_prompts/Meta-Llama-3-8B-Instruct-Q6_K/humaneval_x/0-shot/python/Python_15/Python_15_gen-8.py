def string_sequence(n: int) -> str:
    return ' '.join(map(str, range(n + 1)))  # use map to convert to str and join with space
    # or use f-string: return ' '.join(f'{i}' for i in range(n + 1))  # f-string for conversion to str
    # or use list comprehension: return ' '.join([str(i) for i in range(n + 1)])  # list comprehension for conversion to str
    # or use itertools: return ' '.join(map(str, itertools.count(0, 1)))  # itertools.count for sequence generation
    # or use generator expression: return ' '.join(str(i) for i in range(n + 1))  # generator expression for conversion to str
    # or use for loop: result = ''
    # for i in range(n + 1):
    #     result += str(i) + ' '
    # return result.strip()  # for loop for conversion to str
    # or use recursion: def string_sequence(n):
    #     if n == 0:
    #         return '0'
    #     else:
    #         return str(n) + ' ' + string_sequence(n - 1)
    # return string_sequence(n)  # recursion for conversion to str
    # or use built-in function: return ' '.join(map(str, range(0, n + 1)))  # built-in function for conversion to str
    # or use lambda function: return ' '.join(map(lambda x: str(x), range(n + 1)))  # lambda function for conversion to str
    # or use list comprehension with if condition: return ' '.join([str(i) for i in range(n + 1) if i != 0])  # list comprehension for conversion to str
    # or use if condition with for loop: result = ''
    # for i in range(n + 1):
    #     if i != 0:
    #         result += str(i) + ' '
    # return result.strip()  # if condition with for loop for conversion to str
    # or use recursion with if condition: def string_sequence(n):
    #     if n == 0:
    #         return '0'
    #     elif n == 1:
    #         return '0 1'
    #     else:
    #         return string_sequence(n - 1) +