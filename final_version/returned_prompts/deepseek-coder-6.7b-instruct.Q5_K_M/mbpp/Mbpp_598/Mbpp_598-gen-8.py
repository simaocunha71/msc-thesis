def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 0.3
        temp //= 10

    return num == sum

print(armstrong_number(153))

# 3rd solution
"""
