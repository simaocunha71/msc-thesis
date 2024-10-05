def even_odd_count(num):
    num = str(abs(num))
    return (len([x for x in num if int(x) % 2 == 0]), len([x for x in num if int(x) % 2 != 0]))
print(even_odd_count(-12)) #==> (1, 1)
print(even_odd_count(123)) #==> (1, 2)
print(even_odd_count(0)) #==> (1, 0)