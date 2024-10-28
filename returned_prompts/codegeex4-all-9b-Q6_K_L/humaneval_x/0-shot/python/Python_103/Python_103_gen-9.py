def rounded_avg(n, m):
    if n > m:
        return -1
    avg = sum(range(n, m+1)) / (m - n + 1)
    avg = round(avg)
    return bin(avg)

print(rounded_avg(1, 5))  # "0b11"
print(rounded_avg(7, 5))  # -1
print(rounded_avg(10, 20))  # "0b1111"
print(rounded_avg(20, 33))  # "0b11010"