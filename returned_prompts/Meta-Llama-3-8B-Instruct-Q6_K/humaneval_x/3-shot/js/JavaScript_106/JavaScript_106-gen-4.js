  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      let factorial = 1;
      for (let j = 1; j <= i; j++) {
        factorial *= j;
      }
      result.push(factorial);
    } else {
      let sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }
  return result;
}