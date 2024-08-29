
def right_insertion(lst, n):
    for i in range(len(lst)):
        if n < lst[i]:
            return i
    return len(lst)

print(right_insertion([1,2,4,5],6)) # 4

# ---------------------------------------

