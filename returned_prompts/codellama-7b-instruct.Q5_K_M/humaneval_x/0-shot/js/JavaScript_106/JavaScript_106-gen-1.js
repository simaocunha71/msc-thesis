
const f = (n) => {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(i * factorial(i - 1));
    } else {
      let sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      result.push(sum);
    }
  }
  return result;
};

// f(5) == [1, 2, 6, 24, 15]

