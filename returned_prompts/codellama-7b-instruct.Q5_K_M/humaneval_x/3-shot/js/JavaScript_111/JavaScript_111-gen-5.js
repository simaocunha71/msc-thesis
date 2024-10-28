  var histogram = {}
  var test_list = test.split(' ')
  for (const letter of test_list) {
    if (letter in histogram) {
      histogram[letter] += 1
    } else {
      histogram[letter] = 1
    }
  }
  return histogram
}



