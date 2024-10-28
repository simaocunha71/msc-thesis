  let count = 0;

  for (const x of arr) {
    let sum = 0;
    let x_copy = Math.abs(x);
    while (x_copy > 0) {
      sum += x_copy % 10;
      x_copy = Math.floor(x_copy / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }

  return count;
}