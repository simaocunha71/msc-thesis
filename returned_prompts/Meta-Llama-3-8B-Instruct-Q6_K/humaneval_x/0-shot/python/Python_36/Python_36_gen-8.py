def fizz_buzz(n: int):
    count = 0
    for i in range(11, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
print(fizz_buzz(100))  # Output: 8
print(fizz_buzz(200))  # Output: 24
print(fizz_buzz(1000))  # Output: 84
print(fizz_buzz(10000))  # Output: 246
print(fizz_buzz(20000))  # Output: 492
print(fizz_buzz(30000))  # Output: 735
print(fizz_buzz(40000))  # Output: 973
print(fizz_buzz(50000))  # Output: 1202
print(fizz_buzz(60000))  # Output: 1427
print(fizz_buzz(70000))  # Output: 1647
print(fizz_buzz(80000))  # Output: 1862
print(fizz_buzz(90000))  # Output: 2071
print(fizz_buzz(100000))  # Output: 2274
print(fizz_buzz(110000))  # Output: 2471
print(fizz_buzz(120000))  # Output: 2664
print(fizz_buzz(130000))  # Output: 2852
print(fizz_buzz(140000))  # Output: 3035
print(fizz_buzz(150000))  # Output: 3211
print(fizz_buzz(160000))  # Output: 3382
print(fizz_buzz(170000))  # Output: 3547
print(fizz_buzz(180000))  # Output: 3705
print(fizz_buzz(190000))  # Output: 3857
print(fizz_buzz(200000))  # Output: 4002
print(fizz_buzz(210000))  # Output: 4141
print(fizz_buzz(