def large_product(a, b, k):
    result = []
    for i in a:
        for j in b:
            result.append(i*j)
    result.sort(reverse=True)
    return result[:k]