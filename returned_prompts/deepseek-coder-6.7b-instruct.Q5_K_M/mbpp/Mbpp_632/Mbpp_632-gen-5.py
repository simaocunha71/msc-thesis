def move_zero(lst):
    return lst.sort(key=lambda x: x==0)
    # lst.sort(key=lambda x: x==0) sorts the list based on the condition x==0 (if x is zero, it is considered True and it moves to the end)

print(move_zero([1,0,2,0,3,4]))

# or

def move_zero(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst

print(move_zero([1,0,2,0,3,4]))

# or 

def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

# or 

def move_zero(lst):
    zero = lst.count(0)
    lst = [i for i in lst if i != 0]
    lst.extend([0]*zero)
    return lst

print(move_zero([1,0,2,0,3,4]))


