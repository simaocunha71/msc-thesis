  let total = number;
  if (need < remaining) {
    total += need;
    remaining -= need;
  } else {
    total += remaining;
    remaining = 0;
  }
  return [total, remaining];
}



