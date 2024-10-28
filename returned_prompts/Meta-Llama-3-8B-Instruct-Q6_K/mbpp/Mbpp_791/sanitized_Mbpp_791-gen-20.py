def remove_nested(t):
    if isinstance(t, tuple):
        result = []
        for i in t:
            if isinstance(i, tuple):
                result.extend(remove_nested(i))
            else:
                result.append(i)
        return tuple(result)
    return ()