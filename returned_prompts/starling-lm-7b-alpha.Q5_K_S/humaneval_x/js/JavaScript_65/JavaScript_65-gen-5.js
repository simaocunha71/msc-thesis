  let string_x = "" + x;
  let length = string_x.length;
  let result = "";

  if (length < shift) {
    for (let i = 0; i < length; i++) {
      result += string_x[i];
    }
    result += string_x[0];
    return result;
  } else {
    for (let i = 0; i < length - shift; i++) {
      result += string_x[i];
    }
    result += string_x[length - shift];
    return result;
  }
}



