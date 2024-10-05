  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (Math.floor(lst[i]) === lst[i] && lst[i] > 0) {
      sum += lst[i] * lst[i];
    }
  }
  return sum;
}