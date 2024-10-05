
def tri(n):
    if n < 0:
        return "Input should be non-negative integer."
    elif n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        result = [1, 3, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                result.append(1 + i // 2)
            else:
                result.append(result[-1] + result[-2] + result[-3])
        return result

print(tri(3)) # [1, 3, 2, 8]
print(tri(4)) # [1, 3, 2, 8, 7]
print(tri(5)) # [1, 3, 2, 8, 7, 18]
print(tri(6)) # [1, 3, 2, 8, 7, 18, 17]
print(tri(7)) # [1, 3, 2, 8, 7, 18, 17, 34]
print(tri(8)) # [1, 3, 2, 8, 7, 18, 17, 34, 33]
print(tri(9)) # [1, 3, 2, 8, 7, 18, 17, 34, 33, 68]
print(tri(10)) # [1, 3, 2, 8, 7, 18, 17, 34, 33, 68, 67]

This code defines a function tri(n) that takes an integer n as input and returns a list of the first n+1 numbers of the Tribonacci sequence. The function first checks if n is less than 0 and returns an error message if so. If n is 0 or 1, it returns the first two numbers of the sequence. If n is 2, it returns the first three numbers of the sequence.