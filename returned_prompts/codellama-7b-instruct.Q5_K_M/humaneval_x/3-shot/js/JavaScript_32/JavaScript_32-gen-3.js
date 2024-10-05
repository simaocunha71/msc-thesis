  if (xs.length % 2 == 1) {
    throw new Error('Given list has odd number of coefficients');
  }

  if (xs[xs.length / 2] == 0) {
    throw new Error('Given list has 0 as its largest coefficient');
  }

  const mid_point = xs.length / 2;
  const mid_value = xs[mid_point];

  const left_part = xs.slice(0, mid_point);
  const right_part = xs.slice(mid_point + 1);

  if (poly(left_part, mid_value) == 0) {
    return mid_value;
  }

  if (poly(right_part, mid_value) == 0) {
    return mid_value;
  }

  const left_zero = findZero(left_part);
  const right_zero = findZero(right_part);

  return left_zero + right_zero;
}



