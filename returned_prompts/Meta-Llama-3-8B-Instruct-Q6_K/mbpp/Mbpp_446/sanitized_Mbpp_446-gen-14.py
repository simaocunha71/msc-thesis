def count_Occurrence(tup, elements):
    tup = [x.lower() for x in tup]
    elements = [x.lower() for x in elements]
    count_dict = {}
    for x in tup:
        if x in elements:
            if x in count_dict:
                count_dict[x] += 1
            else:
                count_dict[x] = 1
    return count_dict