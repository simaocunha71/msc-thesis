  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 == 0) {
      sum += lst[i] * lst[i];
    } else if (i % 4 == 0 && i % 3 != 0) {
      sum += lst[i] * lst[i] * lst[i];
    }
  }
  return sum;
}


