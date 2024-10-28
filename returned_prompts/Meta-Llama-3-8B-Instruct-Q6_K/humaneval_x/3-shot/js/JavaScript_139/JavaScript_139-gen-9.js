  let result = 1;
  for (let i = 1; i <= n; i++) {
    let factorial = 1;
    for (let j = 1; j <= i; j++) {
      factorial *= j;
    }
    result *= factorial;
  }
  return result;
}



