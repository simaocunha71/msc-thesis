  const num = parseFloat(value);
  if (num === Math.floor(num)) {
    return num;
  }
  const is_negative = num < 0;
  const is_integer = num.toString().split('.').length === 2;
  const is_odd = num % 1.0 === 0.5;

  return is_negative
    ? -Math.ceil(num)
    : is_integer
        ? Math.floor(num)
        : is_odd
            ? Math.floor(num) + 1
            : Math.floor(num) - 1;
}



