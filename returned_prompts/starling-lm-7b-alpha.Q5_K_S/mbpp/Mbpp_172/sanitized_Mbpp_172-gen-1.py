from collections import Counter
def count_occurance(s):
    return Counter(s).get('std',0)