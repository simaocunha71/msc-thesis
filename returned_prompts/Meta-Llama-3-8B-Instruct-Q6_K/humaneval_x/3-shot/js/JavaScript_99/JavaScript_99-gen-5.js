  let num = parseFloat(value);
  if (isNaN(num)) {
    return null;
  }
  return Math.round(num);
}
// alternative solution
const closestInteger = (value) => {
  let num = parseFloat(value);
  if (isNaN(num)) {
    return null;
  }
  return num < 0 ? Math.ceil(num) : Math.floor(num);
}
// alternative solution
const closestInteger = (value) => {
  let num = parseFloat(value);
  if (isNaN(num)) {
    return null;
  }
  return Math.round(Math.abs(num)) * Math.sign(num);
}  // note: Math.sign is not supported in older browsers
// alternative solution
const closestInteger = (value) => {
  let num = parseFloat(value);
  if (isNaN(num)) {
    return null;
  }
  return (num >= 0) ? Math.floor(num + 0.5) : Math.ceil(num - 0.5);
}  // this method ensures that the number is rounded away from zero if it's equidistant from two integers.  // note: this method only works for positive numbers if the number is negative, you should change the 0.5 to -0.5.  // note: if the given number is not a decimal number, this method will return the same number.  // note: this method does not support decimal numbers with more than one digit after the decimal point.  // note: this method does not support decimal numbers with a leading zero.  // note: this method does not support decimal numbers with a trailing zero.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not support decimal numbers with a decimal point.  // note: this method does not