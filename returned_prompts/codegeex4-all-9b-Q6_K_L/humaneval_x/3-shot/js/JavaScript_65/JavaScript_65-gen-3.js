  let str = x.toString();
  let len = str.length;
  shift = shift % len;
  return str.slice(-shift) + str.slice(0, -shift);
}