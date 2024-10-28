  const number = parseFloat(value);
  const integer = Math.round(number);
  const diff = Math.abs(number - integer);
  const diff_next = Math.abs(number - (integer + 1));
  if (diff_next < diff) {
    return integer + 1;
  }
  return integer;
}



