  var str_x = String(x);
  var str_result = '';

  for (let i = 0; i < shift; i++) {
    var last_char = str_x[str_x.length - 1];
    str_x = str_x.slice(0, str_x.length - 1);
    str_x = last_char + str_x;
  }

  return str_x;
}



