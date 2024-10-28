  if (n > m) {
    return -1;
  }
  let avg = Math.round((n + m) / 2.0);
  return "0b" + avg.toString(2);
}