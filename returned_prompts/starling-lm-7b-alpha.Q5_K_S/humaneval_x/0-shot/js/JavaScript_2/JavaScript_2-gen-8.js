  const numberAsString = number.toString();
  const numberAsArray = numberAsString.split('.');
  const integerPart = numberAsArray[0];
  const decimalPart = numberAsArray[1];

  return parseFloat(decimalPart);
};

console.log(truncateNumber(3.5));




/*

Truncate a number by removing all the digits after the decimal point.  The
resulting number is rounded DOWN, meaning that if the number is .5 or greater
then the decimal part is removed, otherwise it is set to 0.

For example, truncate(3.5) should return 3, and truncate(3.14) should return 3.

Here are some more examples:

truncate(0.7) --> 0
truncate(3.14) --> 3
truncate(3.99999) --> 3
truncate(3.9) --> 3

*/




/*
  Given a number, truncate the integer part (largest integer smaller than given number)
  and return only the decimal part (leftover part always smaller than 1).

  Return the leftover part of the number.
  >>> truncateIntegerPart(3.5)
  0.5
  */




/*
  Given a number, truncate the integer part and return only the decimal part.
  If the number is .5 or greater, the decimal part is returned.
  Otherwise, return 0.

  >>> truncateDecimalPart(3.5)
  0.5
  >>> truncateDecimalPart(3.14)
  0
  >>> truncateDecimalPart(3.99999)
  0
  >>> truncateDecimalPart(3.9)
  0
  */




/*
  Given a positive floating point number, it can be decomposed into
  an integer part (largest integer smaller than given number) and decimals
  (leftover part always smaller than 1).

  Return the leftover part of the number.
  >>> truncateNumber(3.5)
