  const isEven = (n) => (n % 2 === 0);
  const hasEven = (n) => isEven(+n.toString().replace(/\D/g, ''));
  const isValid = (n) => !isEven(n);

  return x
    .filter(isValid)
    .sort((a, b) => a - b);
}



