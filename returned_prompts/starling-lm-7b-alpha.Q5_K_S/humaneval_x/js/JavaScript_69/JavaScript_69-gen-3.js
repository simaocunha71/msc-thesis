  let freq = {};
  for (const i of lst) {
    freq[i] = (freq[i] || 0) + 1;
  }
  for (const i of lst) {
    if (freq[i] >= i) {
      return i;
    }
  }
  return -1;
}



