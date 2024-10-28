  var open = 0, close = 0;

  for (const c of string) {
    if (c == '[') {
      open++;
    } else if (c == ']') {
      close++;
    }
  }

  if (open == close) {
    return false;
  }

  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      open++;
    } else if (string[i] == ']') {
      close++;
    }
    if (open > close) {
      return true;
    }
  }

  return false;
}



