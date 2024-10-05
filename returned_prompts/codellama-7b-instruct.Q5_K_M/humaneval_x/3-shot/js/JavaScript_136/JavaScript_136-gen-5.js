  var smallest_pos = null;
  var largest_neg = null;

  for (const i of lst) {
    if (i > 0) {
      if (smallest_pos === null || i < smallest_pos) {
        smallest_pos = i;
      }
    } else if (i < 0) {
      if (largest_neg === null || i > largest_neg) {
        largest_neg = i;
      }
    }
  }

  return [largest_neg, smallest_pos];
}



