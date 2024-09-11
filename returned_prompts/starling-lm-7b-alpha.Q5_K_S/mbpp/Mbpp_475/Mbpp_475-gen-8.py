"""
def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1])

"""

def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1])


def test_sort_counter():
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]

test_sort_counter()



def sort_by_value(d):
    """
    Function to sort a dictionary by its values in ascending order
    """
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    return sorted_d

def test_sort_by_value():
    d = {'Math':81, 'Physics':83, 'Chemistry':87}
    assert sort_by_value(d)==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]

test_sort_by_value()


def sort_dictionary_by_value(d):
    """
    Function to sort a dictionary by its values in ascending order
    """
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    return sorted_d

def test_sort_dictionary_by_value():
    d = {'Math':81, 'Physics':83, 'Chemistry':87}
    assert sort_dictionary_by_value(d)==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]

test_sort_dictionary_by_value()


def sort_dictionary(d):
    """
    Function to sort a dictionary by its values in ascending order
    """
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    return sorted_d

def test_sort_dictionary():
    d = {'Math':81, 'Physics':83, '