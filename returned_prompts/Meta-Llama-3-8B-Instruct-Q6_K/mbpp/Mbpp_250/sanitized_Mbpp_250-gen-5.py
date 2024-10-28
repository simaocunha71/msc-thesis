def count_X(tup, element):
  return tup.count(element)  # Python's built-in count method does this efficiently
  # Alternative implementation using list comprehension
  # return len([x for x in tup if x == element])  # This is less efficient for large tuples
  # Alternative implementation using dictionary
  # d = {x: tup.count(x) for x in tup}
  # return d.get(element, 0)  # This is also less efficient for large tuples
  # Alternative implementation using recursion
  # def count_X_recursive(tup, element, count=0):
  #   if not tup:
  #     return count
  #   if tup[0] == element:
  #     return count_X_recursive(tup[1:], element, count+1)
  #   else:
  #     return count_X_recursive(tup[1:], element, count)
  # return count_X_recursive(tup, element)  # This is less efficient for large tuples
  # Alternative implementation using itertools
  # import itertools
  # return sum(1 for x in tup if x == element)  # This is less efficient for large tuples
  # Alternative implementation using collections.Counter
  # from collections import Counter
  # return Counter(tup)[element]  # This is less efficient for large tuples
  # Alternative implementation using sorted
  # return len([x for x in sorted(tup) if x == element])  # This is less efficient for large tuples
  # Alternative implementation using zip
  # return len([x for x in zip(tup, tup) if x == element])  # This is less efficient for large tuples
  # Alternative implementation using bisect
  # import bisect
  # return bisect.bisect_right(tup, element) - bisect.bisect_left(tup, element)  # This is less efficient for large tuples
  # Alternative implementation using numpy
  # import numpy as np
  # return np.count_equal(tup, element)  # This is less efficient for large tuples
  # Alternative implementation using scipy
  # from scipy import stats
  # return stats.mode(tup, element)[0][0]  # This is less efficient for large tuples
  # Alternative implementation using pandas
  # import pandas as pd
  # return pd.Series(tup).value_counts().loc[element]  # This is less efficient for large tuples