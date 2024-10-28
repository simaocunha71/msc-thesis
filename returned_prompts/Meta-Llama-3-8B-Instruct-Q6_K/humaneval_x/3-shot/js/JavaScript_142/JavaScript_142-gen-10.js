  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if ((i + 1) % 3 === 0) {
      sum += lst[i] * lst[i];
    } else if ((i + 1) % 4 === 0 && (i + 1) % 3 !== 0) {
      sum += Math.pow(lst[i], 3);
    }
  }
  return sum;
}