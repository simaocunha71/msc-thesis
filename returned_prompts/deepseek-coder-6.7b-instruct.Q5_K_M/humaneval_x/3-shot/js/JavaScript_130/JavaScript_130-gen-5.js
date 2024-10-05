  let result = [3, 2, 8];
  if (n <= 3) return result.slice(0, n);
  for (let i = 3; i < n; i++) {
    if (i % 2 === 0) {
      result.push(1 + i / 2);
    } else {
      result.push(result[i - 1] + result[i - 2] + result[i + 1]);
    }
  }
  return result;
}



