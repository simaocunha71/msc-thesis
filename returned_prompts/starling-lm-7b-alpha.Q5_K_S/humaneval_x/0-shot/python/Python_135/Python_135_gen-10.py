    # We can use a set to keep track of all the elements that we have seen
    # so far. Then, we can iterate through the array and find the first
    # element which is not in the set.

    # First, we check if the array is empty. If it is, then there are no
    # elements in the array and therefore no elements to check. If the array
    # is not empty, we create a set to store the elements.

    if len(arr) == 0:
        return -1

    seen = set()

    # Then, we iterate through the array. If an element is not in the set,
    # then it is an element that we have not seen before.

    for elem in arr:
        if elem not in seen:
            # If the element is not in the set, we add it to the set and
            # return its index.

            seen.add(elem)
            return arr.index(elem)

    # If we have iterated through the entire array and have not found any
    # elements that we have not seen before, then there are no such elements.

    return -1

# Here is an example of how you can use the function.

print(can_arrange([1,2,4,3,5]))
print(can_arrange([1,2,3]))





































































































































































































