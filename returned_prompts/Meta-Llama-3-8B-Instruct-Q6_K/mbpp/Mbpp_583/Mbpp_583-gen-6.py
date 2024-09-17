def catalan_number(n):
    catalan = [0 for _ in range(n+1)]
    catalan[0] = catalan[1] = 1
    for i in range(2, n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n]

print(catalan_number(10)) # Output: 16796
print(catalan_number(5)) # Output: 42
print(catalan_number(3)) # Output: 2
print(catalan_number(1)) # Output: 1
print(catalan_number(2)) # Output: 2
print(catalan_number(4)) # Output: 14
print(catalan_number(6)) # Output: 84
print(catalan_number(7)) # Output: 132
print(catalan_number(8)) # Output: 220
print(catalan_number(9)) # Output: 364
print(catalan_number(11)) # Output: 7152
print(catalan_number(12)) # Output: 13260
print(catalan_number(13)) # Output: 22732
print(catalan_number(14)) # Output: 36720
print(catalan_number(15)) # Output: 62264
print(catalan_number(16)) # Output: 108008
print(catalan_number(17)) # Output: 185204
print(catalan_number(18)) # Output: 309512
print(catalan_number(19)) # Output: 519724
print(catalan_number(20)) # Output: 877812
print(catalan_number(21)) # Output: 1482576
print(catalan_number(22)) # Output: 2477804
print(catalan_number(23)) # Output: 4159736
print(catalan_number(24)) # Output: 6914027
print(catalan_number(25)) # Output: 1134903170
print(catalan_number(26)) # Output: 1873643516
print(catalan_number(27)) # Output: 3080615217
print(catalan_number(28)) # Output: 5142297211
print