from collections import Counter
def frequency_lists(lists):
    flat_list = [item for sublist in lists for item in sublist]
    return dict(Counter(flat_list))  # convert the Counter to a dictionary