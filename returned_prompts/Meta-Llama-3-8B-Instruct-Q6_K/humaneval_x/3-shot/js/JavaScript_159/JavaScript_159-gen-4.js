  let total = number;
  let left = remaining - (need - number);
  return [total + (need - number), left];
}