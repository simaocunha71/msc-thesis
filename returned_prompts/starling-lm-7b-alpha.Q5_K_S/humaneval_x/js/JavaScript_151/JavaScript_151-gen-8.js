  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (typeof lst[i] === 'number' && lst[i] > 0 && lst[i] % 1 === 0) {
      sum += lst[i] * lst[i];
    }
  }
  return sum;
}



