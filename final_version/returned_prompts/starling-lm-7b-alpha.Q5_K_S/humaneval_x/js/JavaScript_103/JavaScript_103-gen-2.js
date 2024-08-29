  if (n > m) {
    return -1;
  }

  let total = (m - n + 1) * ((n + m) / 2);
  let avg = Math.round(total / (m - n + 1));

  return "0b" + avg.toString(2);
}



