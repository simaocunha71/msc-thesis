const digits = (n) => {
  if (n === 0) return 0;
  const str = n.toString();
  let product = 1;
  for (let i = 0; i < str.length; i++) {
    const digit = parseInt(str[i], 10);
    if (digit % 2 === 1) product *= digit;
  }
  return product;
};

