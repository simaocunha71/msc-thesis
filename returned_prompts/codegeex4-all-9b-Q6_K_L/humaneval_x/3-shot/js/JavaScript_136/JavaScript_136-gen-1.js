  let largest = null;
  let smallest = null;

  for (const num of lst) {
    if (num < 0) {
      if (largest == null || num > largest) {
        largest = num;
      }
    } else if (num > 0) {
      if (smallest == null || num < smallest) {
        smallest = num;
      }
    }
  }

  return [largest, smallest];
}

