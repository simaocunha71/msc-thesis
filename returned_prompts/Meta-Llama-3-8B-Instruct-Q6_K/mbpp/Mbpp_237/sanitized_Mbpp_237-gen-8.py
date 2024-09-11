def check_occurences(lst):
    from collections import defaultdict
    d = defaultdict(int)
    for t in lst:
        t = tuple(sorted(t))
        d[t] += 1
    return dict(d)  # Convert defaultdict back to regular dict