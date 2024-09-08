  const num = parseFloat(value);
  const int = Math.round(num);
  const sign = num >= 0 ? 1 : -1;

  if (num === int) {
    return num;
  }

  const diff = Math.abs(num - int);
  const roundUp = diff * sign;
  const roundDown = diff * -sign;

  if (roundUp < roundDown) {
    return int + 1;
  } else {
    return int - 1;
  }
}



