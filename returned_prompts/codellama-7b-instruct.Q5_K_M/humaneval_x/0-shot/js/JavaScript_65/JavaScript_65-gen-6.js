  /*Circular shift the digits of the integer x, shift the digits right by shift
     and return the result as a string.
     If shift > number of digits, return digits reversed.
     >>> circularShift(12, 1)
     "21"
     >>> circularShift(12, 2)
     "12"
     */
  const digits = x.toString().split('');
  const result = [];
  let index = shift;
  while (index--) {
    result.push(digits.pop());
  }
  while (digits.length) {
    result.push(digits.shift());
  }
  return result.join('');
}
