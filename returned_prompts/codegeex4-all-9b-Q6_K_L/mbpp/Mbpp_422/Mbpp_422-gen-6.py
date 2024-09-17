def find_Average_Of_Cube(n: int) -> float:
    total = sum(i**3 for i in range(1, n+1))
    average = total / n
    return average

