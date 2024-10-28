  var largest = null;
  var smallest = null;

  for (const item of lst) {
    if (item < 0) {
      if (largest == null || largest < item) {
        largest = item;
      }
    } else if (item > 0) {
      if (smallest == null || smallest > item) {
        smallest = item;
      }
    }
  }

  return [largest, smallest];
}