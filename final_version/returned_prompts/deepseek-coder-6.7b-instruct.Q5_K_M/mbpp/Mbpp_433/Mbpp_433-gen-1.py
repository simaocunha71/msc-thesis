
def check_greater(array, num):
    for i in array:
        if i <= num:
            return False
    return True

print(check_greater([1, 2, 3, 4, 5], 4))

