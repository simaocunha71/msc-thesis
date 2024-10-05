  let total = number + need;
  let left = remaining - total;

  if (left < 0) {
    left = 0;
  }

  return [total, left];
};