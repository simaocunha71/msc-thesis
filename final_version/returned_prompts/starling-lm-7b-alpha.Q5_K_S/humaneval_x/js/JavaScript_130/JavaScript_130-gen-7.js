  const result = [3];

  for (let i = 2; i <= n + 1; i++) {
    if (i % 2 === 0) {
      result.push(1 + i / 2);
    } else {
      const left = result[i - 1];
      const right = result[i - 2];
      const middle = result[i + 1];
      result.push(left + right + middle);
    }
  }
  return result;
}



