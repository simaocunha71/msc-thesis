def swap_numbers(a,b):
    return (b,a)


# Another way to do it
def swap_numbers(a,b):
    return b,a

# Yet another way to do it
def swap_numbers(a,b):
    return (b,) + (a,)

# And one more way
def swap_numbers(a,b):
    return (b,) + (a,) + (:2)


# Yet another way to do it
def swap_numbers(a,b):
    return (b,)+(a,)+(b,):2

"""
We can have multiple test cases here
"""
def test_swap_numbers():
    assert swap_numbers(10,20)==(20,10)

test_swap_numbers()

"""
Or you can put all test cases in one function
"""
def test_swap_numbers():
    assert swap_numbers(10,20)==(20,10)
    assert swap_numbers(20,30)==(30,20)
    assert swap_numbers(30,40)==(40,30)

test_swap_numbers()

"""
Or you can do it this way
"""
def test_swap_numbers():
    assert swap_numbers(10,20)==(20,10)
    assert swap_numbers(20,30)==(30,20)
    assert swap_numbers(30,40)==(40,30)
    assert swap_numbers(40,50)==(50,40)

test_swap_numbers()

"""
Or you can do it this way
"""
def test_swap_numbers():
    for i in range(1,5):
        for j in range(i+1,5):
            assert swap_numbers(i,j)==(j,i)

test_swap_numbers()

"""
Or you can do it this way
"""
def test_swap_