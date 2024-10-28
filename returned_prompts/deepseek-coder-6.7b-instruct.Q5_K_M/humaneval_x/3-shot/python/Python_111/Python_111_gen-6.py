    result = {}
    for i in test.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    max_value = max(result.values()) if result else 0
    return {k: v for k, v in result.items() if v == max_value}


