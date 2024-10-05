  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0 && i % 4 !== 0) {
      sum += lst[i] ** 2;
    } else if (i % 4 === 0) {
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
}



