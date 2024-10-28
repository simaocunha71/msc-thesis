def maximize_elements(tup1, tup2):
    return tuple(max(a, b) for a, b in zip(tup1, tup2)) + tuple(max(tup1, key=lambda x: x[1]) if i >= len(tup2) else max(tup2, key=lambda x: x[1]) for i in range(len(tup1), len(tup1) + len(tup2)))
    # for i in range(len(tup1), len(tup1) + len(tup2)):
    #     if i < len(tup1):
    #         tup1_max = max(tup1, key=lambda x: x[1])
    #     else:
    #         tup1_max = (0, 0)
    #     if i < len(tup2):
    #         tup2_max = max(tup2, key=lambda x: x[1])
    #     else:
    #         tup2_max = (0, 0)
    #     tup1_max = max(tup1_max, tup2_max, key=lambda x: x[1])
    #     if tup1_max != tup1_max:
    #         tup1_max = tup1_max
    #     else:
    #         tup1_max = tup2_max
    #     result.append(tup1_max)
    # return tuple(result) 
    # return tuple(max(a, b) for a, b in zip(tup1, tup2)) + tuple(max(tup1, key=lambda x: x[1]) if i >= len(tup2) else max(tup2, key=lambda x: x[1]) for i in range(len(tup1), len(tup1) + len(tup2)))
    # return tuple(max(a, b) for a, b in zip(tup1, tup2)) + tuple(max(tup1, key=lambda x: x[1]) if i >= len(tup2) else max(tup2, key=lambda x: x[1]) for i in range(len(tup1), len(tup1) + len(tup2)))
    # for i in range(len(tup1), len(tup1) + len(tup2)):
    #     if i < len(tup1):
    #         tup1_max = max(tup1, key=lambda x: x[1])
    #     else:
    #         tup1_max =