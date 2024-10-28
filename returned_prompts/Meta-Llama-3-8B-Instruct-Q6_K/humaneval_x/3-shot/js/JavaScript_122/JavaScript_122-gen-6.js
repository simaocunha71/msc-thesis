  let sum = 0;
  for (let i = 0; i < k; i++) {
    let num = arr[i];
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
}