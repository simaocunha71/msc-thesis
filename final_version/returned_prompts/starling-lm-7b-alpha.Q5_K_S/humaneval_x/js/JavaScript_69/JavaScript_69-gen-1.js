  const freq_map = {};
  for (const n of lst) {
    if (freq_map.hasOwnProperty(n)) {
      freq_map[n] += 1;
    } else {
      freq_map[n] = 1;
    }
  }
  let max_freq = 0;
  let result = -1;
  for (const n in freq_map) {
    if (freq_map.hasOwnProperty(n)) {
      if (freq_map[n] > max_freq) {
        max_freq = freq_map[n];
        result = Number(n);
      } else if (freq_map[n] == max_freq && Number(n) < result) {
        result = Number(n);
      }
    }
  }
  return result;
}



