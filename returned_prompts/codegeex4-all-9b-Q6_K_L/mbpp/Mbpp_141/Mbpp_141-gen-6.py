def pancake_sort(test_list):
  if len(test_list) <= 1:
    return test_list
  max_index = test_list.index(max(test_list))
  if max_index != len(test_list) - 1:
    test_list = test_list[max_index + 1:] + test_list[:max_index + 1]
    test_list = test_list[::-1]
  test_list = test_list[1:] + [test_list[0]]
  return pancake_sort(test_list[1:]) + [test_list[0]]