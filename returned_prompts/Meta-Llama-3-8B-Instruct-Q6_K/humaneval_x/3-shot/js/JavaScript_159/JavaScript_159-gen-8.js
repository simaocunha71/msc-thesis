  let total = number;
  let left = remaining - (need - number);
  if (left < 0) {
    total += need;
    left = 0;
  }
  return [total, left];
}