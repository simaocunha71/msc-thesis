  var freq = {};
  var max = -1;

  for (const x of lst) {
    if (x in freq) {
      freq[x] += 1;
    } else {
      freq[x] = 1;
    }
    if (freq[x] >= x && x > max) {
      max = x;
    }
  }

  return max;
}