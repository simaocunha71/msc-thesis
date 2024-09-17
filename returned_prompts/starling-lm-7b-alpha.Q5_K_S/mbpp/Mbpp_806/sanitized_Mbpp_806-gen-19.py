def max_run_uppercase(s: str) -> int:
    result = 0
    count = 0
    for i in s:
        if i.isupper():
            count += 1
        else:
            result = max(result, count)
            count = 0
    result = max(result, count)
    return result