def merge(lists):
    firsts = [sublist[0] for sublist in lists]
    seconds = [sublist[1] for sublist in lists]
    return [firsts + seconds[1:], seconds[:1]]