from collections import OrderedDict
def sort_counter(counter):
    return OrderedDict(sorted(counter.items(), key=lambda t: t[1], reverse=True))

