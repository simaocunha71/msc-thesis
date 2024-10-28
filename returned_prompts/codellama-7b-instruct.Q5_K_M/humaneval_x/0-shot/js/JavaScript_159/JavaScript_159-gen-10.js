  let count = number;
  while (count < need) {
    count += remaining;
  }
  return [count, count - need];
}

