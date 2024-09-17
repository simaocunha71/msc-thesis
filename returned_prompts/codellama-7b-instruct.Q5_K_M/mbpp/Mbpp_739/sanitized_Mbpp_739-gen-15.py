def find_Index(n):
    triangular_numbers = [sum(digits) for digits in 
                        map(lambda x: list(map(int, str(x))), range(1, 10 ** n))]
    return triangular_numbers.index(min(triangular_numbers)) + 1