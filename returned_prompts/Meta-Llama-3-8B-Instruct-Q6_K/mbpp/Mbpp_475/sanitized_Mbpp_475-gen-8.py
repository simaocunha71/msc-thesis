from operator import itemgetter
def sort_counter(d):
    return sorted(d.items(), key=itemgetter(1), reverse=True)