def merge(lists):
    firsts = [x[0] for x in lists]
    seconds = [x[1] for x in lists]
    return [firsts + seconds[::2], seconds[1::2]]