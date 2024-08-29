
def first_odd(lst):
    for number in lst:
        if number % 2 == 1:
            return number
    return None

print(first_odd([1,3,5])) # 1
print(first_odd([2,4,6])) # None


