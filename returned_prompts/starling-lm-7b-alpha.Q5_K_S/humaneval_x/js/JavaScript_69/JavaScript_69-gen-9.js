  let freq = {};
  let max = -1;
  for (const c of lst) {
    if (freq[c] === undefined) {
      freq[c] = 0;
    }
    freq[c] += 1;
    if (freq[c] > c) {
      max = Math.max(max, c);
    }
  }
  return max;
}



