  var freq = {};
  for (const x of lst) {
    if (x in freq) {
      freq[x] += 1;
    } else {
      freq[x] = 1;
    }
  }

  for (const x of lst) {
    if (freq[x] >= x) {
      return x;
    }
  }

  return -1;
}



