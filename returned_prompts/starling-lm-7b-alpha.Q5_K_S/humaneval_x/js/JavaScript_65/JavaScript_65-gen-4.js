  let string = String(x);
  let len = string.length;
  if (shift > len) {
    shift = shift % len;
  }
  if (shift == 0) {
    return string;
  }
  if (len == 1) {
    return string;
  }

  let left_part = string.substring(0, len - shift);
  let right_part = string.substring(len - shift);
  return right_part + left_part;
}



