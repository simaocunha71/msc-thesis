
import collections

def histogram(test):
    counts = collections.Counter(test.split())
    return {k: v for k, v in counts.items() if v == max(counts.values())}