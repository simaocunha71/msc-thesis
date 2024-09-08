def move_zero(lst):
    return lst.sort(key=lambda x: x==0)

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return sorted(lst, key=lambda x: x==0)

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return sorted(lst, key=lambda x: x == 0)

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

#OR

def move_zero(lst):
    return sorted(lst, key=lambda x: x == 0)

print(move_zero([1,0,2,0,3,4]))
<jupyter_output>
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0