  var largest_negative = null;
  var smallest_positive = null;

  for (const i of lst) {
    if (i < 0) {
      if (largest_negative == null || i > largest_negative) {
        largest_negative = i;
      }
    } else if (i > 0) {
      if (smallest_positive == null || i < smallest_positive) {
        smallest_positive = i;
      }
    }
  }

  return [largest_negative, smallest_positive];
}



