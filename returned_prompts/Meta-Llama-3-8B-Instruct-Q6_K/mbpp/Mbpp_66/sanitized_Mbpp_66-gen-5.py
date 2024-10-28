def pos_count(lst):
  return sum(1 for x in lst if x > 0)  # or return len([x for x in lst if x > 0]) for list comprehension version