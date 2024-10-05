  let max_freq = -1;
  let result = -1;

  for (let i = 1; i < lst.length; i++) {
    let freq = 1;
    for (let j = i + 1; j < lst.length; j++) {
      if (lst[i] == lst[j]) {
        freq += 1;
      }
    }
    if (freq >= lst[i] && freq > max_freq) {
      max_freq = freq;
      result = lst[i];
    }
  }

  return result;
}



