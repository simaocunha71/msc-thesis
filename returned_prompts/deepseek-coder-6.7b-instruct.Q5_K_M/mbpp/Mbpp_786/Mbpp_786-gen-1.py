
def right_insertion(lst, num):
    for i in range(len(lst)):
        if lst[i] > num:
            return i
    return len(lst)

print(right_insertion([1,2,4,5],6))

