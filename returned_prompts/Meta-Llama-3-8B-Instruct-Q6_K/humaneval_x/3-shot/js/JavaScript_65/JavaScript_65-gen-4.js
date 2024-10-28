  let str = x.toString();
  let len = str.length;
  shift = shift % len;
  return str.substr(shift) + str.substring(0, shift);
}