    # your code here
    def double_the_difference(lst):
        result = 0
        for i in lst:
            if i % 2 == 0:
                continue
            else:
                result += i ** 2
        return result

    # test cases
    print(double_the_difference([1, 3, 2, 0]))  # should print 10
    print(double_the_difference([-1, -2, 0]))  # should print 0
    print(double_the_difference([9, -2]))  # should print 81
    print(double_the_difference([0]))  # should print 0


def double_the_difference(lst):
    result = 0
    for i in lst:
        if i % 2 == 0:
            continue
        else:
            result += i ** 2
    return result


# test cases
print(double_the_difference([1, 3, 2, 0]))  # should print 10
print(double_the_difference([-1, -2, 0]))  # should print 0
print(double_the_difference([9, -2]))  # should print 81
print(double_the_difference([0]))  # should print 0





























































































































































































