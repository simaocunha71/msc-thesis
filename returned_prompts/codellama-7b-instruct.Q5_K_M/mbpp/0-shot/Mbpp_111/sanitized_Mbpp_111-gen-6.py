from collections import Counter
def common_in_nested_lists(nested_lists):
    return [x for x in Counter([y for sublist in nested_lists for y in sublist]).most_common(1)[0][0]]