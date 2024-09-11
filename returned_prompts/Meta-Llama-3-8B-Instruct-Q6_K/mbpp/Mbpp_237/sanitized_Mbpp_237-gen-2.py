def check_occurences(tuples_list):
    from collections import defaultdict
    occurrences = defaultdict(int)
    for t in tuples_list:
        occurrences[t] += 1
    return dict(occurrences) if occurrences else {} # return empty dictionary if input is empty