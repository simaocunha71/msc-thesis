  let result = [];
  for (let i = 2; i <= n; i++) {
    let count = 0;
    while (n % i == 0) {
      n = n / i;
      count++;
    }
    if (count > 0) {
      result = result.concat(new Array(count).fill(i));
    }
  }
  return result;
}