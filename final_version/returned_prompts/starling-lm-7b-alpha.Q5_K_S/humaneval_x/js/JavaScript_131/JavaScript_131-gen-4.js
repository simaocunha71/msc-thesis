  let result = 1;
  let digits = n.toString().split('');
  for (let i = 0; i < digits.length; i++) {
    if (digits[i] % 2 !== 0) {
      result *= Number(digits[i]);
    }
  }

  return result;
}



