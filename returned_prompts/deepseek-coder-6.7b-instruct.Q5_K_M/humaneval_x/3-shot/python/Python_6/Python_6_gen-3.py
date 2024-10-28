    result = []
    for group in paren_string.split():
        count, max_count = 0, 0
        for ch in group:
            if ch == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif ch == ')':
                count -= 1
        result.append(max_count)
    return result


