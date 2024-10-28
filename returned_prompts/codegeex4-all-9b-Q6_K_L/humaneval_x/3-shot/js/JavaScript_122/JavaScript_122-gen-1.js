  var sum = 0;
  for (let i = 0; i < k; i++) {
    let num = arr[i];
    let digits = (num + '').length;
    if (digits <= 2) {
      sum += num;
    }
  }
  return sum;
}