  let str_x = x.toString();
  shift = shift % str_x.length;
  return str_x.substring(shift) + str_x.substring(0, shift);
}