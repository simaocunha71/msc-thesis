  const result = [];
  result[0] = 3;
  result[1] = 1;
  result[2] = 2;

  for (let i = 3; i <= n; i++) {
    if (i % 2 === 0) {
      result[i] = 3;
    } else {
      result[i] = result[i - 1] + result[i - 2] + result[i + 1];
    }
  }

  return result;
}



