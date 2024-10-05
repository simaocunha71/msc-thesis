  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if ((i + 1) % 4 == 0) {
      sum += Math.pow(lst[i], 3);
    } else if ((i + 1) % 3 == 0) {
      sum += Math.pow(lst[i], 2);
    } else {
      sum += lst[i];
    }
  }
  return sum;
}