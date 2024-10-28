def even_odd_count(num):
    num = str(abs(num))
    return (sum(1 for x in num if x in '02468'), sum(1 for x in num if x in '13579'))

print(even_odd_count(-12))  # ==> (1, 1)
print(even_odd_count(123))  # ==> (1, 2)