  var stack = [];

  for (var i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      stack.push(string[i]);
    } else if (string[i] == ']') {
      if (stack.length == 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  if (stack.length == 0) {
    return true;
  } else {
    return false;
  }
}



