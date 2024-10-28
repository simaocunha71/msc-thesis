  let counts = {};
  for (const num of lst) {
    if (num in counts) {
      counts[num] += 1;
    } else {
      counts[num] = 1;
    }
  }

  let max_freq = 0;
  let max_num = -1;
  for (const num in counts) {
    let freq = counts[num];
    if (freq >= max_freq && freq >= num) {
      max_freq = freq;
      max_num = num;
    }
  }
  return max_num;
}