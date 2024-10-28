const uniqueDigits = (x) => {
  const y = [];
  x.forEach((element) => {
    if (element % 2 !== 0) {
      y.push(element);
    }
  });
  return y.sort((a, b) => a - b);
};
