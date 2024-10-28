def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]  # one-liner solution
    # or
    # result = []
    # for sublist in list_of_lists:
    #     result.append(sorted(sublist))
    # return result
    # or
    # return [[x for x in sublist] for sublist in sorted(list_of_lists)]
    # or
    # import operator
    # return [[x for x in sorted(sublist)] for sublist in list_of_lists]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=operator.itemgetter(0))]
    # or
    # return [[x for x in sorted(sublist)] for sublist in list_of_lists]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])]
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda x: x[0])
    # or
    # return [[x for x in sorted(sublist)] for sublist in sorted(list_of_lists, key=lambda