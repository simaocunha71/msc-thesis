    from collections import Counter
    from typing import List

    result = []
    digits = set("One Two Three Four Five Six Seven Eight Nine".split())
    for c in Counter(arr).most_common(20):
        if c[0] in digits:
            result.append(digits[c[0]])
    return result


