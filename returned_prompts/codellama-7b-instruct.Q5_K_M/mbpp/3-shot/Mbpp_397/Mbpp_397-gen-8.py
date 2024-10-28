
def median_numbers(a,b,c):
  median_list = [a,b,c]
  median_list.sort()
  if len(median_list) % 2 == 0:
    median = (median_list[len(median_list)-1] + median_list[len(median_list)-2])/2
  else:
    median = median_list[len(median_list)-1]
  return median


