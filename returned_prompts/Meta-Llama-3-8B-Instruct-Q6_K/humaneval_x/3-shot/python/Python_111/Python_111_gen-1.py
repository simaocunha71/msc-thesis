    from collections import Counter
    counter = Counter(test.split())
    max_count = max(counter.values())
    return {k: v for k, v in counter.items() if v == max_count} if max_count else {}
# or
    result = {}
    max_count = 0
    for char, count in Counter(test.split()).items():
        if count > max_count:
            max_count = count
            result = {char: count}
        elif count == max_count:
            result[char] = count
    return result if result else {}
# or
    result = {}
    max_count = 0
    for char, count in dict.fromkeys(test.split()).items():
        if count > max_count:
            max_count = count
            result = {char: count}
        elif count == max_count:
            result[char] = count
    return result if result else {}
# or
    from collections import defaultdict
    result = defaultdict(int)
    for char in test.split():
        result[char] += 1
    max_count = max(result.values())
    return {k: v for k, v in result.items() if v == max_count} if max_count else {}
# or
    result = {}
    max_count = 0
    for char in test.split():
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return {k: v for k, v in result.items() if v == max(result.values())} if max(result.values()) else {} # or {}
# or
    from collections import defaultdict
    result = defaultdict(int)
    for char in test.split():
        result[char] += 1
    return {k: v for k, v in result.items() if v == max(result.values())} if max(result.values()) else {} # or {}
# or
    from collections import Counter
    counter = Counter(test.split())
    return {k: v for k, v in counter.items() if v == max(counter.values())} if max(counter.values()) else {} # or {}
# or
    result = {}
    for char in test.split():
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result # or {}
# or
    from collections import defaultdict
    result = defaultdict(int)
    for char in test.split():
        result[char] += 1
