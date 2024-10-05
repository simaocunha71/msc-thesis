  let result = [];
  for (let i = 2; i <= n; i++) {
    let count = 0;
    while (n % i === 0) {
      n = n / i;
      count++;
    }
    if (count > 0) {
      result.push(i);
      for (let j = 0; j < count; j++) {
        result.push(i);
      }
    }
  }
  return result;
}