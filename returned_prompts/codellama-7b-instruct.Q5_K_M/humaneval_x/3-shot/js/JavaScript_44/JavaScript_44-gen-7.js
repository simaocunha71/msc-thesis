  let result = '';
  let current_x = x;
  let digits = '0123456789ABCDEF';

  while (current_x > 0) {
    result = digits[current_x % base] + result;
    current_x = Math.floor(current_x / base);
  }

  return result;
}



