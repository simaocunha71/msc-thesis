def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if type(item) == list:
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


# def flatten_list(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if type(item) == list:
#             flat_list.extend(flatten_list(item))
#         else:
#             flat_list.append(item)
#     return flat_list

# assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
#
# def flatten_list(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if type(item) == list:
#             flat_list.extend(flatten_list(item))
#         else:
#             flat_list.append(item)
#     return flat_list
#
# assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80