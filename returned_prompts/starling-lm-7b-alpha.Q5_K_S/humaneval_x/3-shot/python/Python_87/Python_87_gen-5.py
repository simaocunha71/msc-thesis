    def find_index_of_x(lst, x):
        for i in range(len(lst)):
            if x in lst[i]:
                return i
        return -1

    result = []
    index = find_index_of_x(lst, x)

    if index == -1:
        return result

    result.append((index, lst[index].index(x)))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)

    return result


