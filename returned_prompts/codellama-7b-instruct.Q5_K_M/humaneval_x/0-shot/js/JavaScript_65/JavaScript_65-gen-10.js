const circularShift = (x, shift) => {
  if (shift > (Math.log10(x) + 1)) {
    return x.toString().split('').reverse().join('');
  }
  const digits = x.toString().split('');
  const length = digits.length;
  const first = digits.shift();
  digits.push(first);
  return digits.splice(length - shift).join('');
};