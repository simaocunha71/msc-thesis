/* Create a function that takes a value (string) representing a number
  and returns the closest integer to it. If the number is equidistant
  from two integers, round it away from zero.
  Examples
  >>> closestInteger("10")
  10
  >>> closestInteger("15.3")
  15
  Note:
  Rounding away from zero means that if the given number is equidistant
  from two integers, the one you should return is the one that is the
  farthest from zero. For example closestInteger("14.5") should
  return 15 and closestInteger("-14.5") should return -15.
  */
const closestInteger = (value) => {
  const floatValue = parseFloat(value);
  let intPart; // The integer part of the value

  if (floatValue === 'Infinity') {
    throw new Error('Cannot convert Infinity to a number');
  } else if (floatValue === '-Infinity') {
    return -1;
  }
  const roundedIntPart = Math.round(floatValue); // Round the float value to an integer

  intPart = roundDown(roundedIntPart, closestIntegerDigits);
  const isNegative = (intPart < 0) && !isFinite(value);

  return (
    (isNegative ? -1 : isNaN(intPart) ? null : intPart) || // If it's negative or NaN, return the closest integer
    0 * Math.floor(floatValue / closestIntegerDigits) + closestIntegerDigits * intPart
  );
};