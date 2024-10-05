  const number = parseFloat(value);
  const rounded = Math.round(number);
  const diffFromZero = Math.abs(0 - number);
  const diffFromRounded = Math.abs(rounded - number);

  if (diffFromRounded < diffFromZero) {
    return rounded;
  } else {
    return rounded + (number > 0 ? 1 : -1);
  }
}



