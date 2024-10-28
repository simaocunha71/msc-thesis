  let result = 1;
  for (let i = n; i > 0; i--) {
    let temp = 1;
    for (let j = i; j > 0; j--) {
      temp *= j;
    }
    result *= temp;
  }
  return result;
}