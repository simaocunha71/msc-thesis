    def helper(x):
        if x == 0:
            return []
        result = []
        for i in range(10):
            if i % 2 != 0:
                result.append(helper(x - 10 ** i))
        return result

    result = helper(sum(map(int, str(x))))
    result = list(map(str, result))
    result.sort()
    result = "".join(result)
    return int(result)


# If you have Python3, you can use the following code.

# def unique_digits(x):
#     """Given a list of positive integers x. return a sorted list of all 
#     elements that hasn't any even digit.

#     Note: Returned list should be sorted in increasing order.
#     
#     For example:
#     >>> unique_digits([15, 33, 1422, 1])
#     [1, 15, 33]
#     >>> unique_digits([152, 323, 1422, 10])
#     []
#     """

#     result = []
#     for i in range(10):
#         if i % 2 != 0:
#             result.append(unique_digits(x - 10 ** i))
#     result = list(map(str, result))
#     result.sort()
#     result = "".join(result)
#     return int(result)


# Test
# print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
# print(unique_digits([152, 323, 1422, 10]))  # []






































































