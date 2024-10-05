def even_odd_count(num):
    count = [0,0]
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            count[0] += 1
        else:
            count[1] += 1
    return tuple(count)

print(even_odd_count(-12))
print(even_odd_count(123))
print(even_odd_count(0))
print(even_odd_count(4))
print(even_odd_count(-99))