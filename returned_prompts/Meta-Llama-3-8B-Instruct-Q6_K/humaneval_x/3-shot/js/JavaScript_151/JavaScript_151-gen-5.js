  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (typeof lst[i] === 'number' && lst[i] % 1 === 0 && lst[i] >= 0) {
      if (lst[i] % 2 !== 0) {
        sum += Math.pow(lst[i], 2);
      }
    }
  }
  return sum;
}...



