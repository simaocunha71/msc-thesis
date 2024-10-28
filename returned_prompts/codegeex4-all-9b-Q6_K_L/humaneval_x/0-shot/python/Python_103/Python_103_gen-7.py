def rounded_avg(n, m):
    if n > m:
        return -1
    return bin(round(sum(range(n, m+1)) / (m - n + 1)))

print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))