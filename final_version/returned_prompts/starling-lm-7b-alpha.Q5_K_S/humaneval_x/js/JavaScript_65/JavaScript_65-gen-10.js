  let str_x = String(x);
  let len = str_x.length;
  let new_str = '';
  if (shift > len) {
    shift = shift % len;
  }
  for (let i = 0; i < len; i++) {
    if (i + shift >= len) {
      new_str = str_x[i] + new_str;
    } else {
      new_str += str_x[i + shift];
    }
  }
  return new_str;
}



