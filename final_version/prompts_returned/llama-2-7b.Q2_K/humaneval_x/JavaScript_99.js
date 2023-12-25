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
  const values = value.split('.').map((s, ix) => parseFloat(s));
  values[0] = Math.abs(values[0]);
  let firstValue = values[0];
  for (let i = 1; i < values.length; i++) {
    if (firstValue > values[i]) firstValue -= values[i];
    else if (firstValue <= values[i] && values[i] != 0) break;
  }
  let lastNegativeValue = -1,
    roundToPow2 = Math.pow(2, Math.floor(Math.log(Math.abs(lastNegativeValue)) / Math.LN2));
  if (firstValue <= 0) {
    firstValue += roundToPow2;
    lastNegativeValue = firstValue;
  } else {
    const pow2 = Math.pow(2, Math.ceil(Math.log10(firstValue)));
    if (lastNegativeValue < 0) lastNegativeValue += roundToPow2;
    else if (roundToPow2 > 2 * pow2 || firstValue >= lastNegativeValue) {
      const nextPower = Math.floor(Math.log(Math.abs(firstValue)) / Math.LN10);
      const second = nextPower == 0 ? 9 : nextPower;
      if (nextPower > 2 * second || firstValue >= lastNegativeValue)