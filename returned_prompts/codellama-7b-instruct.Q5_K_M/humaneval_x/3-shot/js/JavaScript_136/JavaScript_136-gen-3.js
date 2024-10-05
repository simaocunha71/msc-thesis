  var largest = null;
  var smallest = null;

  for (const element of lst) {
    if (element < 0 && (largest == null || element > largest)) {
      largest = element;
    } else if (element > 0 && (smallest == null || element < smallest)) {
      smallest = element;
    }
  }

  return [largest, smallest];
}



