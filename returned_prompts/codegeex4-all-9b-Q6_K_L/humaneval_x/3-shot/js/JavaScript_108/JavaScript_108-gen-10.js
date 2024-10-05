  let count = 0;

  for (const i of arr) {
    let sum = 0;
    let temp = Math.abs(i);
    while (temp > 0) {
      sum += temp % 10;
      temp = Math.floor(temp / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }

  return count;
}



