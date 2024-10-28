def by_length(arr):
    # filter out all the numbers that are not between 1 and 9 inclusive
    arr = [num for num in arr if 1 <= num <= 9]

    # sort the array
    arr.sort()

    # reverse the array
    arr.reverse()

    # replace each number by its corresponding name
    arr = [str(num) for num in arr]

    # return the array
    return arr

# test the function
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']