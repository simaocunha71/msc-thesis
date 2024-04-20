"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""
# @coding=utf-8
def merge(list_):
  if not list_:
    return [[]]
  merge_res = []
  i = 0
  j = 1
  while i < len(list_) and j < len(list_[i][j]) + 1:
    merge_res.append(list_[i][j])
    i += 1
    j += 2
  return [merge_res]
