  if (n == 0) return [1];
  if (n == 1) return [1, 3, 2];
  if (n == 2) return [1, 3, 2, 8];

  let result = [1, 3, 2];
  for (let i = 3; i < n; i++) {
    let a = result[i-1];
    let b = result[i-2];
    let c = result[i-3];
    result.push(a + b + c);
  }

  return result;
}



