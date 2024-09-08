  let digits = x.toString();
  let length = digits.length;
  if (length <= shift) {
    return digits.split('').reverse().join('');
  }
  return digits.slice(shift) + digits.slice(0, shift);
}



