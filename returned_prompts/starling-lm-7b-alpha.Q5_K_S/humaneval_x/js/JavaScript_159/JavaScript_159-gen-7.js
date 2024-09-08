  let total = number + remaining;
  let left = remaining - (need - number);

  if (left < 0) {
    left = 0;
  }

  return [total, left];
}



