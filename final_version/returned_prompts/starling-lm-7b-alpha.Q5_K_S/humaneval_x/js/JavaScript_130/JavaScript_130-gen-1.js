  if (n == 0) {
    return [];
  }
  let result = [3];
  for (let i = 3; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(1 + i / 2);
    } else {
      let a = result[result.length - 3];
      let b = result[result.length - 2];
      let c = result[result.length - 1];
      result.push(a + b + c);
    }
  }
  return result;
}



