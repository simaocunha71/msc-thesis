  const freq = {};

  for (let i = 0; i < lst.length; i++) {
    if (freq[lst[i]] === undefined) {
      freq[lst[i]] = 1;
    } else {
      freq[lst[i]]++;
    }
  }

  for (let i = Math.max(...lst); i > 0; i--) {
    if (freq[i] !== undefined && freq[i] >= i) {
      return i;
    }
  }

  return -1;
}



