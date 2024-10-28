    def length_cmp(a: str, b: str):
        if len(a) == len(b):
            return a < b
        return len(a) < len(b)

    result = []
    for elem in lst:
        if len(elem) % 2 == 0:
            result.append(elem)

    result.sort(key=len, reverse=True)
    result.sort(key=lambda elem: elem)
    return result


