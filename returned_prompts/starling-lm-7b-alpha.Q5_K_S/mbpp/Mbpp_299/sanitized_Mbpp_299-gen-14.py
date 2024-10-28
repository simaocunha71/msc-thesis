def max_aggregate(tuples_list):
  max_name = ""
  max_score = 0
  for i in tuples_list:
    if i[0] == max_name:
      if i[1] > max_score:
        max_score = i[1]
    else:
      if i[1] > max_score:
        max_name = i[0]
        max_score = i[1]
  return (max_name,max_score)