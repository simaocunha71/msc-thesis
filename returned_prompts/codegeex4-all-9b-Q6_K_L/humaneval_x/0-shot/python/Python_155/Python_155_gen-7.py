def even_odd_count(num):
    num = str(abs(num))
    return (num.count('0') + num.count('2') + num.count('4') + num.count('6') + num.count('8'), num.count('1') + num.count('3') + num.count('5') + num.count('7') + num.count('9'))

print(even_odd_count(-12))  # (1, 1)
print(even_odd_count(123))  # (1, 2)