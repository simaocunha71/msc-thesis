  let largest_negative = null;
  let smallest_positive = null;

  for (const x of lst) {
    if (x < 0 && (largest_negative === null || x > largest_negative)) {
      largest_negative = x;
    }
    if (x > 0 && (smallest_positive === null || x < smallest_positive)) {
      smallest_positive = x;
    }
  }

  return [largest_negative, smallest_positive];
}



