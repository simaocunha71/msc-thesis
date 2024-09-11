from collections import Counter
def check_occurences(tup_list):
    return dict(Counter(tup_list))  # Convert the counter object to a dictionary