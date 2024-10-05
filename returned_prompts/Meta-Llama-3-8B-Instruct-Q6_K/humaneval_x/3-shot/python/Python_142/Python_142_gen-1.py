    return sum(i**2 if i % 3 == 0 else i**3 if i % 4 == 0 and i % 3 != 0 else i for i in lst)  # use list comprehension
    # return sum(i**2 if i % 3 == 0 else i**3 if i % 4 == 0 and i % 3 != 0 else i for i in lst)
    # or
    # total = 0
    # for i in lst:
    #     if i % 3 == 0:
    #         total += i ** 2
    #     elif i % 4 == 0 and i % 3 != 0:
    #         total += i ** 3
    #     else:
    #         total += i
    # return total
    # or
    # result = 0
    # for i, val in enumerate(lst):
    #     if i % 3 == 0:
    #         result += val ** 2
    #     elif i % 4 == 0 and i % 3 != 0:
    #         result += val ** 3
    #     else:
    #         result += val
    # return result
    # or
    # sum_of_squares = sum(i ** 2 if i % 3 == 0 else i ** 3 if i % 4 == 0 and i % 3 != 0 else i for i in lst)
    # return sum_of_squares
    # or
    # result = 0
    # for i in lst:
    #     if i % 3 == 0:
    #         result += i ** 2
    #     elif i % 4 == 0 and i % 3 != 0:
    #         result += i ** 3
    #     else:
    #         result += i
    # return result
    # or
    # result = 0
    # for i in lst:
    #     if i % 3 == 0:
    #         result += i ** 2
    #     elif i % 4 == 0 and i % 3 != 0:
    #         result += i ** 3
    #     else:
    #         result += i
    # return result
    # or
    # result = 0
   