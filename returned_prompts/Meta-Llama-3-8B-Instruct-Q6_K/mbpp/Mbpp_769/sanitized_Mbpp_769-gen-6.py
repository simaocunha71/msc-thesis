from collections import Counter
def Diff(list1, list2):
  list1_count = Counter(list1)
  list2_count = Counter(list2)
  diff_list = list(set(list1) - set(list2))
  diff_list += list(set(list2) - set(list1))
  return sorted([x for x in diff_list if list1_count[x] > list2_count.get(x, 0) or list2_count.get(x, 0) > list1_count[x]])