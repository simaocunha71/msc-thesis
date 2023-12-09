
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError as ee:
        print("Exception in converting to float!")

    try:
        a = int(a)
        b = int(b)
    except ValueError as ee:
        print("Exception in converting to int!")
    if a == b:
        return None
    elif (str(a) < str(b)):
        return -1
    else:
        return 1


def compare_many(alist, blist):
    """
    Create a function that takes a list of integers and another list of integers, floats or strings representing real numbers.
    For each item in the first list, find its matching item in the second list by comparing each item to every other item. If there is no match, return None. Otherwise, if the given items do not have the same value type (either integer or float), print a ValueError exception message with the string "cannot compare" and an explanation of the error. Return 0 if the first list has smaller values than in second list and -1 otherwise.
    """
    n = len(alist)

    for i in range(0,n):
        try:
            a = float(alist[i])
            b = float(blist[i % len(blist)])
            if (str(a) < str(b)):  # a and b are different types of real number
                print("Cannot compare", alist[i], "