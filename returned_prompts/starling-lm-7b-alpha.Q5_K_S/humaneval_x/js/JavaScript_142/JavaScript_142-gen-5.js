  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 == 0) {
      lst[i] = lst[i] * lst[i];
    } else if (i % 4 == 0 && i % 3 != 0) {
      lst[i] = lst[i] * lst[i] * lst[i];
    }
    sum += lst[i];
  }
  return sum;
}



