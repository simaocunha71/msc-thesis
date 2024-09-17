
def max_aggregate(marks:list)->tuple:
  marks_dict = {}
  for item in marks:
    name, score = item
    if name not in marks_dict:
      marks_dict[name] = score
    else:
      marks_dict[name] += score
  return max(marks_dict.items(), key=lambda x: x[1])


