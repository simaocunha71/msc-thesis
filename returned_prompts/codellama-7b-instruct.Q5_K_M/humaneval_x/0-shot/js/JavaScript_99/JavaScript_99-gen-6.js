  // first, turn the value into a number
  const num = Number(value);

  // next, get the absolute value of the difference between the number and the rounded version of the number
  const absDiff = Math.abs(num - Math.round(num));

  // now, check if the absolute difference is less than 0.5
  if (absDiff < 0.5) {
    return num;
  }

  // otherwise, check if the number is positive or negative
  if (num > 0) {
    return num - absDiff;
  } else {
    return num + absDiff;
  }
}
