  if (n > m) {
    return -1;
  }

  const sum = n + (m - n);
  const avg = sum / 2;
  const bin = avg.toString(2);

  return bin;
}



