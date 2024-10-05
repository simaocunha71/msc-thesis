  let freqs = {};

  for (const x of lst) {
    freqs[x] = (freqs[x] || 0) + 1;
  }

  for (const x of lst) {
    if (freqs[x] >= x) {
      return x;
    }
  }

  return -1;
}



