  let max_freq = 0;
  let result = -1;
  for (let i = 0; i < lst.length; i++) {
    let count = 0;
    for (let j = 0; j < lst.length; j++) {
      if (lst[i] === lst[j]) {
        count++;
      }
    }
    if (count >= lst[i] && lst[i] > 0 && count > max_freq) {
      max_freq = count;
      result = lst[i];
    }
  }
  return result;
}