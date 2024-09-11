def mul_even_odd(l):
    ev=0
    od=0
    for i in l:
        if i%2==0:
            ev=ev*i
        else:
            od=od*i
    if od==0:
        return ev
    elif ev==0:
        return od
    else:
        return ev*od



def test_mul_even_odd():
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    print("All Tests Passed")

test_mul_even_odd()








"""
def mul_even_odd(l):
    ev=0
    od=0
    for i in l:
        if i%2==0:
            ev=ev*i
        else:
            od=od*i
    if od==0:
        return ev
    elif ev==0:
        return od
    else:
        return ev*od

def test_mul_even_odd():
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    print("All Tests Passed")
"""














"""
def mul_even_odd(l):
    ev=0
    od=0
    for i in l:
        if i%2==0:
            ev=ev*i
        else:
            od=od*i
    if od==0:
        return ev
    elif ev==0:
        return od
    else:
        return ev*od

def test_mul_even_odd():
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    print("All Tests Passed")
"""



"""
def mul_even_odd(l):
    ev=0
    od=0
    for i in l:
        if i%2==0:
            ev=ev*i
        else:
            od=od*i
    if od==0:
        return ev
   