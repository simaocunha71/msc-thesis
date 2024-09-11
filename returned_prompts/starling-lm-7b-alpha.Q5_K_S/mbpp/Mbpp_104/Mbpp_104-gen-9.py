"""
def sort_sublists(sublists):
    for i in range(len(sublists)):
        sublists[i].sort()
    return sublists

def test_sort_sublists():
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    print("All tests passed!")

test_sort_sublists()
"""

def sort_sublists(sublists):
    for sublist in sublists:
        sublist.sort()
    return sublists

def test_sort_sublists():
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    print("All tests passed!")

test_sort_sublists()











"""
The function `sort_sublists` takes a list of lists as its argument, and it sorts each sublist in the list. It uses a for loop to iterate over each sublist in the given list, and for each sublist, it uses the `sort` method to sort the sublist in ascending order. Finally, it returns the sorted list of lists.

To test the function, the function `test_sort_sublists` is defined. It calls the `sort_sublists` function with a sample input `([["green", "orange"], ["black", "white"], ["white", "black", "orange"]])`, and checks if the returned value is equal to the expected output `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`. If the assertion passes, it prints "All tests passed!".

By running the `test_sort_sublists` function, we can verify that the `sort_sublists` function is correctly sorting each sublist in the given list.
"""

```

```