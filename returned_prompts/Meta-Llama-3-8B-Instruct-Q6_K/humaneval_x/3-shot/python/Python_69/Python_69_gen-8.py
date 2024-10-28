    from collections import Counter
    count = Counter(lst)
    max_freq = max(count.values())
    max_value = -1
    for num, freq in count.items():
        if freq >= num and num > 0 and freq > max_value:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    max_freq = 0
    max_value = -1
    for num in lst:
        if num > 0:
            if num > max_freq:
                max_freq = num
                max_value = num
            elif num == max_freq:
                max_value = -1
                break
    return max_value if max_value > 0 else -1
# or
    from collections import defaultdict
    d = defaultdict(int)
    for num in lst:
        d[num] += 1
    max_value = -1
    for num, freq in d.items():
        if num > 0 and freq >= num:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    max_value = -1
    for num in lst:
        if num > 0 and lst.count(num) >= num:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    from collections import Counter
    count = Counter(lst)
    max_value = -1
    for num, freq in count.items():
        if num > 0 and freq >= num:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    max_value = -1
    for num in lst:
        if num > 0 and lst.count(num) >= num:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    max_value = -1
    for num in lst:
        if num > 0 and lst.count(num) >= num:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    max_value = -1
    for num in lst:
        if num > 0 and lst.count(num) >= num:
            max_value = num
    return max_value if max_value > 0 else -1
# or
    max_value = -1
    for num in lst:
        if num > 0