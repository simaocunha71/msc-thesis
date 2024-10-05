  var largest = null;
  var smallest = null;

  for (const i of lst) {
    if (i > 0) {
      if (smallest == null || i < smallest) {
        smallest = i;
      }
    } else if (i < 0) {
      if (largest == null || i > largest) {
        largest = i;
      }
    }
  }

  return [largest, smallest];
}



