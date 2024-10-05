  let sum = 0;
  for (let i = 0; i < k; i++) {
    let num = Math.abs(arr[i]);
    if (num < 10 || num >= 100) {
      sum += num;
    }
  }
  return sum;
}