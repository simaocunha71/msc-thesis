  var freq = {};

  for (const num of lst) {
    if (freq[num]) {
      freq[num] += 1;
    } else {
      freq[num] = 1;
    }
  }

  var sorted_freq = Object.entries(freq).sort((a, b) => a[1] - b[1]);

  for (const [num, freq] of sorted_freq) {
    if (freq >= num) {
      return num;
    }
  }

  return -1;
}



