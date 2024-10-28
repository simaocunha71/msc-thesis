def monotonic(l: list):
    if len(l) < 2:
        return True

    increasing = l[1] >= l[0]
    decreasing = l[1] <= l[0]

    for i in range(2, len(l)):
        if increasing and l[i] < l[i-1]:
            return False
        if decreasing and l[i] > l[i-1]:
            return False

    return True
# This function checks if the list is monotonically increasing or decreasing.
# It does this by first checking the first two elements to see if the list is either increasing or decreasing.
# Then it iterates over the rest of the list to check if the list remains increasing or decreasing.
# If it finds a pair of elements where the list is no longer increasing or decreasing, it returns False.
# If it gets through the whole list without finding such a pair, it returns True.