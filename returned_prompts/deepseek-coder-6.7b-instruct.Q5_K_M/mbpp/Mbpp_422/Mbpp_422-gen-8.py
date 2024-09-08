def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    avg = sum / n
    return avg

print(find_Average_Of_Cube(2))

# Output: 4.5

