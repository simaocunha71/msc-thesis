  var sum = 0;
  for (let i = 0; i < k; i++) {
    let num = arr[i];
    let digits = 0;
    while (num > 0) {
      num = Math.floor(num / 10);
      digits += 1;
    }
    if (digits <= 2) {
      sum += arr[i];
    }
  }
  return sum;
}