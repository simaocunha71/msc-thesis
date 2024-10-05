  let result = 1;
  for (let i = 1; i <= n; i++) {
    let temp = 1;
    for (let j = 1; j <= i; j++) {
      temp *= j;
    }
    result *= temp;
  }
  return result;
}