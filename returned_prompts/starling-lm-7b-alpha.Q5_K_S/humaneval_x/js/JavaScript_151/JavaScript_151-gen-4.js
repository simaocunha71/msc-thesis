  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] >= 0 && Number.isInteger(lst[i])) {
      if (lst[i] % 2 === 1) {
        sum += lst[i] * lst[i];
      }
    }
  }
  return sum;
}


