  let freq = {};
  for (let i = 0; i < lst.length; i++) {
    if (!freq[lst[i]]) {
      freq[lst[i]] = 0;
    }
    freq[lst[i]] += 1;
  }
  for (let i = Math.max(...lst); i > 0; i--) {
    if (freq[i] >= i) {
      return i;
    }
  }
  return -1;
}


