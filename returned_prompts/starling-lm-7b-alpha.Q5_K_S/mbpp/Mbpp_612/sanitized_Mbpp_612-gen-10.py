def merge(lists):
    firsts = []
    seconds = []
    for l in lists:
        firsts.append(l[0])
        seconds.append(l[1])
    return [firsts, seconds]