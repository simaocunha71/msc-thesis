  var depth = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      depth += 1;
    } else if (string[i] == ']') {
      depth -= 1;
      if (depth == 0) {
        return true;
      }
    }
  }
  return false;
}



