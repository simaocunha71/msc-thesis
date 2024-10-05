function closestInteger(value) {
    const num = parseFloat(value);
    const int = Math.round(num);

    if(num - int > 0) {
        return Math.ceil(num);
    } else {
        return Math.floor(num);
    }
}


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
    const num = parseFloat(value);
    const int = Math.round(num);

    if(num - int > 0) {
        return Math.ceil(num);
    } else {
        return Math.floor(num);
    }
}


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
    const num = parseFloat(value);
    const int = Math.round(num);

    if(num - int > 0) {
        return Math.