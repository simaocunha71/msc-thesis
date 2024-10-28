  let result = 0;
  let digits = n.toString().split('');
  for (const digit of digits) {
    const number = parseInt(digit);
    if (number % 2 == 1) {
      result *= number;
    }
  }

  return result;
}



