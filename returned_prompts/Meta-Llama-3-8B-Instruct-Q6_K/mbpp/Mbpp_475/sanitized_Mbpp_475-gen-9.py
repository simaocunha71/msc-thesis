from operator import itemgetter
def sort_counter(counter):
  return sorted(counter.items(), key=itemgetter(1), reverse=True)  # sort by value in descending order