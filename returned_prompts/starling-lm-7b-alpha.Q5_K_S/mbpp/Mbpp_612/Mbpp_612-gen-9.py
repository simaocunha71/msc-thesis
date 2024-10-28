
def merge(lists):
    firsts = [x[0] for x in lists]
    seconds = [x[1] for x in lists]
    return [[firsts[0]], [firsts[1]] + seconds, [firsts[2]] + seconds]


