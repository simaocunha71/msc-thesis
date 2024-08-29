def first_odd(num_list):
    for num in num_list:
        if num%2 != 0:
            return num
    return None

print(first_odd([1,3,5])) # 1


