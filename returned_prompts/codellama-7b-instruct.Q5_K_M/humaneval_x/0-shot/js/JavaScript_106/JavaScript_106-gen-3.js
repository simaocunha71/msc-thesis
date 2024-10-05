const f = (n) => {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      result.push(i * factorial(i - 1));
    } else {
      result.push(i + sum(1, i));
    }
  }
  return result;
};

const factorial = (n) => {
  if (n === 1) return 1;
  return n * factorial(n - 1);
};

const sum = (a, b) => {
  let total = 0;
  for (let i = a; i <= b; i++) {
    total += i;
  }
  return total;
};

/*
  f(5) should return [1, 2, 6, 24, 15]
  */
const result = f(5);
console.log(result);
