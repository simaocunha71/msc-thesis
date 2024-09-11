"""
def count_X(tup, elem):
    count = 0
    for i in tup:
        if i == elem:
            count += 1
    return count
"""

def count_X(tup, elem):
    return tup.count(elem)

def test_count_X():
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert count_X((1, 2, 3, 1, 2, 3), 2) == 2
    assert count_X((1, 2, 3, 1, 2, 3, 2), 2) == 3
    print("All tests passed.")

test_count_X()



"""
The function `count_X` should take in a tuple and an element, and count the number of times the element appears in the tuple. It should return the count.

The provided code defines a function `count_X` that takes in a tuple and an element, and uses a `for` loop to iterate over the tuple. For each element in the tuple, it checks if the element is equal to the input element. If it is, it increments a counter variable. After iterating over the entire tuple, the function returns the count.

The provided test cases check the function `count_X` with different inputs. The first test case checks that the function correctly counts the number of occurrences of the element 4 in the tuple (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), which should be 0. The second test case checks that the function correctly counts the number of occurrences of the element 2 in the tuple (1, 2, 3, 1, 2, 3), which should be 2. The third test case checks that the function correctly counts the number of occurrences of the element 2 in the tuple (1, 2, 3, 1, 2, 3, 2), which should be 