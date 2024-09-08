  if (n > m) {
    return -1;
  }
  let sum = (m - n + 1) * ((n + m) / 2);
  let avg = Math.round(sum / (m - n + 1));
  let binary_str = (avg).toString(2);
  return binary_str;
}



