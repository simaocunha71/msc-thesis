from operator import itemgetter
def sort_counter(dict_val):
    return sorted(dict_val.items(), key=itemgetter(1), reverse=True)  # sort by value in descending order