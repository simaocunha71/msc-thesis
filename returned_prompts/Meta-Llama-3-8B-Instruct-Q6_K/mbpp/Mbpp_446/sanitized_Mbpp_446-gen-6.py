def count_Occurrence(tuple1, tuple2):
  count_dict = {}
  for item in tuple1:
    if item in tuple2:
      if item in count_dict:
        count_dict[item] += 1
      else:
        count_dict[item] = 1
  return sum(count_dict.values())  # Return the sum of the values in the dictionary