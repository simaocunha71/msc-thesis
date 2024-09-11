def list_split(lst, n):
    output = []
    while lst:
        output.append(lst[:n])
        lst = lst[n:]
    return output


# Alternative solution using generator expression
def list_split_alt(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


# Test cases
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
assert list_split([1, 2, 3, 4, 5], 2)==[[1, 2], [3, 4], [5]]

# Alternative solution test cases
assert list_split_alt(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
assert list_split_alt([1, 2, 3, 4, 5], 2)==[[1, 2], [3, 4], [5]]


"""
The function `list_split` takes in a list and an integer `n` and splits the list into smaller lists for every `n`th element. It returns a list of the resulting lists.

The function uses a `while` loop to iterate over the input list `lst` until it becomes empty. In each iteration, it appends a sublist of `n` elements from the beginning of `lst` to the `output` list, and updates `lst` to the remaining elements. This process continues until `lst` becomes empty.

The `output` list is then returned as the result.
