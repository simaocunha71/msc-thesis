  let sum = 0;
  for (let i = 0; i < k; i++) {
    let num = arr[i];
    if (num < 10) {
      sum += num;
    } else if (num < 100) {
      sum += num % 10;
    }
  }
  return sum;
}