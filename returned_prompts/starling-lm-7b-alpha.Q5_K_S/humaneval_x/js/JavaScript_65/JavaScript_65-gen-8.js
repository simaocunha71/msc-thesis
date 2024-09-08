  let x_string = x.toString();
  let result = "";

  if (shift > x_string.length) {
    for (let i = 0; i < x_string.length; i++) {
      result += x_string[i];
    }
    result = result.slice(0, -1);
    result += x_string[0];
    return result;
  } else {
    for (let i = 0; i < x_string.length - shift; i++) {
      result += x_string[i];
    }
    result += x_string.slice(-shift);
    return result;
  }
}



