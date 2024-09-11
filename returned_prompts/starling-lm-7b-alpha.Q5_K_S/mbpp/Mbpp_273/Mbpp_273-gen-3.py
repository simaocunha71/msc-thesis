def double_at_index(t, n):
    result = []
    for i in range(len(t)):
        if i != n:
            result.append(t[i])
        else:
            result.append(t[i] * 2)
    return tuple(result)


"""
Write a function that takes in a tuple and a number. The function should return a new tuple that