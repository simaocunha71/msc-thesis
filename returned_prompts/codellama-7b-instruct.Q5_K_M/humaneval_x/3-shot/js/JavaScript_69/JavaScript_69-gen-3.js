  var freq = {};
  for (let i of lst) {
    if (i in freq) {
      freq[i] += 1;
    } else {
      freq[i] = 1;
    }
  }

  for (let i of lst) {
    if (i >= 1 && freq[i] >= i) {
      return i;
    }
  }
  return -1;
}



