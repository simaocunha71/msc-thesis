  let result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(factorial(i));
    } else {
      let sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }
  return result;

  function factorial(i) {
    let result = 1;
    for (let j = 2; j <= i; j++) {
      result *= j;
    }
    return result;
  }
}