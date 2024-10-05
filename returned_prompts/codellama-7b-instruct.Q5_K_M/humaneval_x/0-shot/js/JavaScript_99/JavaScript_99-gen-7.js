/*
  Solution
  The idea is to subtract the value from the next integer, then subtract
  the value from the previous integer. If the difference between the
  two is less than the difference between the value and the integer
  that is being subtracted from it, then we want to return that integer.
  Otherwise, we want to return the other integer.
  The way this works is that if the value is between two integers,
  subtracting it from the next integer will result in a negative
  value, and subtracting it from the previous integer will result in
  a positive value. If the absolute value of the difference between
  the two is less than the absolute value of the difference between
  the value and the integer being subtracted from it, then we want to
  return the other integer.
*/
  const nextInteger = parseInt(value) + 1;
  const previousInteger = parseInt(value) - 1;
  const differenceNextInteger = Math.abs(value - nextInteger);
  const differencePreviousInteger = Math.abs(value - previousInteger);
  if (differenceNextInteger < differencePreviousInteger) {
    return previousInteger;
  } else {
    return nextInteger;
  }
};
