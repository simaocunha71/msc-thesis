    arr = [str(i) for i in arr if 1 <= i <= 9]
    arr.sort(reverse=True)
    result = [str(i) for i in range(1, 10)]
    return result[::-1] if arr else []


