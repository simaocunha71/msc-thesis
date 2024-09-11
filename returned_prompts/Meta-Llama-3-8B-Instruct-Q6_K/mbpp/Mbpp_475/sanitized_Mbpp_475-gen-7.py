from operator import itemgetter
def sort_counter(counter_dict):
    return sorted(counter_dict.items(), key=itemgetter(1), reverse=True)