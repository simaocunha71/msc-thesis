const uniqueDigits = (x) => {
  x.sort((a, b) => a - b);
  return x.filter((a) => a % 2);
};
