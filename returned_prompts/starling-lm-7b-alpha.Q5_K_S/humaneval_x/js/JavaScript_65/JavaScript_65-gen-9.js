  let digits = x.toString();
  let num_digits = digits.length;
  if (shift > num_digits) {
    shift = shift % num_digits;
  }
  if (shift == 0) {
    return digits;
  }
  let result = digits.slice(num_digits - shift);
  result += digits.slice(0, num_digits - shift);
  return result;
}



