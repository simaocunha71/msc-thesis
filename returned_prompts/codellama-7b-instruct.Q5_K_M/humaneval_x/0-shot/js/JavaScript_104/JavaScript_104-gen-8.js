const uniqueDigits = (x) => {
  const y = [];
  x.forEach((num) => {
    if (num % 2 !== 0) {
      y.push(num);
    }
  });
  return y.sort((a, b) => a - b);
};

