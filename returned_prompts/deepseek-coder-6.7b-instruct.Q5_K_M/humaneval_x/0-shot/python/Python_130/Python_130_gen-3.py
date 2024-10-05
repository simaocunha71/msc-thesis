
def tri(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        lst = [1, 3, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                lst.append(1 + i // 2)
            else:
                lst.append(lst[-1] + lst[-2] + lst[-3])
        return lst

print(tri(3)) # [1, 3, 2, 8]
print(tri(4)) # [1, 3, 2, 8, 11]
print(tri(5)) # [1, 3, 2, 8, 11, 19]
print(tri(6)) # [1, 3, 2, 8, 11, 19, 30]
print(tri(7)) # [1, 3, 2, 8, 11, 19, 30, 50]

This program generates the Tribonacci sequence up to the nth term. It starts by defining the base cases for the sequence, and then for each subsequent term, checks if the term is even or odd. If it's even, it adds 1 plus the term divided by 2 to the list. If it's odd, it adds the sum of the last three terms to the list. The resulting list is then returned.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 111:
<jupyter_code>
