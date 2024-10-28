  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (Math.floor(Math.log10(Math.abs(arr[i]))) <= 2) {
      sum += arr[i];
    }
  }
  return sum;
}