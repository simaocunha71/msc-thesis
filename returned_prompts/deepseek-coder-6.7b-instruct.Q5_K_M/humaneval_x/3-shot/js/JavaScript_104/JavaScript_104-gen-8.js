  const hasEvenDigit = num => {
    const digits = num.toString().split('');
    return digits.some(digit => digit % 2 === 0);
  }

  return x.filter(num => !hasEvenDigit(num)).sort((a, b) => a - b);
}



