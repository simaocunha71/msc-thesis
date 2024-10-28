from collections import defaultdict
def check_occurences(tuples):
    occurrences = defaultdict(int)
    for t in tuples:
        occurrences[t] += 1
    return dict(occurrences) if occurrences else dict()  # return empty dictionary if input is empty