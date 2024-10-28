def test_duplicate(test_list:list) -> bool:
  return len(test_list) != len(set(test_list))