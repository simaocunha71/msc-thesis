  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
    let value = lst[i];
    if (i % 3 == 0) {
      value = value * value;
    } else if (i % 4 == 0) {
      value = value * value * value;
    }
    sum += value;
  }

  return sum;
}