  const freq = {};
  for (const i of lst) {
    freq[i] = freq[i] || 0;
    freq[i] += 1;
  }
  for (const i of lst) {
    if (freq[i] >= i && i > 0) {
      return i;
    }
  }
  return -1;
}



