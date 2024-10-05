  let result = 1;
  for (let i = n; i > 0; i--) {
    let factorial = 1;
    for (let j = 1; j <= i; j++) {
      factorial *= j;
    }
    result *= factorial;
  }
  return result;
}