from collections import defaultdict
def remove_dirty_chars(s1, s2):
    d = defaultdict(int)
    for i in range(len(s2)):
        d[s2[i]] += 1

    s3 = ''
    for i in range(len(s1)):
        if d[s1[i]] == 0:
            s3 += s1[i]
    return s3
s1 = "probasscurve"
s2 = "pros"