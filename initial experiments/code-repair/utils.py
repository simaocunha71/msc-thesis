def test_find_common(f):
  inputs = [
    ([1,2,3],[1]),
    ([1,2,3,4,5],[1,3,5])
  ]

  outputs = [[1], [1,3,5]]

  for idx in range(len(inputs)):
    i = inputs[idx]
    expected = outputs[idx]
    result = f(i[0], i[1])
    assert result == expected, f"for inputs {i[0]} and {i[1]} expected {expected}; but got {result}"
  
  print("All tests passed")
