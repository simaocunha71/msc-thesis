"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tup):
    print('Element',end=' ')
    for k in tup:
        if len(k)!=0:print(k,end=' ')
        else:print(k,' ')

    print('End')
    x = input()
    
    if x=='':return True
    else:return False
check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"))