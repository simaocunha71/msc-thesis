  const tribonacci = [];
  tribonacci[0] = 1;
  tribonacci[1] = 3;
  tribonacci[2] = 2;
  tribonacci[3] = 8;
  for (let i = 4; i < n + 1; i++) {
    if (i % 2 === 0) {
      tribonacci[i] = (1 + i / 2);
    } else {
      tribonacci[i] = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1];
    }
  }
  return tribonacci;
}

// better way
const tri = (n) => {
  const tribonacci = [1, 3, 2];
  for (let i = 4; i <= n; i++) {
    if (i % 2 === 0) {
      tribonacci.push(1 + i / 2);
    } else {
      tribonacci.push(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1]);
    }
  }
  return tribonacci;
}
