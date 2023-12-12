/* Given a positive floating point number, it can be decomposed into
  and integer part (largest integer smaller than given number) and decimals
  (leftover part always smaller than 1).

  Return the decimal part of the number.
  >>> truncateNumber(3.5)
  0.5
  */
const truncateNumber = (number) => {
  const sign = Math.signbit(number); // -1 is positive or zero, +1 is negative
  const intPart = Math.abs(number), // integer part in absolute value
    decimals = Math.round((intPart * 100) / 100); // the remainder as a decimal; if
                                            // it's positive, then it's a fraction of
                                            // a larger integer
  return sign > 0 ? (decimals < 2 && intPart === decimals ? -1 : decimals) : (intPart === -1 ? -1 : intPart);
};

export default truncateNumber;
