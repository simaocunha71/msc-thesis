
def pancake_sort(test_list):
  def flip(i,j):
    test_list[i:j+1] = reversed(test_list[i:j+1])
  while len(test_list) > 1:
    max_elem = max(test_list)
    max_elem_index = test_list.index(max_elem)
    flip(0,max_elem_index)
    flip(0,len(test_list)-1)
    test_list.pop()
  return test_list


