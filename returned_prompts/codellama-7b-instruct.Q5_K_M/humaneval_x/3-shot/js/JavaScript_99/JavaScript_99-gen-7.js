  const number = parseFloat(value);

  if (number === 0) {
    return 0;
  }

  const closest_integer = Math.round(number);
  const closest_integer_absolute = Math.abs(closest_integer);

  const number_absolute = Math.abs(number);
  const number_decimal_part = number_absolute % 1.0;

  if (number_decimal_part === 0.5) {
    return closest_integer > 0 ? closest_integer : closest_integer - 1;
  }

  if (closest_integer_absolute < number_absolute) {
    return closest_integer;
  }

  if (closest_integer > 0) {
    return closest_integer - 1;
  }

  return closest_integer + 1;
}



