from operator import itemgetter
def sort_counter(score):
    return sorted(score.items(), key=itemgetter(1), reverse=True)