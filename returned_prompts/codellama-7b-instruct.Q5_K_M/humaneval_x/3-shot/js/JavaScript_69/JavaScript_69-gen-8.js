  var result = -1;
  var freq = {};
  var max_freq = 0;

  for (const i of lst) {
    if (freq[i]) {
      freq[i] += 1;
    } else {
      freq[i] = 1;
    }
    if (freq[i] > max_freq) {
      max_freq = freq[i];
    }
  }

  for (const i of lst) {
    if (freq[i] >= i) {
      result = i;
      break;
    }
  }

  return result;
}



