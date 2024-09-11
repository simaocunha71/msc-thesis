"""
def even_position(input_list):
    for index, value in enumerate(input_list):
        if index % 2 != 0 and value % 2 == 0:
            return False
    return True

"""

def even_position(input_list):
    for index, value in enumerate(input_list):
        if index % 2 != 0 and value % 2 == 0:
            return False
    return True


def test_even_position():
    assert even_position([3,2,1]) == False
    assert even_position([3,2,4,1,6,8]) == True
    assert even_position([3,2,4,1]) == False
    assert even_position([3,2,4,1,8]) == True
    assert even_position([3,2,4,1,6]) == False
    assert even_position([3,2,4,1,6,8,10]) == True

test_even_position()


def even_position(input_list):
    for i in range(len(input_list)):
        if i % 2 != 0 and input_list[i] % 2 == 0:
            return False
    return True


def test_even_position():
    assert even_position([3,2,1]) == False
    assert even_position([3,2,4,1,6,8]) == True
    assert even_position([3,2,4,1]) == False
    assert even_position([3,2,4,1,8]) == True
    assert even_position([3,2,4,1,6]) == False
    assert even_position([3,2,4,1,6,8,10]) == True

test_even_position()


def even_position(input_list):
    for i in range(len(input_list)):
        if i % 2 != 0 and input_list[i] % 2 == 0:
            return False
    return True

def test_even_position():
    assert even_position([3,2,1]) == False
