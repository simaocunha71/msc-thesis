const f = (n) => {
  let arr = [];
  for (let i = 1; i < n; i++) {
    if (i % 2 === 0) {
      arr.push(i * factorial(i - 1));
    } else {
      arr.push(i * (i + 1) / 2);
    }
  }
  return arr;
};

