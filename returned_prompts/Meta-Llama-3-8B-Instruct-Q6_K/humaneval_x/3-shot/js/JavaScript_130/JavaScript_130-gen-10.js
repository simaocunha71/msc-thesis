  let result = [1];
  if (n > 0) {
    result.push(3);
  }
  if (n > 1) {
    result.push(2);
  }
  for (let i = 3; i <= n; i++) {
    let sum = 0;
    if (i % 2 === 0) {
      sum = 1 + i / 2;
    } else {
      sum = result[i - 1] + result[i - 2] + result[i - 3];
    }
    result.push(sum);
  }
  return result;
}
