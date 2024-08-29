  const onlyDigits = n => Number(n.toString().replace(/\D/g, ''));
  const isEven = n => n % 2 === 0;
  const isOdd = n => !isEven(n);
  const onlyOddNumbers = x.filter(onlyDigits).filter(isOdd);
  const sorted = onlyOddNumbers.sort((a, b) => a - b);
  return sorted;
}



