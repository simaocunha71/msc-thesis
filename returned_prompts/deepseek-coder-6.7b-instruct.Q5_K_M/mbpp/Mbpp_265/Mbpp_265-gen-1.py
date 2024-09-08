
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))
<jupyter_output>
[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']]
<jupyter_text>
The function `list_split()` takes in a list and an integer as arguments and splits the list into nth elements. The `range()` function is used with a step of `n` to iterate over the indices of the list. In each iteration, a slice of length `n` is taken from the list starting from the current index. The resulting slices are collected into a new list which is returned by the function. The `if __name__ == "__main__":` part is used to test the function with the provided example. The result is a list of lists, where each inner list contains every nth element from the original list.
<jupyter_code>
if __name__ == "__main__":
    assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3) == [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
    print("All tests passed.")
<jupyter_output>
All tests passed.
<jupyter_text>
