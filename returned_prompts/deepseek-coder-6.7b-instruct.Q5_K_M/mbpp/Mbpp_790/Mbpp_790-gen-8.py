
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True

#Test Cases
print(even_position([3,2,1])) #False
print(even_position([2,3,4,5,6,7,8])) #True
print(even_position([2,4,6,7,9])) #False

