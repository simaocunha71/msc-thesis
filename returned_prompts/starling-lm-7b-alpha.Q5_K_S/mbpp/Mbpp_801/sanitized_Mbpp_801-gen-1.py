def test_three_equal(x,y,z):
    if x==y and y==z:
        return 3
    elif x==y and y!=z:
        return 2
    elif y==z and y!=x:
        return 2
    elif z==x and z!=y:
        return 2
    else:
        return 0