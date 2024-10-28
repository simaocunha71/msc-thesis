def find_Index(n):
    triangular_numbers = [1]
    index = 0
    while len(str(triangular_numbers[-1])) < n:
        index += 1
        triangular_numbers.append(index*(index+1)//2)
    return index