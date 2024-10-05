  let str_x = x.toString();
  shift = shift % str_x.length;
  return str_x.slice(shift) + str_x.slice(0, shift);
}