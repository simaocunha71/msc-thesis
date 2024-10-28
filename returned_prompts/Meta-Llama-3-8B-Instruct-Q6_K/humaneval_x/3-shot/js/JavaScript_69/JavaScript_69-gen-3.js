  let max_freq = 0;
  let max_num = -1;
  let freq_map = {};

  for (let num of lst) {
    if (!freq_map[num]) {
      freq_map[num] = 0;
    }
    freq_map[num]++;
    if (freq_map[num] >= num && num > max_num) {
      max_num = num;
    }
  }

  return max_num;
}  //  or return max_num > 0 ? max_num : -1;  // for code golf


