  var sum = 0;

  for (let i = 0; i < Math.min(k, arr.length); i++) {
    let num = arr[i];
    if (num < 10) {
      sum += num;
    } else {
      let last_digit = num % 10;
      sum += last_digit;
    }
  }

  return sum;
}