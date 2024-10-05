const evenOddCount = (num) => {

  const digits = String(num).split('').map(Number);
  const odd = digits.filter(digit => digit % 2).length;
  const even = digits.length - odd;

  return [even, odd];
};
