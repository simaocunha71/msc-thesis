  var stack = [];
  var open_brackets = 0;
  var close_brackets = 0;
  var last_open_bracket_index = -1;

  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      open_brackets += 1;
      stack.push(i);
      last_open_bracket_index = i;
    } else if (string[i] == ']') {
      close_brackets += 1;
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
      if (stack.length == 0) {
        if (close_brackets - open_brackets > 1) {
          return true;
        }
        open_brackets = 0;
        close_brackets = 0;
      }
    }
  }

  if (stack.length != 0) {
    return false;
  }

  return false;
}