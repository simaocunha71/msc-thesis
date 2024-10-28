  let max_freq = 0;
  let max_num = -1;

  for (let i = 0; i < lst.length; i++) {
    let freq = lst.filter(x => x === lst[i]).length;
    if (freq >= lst[i] && lst[i] > 0 && freq > max_freq) {
      max_freq = freq;
      max_num = lst[i];
    }
  }

  if (max_num === -1) {
    return -1;
  }

  return max_num;
}